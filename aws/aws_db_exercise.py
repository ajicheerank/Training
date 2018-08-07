import requests as rq
import boto3 as boto
import zipfile
import fileinput

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
                bucket_exer.download_file(files.key,"D:/Users/AjiCheeranK/Downloads/airbnb_data/zips/" + files.key)
                z_file = zipfile.ZipFile("D:/Users/AjiCheeranK/Downloads/airbnb_data/zips/" + files.key,"r")
                z_file.extractall("D:/Users/AjiCheeranK/Downloads/airbnb_data/")
                z_file.close()


if __name__ == '__main__':
    download_file('aarhus')


    room_data = rq.get(url="https://s3.amazonaws.com/tomslee-airbnb-data-2/", stream = True)
    #host_data = rq.get(url="http://airbnb.com/users/show/host_id", stream = True)
    
    #print(room_data.content)
    
    fs = open("airbnb_room_data.xml","w")
    fs.write(str(room_data.text))
    fs.close()
    
    #for line in fileinput.input("airbnb_room_data.xml", inplace=True):
        #line.replace("><",">\n<")