import urllib
import urllib2
import simplejson

usa_cities = 'zipzap/usa_cities.csv'
merchantid = 946


def get_usa_cities():
    cities = []
    with open(usa_cities, 'rb') as cities_file:
        for line in cities_file:
            cities.append(line.strip())
    return cities


def call_zipzap(location):
    location_encode = urllib.urlencode({'searchAddress': location, 'MerchantID': merchantid})
    url = 'https://www.cashpayment.com/API/PaymentCenter?%s' % location_encode
    f = urllib2.urlopen(url)
    json = simplejson.load(f)
    f.close()
    return json


def convert_to_coinmap(data):
    j = {
        'id': data['ID'],
        'name': data['PaymentCenterName'],
        'lat': data['GeoLat'],
        'lon': data['GeoLong'],
        'type': 'node',
        'tags': {
            'payment:bitcoin': 'yes',
            'zipzap': 'zipzap',
            'addr:city': data['City'],
            'add:country': 'USA',
        },
        'website': 'http://zipzapinc.com'
    }
    return j


def get_zipzap_points():
    cities = get_usa_cities()
    result = {}
    for c in cities:
        data = call_zipzap(c)
        for point in data:
            zipzap_loc = convert_to_coinmap(point)
            if zipzap_loc['id'] not in result:
                result[zipzap_loc['id']] = zipzap_loc
    return result.values()