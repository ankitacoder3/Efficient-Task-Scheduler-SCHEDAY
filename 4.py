# Schedule Library imported
import schedule
import time
import keyboard

#class structure
class Task:
    def __init__(self, number, name, start_date, start_time, finish_date, finish_time, value, capacity, frequency, desired_start_date, desired_start_time, execution_time):
        self.number=number
        self.name = name
        self.start_date = start_date
        self.start_time = start_time
        self.finish_date = finish_date
        self.finish_time = finish_time
        self.desired_start_date = desired_start_date
        self.desired_start_time = desired_start_time
        self.value = value
        self.capacity = capacity
        self.frequency = frequency
        self.execution_time = execution_time

    def show(self):
        print('Task no.:',self.number,'\t Task name:',self.name,'\t Start date:',self.start_date,self.start_time,self.finish_date, self.finish_time, self.desired_start_date, self.desired_start_time, self.capacity, self.value, self.frequency, self.execution_time)

#welcome           
print("WELCOME to Scheday!")
print("Press:- space bar to enter new task;")

#Initializing variables 
wait_Tasks=[]
Tasks=[]
reschedule_time=10 #seconds
starve_time= 30 #seconds
task_number=0

    
# Functions setup
def Keyboard():
    if keyboard.is_pressed(' '):
        new()

'''
    if keyboard.is_pressed('s'):
        i=0
        while wait_Tasks:
            t1=wait_Tasks[i]
            t1.show()
            i+=1
'''

  
def new():
    #task_number=0
    print("\n__________________________New Task_____________________________\n")
    new_task=input("Enter new task:")
    nt=new_task
    wait_Tasks.append(new_task)
    start_date=input("Enter start date:")
    start_time=input("Enter start time:")
    desired_start_date=input("Enter  desired start date:")
    desired_start_time=input("Enter desired start time:")
    finish_date=input("Enter finish date:")
    finish_time=input("Enter finish time:")
    value=input("Enter value:")
    capacity=input("Enter capacity:")
    frequency=input("Enter frequency:")
    execution_time=input("Enter execution time:")
    nt= Task(task_number,new_task, start_date, start_time, finish_date, finish_time, value, capacity, frequency, desired_start_date, desired_start_time, execution_time)
    #task_number+=1
    print("\n____________________New Task Summary___________________________\n")
    nt.show()
    print("\n_______________________________________________________________\n")



def reschedule():
    print("\n-----------------Regular Rescheduling Tasks--------------------\n")
    
def no_starve():
    print("\n------------Avoid Starvation Rescheduling Tasks----------------\n")


# Task scheduling

schedule.every(1).seconds.do(Keyboard)
schedule.every(reschedule_time).seconds.do(reschedule)
schedule.every(starve_time).seconds.do(no_starve)


'''
ignore just fr reference
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
