import boto3
import requests
#from json2table import convert

session = boto3.Session(profile_name='default')
cli = session.client('rekognition')
    
def open_image(img):    
    #img = open(img,'r+')
    imgdata = img#.read()
        
    imgobj = {'Bytes':imgdata}
    imgAttr=['ALL']
    return imgobj,imgAttr
    
def detect_face_and_label(image,attribute):    
    face = cli.detect_faces(Image=image, Attributes=attribute)
    label = cli.detect_labels(Image=image)
    
    for details in face['FaceDetails']:
        for emotions in details['Emotions']:
            print ("Emotion Type = {} and Confidence = {}" .format(emotions['Type'], emotions['Confidence']))
    #print(face)
    #print(label)
    #to_table(fa
    
def get_image_from_url(url):
    req = requests.get(url, stream = True) 
    return req.content

def to_table(j_inp):
    table_attr = {"style" : "width:100%", "class" : "table table-striped"}
    print(convert(j_inp,build_direction = "TOP_TO_BOTTOM", table_attributes=table_attr))


if __name__ == '__main__':    
    
    input_url = input("input the list of url seperated by comma: ")
    lst_url = input_url.split(",")
    #print (lst_url)
    
    for url in lst_url:   
        print (url)
        img = get_image_from_url('http://stash.compciv.org/2017/obama.jpg')    
        img,attr = open_image(img)    
        detect_face_and_label(img,attr)
    
    #http://stash.compciv.org/2017/obama.jpg, http://stash.compciv.org/2017/trump.jpg
    
    
    
    
    
    
    