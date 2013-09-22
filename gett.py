import urllib, urllib2, json, requests
lat = '29.8749' #edit this 
lon = '77.8899'  #edit this
new_sample = 'http://maps.googleapis.com/maps/api/geocode/json?latlng='+lat+','+lon+'&sensor=false'
request = urllib2.Request(new_sample, None, {'Referer': 'testing'})
redi = urllib2.urlopen(request)
redit = redi.read()
son = json.loads(redit)
typ = []
val = []
f = son['results'][0]['address_components']
i = 0
for add in f :
	typ.append(add['types'][0])
	val.append(add['long_name'])
	i = i + 1
k = 0
for k in range(0,i):
	print "%s :- %s" % (typ[k],val[k])
