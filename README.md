<a name="readme-top"></a>

# Scheduler-SCHEDAY

```Scheday``` is a complex ```scheduler```, implemented using the concepts of classes.

<details>
  <summary color= blue >Table of Contents</summary>
  <li> Objective </li>
<li> Introduction </li>
<li> Prerequisites and Techstack</li>
<li> Steps for execution</li>
<li> Usage</li>
  <li> Final Outcome</li>
  <li> Expansion</li>
</details>
</br>


## Objective
To build an efficient scheduler application which -
1.	Can accomodate new tasks
2.	Has no job starvation
3.	Starts any task within 2hours of its desired start time.
4.	Can provide basic statistical and analytical report, such as jobs for day, capacity utilization for day, etc..

<p align="right"><a href="#readme-top">back to top</a></p>
  </br>


## Introduction
* The name of this idea is "Scheday" which stands for 'Scheduler for the day'. (ie, for any day it gives maximum value )
* The scheduler has the following properties-
    *	New jobs - As and when new jobs are added it is added to a waiting list.
    *	Rescheduling- After a certain time, say 'reschedule time' the scheduler reschedules all the jobs, except the current running job.
    That is all jobs in the scheduler plus the jobs in waiting list are rescheduled (with the exception of the current running job).
    This 'reschedule time' can be 5min Or 2min , according to user requirements.
    *	Priority - Based on the desired start time, the job has to be started within 2 hrs of that. Based on this priority is given.
      While taking care of this completion time is also kept in mind.
    *	Starvation- After a certain amount of time, say 'starve time' the jobs are reviewed.
    In this review,the job that will execute last is rescheduled in between of the jobs before it depending on the desired start time and completion time.
    After every 'starve time' this review occurs. 'starve time' can be say 10min Or 5min , depending on no of tasks etc.
    *	Analysis- All of these tasks, their start time, completion time, desired start time, if the task is completed etc is stored in a csv Or excel.
      From this csv Or excel required data is got and analysed by a code, which gives output as basic reports

  </br>
  
* Features:
  
    *	One can dynamically add new tasks.
  
     *	One can view pending task details as a list.
  
    *	Tasks can be entered on this.
  
    *	At a time thousand tasks can be run.
  
     *	Tasks can also be executed from a csv wherein it reads each and every task and executes them.
  

<p align="right"><a href="#readme-top">back to top</a></p>
  </br>
  
## Prerequisites and Techstack
* Languages used- Python
* Various languages such as python, c, html, react, etc... can be used to implement scheday

<p align="right"><a href="#readme-top">back to top</a></p>
  </br>

## Steps for Execution
 1. Clone the ``` 'Scheduler-SCHEDAY' ``` github repository.
  ```sh 
  git clone https://github.com/ankitacoder3/Scheduler-SCHEDAY.git 
  ```
 2. Navigate to the ``` 'SCHEDAY' ``` Directory in that.
  ```sh
  cd Scheduler-SCHEDAY
  cd SCHEDAY
  ```
  3. Open the ```SCHEDAY.py``` in python idle or terminal.  

  4. Run ``` SCHEDAY.py``` by selecting the ```run option``` in python idle, or by using the command prompt.
  ```sh
  python SCHEDAY.py
  ```
5. Output can be viewed on the SHELL (for python idle), or command line interface (for command prompt).

<p align="right"><a href="#readme-top">back to top</a></p>
  </br>
  
## Usage
There are several applications of this in different areas of life, such as-
1.	To plan events or activities for any person or customer.
2.	To schedule events for systems.
3.	To help people plan and prioritize their work, etc...

   <p align="right"><a href="#readme-top">back to top</a></p>
  </br>
  
## Final outcome 
The final outcome of scheday is-
1. The application can be made web compatible.
2. It can deployed on a real time website
  * So that many people can use their time efficiently and productively
  * This website will be easily accessible, feasible, and user-friendly

<p align="right"><a href="#readme-top">back to top</a></p>
  </br>

## Expansion
This idea can be expanded in the following ways
1.	Deployed on a website In this way the user can schedule a task for his computer from remote locations
2.	GUI can be added For making it wasy for the user to interpret this application


<p align="right"><a href="#readme-top">back to top</a></p>
  </br>
