'''
Created on 1 Aug 2013

@author: Jamie
'''

import requests
import json

import logging
logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

root = 'https://localbitcoins.com/'

def countrycodes():
    r = requests.get(root+'api/countrycodes/').json()
    return r['data']['cc_list']

def payment_methods(countrycode=''):
    r = requests.get(root+'api/payment_methods/%s' % countrycode).json()
    return r['data']['methods']

def currencies():
    r = requests.get(root+'api/currencies').json()
    return r['data']['currencies']

def get_buy_ads(currency=None, countrycode=None, payment_method=None):
    return _get_ads('buy-bitcoins-online/', currency, countrycode, payment_method)

def get_sell_ads(currency=None, countrycode=None, payment_method=None):
    return _get_ads('sell-bitcoins-online/', currency, countrycode, payment_method)

def get_local_buy_ads(location):
    geocode = _geocode(location)
    places = _get_places(geocode['lat'], geocode['lng'])
    url = places[0]['buy_local_url']
    ads = _get_local_ads(url)
    return ads

def get_local_sell_ads(location):
    geocode = _geocode(location)
    places = _get_places(geocode['lat'], geocode['lng'])
    url = places[0]['sell_local_url']
    ads = _get_local_ads(url)
    return ads

def _get_local_ads(url):
    r = requests.get(url)
    ads = json.loads(r.text)
    return ads['data']['ad_list']

def _get_places(lat, lng, countrycode=None, location_string=None):
    r = requests.get(root+'/api/places?',
                     params={'lat': lat, 'lon': lng,
                              'countrycode': countrycode,
                              'location_string': location_string}).json()
    places = r['data']['places']
    return places


def _get_ads(trade_type, currency=None, countrycode=None, payment_method=None):
    url = root + trade_type
    country_ads = []
    currency_ads = []
    
    if not countrycode == None:
        url1 = url + countrycode + '/name/'
        if not payment_method == None:
            url1 += payment_method + '/'
        url1 += '.json'
        r = requests.get(url1).json()
        country_ads = r['data']['ad_list']
        
    if not currency == None:
        url2 = url + currency + '/'
        if not payment_method == None:
            url2 += payment_method + '/'
        url2 += '.json'
        r = requests.get(url2).json()
        currency_ads = r['data']['ad_list']
        
    if countrycode == None and currency == None:
        if not payment_method == None:
            url += payment_method + '/'
        url += '.json'
        r = requests.get(url).json
        ad_list = r['data']['ad_list']

    elif not countrycode == None and not currency == None:
        ad_list = [item for item in currency_ads if item in country_ads]
        
    else:
        ad_list = country_ads + currency_ads
        
    return {'success': 1, 'ad_list': ad_list}

def _geocode(location):
    gmaps_url = 'https://maps.google.com/maps/api/geocode/json?'
    r = requests.get(gmaps_url,
                     params={'address': location,
                             'sensor': 'false'}).json()
    if r['status'] == 'OK':
        geocoded = r['results'][0]['geometry']['location']
        return {'success': 1, 'lat': geocoded['lat'], 'lng': geocoded['lng']}
    else:
        return {'success': 0}
    

def test():
    pass

def main():
    test()

if __name__ == '__main__':
    main()
