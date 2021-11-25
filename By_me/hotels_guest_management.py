
#####################OPERATION FUNCTION#################################
def process():
    guest_list = []
    guest_num = int(input("How many guests will you proceed ? "))
    i = 0
    while i <= guest_num:
        guest_name = str(input("Input the guest {} exact name: ".format(i)))
        guest_list.append(guest_name)
        i += 1
    return guest_list



######################REGISTER NEW GUESTS###############################""
#fill a file with the list returned by process function  content
def sign_in():
    new_guests = process()
    with open("guests.txt", "a") as guests:
        for i in new_guests:
            guests.write(i + "\n")
    guests.close()



##############REMOVE GUESTS WHO ARE LEAVING IN GUESTS LIST################
def sign_out():
    check_out_guests = process()
    temporary_list = []
    with open("guests.txt") as guests:
        for g in guests:
            temporary_list.append(g.strip())

    with open("guests.txt", "w") as guests:
        for name in temporary_list:
            if name not in check_out_guests:
                guests.write(name + "\n")



##############VERIFY IF GUESTS ARE STILL IN  HOTEL##########################
def checking():
    guests_to_check = process()
    checked_in = []

    with open("guests.txt","r") as guests:
        for g in guests:
            checked_in.append(g.strip())
        for g_c in guests_to_check:
            if g_c in checked_in:
                print("{} is checked in".format(g_c))
            else:
                print("{} is not checked in".format(g_c))



#############################CHOOSE WHAT TO DO###################################
to_do = int(input("What do you want to do ? \nPlease choose \n(1) for guests registration \n(2) for guests unsubscription \n(3) for guests checking \nEnter your choice : "))
if to_do == 1:
    sign_in()
elif to_do == 2:
    sign_out()
else:
    checking()





####################################################################################
"""Problems and future improvments :
    -Start conting from 1
    -Prevent the add of a guests more than one time
    -Handle user error : data type errors (ex: int instead str / name instead number)
"""
