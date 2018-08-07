import fix_yahoo_finance as fy
from datetime import date, timedelta
from time import strftime
import boto3
import pprint as pp

#init Variables
today = date.today()
yday = today - timedelta(5)
dformat = '%Y-%m-%d'

#init s3
session = boto3.Session(profile_name = "default")
s3_res = session.resource("s3")
s3_cli = session.client("s3")
bucket_aji = s3_res.Bucket("aji-invesco-bucket")
bucket_aji1 = s3_res.Bucket("aji-invesco-bucket1")

def download_files_from_bucket():
    paginator =  s3_cli.get_paginator("list_objects")
    for result in paginator.paginate(Bucket = bucket_aji.name):
        if result.get("Contents") is not None:
            for file in result.get("Contents"):
                s3_res.meta.client.download_file(bucket_aji.name, file.get("Key"), file.get("Key"))

def copy_files_from_1bucket_to_2bucket():
    for file in bucket_aji.objects.all():
        source = {"Bucket" : bucket_aji.name, "Key" : file.key}
        bucket_aji1.copy(source,file.key)
        

def upload_files_to_s3(file_list):
    try:
        for file in file_list:
            bucket_aji.upload_file(file, file)
    except Exception as x:
        pp.pprint(x)
        
def remove_files_from_s3():
    try:
        for file in bucket_aji.objects.all():
            print(file)
            file.delete()            
    except Exception as x:
        pp.pprint(x)
    

def download_data_4_symbols(ticker):
    try:
        data = fy.download(ticker,yday.strftime(dformat),today.strftime(dformat))
        return data
    except Exception as e:
        pp.pprint(e)
    
def write_to_file(file_name, data):
    try:
        fs = open(file_name, "a")
        fs.write(data.to_csv())
        fs.close()
        return file_name
    except Exception as e:
        pp.pprint(e)

if __name__ == "__main__":
    copy_files_from_1bucket_to_2bucket()
    #remove_files_from_s3()
    #download_files_from_bucket()
    #lstTicker = input("Input ticker seperated by , : ").split(",")
    file_list = []
    try:
        for ticker in lstTicker:   
            ticker = ticker.strip()
            #data = download_data_4_symbols(ticker)
            file_name = write_to_file(ticker+".txt", data)
            file_list.append(file_name)
        #upload the file to s3
        upload_files_to_s3(file_list)
    except Exception as e:
        pp.pprint(e)
        
    