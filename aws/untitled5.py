import fix_yahoo_finance as fy
from datetime import date, timedelta
from time import strftime
import boto3
import pprint as pp

#init Variables
today = date.today()
yday = today - timedelta(1)
dformat = '%Y-%m-%d'

#init s3
session = boto3.Session(profile_name = "default")
s3_res = session.resource("s3")
bucket_aji = s3_res.Bucket("aji-invesco-bucket")

def upload_files_to_s3(file_list):
    try:
        for file in file_list:
            bucket_aji.upload_file(file, file)
    except Exception as x:
        pp.pprint(x)

def download_data_4_symbols(ticker):
    try:
        data = fy.download('MMM',yday.strftime(dformat),today.strftime(dformat))
        return data
    except Exception as e:
        pp.pprint(e)
    
def write_to_file(file_name, data):
    fs = open(file_name, "a")
    fs.write(data.to_csv())
    fs.close()
    return file_name


if __name__ == "__main__":
    lstTicker = input("Input ticker seperated by , : ").split(",")
    file_list = []
    for ticker in lstTicker:        
        data = download_data_4_symbols(ticker)
        file_name = write_to_file(ticker+".txt", data)
        file_list.append(file_name)
    #upload the file to s3
    upload_files_to_s3(file_list)