from datetime import datetime
import requests
import csv
from models.Zerodha_Master_List import Zerodha_Master_List
from database.database import DBSession
from pprint import pprint
import json

a = requests.get("https://api.kite.trade/instruments")

csvList = a.content.decode('utf-8')
csvList = csv.DictReader(csvList.splitlines(),delimiter=',')
my_list = list(csvList)
zerodha_master_list_line_items = list()
for line in my_list:
    list_item = Zerodha_Master_List()
    list_item.instrument_token = line['instrument_token']
    list_item.exchange_token = line['exchange_token']
    list_item.trading_symbol = line['tradingsymbol']
    list_item.security_name = line['name']
    list_item.last_price = line['last_price']
    list_item.expiry = line['expiry'] if line['expiry'] else None
    list_item.strike_price = line['strike']
    list_item.tick_size = line['tick_size']
    list_item.lot_size = line['lot_size']
    list_item.instrument_type = line['instrument_type']
    list_item.segment = line['segment']
    list_item.exchange = line['exchange']
    list_item.insertion_timestamp = datetime.now().date()
    zerodha_master_list_line_items.append(list_item)

DBSession.bulk_save_objects(zerodha_master_list_line_items)
DBSession.commit()