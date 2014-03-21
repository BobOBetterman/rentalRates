import urllib2

#import simplejson as json

import json
import gviz_api
import time

anchor = 675995779
dataNew = []
description = {"date": ("number", "Date"), "price0": ("number", "Rent"), "price1": ("number", "Rent"), "price2": ("number", "Rent"), "price3": ("number", "Rent")}

while True:
	url = "http://polling.3taps.com/poll?auth_token=267b3ec711e58733c1fc2227ca30e555&anchor=675995779&category=RHFR&location.city=USA-SFO-ATH|USA-SFO-CUP|USA-SFO-LOA|USA-SFO-MEN|USA-SFO-MUA|USA-SFO-PAL|USA-SFO-RED|USA-SFO-STA|USA-SFO-SUN&retvals=timestamp,price,annotations,location"
	data = urllib2.urlopen(url).read()
	data = json.loads(data)

	anchor = data['anchor']

# description = {"date": ("number", "Date"), "price0": ("number", "Rent"), "price1": ("number", "Rent"), "price2": ("number", "Rent"), "price3": ("number", "Rent")}

	i = 0
# dataNew = []

	for item in data['postings']:
		if data['postings'][i]['price'] > 0:

			if 'bedrooms' in data['postings'][i]['annotations']:

				if data['postings'][i]['annotations']['bedrooms'] == 'studio':
					dataNew.append({"date": data['postings'][i]['timestamp'], "price0": data['postings'][i]['price']})
				elif data['postings'][i]['annotations']['bedrooms'] == '1br':
#				dataNew.append({"date": data['postings'][i]['timestamp'], "price": data['postings'][i]['price'], "bedrooms": data['postings'][i]['annotations']['bedrooms'], "location": data['postings'][i]['location']['city']})
					dataNew.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price']})
				elif data['postings'][i]['annotations']['bedrooms'] == '2br':
#				dataNew.append({"date": data['postings'][i]['timestamp'], "price": data['postings'][i]['price'], "bedrooms": data['postings'][i]['annotations']['bedrooms'], "location": data['postings'][i]['location']['city']})
					dataNew.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price']})
				elif data['postings'][i]['annotations']['bedrooms'] == '3br':
#				dataNew.append({"date": data['postings'][i]['timestamp'], "price": data['postings'][i]['price'], "bedrooms": data['postings'][i]['annotations']['bedrooms'], "location": data['postings'][i]['location']['city']})
					dataNew.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price']})



		i = i + 1

	dataTable = gviz_api.DataTable(description)
	dataTable.LoadData(dataNew)

	jsonData = dataTable.ToJSon(columns_order=("date", "price0", "price1", "price2", "price3"), order_by="date")

	time.sleep(28800)
