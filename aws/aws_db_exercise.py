import requests as rq
import boto3 as boto
import zipfile
import fileinput
import pandas as pd
import os
import csv
import pprint

b_session = boto.Session(profile_name = "default")
b_client = b_session.client("s3")
b_resource = boto.resource("s3")
bucket_exer = b_resource.Bucket("tomslee-airbnb-data-2")
bucket_aji = b_resource.Bucket("aji-invesco-bucket1")

def download_file(location):
    for files in bucket_exer.objects.all():   
        if files.key[:-4].lower() == location.lower() or location.lower() == "all":
            #bucket_aji.copy({"Bucket":bucket_exer.name, "Key": files.key}, "airbnb_data/" + files.key)            
            if files.key[-4:].lower() == ".zip":
                bucket_exer.download_file(files.key, download_folder + files.key)                
                z_file = zipfile.ZipFile(download_folder + files.key, "r")
                z_file.extractall(extract_folder)
                z_file.close()
                if os.path.exists(data_folder+ files.key[:-4].lower()+"\\"):
                    for file in os.listdir(data_folder + files.key[:-4].lower()+"\\"):
                        print(file)
                        df = pd.read_csv(data_folder + files.key[:-4].lower()+"\\"+str(file))
                        df['city'] = files.key[:-4].lower()
                        df[col].to_csv(output_folder + output_file_name, index = False, header = False, mode = 'a')                
                    
                z_file.close()
    
def create_outputfile(filename):
    if os.path.exists(filename):
        os.remove(filename)
    with open (filename, "w") as fs:
        fs.write("city,room_id,host_id,room_type,borough,neighborhood,reviews,overall_satisfaction,accommodates,accommodates,minstay,last_modified")
        fs.close()
        return True
        
if __name__ == '__main__':
    #init variables
    col = ['city','room_id','host_id','room_type','borough','neighborhood','reviews','overall_satisfaction','accommodates','price','minstay','last_modified']
    download_folder = "D:/Users/AjiCheeranK/Downloads/airbnb_data/zips/"
    extract_folder = "D:/Users/AjiCheeranK/Downloads/airbnb_data/"
    output_folder = "D:\\Users\\AjiCheeranK\\Downloads\\airbnb_data\\s3_files\\"
    output_file_name = "Master.csv"
    
    #create a output file with headers
    if create_outputfile(output_folder + output_file_name):
        download_file('all')
        
    #upload the master file to s3 bucket
    if os.path.exists(filename):
        bucket_aji.upload_file(Filename= output_folder + output_file_name, Key = "airbnb_data/" + output_file_name)
    
    