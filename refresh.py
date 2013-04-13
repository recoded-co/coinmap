#!/usr/bin/python
import urllib
import urllib2
from lxml import etree
import os

data = {'data': '<query type="node"><has-kv k="payment:bitcoin" v="yes"/></query><print/>'}
req = urllib2.Request('http://www.overpass-api.de/api/interpreter', urllib.urlencode(data))
f = urllib2.urlopen(req)
tree = etree.parse(f)
f.close()

scriptdir = os.path.dirname(os.path.abspath(__file__))

with open(scriptdir + '/coinmap.txt', 'w') as f:
  f.write('lat\tlon\ttitle\tdescription\ticonSize\ticonOffset\ticon\n')
  for e in tree.findall('node'):
    lat = e.get('lat')
    lon = e.get('lon')
    tags = {}
    for i in list(e):
      tags[i.get('k')] = i.get('v')
    if 'name' in tags:
      title = tags['name']
    else:
      title = 'node#%d' % i.get('id')
    desc = ''
    desc += '%s %s<br/>' % (tags.get('addr:street', ''), tags.get('addr:housenumber', ''))
    desc += '%s %s<br/>' % (tags.get('addr:postcode', ''), tags.get('addr:city', ''))
    desc += '%s<br/>' % (tags.get('addr:country', ''))
    if 'website' in tags:
      desc += '<a href="%s">%s</a>' % (tags['website'], tags['website'])
    icon = 'bitcoin'
    if tags.get('shop') == 'jewelry':
      icon = 'icons/shopping_jewelry2.n.24'
    if tags.get('shop') == 'bicycle':
      icon = 'icons/shopping_bicycle.n.24'
    if tags.get('tourism') == 'hotel':
      icon = 'icons/accommodation_hotel.n.24'
    f.write(lat)
    f.write('\t')
    f.write(lon)
    f.write('\t')
    f.write(title.encode('utf-8'))
    f.write('\t')
    f.write(desc.encode('utf-8'))
    f.write('\t')
    f.write('24,24') # iconSize
    f.write('\t')
    f.write('-12,-12') # iconOffset
    f.write('\t')
    f.write('%s.png' % icon)
    f.write('\n')
