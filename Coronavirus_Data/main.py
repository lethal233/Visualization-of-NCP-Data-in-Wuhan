import new_death_and_discharged_and_confirmed as m1
import culmulated_death_and_discharged as m2
import death_and_discharged_rates as m3
import Critical_and_Current as m4
import culmulated_cases as m5


print("----------------------------------------------------------------------------")
print("|                         SELECT MODE TO MOVE ON                           |")
print("| 1. The statistics about the new death & discharged & confirmed cases     |")
print("| 2. The statistics about the culmulated death & discharged cases          |")
print("| 3. The statistics about the death & discharged rates                     |")
print("| 4. The statistics about the critical & current cases                     |")
print("| 5. The statistics about the culmulated cases                             |")
print("----------------------------------------------------------------------------")

while(True):
    msg = input("To select the mode(1,2,3,4,5), and input 0 to exit: ")
    try:
        a = int(msg)
    except ValueError:
        print("Please input the right form...")
        continue
    else:
        if a == 1:
            m1.graphing()
        elif a == 2:
            m2.graphing()
        elif a == 3:
            m3.graphing()
        elif a == 4:
            m4.graphing()
        elif a == 5:
            m5.graphing()
        elif a == 0:
            break
        else:
            print("please input the correct value....")
print("-----------------------Exit the program-------------------------------------")
