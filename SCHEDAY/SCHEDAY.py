# Schedule Library imported
import schedule
import time


def adjust_width(content, total_width):
    content_length = len(content)
    if content_length > total_width:
        return content[:total_width]  # Truncate content if it exceeds total width
    remaining_space = total_width - content_length
    return content + " " * remaining_space  # Add spaces if content is shorter


# Class structure
class Task:
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
        print("\n╔" + "═" * (total_width + 2) + "╗")
        print("║" + adjust_width(" Task Details ", total_width + 2).center(total_width) + "║")
        print("╠" + "═" * (total_width + 2) + "╣")
        
        # Line 1: Task No. and Task Name
        line1 = f"Task No.: {self.number:<30} | Task Name: {self.name}"
        print(f"║ {adjust_width(line1, total_width)} ║")

        # Line 2: Start Date and Start Time
        line2 = f"Start Date: {self.start_date:<28} | Start Time: {self.start_time}"
        print(f"║ {adjust_width(line2, total_width)} ║")
        
        # Line 3: Finish Date and Finish Time
        line3 = f"Finish Date: {self.finish_date:<27} | Finish Time: {self.finish_time}"
        print(f"║ {adjust_width(line3, total_width)} ║")
        
        # Line 4: Desired Start Date and Desired Start Time
        line4 = f"Desired Start Date: {self.desired_start_date:<20} | Desired Start Time: {self.desired_start_time}"
        print(f"║ {adjust_width(line4, total_width)} ║")
        
        # Line 5: Capacity and Value
        line5 = f"Capacity: {self.capacity:<30} | Value: {self.value}"
        print(f"║ {adjust_width(line5, total_width)} ║")
        
        # Line 6: Frequency and Execution Time
        line6 = f"Frequency: {self.frequency:<29} | Execution Time: {self.execution_time:}"
        print(f"║ {adjust_width(line6, total_width)} ║")
        
        # Footer of the box
        print("╚" + "═" * (total_width + 2) + "╝")


# Welcome message
print()
print("════════════════════════════════════════════════════════════════════════════")

print()
print("╔═══════════════════════════════════════════════════════════════════════════╗")
print("║                               WELCOME to SCHEDAY!                         ║")
print("║                        Your Efficient Task Scheduler                      ║")
print("╚═══════════════════════════════════════════════════════════════════════════╝\n")

# Initializing variables 
wait_Tasks = []
Tasks = []
task_number = 0

# Creating instances
def create_instances(min, max, L):
    L1 = ["t"]
    for i in range(min, max):
        L.append(i)
        L[i] = L1[0] + str(L[i])    
    return L

instances = {}
L = []
L = create_instances(0, 1000, L)

# Helper function to get input or default value
def get_input_or_default(prompt, default_value, suffix=""):
    full_prompt = f"{prompt} (default: {default_value} {suffix}) : "
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



# Create new task
def new():
    print()
    print("╔═══════════════════════════════════════════════════════════════════════════╗")
    print("║                               New Task Creation                           ║")
    print("╚═══════════════════════════════════════════════════════════════════════════╝\n")
    
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
    new_task = get_input_or_default("Enter new task", default_task)
    start_date = get_input_or_default("Enter start date", default_start_date)
    start_time = get_input_or_default("Enter start time", default_start_time)
    desired_start_date = get_input_or_default("Enter desired start date", default_desired_start_date)
    desired_start_time = get_input_or_default("Enter desired start time", default_desired_start_time)
    finish_date = get_input_or_default("Enter finish date", default_finish_date)
    finish_time = get_input_or_default("Enter finish time", default_finish_time)
    value = get_input_or_default("Enter value", default_value)
    capacity = get_input_or_default("Enter capacity", default_capacity)
    frequency = get_input_or_default("Enter frequency", default_frequency)
    execution_time = get_input_or_default("Enter execution time", default_execution_time)

    # Object instance
    task_number = num  # For input
    task = Task(task_number, new_task, start_date, start_time, finish_date, finish_time, value, capacity, frequency, desired_start_date, desired_start_time, execution_time)
    
    Tasks.append(task)  # Add task to Tasks list
    instances.update({num: task})

    print()
    print("╔═══════════════════════════════════════════════════════════════════════════╗")
    print("║                                New Task Summary                           ║")
    print("╚═══════════════════════════════════════════════════════════════════════════╝\n")
    task.show()
    
# View pending tasks


def view_pending_tasks():
    print()
    print("╔═══════════════════════════════════════════════════════════════════════════╗")
    print("║                             Pending Task Summary                          ║")
    print("╚═══════════════════════════════════════════════════════════════════════════╝")
    print("║  "," "*70, " ║")
    
    if not Tasks:
        print("║ ", end=" ")
        print("No pending tasks.", end=" "*55)
        print(" ║", end="")
        print()
    
    # Show tasks in 'Tasks' list
    else:
        print("║  "," "*70, " ║")
        for task in Tasks:
            task.show()
            print()
        
    print("║  "," "*70, " ║")
    print("╚═══════════════════════════════════════════════════════════════════════════╝\n")

# Rescheduling tasks
def reschedule():
    print()
    print("╔═══════════════════════════════════════════════════════════════════════════╗")
    print("║                          Regular Rescheduling of Tasks                    ║")
    print("╚═══════════════════════════════════════════════════════════════════════════╝\n")

# Rescheduling to avoid task starvation    
def no_starve():
    print()
    print("╔═══════════════════════════════════════════════════════════════════════════╗")
    print("║                        Starvation Prevention Reschedule                   ║")
    print("╚═══════════════════════════════════════════════════════════════════════════╝\n")

# Day summary (to be stored in CSV)
def day_summary():
    print()
    print("╔═══════════════════════════════════════════════════════════════════════════╗")
    print("║                                 Day Summary                               ║")
    print("╚═══════════════════════════════════════════════════════════════════════════╝\n")
    # Day summary logic goes here

# Initializing user-based variables
def start_screen():
    global reschedule_time, starve_time

    print()
    print("╔═══════════════════════════════════════════════════════════════════════════╗")
    print("║                              SCHEDAY Starting...                          ║")
    print("╚═══════════════════════════════════════════════════════════════════════════╝\n")
    
    # Default values for reschedule and starve time (in minutes)
    default_reschedule_minutes = 2
    default_starve_minutes = 3
    
    # Taking user input with default options
    print("Enter integer values for 'reschedule time' or 'starve time'. ")
    reschedule_minutes = get_input_or_default("Enter reschedule time (in mins)", default_reschedule_minutes, "(mins)")
    starve_minutes = get_input_or_default("Enter starve time (in mins)", default_starve_minutes, "(mins)")
    
    # Convert minutes to seconds
    reschedule_time = reschedule_minutes * 60
    starve_time = starve_minutes * 60

    print(f"\nReschedule time set to {reschedule_time} seconds ({reschedule_minutes} minutes)")
    print(f"Starve time set to {starve_time} seconds ({starve_minutes} minutes)\n")

    print()
    print("╔═══════════════════════════════════════════════════════════════════════════╗")
    print("║                                SCHEDAY Active!                            ║")
    print("╚═══════════════════════════════════════════════════════════════════════════╝\n")
    
    # Schedule tasks after reschedule_time and starve_time are set
    schedule.every(1).seconds.do(menu)  # Start the main loop without requiring the menu
    schedule.every(reschedule_time).seconds.do(reschedule)
    schedule.every(starve_time).seconds.do(no_starve)
    schedule.every().day.at("00:00").do(day_summary)

# Main menu to handle user commands
def menu():
    print()
    print("╔═════════════════════════════════════════════╗")
    print("║                 SCHEDAY MENU                ║")
    print("╠═════════════════╦═══════════════════════════╣")
    print("║      Option     ║        Description        ║")
    print("╠═════════════════╬═══════════════════════════╣")
    print("║       'N'       ║ Create a new task         ║")
    print("║       'S'       ║ View pending tasks        ║")
    print("║       'Q'       ║ Quit SCHEDAY              ║")
    print("╚═════════════════╩═══════════════════════════╝\n")
    
    command = input("Your choice: ").strip().upper()  # Convert input to uppercase to handle both cases

    if command == 'N':
        new()  # Create a new task
    elif command == 'S':
        view_pending_tasks()  # View pending tasks
    elif command == 'Q':
        print("Exiting SCHEDAY... Thank you! \n")
        exit()
    else:
        print("Invalid command. Please try again. \n")

# Call start_screen once to take user inputs
start_screen()

# Loop so that the scheduling task keeps on running all the time
while True:
    # Checks whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)
