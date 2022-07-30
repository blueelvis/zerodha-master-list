from google.cloud import storage
from datetime import datetime, timezone, timedelta
import requests

def zerodha_master_list_dumper(request):
    zerodha_instrument_csv_list_response = requests.get("https://api.kite.trade/instruments")
    zerodha_instrument_csv_list_response.raise_for_status()

    csvList = zerodha_instrument_csv_list_response.content.decode('utf-8')
    storage_client = storage.Client()
    storage_bucket = storage.Bucket(storage_client, name="zerodha-master-list-data")

    blob_file_name = datetime.now(timezone(timedelta(hours=5.5))).strftime("%Y_%m_%d.csv")
    storage_blob = storage_bucket.blob(blob_name= blob_file_name)
    storage_blob.upload_from_string(csvList,content_type='text/csv')

    return f"Dumped successfully."
