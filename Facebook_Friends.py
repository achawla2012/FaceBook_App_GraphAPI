import Facebook
import os

def facebook_friend():    
    facebook = Facebook.GraphAPI('<ACCESS_TOKEN>')
    user = facebook.get_object("me")
    friends = facebook.get_connections(user["id"], "friends")
    for friend in friends['data']:
        print friend['name'].encode('utf-8')


if __name__=="__main__":
    facebook_friend()
