import requests, json, time

interval = 15*60
data = dict()
while True:
	endpoint = "https://test.deribit.com/api/v2/public/get_book_summary_by_currency"
	params = {"currency" : "BTC", "kind" : "option"}
	response = requests.get(endpoint, params = params)
	response_json = response.json()
	if "error" in response_json:
		print(time.asctime(), "error when requesting files")
		data[response_json['usOut']] = response_json["error"]
	else:
		print(time.asctime(), "data acquisition successful")
		data[response_json['usOut']] = response_json["result"]
	if(time.localtime().tm_hour == 23 and time.localtime().tm_min>45):
		with open(time.asctime()+".json", "w") as fp:
			json.dump(data, fp, indent = "\t")
			data.clear()
	time.sleep(interval)
