import Other_Functions.send_neshama as send_neshama
from Program.Send import Send as Send
from Program.Button import Button as Button


import Other_Functions.rolling_left_neshama as rolling_left
import Other_Functions.rolling_right_neshama as rolling_right

def Func(Bot_Variables):


    Chat_ID = Bot_Variables[1]

    Message = Bot_Variables[4]
    Users = Bot_Variables[10][0]
    update = Bot_Variables[12]
    context = Bot_Variables[14]


    Users.update_one({"chat_id": Chat_ID}, {"$set": {"neshama.name" : Message}})

    write_type = Users.find_one({"chat_id": Chat_ID})["write_type"]


    Send.Inline_Keyboard(Bot_Variables, send_neshama.Func(Message[0] , Bot_Variables),
                                Button.Inline(["C", "⬅️", rolling_left.Func(write_type)],

                                              ["C", "➡️", rolling_right.Func(write_type)]))

    Users.update_one({"chat_id": Chat_ID}, {"$set": {"virtual_location" : "עוד ➕"}})
    Users.update_one({"chat_id": Chat_ID}, {"$set": {"neshama.place" : 0}})
