import urllib, urllib2, json

city = 'Roorkee'
url = 'http://maps.google.com/maps/api/geocode/json?address='+city+'&sensor=false'
ope = urllib2.urlopen(url)
ope1 = ope.read()
son = json.loads(ope1)
#print son
cin = son['results'][0]['geometry']['bounds']

nlat = cin['northeast']['lat']
nlon = cin['northeast']['lng']
slat = cin['southwest']['lat']
slon = cin['southwest']['lng']
print "northeast lattitude of %s is %s" % (city,nlat)
print "northeast longitude os %s is %s" % (city,nlon)
print "southwest lattitude of %s is %s" % (city,slat)
print "southwest lattitude of %s is %s" % (city,slon)
#for full address
arr = []
for t in son['results'][0]['address_components'] :
	arr.append(t['long_name'])
print "City :- %s \nDistrict :- %s \nState :- %s \nCountry :- %s" % (arr[0],arr[1],arr[2],arr[3])

	
