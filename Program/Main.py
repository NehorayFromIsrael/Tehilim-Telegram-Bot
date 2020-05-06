#!/usr/bin/python3

from telegram.ext.dispatcher import run_async
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import Add_User_Info as Add_User_Info
import Program.Inline_Funcs as Inline_Funcs
import Program.Markup_Funcs as Markup_Functions
import Program.Update_Last_Seen_And_UserName as Update_Last_Seen_And_UserName
import Program.Get_Bot_Variables as Get_Bot_Variables
import Message_Handler.Start.Start as START
import Message_Handler.Start.Message_Handler as MES_HANDEL
import Program.Update_Phone as Update_Phone
import Program.Update_Location as Update_Location
import time
import threading
import Program.root_keyboard as root_keyboard
from Program.Send import Send as Send
from Program.Button import Button as Button
import Other_Functions.Send_chapter as SSend_chapter
import  Other_Functions.Send_Book as Send_Book

import Other_Functions.favoriets_name_random as favoriets_name
#*******************************************************************************************



class Telegram_Bot(object):

    """ this class includes the bot dispatcher(task manager), defenition of start command in the bot and messeage handler"""

    TOKEN = ''


    Bot_Variables = []

    #*******************************************************************************************

    # - Bot Dispatcher (bot task manager) - #
    @classmethod
    def bot_dispatcher(cls):

        # - Creating dispatcher object - #
        updater = Updater(cls.TOKEN,use_context=True,workers=32)
        dispatcher = updater.dispatcher



        # - Add Bot Start Command To Dispatcher - #
        dispatcher.add_handler(CommandHandler("start", cls.deep_linked, Filters.regex("T")))

        start_comm = CommandHandler('start', cls.start)
        dispatcher.add_handler(start_comm)


        # - Add Bot Message Handler Command To Handel Mesagess (Recives messages and decide what to do) - #



        dispatcher.add_handler(MessageHandler(Filters.all, cls.Message_Handler))

        # - Add inline patterns - #
        Inline_Functions_list = Inline_Funcs.Func()



        for i in range(len(Inline_Functions_list)):
            dispatcher.add_handler(CallbackQueryHandler(Inline_Functions_list[i][0], pattern=Inline_Functions_list[i][1]))


        # - Start checking for updates (checking for new messages) - #
        updater.start_polling()

        # - If the program close, stop getting updates - #
        updater.idle()


    # - Start command - #
    @classmethod
    @run_async
    def start(cls,update, context):

        cls.Bot_Variables = Get_Bot_Variables.Func([update,context])

        START.Func(update, context)

        # - save user information in database - #
        Add_User_Info.Func(cls.Bot_Variables)




    @classmethod
    @run_async
    def deep_linked(cls,update, context):
        cls.start(update, context)
        cls.Bot_Variables = Get_Bot_Variables.Func([update,context])
        deep_link = update["message"]["text"]
        seperator = ""





        for i in range(8,len(deep_link),1):
            seperator = seperator + deep_link[i]

        if len(seperator) <4:
            chapter = int(seperator)
            Users = cls.Bot_Variables[10][0]
            Users.update_one({"chat_id": cls.Bot_Variables[1]}, {"$set": {"random_chapter": chapter}})

            Send.Inline_Keyboard(cls.Bot_Variables, Send_Book.Func(chapter, cls.Bot_Variables),
                                 Button.Inline(
                                     ["C", favoriets_name.Func(update, context), "add_random_chapter_to_favoeites"]),
                                 Button.Inline(["C", "🔴 סמן כנקרא 🔴", "mark_random_as_read"])
                                 )








        Users = cls.Bot_Variables[10][0]
        Names = cls.Bot_Variables[10][2]

        name = Names.find_one({"seperator":seperator})


        men_name = name["name"]
        chat = name["chat_id"]


        to = name["for"]

        stats = name["chapters_stats"]

        Chapter = ""
        chapters_read = len(stats)


        if len(stats) < 150:
            for i in range(150):
                 if (not i in stats):
                     Chapter = i
                     break

            Users.update_one({"chat_id": cls.Bot_Variables[1]}, {"$set": {"read for name.name": [men_name,Chapter ]}})
            Users.update_one({"chat_id": cls.Bot_Variables[1]}, {"$set": {"read for name.chat": chat}})
            next = name["link"]

            llist = [Chapter,chapters_read,men_name,to,cls.Bot_Variables]

            t =  SSend_chapter.Func(llist)


            Send.Inline_Keyboard(cls.Bot_Variables, t,

                             Button.Inline(["C", "⭕️ סמן כנקרא ⭕️", "mark_as_read_for_name"]),
                             Button.Inline(["u", "➕ פרק נוסף ➕️", next]))
        else:
            text = " ✡✅ קריאת פרקי ספר התהילים {} {} הסתיימה בהצלחה ✅️✡️🙏🙏🙏".format(to ,men_name)
            Send.Message(cls.Bot_Variables,text)













#*******************************************************************************************

    # - Message Handler (Recives messages and decide what to do) - #
    @classmethod
    @run_async
    def Message_Handler(cls,update,context):

        cls.Bot_Variables = Get_Bot_Variables.Func([update,context])
        Markup_Functions.Func(cls.Bot_Variables)


        MES_HANDEL.Func(update,context)

        # - update last seen and username - #
        Update_Last_Seen_And_UserName.Func(cls.Bot_Variables)

        Update_Phone.Func(cls.Bot_Variables)
        Update_Location.Func(cls.Bot_Variables)
        root_keyboard.Func(cls.Bot_Variables)
#*******************************************************************************************

