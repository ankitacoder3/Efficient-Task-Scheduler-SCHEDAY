# Schedule Library imported
import schedule
import time
import keyboard
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  

#Initializing

print("WELCOME to Scheday!")
print("Press:- space bar to enter new task; q to quit;")
wait_Tasks=[]
Tasks=[]
reschedule_time=10 #seconds
starve_time= 30 #seconds
SCHEDAY = 0
    
# Functions setup

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  

def Keyboard():
    if keyboard.is_pressed(' '):
        new()
        
    '''if keyboard.is_pressed(';'):
        print("Quiting SCHEDAY!")
        print(" press x to cancel")
        SCHEDAY = 1
        
    if keyboard.is_pressed('x'):
        SCHEDAY = 0'''

  
def new():
    clear()
    new_task=input("Enter new task: ")
    wait_Tasks.append(new_task)

def reschedule():
    i=5
    print(i)
    
def no_starve():
    i=500
    print(i)


# Task scheduling
schedule.every(1).seconds.do(Keyboard)
schedule.every(reschedule_time).seconds.do(reschedule)
schedule.every(starve_time).seconds.do(no_starve)


'''

# Every day at 12am or 00:00 time bedtime() is called.
schedule.every().day.at("12:24").do(bedtime)

# After every 5 to 10mins in between run work()
schedule.every(5).to(10).minutes.do(work)

# Every monday good_luck() is called
schedule.every().monday.do(good_luck)

# Every tuesday at 18:00 sudo_placement() is called
schedule.every().tuesday.at("18:00").do(sudo_placement)
'''
# Loop so that the scheduling task keeps on running all time
while True:
    #Keyboard()
    #print ("task runnuing")
    
        
    # Checks whether a scheduled task is pending to run or not
    schedule.run_pending()
    #time.sleep(1)
