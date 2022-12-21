
## NOTE : THIS PROJECT IS GIVE SOME BASIC DATA OF USER GIVEN COMPANY WITH PARTICULAR DATE THIS PROJECT GIVE TWO DAYS DATA LIKE LOW,HIGH,OPEN,CLOSE,VOLUME,SYMBOL,EXCHANGE OR ETC ##


import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


stock_name = input("Enter your stock name like AAPL/AMZN/GOOGL that : ")
date_of_stock_from = input("Enter which date would like you formate is YYYY-MM-DD: ")
#date_of_stock_to = input("Enter the date whould you like end formate is YYYY-MM-DD: ")

stock_market_endpoint = "http://api.marketstack.com/v1/eod"


acces_key = "YOUR API KEY"
twi_account_sid = "YOUR TWI ACCOUNT SID"
auth_token = "YOUR TWI AUTH TOKEN"



stock_market_link = "https://www.nasdaq.com/"

param = {
    "access_key":acces_key,
    "symbols":stock_name,
    "exchange":"XNAS",
    "date_from":date_of_stock_from,
    # "date_to":date_of_stock_to,
    "interval":"24hour",
    "sort":"ASC",
    "limit":"2"
}

response = requests.get(url=stock_market_endpoint,params=param)
data = response.json()
print(data)



data_list_open_price_1 = data["data"][0]["open"]
data_list_high_price_1 = data["data"][0]["high"]
data_list_price_date_1 = data["data"][0]["date"]
data_list_symbol_1 = data["data"][0]["symbol"]
data_list_exchange_1 = data["data"][0]["exchange"]
data_list_low_price_1 = data["data"][0]["low"]
data_list_close_price_1 = data["data"][0]["close"]
data_list_volume_1 = data["data"][0]["volume"]
data_list_dividend_1 = data["data"][0]["dividend"]
data_list_split_factor_1 = data["data"][0]["split_factor"]
data_list_adj_high_1 = data["data"][0]["adj_high"]
data_list_adj_low_1 = data["data"][0]["adj_low"]
data_list_adj_close_1 = data["data"][0]["adj_close"]
data_list_adj_open_1 = data["data"][0]["adj_open"]
data_list_adj_volume_1 = data["data"][0]["adj_volume"]
date_1 = data["data"][0]["date"]


data_list_open_price_2 = data["data"][1]["open"]
data_list_high_price_2 = data["data"][1]["high"]
data_list_price_date_2 = data["data"][1]["date"]
data_list_symbol_2 = data["data"][1]["symbol"]
data_list_exchange_2 = data["data"][1]["exchange"]
data_list_low_price_2 = data["data"][1]["low"]
data_list_close_price_2 = data["data"][1]["close"]
data_list_volume_2 = data["data"][1]["volume"]
data_list_dividend_2 = data["data"][1]["dividend"]
data_list_split_factor_2 = data["data"][1]["split_factor"]
data_list_adj_high_2 = data["data"][1]["adj_high"]
data_list_adj_low_2 = data["data"][1]["adj_low"]
data_list_adj_close_2 = data["data"][1]["adj_close"]
data_list_adj_open_2 = data["data"][1]["adj_open"]
data_list_adj_volume_2 = data["data"][1]["adj_volume"]
date_2 = data["data"][1]["date"]

data_diff_oh = data_list_high_price_1-data_list_open_price_1

data_diff_oh_2 = float(data_list_high_price_2-data_list_open_price_2)

data_diff_volume = float(data_list_volume_2-data_list_volume_1)

data_diff_divi = float(data_list_dividend_2-data_list_dividend_1)

data_diff_split = float(data_list_split_factor_2-data_list_split_factor_1)

proxy_client = TwilioHttpClient()


client = Client(twi_account_sid,auth_token)

message = client.messages \
        .create(
        body=f"some information about your stock {stock_name} stock_date : {date_2,date_1} data_diff_oh : {data_diff_oh} \n data_diff_oh : {data_diff_oh_2} \n data_diff_volume : {data_diff_volume} \n data_diff_divi : {data_diff_divi} \n data_diff_split : {data_diff_split} \n stock_symbol : {data_list_symbol_1} \n stock_exchange : {data_list_exchange_1} \n and here is link you show your stock : {stock_market_link}",
        from_="YOUR twillo MO",

        to="TO RECIVER"
    )

print(message.status)
