import boto3
from optparse import OptionParser

def parse_phoneandmsg():
    parser = OptionParser()
    parser.add_option("-n","--PhoneNumber", type = 'str', dest="phno")
    parser.add_option("-m","--Message", type = 'str', dest="msg")
    (options,args) = parser.parse_args()
    #print (type(str(options.phno)))
    #Call Send message
    return options.phno,options.msg

def send_msg(phno,msg):    
    session = boto3.Session(profile_name='default')
    sns=session.client('sns')    
    response = sns.publish (PhoneNumber = phno, Message = msg)
    print (phno,msg, response)

if __name__ == '__main__':   
    options,args = parse_phoneandmsg()
    send_msg(options,args)
