import Program.Get_Bot_Variables as Get_Bot_Variables
from Program.Send import Send as Send
from Program.Button import Button as Button

# - use this template to create functions in your bot , variables and functions are listed down below - #
# - its highly recommended not to change any line from this template (just add your code down below, dont edit any existing lines) - #



def Func(update,context):

    """
    ---- imports ----

    import Program.Get_Bot_Variables as Get_Bot_Variables

    from Program.Send import Send as Send

    from Program.Button import Button as Button

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



    Message = Bot_Variables[4]

    Chat_ID = Bot_Variables[1]
    Users = Bot_Variables[10][0]
    Names = Bot_Variables[10][2]

    Users.update_one({"chat_id": Chat_ID}, {"$set": {"virtual_location" : "איזור אישי 🙎‍♂️"}})

    Names.update_one({"chat_id": Chat_ID,"status": "pending"}, {"$set": {"for":Message}})





    for_name = Message + " "+ Names.find_one({"chat_id":Chat_ID,"status":"pending"})["name"]


    text = """
    דוגמא איך יראה פרק תהילים כשמשתמש יקבל אותו עם השם שרשמת:
    
מספר הפרקים שנקראו על שם {}: 0 ( % 0.0  )
מספר פרקים שנשארו לסיום התהילים על שמו: 150 ( % 100.0  )

פרק: קל״ח ( 138 )

{}

לְדָוִד אוֹדְךָ בְכָל־לִבִּי נֶגֶד אֱלֹהִים אֲזַמְּרֶךָּ׃ אֶשְׁתַּחֲוֶה אֶל־הֵיכַל קָדְשְׁךָ וְאוֹדֶה אֶת־שְׁמֶךָ עַל־חַסְדְּךָ וְעַל־אֲמִתֶּךָ כִּי־הִגְדַּלְתָּ עַל־כָּל־שִׁמְךָ אִמְרָתֶךָ׃ בְּיוֹם קָרָאתִי וַתַּעֲנֵנִי תַּרְהִבֵנִי בְנַפְשִׁי עֹז׃ יוֹדוּךָ יְהוָה כָּל־מַלְכֵי־אָרֶץ כִּי שָׁמְעוּ אִמְרֵי־פִיךָ׃ וְיָשִׁירוּ בְּדַרְכֵי יְהוָה כִּי גָדוֹל כְּבוֹד יְהוָה׃ כִּי־רָם יְהוָה וְשָׁפָל יִרְאֶה וְגָבֹהַּ מִמֶּרְחָק יְיֵדָע׃ אִם־אֵלֵךְ בְּקֶרֶב צָרָה תְּחַיֵּנִי עַל אַף אֹיְבַי תִּשְׁלַח יָדֶךָ וְתוֹשִׁיעֵנִי יְמִינֶךָ׃ יְהוָה יִגְמֹר בַּעֲדִי יְהוָה חַסְדְּךָ לְעוֹלָם מַעֲשֵׂי יָדֶיךָ אַל־תֶּרֶף׃
    
    """.format(for_name,for_name)

    Send.Inline_Keyboard(Bot_Variables, text,
                         Button.Inline(
                                       ["C", "✅ אשר ופרסם ✅", "aproove_post"],
                             ["C", "🖌️ ערוך שוב 🖌️", "post_name"]

                         ),

    Button.Inline(
        ["C", "❌ ביטול ❌", "canel_post"],


    )

                         )
