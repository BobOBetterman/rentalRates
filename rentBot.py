import urllib2

#import simplejson as json

import json
import gviz_api
import time
import datetime

#  If you get a key error on the anchor = data['anchor'] line below, it's probably because the initial anchor value was too low, and 3taps has already deleted it. Just increase the initial anchor value until the program runs.
anchor = "625200000"
#dataNew = []
description = {"date": ("datetime", "Date"), "price0": ("number", "0BR Rent"), "price1": ("number", "1BR Rent"), "price2": ("number", "2BR Rent"), "price3": ("number", "3BR Rent"), "numBed": ("number", "Number of Bedrooms"), "city": ("string", "City")}
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
              dataNew.append({"date": datetime.datetime.utcfromtimestamp(dataOld[j]['date']), "price0": dataOld[j]['price0'], "numBed": dataOld[j]['numBed'], "city": dataOld[j]['city']})
            if 'price1' in dataOld[j]:
              dataNew.append({"date": datetime.datetime.utcfromtimestamp(dataOld[j]['date']), "price1": dataOld[j]['price1'], "numBed": dataOld[j]['numBed'], "city": dataOld[j]['city']})
            if 'price2' in dataOld[j]:
              dataNew.append({"date": datetime.datetime.utcfromtimestamp(dataOld[j]['date']), "price2": dataOld[j]['price2'], "numBed": dataOld[j]['numBed'], "city": dataOld[j]['city']})
            if 'price3' in dataOld[j]:
              dataNew.append({"date": datetime.datetime.utcfromtimestamp(dataOld[j]['date']), "price3": dataOld[j]['price3'], "numBed": dataOld[j]['numBed'], "city": dataOld[j]['city']})

            j = j + 1

        x = 1

	f1.write(anchor + '\n')

	f1.close()
        f3 = open('chartDataRaw', 'w')

	anchor = data['anchor']
	anchor = str(anchor)

        '''
        Okay, so I guess this is a comment block? I certainly hope so... Anyway, here's how the cities work. Numbers correspond to cities in the following manner:
        0 = Atherton
        1 = Cupertino
        2 = Los Altos
        3 = Menlo Park
        4 = Mountain View
        5 = Palo Alto
        6 = Redwood City
        7 = Stanford
        8 = Sunnyvale
        '''

	i = 0

	for item in data['postings']:
		if data['postings'][i]['price'] > 0:

			if 'bedrooms' in data['postings'][i]['annotations']:
                          if 'city' in data['postings'][i]['location']:

				if data['postings'][i]['annotations']['bedrooms'] == 'studio':
                                  if data['postings'][i]['location']['city'] == 'USA-SFO-ATH':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price0": data['postings'][i]['price'], "numBed": 0, "city": "Atherton"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price0": data['postings'][i]['price'], "numBed": 0, "city": "Atherton"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-CUP':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price0": data['postings'][i]['price'], "numBed": 0, "city": "Cupertino"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price0": data['postings'][i]['price'], "numBed": 0, "city": "Cupertino"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-LOA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price0": data['postings'][i]['price'], "numBed": 0, "city": "Los Altos"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price0": data['postings'][i]['price'], "numBed": 0, "city": "Los Altos"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-MEN':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price0": data['postings'][i]['price'], "numBed": 0, "city": "Menlo Park"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price0": data['postings'][i]['price'], "numBed": 0, "city": "Menlo Park"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-MUA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price0": data['postings'][i]['price'], "numBed": 0, "city": "Mountain View"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price0": data['postings'][i]['price'], "numBed": 0, "city": "Mountain View"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-PAL':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price0": data['postings'][i]['price'], "numBed": 0, "city": "Palo Alto"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price0": data['postings'][i]['price'], "numBed": 0, "city": "Palo Alto"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-RED':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price0": data['postings'][i]['price'], "numBed": 0, "city": "Redwood City"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price0": data['postings'][i]['price'], "numBed": 0, "city": "Redwood City"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-STA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price0": data['postings'][i]['price'], "numBed": 0, "city": "Stanford"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price0": data['postings'][i]['price'], "numBed": 0, "city": "Stanford"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-SUN':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price0": data['postings'][i]['price'], "numBed": 0, "city": "Sunnyvale"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price0": data['postings'][i]['price'], "numBed": 0, "city": "Sunnyvale"})
				elif data['postings'][i]['annotations']['bedrooms'] == '1br':
#				dataNew.append({"date": data['postings'][i]['timestamp'], "price": data['postings'][i]['price'], "bedrooms": data['postings'][i]['annotations']['bedrooms'], "location": data['postings'][i]['location']['city']})
#					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']).strftime('new Date(%Y, %m, %d, %H, %M, %S)'), "price1": data['postings'][i]['price']})
#					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price1": data['postings'][i]['price'], "numBed": 1, "city": data['postings'][i]['location']['city']})
#					dataOld.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price'], "numBed": 1, "city": data['postings'][i]['location']['city']})
                                  if data['postings'][i]['location']['city'] == 'USA-SFO-ATH':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price1": data['postings'][i]['price'], "numBed": 1, "city": "Atherton"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price'], "numBed": 1, "city": "Atherton"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-CUP':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price1": data['postings'][i]['price'], "numBed": 1, "city": "Cupertino"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price'], "numBed": 1, "city": "Cupertino"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-LOA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price1": data['postings'][i]['price'], "numBed": 1, "city": "Los Altos"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price'], "numBed": 1, "city": "Los Altos"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-MEN':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price1": data['postings'][i]['price'], "numBed": 1, "city": "Menlo Park"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price'], "numBed": 1, "city": "Menlo Park"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-MUA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price1": data['postings'][i]['price'], "numBed": 1, "city": "Mountain View"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price'], "numBed": 1, "city": "Mountain View"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-PAL':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price1": data['postings'][i]['price'], "numBed": 1, "city": "Palo Alto"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price'], "numBed": 1, "city": "Palo Alto"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-RED':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price1": data['postings'][i]['price'], "numBed": 1, "city": "Redwood City"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price'], "numBed": 1, "city": "Redwood City"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-STA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price1": data['postings'][i]['price'], "numBed": 1, "city": "Stanford"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price'], "numBed": 1, "city": "Stanford"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-SUN':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price1": data['postings'][i]['price'], "numBed": 1, "city": "Sunnyvale"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price1": data['postings'][i]['price'], "numBed": 1, "city": "Sunnyvale"})
				elif data['postings'][i]['annotations']['bedrooms'] == '2br':
#				dataNew.append({"date": data['postings'][i]['timestamp'], "price": data['postings'][i]['price'], "bedrooms": data['postings'][i]['annotations']['bedrooms'], "location": data['postings'][i]['location']['city']})
#					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price2": data['postings'][i]['price'], "numBed": 2, "city": data['postings'][i]['location']['city']})
#					dataOld.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price'], "numBed": 2, "city": data['postings'][i]['location']['city']})
                                  if data['postings'][i]['location']['city'] == 'USA-SFO-ATH':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price2": data['postings'][i]['price'], "numBed": 2, "city": "Atherton"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price'], "numBed": 2, "city": "Atherton"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-CUP':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price2": data['postings'][i]['price'], "numBed": 2, "city": "Cupertino"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price'], "numBed": 2, "city": "Cupertino"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-LOA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price2": data['postings'][i]['price'], "numBed": 2, "city": "Los Altos"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price'], "numBed": 2, "city": "Los Altos"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-MEN':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price2": data['postings'][i]['price'], "numBed": 2, "city": "Menlo Park"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price'], "numBed": 2, "city": "Menlo Park"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-MUA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price2": data['postings'][i]['price'], "numBed": 2, "city": "Mountain View"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price'], "numBed": 2, "city": "Mountain View"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-PAL':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price2": data['postings'][i]['price'], "numBed": 2, "city": "Palo Alto"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price'], "numBed": 2, "city": "Palo Alto"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-RED':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price2": data['postings'][i]['price'], "numBed": 2, "city": "Redwood City"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price'], "numBed": 2, "city": "Redwood City"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-STA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price2": data['postings'][i]['price'], "numBed": 2, "city": "Stanford"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price'], "numBed": 2, "city": "Stanford"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-SUN':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price2": data['postings'][i]['price'], "numBed": 2, "city": "Sunnyvale"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price2": data['postings'][i]['price'], "numBed": 2, "city": "Sunnyvale"})
				elif data['postings'][i]['annotations']['bedrooms'] == '3br':
#				dataNew.append({"date": data['postings'][i]['timestamp'], "price": data['postings'][i]['price'], "bedrooms": data['postings'][i]['annotations']['bedrooms'], "location": data['postings'][i]['location']['city']})
#					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price3": data['postings'][i]['price'], "numBed": 3, "city": data['postings'][i]['location']['city']})
#					dataOld.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price'], "numBed": 3, "city": data['postings'][i]['location']['city']})
                                  if data['postings'][i]['location']['city'] == 'USA-SFO-ATH':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price3": data['postings'][i]['price'], "numBed": 3, "city": "Atherton"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price'], "numBed": 3, "city": "Atherton"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-CUP':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price3": data['postings'][i]['price'], "numBed": 3, "city": "Cupertino"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price'], "numBed": 3, "city": "Cupertino"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-LOA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price3": data['postings'][i]['price'], "numBed": 3, "city": "Los Altos"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price'], "numBed": 3, "city": "Los Altos"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-MEN':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price3": data['postings'][i]['price'], "numBed": 3, "city": "Menlo Park"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price'], "numBed": 3, "city": "Menlo Park"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-MUA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price3": data['postings'][i]['price'], "numBed": 3, "city": "Mountain View"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price'], "numBed": 3, "city": "Mountain View"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-PAL':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price3": data['postings'][i]['price'], "numBed": 3, "city": "Palo Alto"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price'], "numBed": 3, "city": "Palo Alto"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-RED':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price3": data['postings'][i]['price'], "numBed": 3, "city": "Redwood City"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price'], "numBed": 3, "city": "Redwood City"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-STA':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price3": data['postings'][i]['price'], "numBed": 3, "city": "Stanford"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price'], "numBed": 3, "city": "Stanford"})
                                  elif data['postings'][i]['location']['city'] == 'USA-SFO-SUN':
					dataNew.append({"date": datetime.datetime.utcfromtimestamp(data['postings'][i]['timestamp']), "price3": data['postings'][i]['price'], "numBed": 3, "city": "Sunnyvale"})
					dataOld.append({"date": data['postings'][i]['timestamp'], "price3": data['postings'][i]['price'], "numBed": 3, "city": "Sunnyvale"})



		i = i + 1

        json.dump(dataOld, f3)
        f3.close()

	dataTable = gviz_api.DataTable(description)
	dataTable.LoadData(dataNew)

	jsonData = dataTable.ToJSon(columns_order=("date", "price0", "price1", "price2", "price3", "numBed", "city"), order_by="date")

	f2.write(jsonData)
#	json.dump(jsonData, f2)

	f2.close()

#  Let's make the call every three hours:
	time.sleep(10800)

#  I was making the call every eight hours originally, but I'd rather it catch up to present time faster, and I want to make very sure it keeps ahead of postings, rather than falling behind. It's not like calling eight times a day is going to break their system.
#	time.sleep(28800)
#	time.sleep(30)
