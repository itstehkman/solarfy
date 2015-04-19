import urllib
import json
values = {}
count = 0
url = "https://utilityapi.com/api/services.json?access_token=hackathontoken"
response = urllib.urlopen(url);
data = json.loads(response.read())
for x in range (0, 15):
    key = data[x]["utility_billing_address"]
    total = 0
    billcount = data[x]["bill_count"]
    billUrl = "https://utilityapi.com/api/services/" + data[x]["uid"] + "/bills.json?access_token=hackathontoken"
    responseNew = urllib.urlopen(billUrl)
    billData = json.loads(responseNew.read())
    
    for y in range(len(billData)):
        total += billData[y]["bill_total"]


    total = total/y;
    newtotal = round(total, 2)
    #total = total/100.00
    values[x] = (key.strip().split(",")[0],newtotal)
js=json.dumps(values)

print js