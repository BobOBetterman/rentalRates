import urllib2

#import simplejson as json

import json
import gviz_api
import time
import datetime

#  If you get a key error on the anchor = data['anchor'] line below, it's probably because the initial anchor value was too low, and 3taps has already deleted it. Just increase the initial anchor value until the program runs.
anchor = "617100000"
#dataNew = []
description = {"date": ("datetime", "Date"), "price0": ("number", "0BR Rent"), "price1": ("number", "1BR Rent"), "price2": ("number", "2BR Rent"), "price3": ("number", "3BR Rent")}
url1 = "http://polling.3taps.com/poll?auth_token=267b3ec711e58733c1fc2227ca30e555&anchor="
url2 = "&category=RHFR&location.city=USA-SFO-ATH|USA-SFO-CUP|USA-SFO-LOA|USA-SFO-MEN|USA-SFO-MUA|USA-SFO-PAL|USA-SFO-RED|USA-SFO-STA|USA-SFO-SUN&retvals=timestamp,price,annotations,location"
x = 0

while True:
#while x < 2:
#	url = "http://polling.3taps.com/poll?auth_token=267b3ec711e58733c1fc2227ca30e555&anchor=675995779&category=RHFR&location.city=USA-SFO-ATH|USA-SFO-CUP|USA-SFO-LOA|USA-SFO-MEN|USA-SFO-MUA|USA-SFO-PAL|USA-SFO-RED|USA-SFO-STA|USA-SFO-SUN&retvals=timestamp,price,annotations,location"
	url = url1 + anchor + url2
	data = urllib2.urlopen(url).read()
	data = json.loads(data)

	f1 = open('anchors', 'a')
	f2 = open('chartData', 'w')
#  The next couple lines are for appending the data to the end of the existing file, rather than keeping the whole array in memory for ever. I think I'd like to do this instead, but I have to check to see how Google Charts handles multiple JSON objects first.
#	f2 = open('chartData', 'a')
	dataNew = []
        dataOld = []

        if x > 0:
          f3 = open('chartDataRaw', 'r')
          dataOld = json.load(f3)
          f3.close()

          j = 0

          for item in dataOld:
            if 'price0' in dataOld[j]:
              dataNew.append({"date": datetime.datetime.utcfromtimestamp(dataOld[j]['date']), "price0": dataOld[j]['price0']})
            if 'price1' in dataOld[j]:
              dataNew.append({"date": datetime.datetime.utcfromtimestamp(dataOld[j]['date']), "price1": dataOld[j]['price1']})
            if 'price2' in dataOld[j]:
              dataNew.append({"date": datetime.datetime.utcfromtimestamp(dataOld[j]['date']), "price2": dataOld[j]['price2']})
            if 'price3' in dataOld[j]:
              dataNew.append({"date": datetime.datetime.utcfromtimestamp(dataOld[j]['date']), "price3": dataOld[j]['price3']})

            j = j + 1

        x = 1

	f1.write(anchor + '\n')

	f1.close()
        f3 = open('chartDataRaw', 'w')

	anchor = data['anchor']
	anchor = str(anchor)

	i = 0

	for item in data['postings']:
		if data['postings'][i]['price'] > 0:

			if 'bedrooms' in data['postings'][i]['annotations']:

				if data['postings'][i]['annotations']['bedrooms'] == 'studio':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price0": data['postings'][i]['price']})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price0": data['postings'][i]['price']})
				elif data['postings'][i]['annotations']['bedrooms'] == '1br':
#				dataNew.append({"date": data['postings'][i]['timestamp'], "price": data['postings'][i]['price'], "bedrooms": data['postings'][i]['annotations']['bedrooms'], "location": data['postings'][i]['location']['city']})
#					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']).strftime('new Date(%Y, %m, %d, %H, %M, %S)'), "price1": data['postings'][i]['price']})
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price1": data['postings'][i]['price']})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price']})
				elif data['postings'][i]['annotations']['bedrooms'] == '2br':
#				dataNew.append({"date": data['postings'][i]['timestamp'], "price": data['postings'][i]['price'], "bedrooms": data['postings'][i]['annotations']['bedrooms'], "location": data['postings'][i]['location']['city']})
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price2": data['postings'][i]['price']})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price']})
				elif data['postings'][i]['annotations']['bedrooms'] == '3br':
#				dataNew.append({"date": data['postings'][i]['timestamp'], "price": data['postings'][i]['price'], "bedrooms": data['postings'][i]['annotations']['bedrooms'], "location": data['postings'][i]['location']['city']})
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price3": data['postings'][i]['price']})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price']})



		i = i + 1

        json.dump(dataOld, f3)
        f3.close()

	dataTable = gviz_api.DataTable(description)
	dataTable.LoadData(dataNew)

	jsonData = dataTable.ToJSon(columns_order=("date", "price0", "price1", "price2", "price3"), order_by="date")

	f2.write(jsonData)
#	json.dump(jsonData, f2)

	f2.close()

#  Let's make the call every three hours:
	time.sleep(10800)

#  I was making the call every eight hours originally, but I'd rather it catch up to present time faster, and I want to make very sure it keeps ahead of postings, rather than falling behind. It's not like calling eight times a day is going to break their system.
#	time.sleep(28800)
#	time.sleep(30)
