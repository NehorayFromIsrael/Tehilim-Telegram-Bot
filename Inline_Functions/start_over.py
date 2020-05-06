import Program.Get_Bot_Variables as Get_Bot_Variables
from Program.Send import Send as Send
from Program.Button import Button as Button
import threading
import Other_Functions.Send_Book as Send_Book
import Other_Functions.favoriets_name as favoriets_name
import Other_Functions.is_read_name as is_read_name
import Other_Functions.rolling_left as rolling_left
import Other_Functions.rolling_right as rolling_right

def Func(update,context):

    threading.Thread(target=Your_Code,args=(update,context)).start()


# - use this template to create functions in your bot , variables and functions are listed down below - #
# - its highly recommended not to change any line from this template (just add your code down below, dont edit any existing lines) - #





def Your_Code(update,context):

    """
    ---- imports ----

    from Program.Send import Send as Send

    from Program.Button import Button as Button

    import Program.Get_Bot_Variables as Get_Bot_Variables

    import threading

    """

    Bot_Variables = Get_Bot_Variables.Func([update,context])

    # - Variables - #
    """
    TOKEN = Bot_Variables[0]
    Chat_ID = Bot_Variables[1]
    First_Name = Bot_Variables[2]
    UserName = Bot_Variables[3]
    Message = Bot_Variables[4]
    Message_ID = Bot_Variables[5]
    File_ID = Bot_Variables[6]
    Virtual_Location = Bot_Variables[7]
    User_Privileges = Bot_Variables[8]
    User_Lang = Bot_Variables[9]
    Mongo_Collections = Bot_Variables[10]
    Json_Message = Bot_Variables[11]
    Update = Bot_Variables[12]
    Other_Variables = Bot_Variables[13]
    Context = Bot_Variables[14]
    
    """

    """
    --- Send Class ---


Send.Message(Bot_Variables,"Paste Text Here")

Send.Keyboard(Bot_Variables, "Text Here",
                  Button.Markup("button 1"),
                  Button.Markup(Button.Markup_Location("Send_Location")),
                  Button.Markup( Button.Markup_Phone("Send_Phone") , "button 5", "button 6"))



#NOTE: when when you used Button.Inline() for creating buttons for inline keyboard this is the syntax:
# ["URL/CALLBACK Button type( u/c )","button text","the url or callback name"]
# the callback name is the name you gave to the file you created in "Inline_Function" folder (not include the .py extinction)

Send.Inline_Keyboard(Bot_Variables, "Text Here" ,
                         Button.Inline(  ["U","URL Button","https://www.google.co.il/"] ,  ["C","Callback Button","Template"] ) ,
                         Button.Inline(["C","Callback Button","Template"] ,["U","URL Button","https://www.google.co.il/"])
                         )

# send edited keyboard, its edit current inline keyboard and change buttons give deep navigation effect

Send.Edited_Inline_Keyboard(Bot_Variables,"Text Here",
                            Button.Inline(["u","URL Button","www.google.co.il"])
                            )


Send.Callback_Answer(Bot_Variables,"Callback Query Answer")

Send.Callback_Alert(Bot_Variables,"Callback Query Alert")

Send.Forword(Bot_Variables,from_chat_id,to_chat_id,message_id)


# send any file by file id , type : video/voice message/photo/document/sticker
Send.Any_File(Bot_Variables,file_id,caption)


--- Buttons Types ---

# regular markup button
Button.Markup("button text1","button text2")

# make button markup to send user location
Button.Markup_Location("button text")

# make button markup to send user phone number
Button.Markup_Phone("button text")

# regular inline button
Button.Inline( ["URL/CALLBACK Button type( u/c )","button text","the url or callback name"])

#syntax:

* each time activated gives 1 rows of buttons


#Markup synatx
Send.Keyboard(Bot_Variables, "Text Here",
                  Button.Markup("button 1"),
                  Button.Markup(Button.Markup_Location("Send_Location")),
                  Button.Markup( Button.Markup_Phone("Send_Phone") , "button 5", "button 6"))


#Inline synatx
#NOTE: when when you used Button.Inline() for creating buttons for inline keyboard this is the syntax:
# ["URL/CALLBACK Button type( u/c )","button text","the url or callback name"]
# the callback name is the name you gave to the file you created in "Inline_Function" folder (not include the .py extinction)

Send.Inline_Keyboard(Bot_Variables, "Text Here" ,
                         Button.Inline(  ["U","URL Button","https://www.google.co.il/"] ,  ["C","Callback Button","Template"] ) ,
                         Button.Inline(["C","Callback Button","Template"] ,["U","URL Button","https://www.google.co.il/"])
                         )

    """




    Chat_ID = Bot_Variables[1]
    Users = Bot_Variables[10][0]

    user = Users.find_one({"chat_id":Chat_ID})

    chapter = int(user["book"]["bookmark"])
    book_chapters = user["book"]["chapters"]
    is_read_chapters = len(user["book"]["chapters"])
    write_type = user["write_type"]


    Users.update_one({"chat_id": Chat_ID}, {"$set": {"book.chapters": []}})
    Users.update_one({"chat_id": Chat_ID}, {"$set": {"book.bookmark": 0}})


    Send.Edited_Inline_Keyboard(Bot_Variables, Send_Book.Func(0,Bot_Variables),
                                Button.Inline(["C", "⬅️", rolling_left.Func(chapter,book_chapters,write_type)],
                                              ["C", favoriets_name.Func(update, context), "Favorite"],
                                              ["C", "➡️", rolling_right.Func(chapter,book_chapters,write_type)]),
                                Button.Inline(["C", is_read_name.Func(update, context), "is_read"]))