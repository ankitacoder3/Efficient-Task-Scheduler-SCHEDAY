# Schedule Library imported
import schedule
import time
import sys

# Class structure
class Task:

    # Class functions

    def __init__(self, number, name, start_date, start_time, finish_date, finish_time, value, capacity, frequency, desired_start_date, desired_start_time, execution_time):
        self.number = number
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
        total_width = 80  # Set width to fit the content dynamically
        
        # Task Details Header
        print("║     ╔" + "═" * (total_width + 2) + "╗      ║")
        print("║     ║" + adjust_width(" Task Details ", total_width + 2).center(total_width) + "║      ║")
        print("║     ╠" + "═" * (total_width + 2) + "╣      ║")
        
        # Line 1: Task No. and Task Name
        line1 = f"Task No.: {self.number:<30} | Task Name: {self.name}"
        print(f"║     ║ {adjust_width(line1, total_width)} ║      ║")

        # Line 2: Start Date and Start Time
        line2 = f"Start Date: {self.start_date:<28} | Start Time: {self.start_time}"
        print(f"║     ║ {adjust_width(line2, total_width)} ║      ║")
        
        # Line 3: Finish Date and Finish Time
        line3 = f"Finish Date: {self.finish_date:<27} | Finish Time: {self.finish_time}"
        print(f"║     ║ {adjust_width(line3, total_width)} ║      ║")
        
        # Line 4: Desired Start Date and Desired Start Time
        line4 = f"Desired Start Date: {self.desired_start_date:<20} | Desired Start Time: {self.desired_start_time}"
        print(f"║     ║ {adjust_width(line4, total_width)} ║      ║")
        
        # Line 5: Capacity and Value
        line5 = f"Capacity: {self.capacity:<30} | Value: {self.value}"
        print(f"║     ║ {adjust_width(line5, total_width)} ║      ║")
        
        # Line 6: Frequency and Execution Time
        line6 = f"Frequency: {self.frequency:<29} | Execution Time: {self.execution_time:}"
        print(f"║     ║ {adjust_width(line6, total_width)} ║      ║")
        
        # Footer of the box
        print("║     ╚" + "═" * (total_width + 2) + "╝      ║")


# Task Manager Functions

# Adjusting width helper function
def adjust_width(content, total_width):
    content_length = len(content)
    if content_length > total_width:
        return content[:total_width]  # Truncate content if it exceeds total width
    remaining_space = total_width - content_length
    return content + " " * remaining_space  # Add spaces if content is shorter


# Creating instances function
def create_instances(min, max, L):
    L1 = ["t"]
    for i in range(min, max):
        L.append(i)
        L[i] = L1[0] + str(L[i])    
    return L

instances = {}
L = []
L = create_instances(0, 1000, L)


# Get input or default value function
def get_input_or_default(prompt, default_value, suffix=""):
    if suffix:
        full_prompt = f"{prompt} (default: {default_value} {suffix}) : "
    else:
        full_prompt = f"{prompt} (default: {default_value}) : "

    user_input = input(full_prompt).strip()
    
    # Handle different types of default values
    if isinstance(default_value, int):
        return int(user_input) if user_input.isdigit() else default_value
    elif isinstance(default_value, float):
        try:
            return float(user_input) if user_input else default_value
        except ValueError:
            return default_value
    else:
        return user_input if user_input else default_value


# Create new task function
def new():
    print()
    print("╔═══════════════════════════════"+"═"*20+"════════════════════════════════════════════╗")
    print("║           "+" "*10+"                    New Task Creation       "+" "*10+"                    ║")
    print("╚═══════════════════════════════"+"═"*20+"════════════════════════════════════════════╝")
    print("║     ╔═ NEW TASK"," "*75, "  ║")
    print("║     ║"," "*90, " ")
    
    # Task count
    num = len(Tasks) + len(wait_Tasks)

    # Default values for new task
    default_task = "Default Task"
    default_start_date = "2024-09-10"
    default_start_time = "10:00"
    default_desired_start_date = "2024-09-11"
    default_desired_start_time = "11:00"
    default_finish_date = "2024-09-15"
    default_finish_time = "18:00"
    default_value = "100"
    default_capacity = "10"
    default_frequency = "Once"
    default_execution_time = "120"

    # Inputs with option for default values
    new_task = get_input_or_default("║     ╠ Enter new task", default_task)
    start_date = get_input_or_default("║     ╠ Enter start date", default_start_date)
    start_time = get_input_or_default("║     ╠ Enter start time", default_start_time)
    desired_start_date = get_input_or_default("║     ╠ Enter desired start date", default_desired_start_date)
    desired_start_time = get_input_or_default("║     ╠ Enter desired start time", default_desired_start_time)
    finish_date = get_input_or_default("║     ╠ Enter finish date", default_finish_date)
    finish_time = get_input_or_default("║     ╠ Enter finish time", default_finish_time)
    value = get_input_or_default("║     ╠ Enter value", default_value)
    capacity = get_input_or_default("║     ╠ Enter capacity", default_capacity)
    frequency = get_input_or_default("║     ╠ Enter frequency", default_frequency)
    execution_time = get_input_or_default("║     ╠ Enter execution time", default_execution_time)

    # Object instance
    task_number = num  # For input
    task = Task(task_number, new_task, start_date, start_time, finish_date, finish_time, value, capacity, frequency, desired_start_date, desired_start_time, execution_time)
    
    Tasks.append(task)  # Add task to Tasks list
    instances.update({num: task})
    
    print("║     ╚"," "*90, " ")
    print("╚══════════════════════════════════════"+"═"*20+"═════════════════════════════════════╝\n")

    print()
    print("╔════════════════════════════"+"═"*20+"═══════════════════════════════════════════════╗")
    print("║           "+" "*10+"                     New Task Summary             "+" "*10+"              ║")
    print("╚═══════════════════════════════"+"═"*20+"════════════════════════════════════════════╝")
    print("║  "," "*90, " ║")

    task.show()

    print("║  "," "*90, " ║")
    print("╚══════════════════════════════════════"+"═"*20+"═════════════════════════════════════╝\n")


# View pending tasks function
def view_pending_tasks():
    print()
    print("╔════════════════════════════════════"+"═"*20+"═══════════════════════════════════════╗")
    print("║                     "+" "*10,"        Pending Task Summary "+" "*10+"                        ║")
    print("╚══════════════════════════════════════"+"═"*20+"═════════════════════════════════════╝")
    print("║  "," "*90, " ║")
    
    if not Tasks:
        print("║ ", end=" ")
        print("No pending tasks.", end=" "*75)
        print(" ║")
        
    # Show tasks in 'Tasks' list
    else:
        print("║  "," "*90, " ║")
        for task in Tasks:
            task.show()
            print("║  "," "*90, " ║") 
        
    print("║  "," "*90, " ║")
    print("╚══════════════════════════════════════"+"═"*20+"═════════════════════════════════════╝\n")


# Delete task function
def delete_task():
    print()
    print("╔══════════════════════════════"+"═"*20+"═════════════════════════════════════════════╗")
    print("║                "+" "*10+"          Task Deletion        "+" "*12+"                          ║")
    print("╚═══════════════════════════════"+"═"*20+"════════════════════════════════════════════╝")
    print("║  "," "*90, " ║")
    
    if not Tasks:
        print("║ ", end=" ")
        print("No tasks available to delete.  ", end=" "*60)
        print("  ║")
        print("║  "," "*90, " ║")
        print("╚═══════════════════════════════"+"═"*20+"════════════════════════════════════════════╝\n")
        return
    
    # Instructions to view all tasks

    print("║ To view all the Task numbers, select 'View pending tasks' option from MENU "+" "*18+" ║")
    print("║  "," "*90, " ║")
    
    # Prompt the user to enter the task number they want to delete

    # Display the input prompt and capture the task number
    task_num = input("║ Enter the Task Number you want to delete (enter any whole no.): ").strip()

    # To maintain formatting, move one line up and overwrite that

    # To do this, use ANSI escape sequence to move the cursor up by one line, and to the start of that line
    sys.stdout.write("\033[A")  # Moves the cursor up one line
    sys.stdout.write("\r") # Moves the cursor to the start of the line

    # Finally print the prompth and user-input, in the required format
    if(task_num==" " or task_num == "\n"):
        task_num = " -"
    print(f"║ Enter the Task Number you want to delete (enter any whole no.): {task_num}  "+" "*25+"  ║")

    # Creating a flag to keep track of the type of task_num variable
    flag = 1 # Initializing flag to 1
     
    if task_num.isdigit(): 
        flag = 0  # If flag is 0, task_num is digit
        task_num = int(task_num) 

        # Search for the task with the given number
        task_found = False
        for task in Tasks:
            if task.number == task_num:
                Tasks.remove(task)
                task_found = True
                print("║  "," "*90, " ║")
                print(f"║ Task No. {task_num} has been successfully deleted!  "+" "*50+" ║")
                break
    # Invalid input given
    if(flag==1):
        print("║  "," "*90, " ║")
        print(f"║ INVALID INPUT GIVEN! Task not found.  "+" "*55+" ║")
        print(f"║ Please try again! INPUT only whole numbers as task no.!  "+" "*35+"  ║")
    
    # Task not found
    elif (flag==0 and task_found==False):
        print("║  "," "*90, " ║")
        print(f"║ Task No. {task_num} not found. Try Again! "+" "*60+" ║")

    # end of task deletion function
    print("║  "," "*90, " ║")
    print("╚═══════════════════════════════"+"═"*20+"════════════════════════════════════════════╝\n")


# SCHEDAY Scheduler Functions

# Initialize scheduler function
def start_scheduling():
    print()
    print("╔══════════════════════════════════"+"═"*20+"═════════════════════════════════════════╗")
    print("║                      "+" "*10+"        SCHEDAY Starting...        "+" "*10+"                  ║")
    print("╚══════════════════════════════════"+"═"*20+"═════════════════════════════════════════╝")
    print("║  "," "*90, " ║")
    # Initializing user-based variables

    global reschedule_time, starve_time

    # Default values for reschedule and starve time (in minutes)
    default_reschedule_minutes = 2
    default_starve_minutes = 3
    
    # Taking user input with default options
    print("║     ╔═ NOTE: Enter integer values for 'reschedule time' or 'starve time'. "," "*22, "")
    print("║     ║"," "*90, " ")

    reschedule_minutes = get_input_or_default("║     ╠ Enter reschedule time (in mins)", default_reschedule_minutes, "(mins)")
    starve_minutes = get_input_or_default("║     ╠ Enter starve time (in mins)", default_starve_minutes, "(mins)")
    print("║     ║"," "*90, " ")
    
    # Convert minutes to seconds
    reschedule_time = reschedule_minutes * 60
    starve_time = starve_minutes * 60

    print(f"║     ╠ Reschedule time set to {reschedule_time} seconds ({reschedule_minutes} minutes)")
    print(f"║     ╠ Starve time set to {starve_time} seconds ({starve_minutes} minutes)")
    print("║     ╚"," "*90, " ")
    print("╚══════════════════════════════════════"+"═"*20+"═════════════════════════════════════╝\n")

    print()
    print("╔═════════════════════════════════"+"═"*20+"══════════════════════════════════════════╗")
    print("║                   "+" "*10+"             SCHEDAY Active!      "+" "*10+"                      ║")
    print("╚═══════════════════════════════════"+"═"*20+"════════════════════════════════════════╝\n")
    
    # Schedule tasks after reschedule_time and starve_time are set
    schedule.every(1).seconds.do(menu)  # Start the main loop without requiring the menu
    schedule.every(reschedule_time).seconds.do(reschedule)
    schedule.every(starve_time).seconds.do(no_starve)
    schedule.every().day.at("00:00").do(day_summary)


# SCHEDAY Welcome Screen
def welcome(): 
    # Welcome message
    print()
    print("═════════════════════════════════════"+"═"*20+"═══════════════════════════════════════")

    print()
    print("╔══════════════════════════════════"+"═"*20+"═════════════════════════════════════════╗")
    print("║                  "+" "*10+"             WELCOME to SCHEDAY!  "+" "*10+"                       ║")
    print("║                "+" "*10+"        Your Efficient Task Scheduler    "+" "*10+"                  ║")
    print("╚═══════════════════════════════════"+"═"*20+"════════════════════════════════════════╝\n")


# Exiting SCHEDAY
def quit_SCHEDAY():
    print()
    print("╔════════════════════════════════════"+"═"*20+"═══════════════════════════════════════╗")
    print("║                     "+" "*10,"        EXITING SCHEDAY !    "+" "*10+"                        ║")
    print("╚══════════════════════════════════════"+"═"*20+"═════════════════════════════════════╝")
    print("║  "," "*90, " ║")

    # Exit Screen
    print("║ ", end="")
    print("EXITING SCHEDAY! Thank you! ", end=" "*65)
    print(" ║")

    print("║  "," "*90, " ║")
    print("╚══════════════════════════════════════"+"═"*20+"═════════════════════════════════════╝\n\n")
       
    # Exiting
    exit()


# SCHEDAY Main Menu 
def menu():
    print()
    print(" "+" "*10+"╔═════════════════════════════════════════════╗")
    print(" "+" "*10+"║                 SCHEDAY MENU                ║")
    print(" "+" "*10+"╠═════════════════╦═══════════════════════════╣")
    print(" "+" "*10+"║      Option     ║        Description        ║")
    print(" "+" "*10+"╠═════════════════╬═══════════════════════════╣")
    print(" "+" "*10+"║       'A'       ║ Create a new task         ║")
    print(" "+" "*10+"║       'B'       ║ View pending tasks        ║")
    print(" "+" "*10+"║       'C'       ║ Delete a task             ║")
    print(" "+" "*10+"║       'Z'       ║ Quit SCHEDAY              ║")
    print(" "+" "*10+"╚═════════════════╩═══════════════════════════╝\n")
    
    command = input("Your choice: ").strip().upper()  # Convert input to uppercase to handle both cases

    if command == 'A':
        new()  # Create a new task
    elif command == 'B':
        view_pending_tasks()  # View pending tasks
    elif command == 'C':
        delete_task() # Delete a task
    elif command == 'Z':
        quit_SCHEDAY() # Exiting SCHEDAY
    else:
        print("Invalid command. Please try again. \n")

# To be implemented functions

# Rescheduling tasks function
def reschedule():
    print()
    print("╔══════════════════════════════"+"═"*20+"═════════════════════════════════════════════╗")
    print("║                   "+" "*10+"       Regular Rescheduling of Tasks "+" "*10+"                   ║")
    print("╚═══════════════════════════════"+"═"*20+"════════════════════════════════════════════╝\n")

    ''' 
    # Adding functionality

     Uncomment line to print any statements
    
    '''

# Rescheduling funtion, to avoid task starvation    
def no_starve():
    print()
    print("╔══════════════════════════════"+"═"*20+"═════════════════════════════════════════════╗")
    print("║                  "+" "*10+"      Starvation Prevention Reschedule    "+" "*10+"               ║")
    print("╚══════════════════════════════"+"═"*20+"═════════════════════════════════════════════╝\n")

# Day summary function 
def day_summary():
    # (to be stored in CSV)

    print()
    print("╔═════════════════════════════════"+"═"*20+"══════════════════════════════════════════╗")
    print("║                        "+" "*10+"         Day Summary       "+" "*10+"                        ║")
    print("╚═══════════════════════════════════"+"═"*20+"════════════════════════════════════════╝\n")
    # Day summary logic goes here


# Driver Code

welcome ()

# Initializing variables 
wait_Tasks = []
Tasks = []
task_number = 0

# Call start_scheduling once to take user inputs and to start running the scheduling
start_scheduling()

# Loop so that the scheduling task keeps on running all the time
while True:
    # Checks whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)
