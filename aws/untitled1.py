import boto3
import json

session = boto3.Session(profile_name = "default")
cli = session.client('iam')

def create_group(grp_name):
    response = cli.create_group(GroupName=grp_name)
    return response

def create_user(usr_name):
    response = cli.create_user(UserName = usr_name)
    return response

def add_user_to_grp(grp_name, usr_name):
    response = cli.add_user_to_group(GroupName = grp_name, UserName = usr_name)
    return response

def rem_user_from_grp(grp_name, usr_name):
    response = cli.remove_user_from_group(GroupName = grp_name, UserName = usr_name)
    return response

def rem_user(usr_name):
    response = cli.delete_user(UserName = usr_name)
    return response

def get_user(usr_name):
    response = cli.get_user(UserName = usr_name)
    UserName,  UserId = "", ""
    
    for sstr,value in response['User'].items():                
        if sstr == "UserName" :
            UserName =  value
        elif sstr == "UserId" :
            UserId = value
    return "User Name = {} and User ID = {}".format(UserName,UserId)

def get_group(grp_name):
    response = cli.get_group(GroupName = grp_name)
    user_list = []
    group_name = ""
    for sstr in response['GroupName']:
        print(sstr)
        #group_name = sstr['GroupName']
        
    for sstr in response["Users"]:
        user_list.append(sstr['UserName'])
        #pass
        #print (sstr,value)
    
    
    return response

if __name__ == '__main__':
    
    usr,grp = "kunhua", "Invesco_Training"
    
    #create_group(grp)
    print (get_group(grp))
    #create_user(usr)
    print (get_user(usr))
    #add_user_to_grp(grp,usr)
    #rem_user_from_grp(grp,usr)
    #print (get_group(grp))
    #rem_user(usr)
    #print (get_user(usr))
    

