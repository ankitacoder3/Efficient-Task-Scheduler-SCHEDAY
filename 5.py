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
        print('Task no.:',self.number,'\t Task name:',self.name,'\t Start date:',self.start_date,'\t Start time:',self.start_time,'\t Finish date:',self.finish_date,
              '\t Finish time:',self.finish_time,'\t Desired start date:', self.desired_start_date,'\t Desired start time:', self.desired_start_time,
              '\t Capacity:', self.capacity,'\t Value:', self.value, '\t Frequency:',self.frequency, '\t Execution time:',self.execution_time)

#welcome           
print("WELCOME to Scheday!")
print("Press:- space bar to enter new task;")

#Initializing variables 
wait_Tasks=[]
Tasks=[]
reschedule_time=10 #seconds
starve_time= 30 #seconds
task_number=0


#creating instances
def create_instances(min,max,L):
    L1=["t"]
    for i in range(min,max):
        L.append(i)
        L[i]=L1[0]+str(L[i])    
    #print(L1)
    #print(L)
    return L

instances=[]
L=create_instances(0,1000,instances)
#print(instances)
#create a function later to handle more than 1000 tasks
    
# Functions setup
    
def Keyboard( ):    #this can be menu 
    if keyboard.is_pressed(' '):
        job=new( )
        return job


    if keyboard.is_pressed('s'):
        i=0
        while i<len(wait_Tasks): #should be Tasks
            instances[0].show()
            i+=1

    
  
def new():
    print("\n__________________________New Task_____________________________\n")
    if len(wait_Tasks)==0:
        num=len(wait_Tasks) #should be Tasks
    else:
        num=len(wait_Tasks)

    new_task=input("Enter new task:")
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
    task_number=num

    
    L[num]= Task(task_number,new_task, start_date, start_time, finish_date, finish_time, value, capacity, frequency, desired_start_date, desired_start_time, execution_time)
    instances.append(L[num])
    print("\n____________________New Task Summary___________________________\n")
    instances[num].show()
    print("\n_______________________________________________________________\n")
    print("in",task_number)
    return L[num]




def reschedule():
    print("\n-----------------Regular Rescheduling Tasks--------------------\n")
    
def no_starve():
    print("\n------------Avoid Starvation Rescheduling Tasks----------------\n")

def check( ):
    print("out",task_number)

def day_summary():
    print(9)


# Task scheduling

schedule.every(1).seconds.do(Keyboard)
schedule.every(reschedule_time).seconds.do(reschedule)
schedule.every(starve_time).seconds.do(no_starve)

schedule.every().day.at("00:00").do(day_summary)

#trial
schedule.every(50).seconds.do(check)



'''
ignore just fr reference
# Every day at 12am or 00:00 time bedtime() is called.
schedule.every().day.at("00:00").do(bedtime)

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
