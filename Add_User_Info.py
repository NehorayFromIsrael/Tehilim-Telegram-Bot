from datetime import date
import Program.Get_Houer as Time


def Func(Bot_Variables):

    """   Adding user info to database    """
    Users_Mongo = Bot_Variables[10][0]
    Chat_ID = Bot_Variables[1]
    First_Name = Bot_Variables[2]
    UserName = Bot_Variables[3]

    user ={
    "chat_id":Chat_ID,
    "first_name":First_Name,
    "user_name":UserName,
    "joined_time": {"date":date.today().strftime("%d/%m/%Y"),"time":Time.Get_Houer()},
    "last_seen": {"date":date.today().strftime("%d/%m/%Y"),"time":Time.Get_Houer()},
    "bot_user":"",
    "user privileges":"user",
    "virtual_location":"Home_Page",
    "language": "default",
    "phone": "",

    "book": {"bookmark":"0","chapters":[]},
    "favorites": []
    ,
        "stats_chapters":{}
,
        "write_type": "right to left",
        "random_chapter": "0"
        ,"luck":"הגדר מזל",
        "neshama": {"name":"","place":0},
        "read for name": {"chat":"","name":""}

    }
    condition = Users_Mongo.find({"chat_id":Chat_ID}).count()>0
    if condition == False:

        # - Add user info - #
        Users_Mongo.insert_one(user)



