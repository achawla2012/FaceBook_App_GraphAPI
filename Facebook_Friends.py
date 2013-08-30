import Facebook
import os

facebook = Facebook.GraphAPI('<ACCESS_TOKEN>')
user = facebook.get_object("me")

#Post message on the wall of group with ID = "GroupID"
def PostOnGroupWall(GroupID):
    facebook.put_object(GroupID, "feed", message="<MESSAGE>")    

#List out the friends' name who are in the friend list.
def facebook_friend():    
    friends = facebook.get_connections(user["id"], "friends")
    for friend in friends['data']:
        print friend['name'].encode('utf-8')

if __name__=="__main__":
    facebook_friend()
    PostOnGroupWall("<GROUP_ID>")
