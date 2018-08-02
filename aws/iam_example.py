import boto3
import pprint

session = boto3.Session(profile_name = "default")
cli = session.client('iam')

def check_group(grp_name):  
    try:
        response = cli.get_group(GroupName = grp_name)    
        group_name = ""
        for sstr,value in response['Group'].items():
            if sstr in ['GroupName']:
                group_name = value
                if group_name == "":
                    return True        
            else:
                return Fasle
    except Exception as e:        
        pprint.pprint(e)
        return False

def create_group(grp_name):
    if check_group(grp_name):
        response = cli.create_group(GroupName=grp_name)
        if not check_group(grp_name): response = "Great! group created"
    else:
        response = "Group Already exists"           
        

        
    return response

def create_user(usr_name):
    response = cli.create_user(UserName = usr_name)
    return response

def add_user_to_grp(grp_name, usr_name):
    response = cli.add_user_to_group(GroupName = grp_name, UserName = usr_name)
    return response

def list_groups_for_user(usrName):
    group_list = cli.list_groups_for_user(UserName=usrName)
    return group_list

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
    for sstr,value in response['Group'].items():
        if sstr in ['GroupName']:
            group_name = value
    for sstr in response["Users"]:
        user_list.append(sstr['UserName'])
        #pass
        #print (sstr,value)
    return {group_name: user_list}

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
    

