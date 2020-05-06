import Program.Connect_To_Mongo as CM
from Program.Send import Send as Send

TOKEN = "1102932689:AAFXsw2xyFRDd_7XBUkEDFHp_uzX3jXLfL0"

database = "Tehilim"
collection = "Users"

test_id = 42155571
activate = False

message_text = "לקהל המשתמשים שלנו אנחנו שמחים לבשר שעדכנו את הבוט , נוספו האפשרויות להשתמש בקריאה משותפת , לאותיות נשמה שמירה במועדפים ועוד! על מנת לקבל את העדכון פשוט לחצו על הפקודה /start 😜😎😇"


#__________________________________________________________________________________________________________
Users = CM.Func(database,collection)

ids = Users.find({})
len_ids = Users.count_documents({})
chats = []
print("Total Users:",str(len_ids),"\n")
if activate:

    for i in range(len_ids):
        chats.append(ids[i]["chat_id"])

    for i in range(len_ids):
        Send.Message([TOKEN,chats[i]],message_text)

else:
    for i in range(len_ids):
        chats.append(ids[i]["chat_id"])
    print(chats)

    Send.Message([TOKEN, test_id], message_text)