import requests, json, time

ENDPOINT = "https://deribit.com/api/v2/public/get_book_summary_by_currency"
INTERVAL = 15*60
PARAMS_BTC = {"currency" : "BTC", "kind" : "option"}
PARAMS_ETH = {"currency" : "ETH", "kind" : "option"}


def get_data(params, data):
	try:
		response = requests.get(ENDPOINT, params = params)
	except:
		print(time.asctime(), params["currency"], "error when requesting files")
		return
	response_json = response.json()
	if "error" in response_json:
		print(time.asctime(), params["currency"], "error within response")
		data[response_json['usOut']] = response_json["error"]
	else:
		print(time.asctime(), params["currency"], "data acquisition successful")
		data[response_json['usOut']] = response_json["result"]

	
def save_file(data, cur):
	with open(cur+time.asctime()+".json", "w") as fp:
		json.dump(data, fp, indent = "\t")
		data.clear()


def main(data_btc, data_eth):
	while True:
		get_data(PARAMS_BTC, data_btc)
		get_data(PARAMS_ETH, data_eth)	
		if(time.localtime().tm_hour == 23 and time.localtime().tm_min>=45):
			save_file(data_btc, "BTC ")
			save_file(data_eth, "ETH ")
		time.sleep(INTERVAL)
	
if __name__ == "__main__":
	data_btc = dict()
	data_eth = dict()
	try:
		main(data_btc, data_eth)
	except KeyboardInterrupt:
		print("Interrupted by user")
	finally:
		save_file(data_btc, "BTC ")
		save_file(data_eth, "ETH ")
