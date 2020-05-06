import random
import string

def Func(Bot_Variables,stringLength=16):
    Names = Bot_Variables[10][2]
    while True:
        lettersAndDigits = string.ascii_letters + string.digits


        link = ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

        link_exist = Names.find({"link": link}).count() > 0

        if (not link_exist):
            break

    return link


