import Program.Connect_To_Mongo as Mon



# - SET BOT TOKEN - #

#TOKEN = "1102932689:AAFXsw2xyFRDd_7XBUkEDFHp_uzX3jXLfL0"
TOKEN = ""

#_______________________________________________________#
# - SET DATABASES - #

# - database names list - #
Database_Name = ["Tehilim2"]


# - get collections use func: Mon.Func(Database_Name,Collection_Name) - #
Mongo_Users = Mon.Func(Database_Name[0], "Users")
Mongo_Locations = Mon.Func(Database_Name[0], "Locations")
Mongo_Names = Mon.Func(Database_Name[0], "Names")


# - Add mongo collections to list - # 
collections = [Mongo_Users,Mongo_Locations,Mongo_Names]

#_______________________________________________________#

# - PASS OTHER VARIABLES INSIDE "Bot_Variables" ARREY

Other_Variables = []


# - requirements , add to list for automatic req installation- #
req = []

