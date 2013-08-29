import Facebook
import os
import datetime
now = datetime.datetime.now()

facebook = Facebook.GraphAPI('<ACCESS_TOKEN')
user = facebook.get_object("me")

def Wall_post(Birthday):
    for user in Birthday:
        facebook.put_wall_post("Happy Birthday :)",{},str(user['uid']))
  
def FB_friendBirthday():    
    friends = facebook.get_connections(user["id"], "friends")
    query = """SELECT uid,birthday_date FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())"""
    UserDetail = facebook.fql(query);
    detail = UserDetail['data']
    TodayBirthDay=[]
    for friend in detail:
        if (friend['birthday_date'] is not None):
            birthdate = (friend['birthday_date']).split('/')
            if ( int(birthdate[0]) == now.month and int(birthdate[1]) == now.day):
                TodayBirthDay.append(friend)
    return TodayBirthDay

if __name__=="__main__":
    Result = FB_friendBirthday()
    Wall_post(Result)
