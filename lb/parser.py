import public as local_bitcoins

country_codes_filename = 'lb/country_names_and_code_elements.csv'


def get_country_codes():
    import csv
    code_to_name = {}
    with open(country_codes_filename, 'rb') as codes_file:
        reader = csv.reader(codes_file, delimiter=';')
        for row in reader:
            if len(row) == 2:
                code = row[1]
                name = row[0]
                code_to_name[code] = name
    return code_to_name


def get_lb_country_codes():
    return local_bitcoins.countrycodes()


def convert_lb_to_cm_element(data):
    e = data['data']
    j = {
        'id': e.get('profile', {}).get('id', '-1'),
        'lat': e.get('lat', None),
        'lon': e.get('lon', None),
        'type': 'node',
        'tags': {
            'payment:bitcoin': 'yes',
            'local_bitcoins': 'local_bitcoins',
            'addr:city': e.get('city', ''),
            'add:country': e.get('countrycode', ''),
            'contact:website': 'https://localbitcoins.com/accounts/profile/'
                                    + e.get('profile', {}).get('username', '')
        },
        'website': 'http://localbitcoins.com'
    }
    return j


def get_lb_points():
    lb_countrycodes = get_lb_country_codes()

    if not lb_countrycodes:
        return []

    code_to_name = get_country_codes()

    result = {}
    for code in lb_countrycodes:
        country = code_to_name[code]

        query = '%s,%s' % (country.decode('utf-8'), code)
        bl_data = local_bitcoins.get_local_sell_ads(query)
        for entry in bl_data:
            j = convert_lb_to_cm_element(entry)
            if j['id'] not in result:
                result[j['id']] = j
    return result.values()