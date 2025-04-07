<a name="readme-top"></a>
# Efficient-Task-Scheduler-SCHEDAY

```Scheday``` is a complex ```scheduler```, implemented using the concepts of classes.

<br>

<details open>

  <summary style="color: red;">Table of Contents</summary>
<li> <a href="#a1">Introduction</a></li>
<li> <a href="#a2"> Prerequisites and Techstack</a></li>
<li> <a href="#a3"> Steps for Execution </a></li>
<li> <a href="#a5">Screenshots</a></li>
<li> <a href="#a4">Usage</a></li>
  <li> Objective </li>
  <li> Final Outcome</li>
  <li> Expansion</li>
<a href="#end"><u><i>Skip to END...</i></u></a>
</details>
</br>

<a name="a1"></a>
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
  

</br>


### <b>Files :</b> 
The ```Efficient-Task-Scheduler-SCHEDAY Directory``` contains the following files:
  
  - 1- ```'SCHEDAY.py'  File```- contains the SCHEDAY Application code.
    
  - 2- ```'Screenshots' Directory```- contains Screenshots on various tasks from the SCHEDAY Application.
</br>

### <b>Repository Structure :</b> 

<details>
  <summary color= blue ><u><b><i>Efficient-Task-Scheduler-SCHEDAY repo structure</i></b> click...</u></summary>

  Below is the structure of the ```Efficient-Task-Scheduler-SCHEDAY``` project repository
  
  ```plaintext
    Efficient-Task-Scheduler-SCHEDAY/
    │   
    ├── SCHEDAY/           # Project Folder
    │   │              
    │   ├── SCHEDAY.py              # Application
    │   │     
    │   │ 
    │   ├── Screenshots/            # Screenshots-Folder              # 
    │   │    ├── Image_1a.png
    │   │    ├── Image_1b.png
    │   │    ├── Image_2.png
    │   │    ├── Image_3a.png
    │   │    ├── Image_3b.png
    │   │    ├── Image_3c.png
    │   │    ├── Image_4a.png
    │   │    ├── Image_4c.png
    │   │    ├── Image_5.png
    │   │    ├── Image_6.png
    │   │    ├── Image_r1.png
    │   │    ├── Image_r2.png     
    │   │    └── # 
    │   │ 
    │   └── #
    │   
    └─── README.md           # Repository README
    
  ```

</details>
</br>


## <b>Objective :</b> 
To build an ```efficient scheduler application``` which -
1.	Can accomodate <i>new tasks</i>
2.	Has <i>no job starvation</i>
3.	Starts any task within 2hours of its <i>desired start time</i>.
4.	Can provide basic statistical and analytical <i>report</i>, such as jobs for day, capacity utilization for day, etc..
</br>


###
###

  <p align="right"><a href="#readme-top">Back to TOP</a></p>
  </br>


## Prerequisites and Techstack
* Languages used- Python
* Various languages such as python, c, html, react, etc... can be used to implement scheday

<p align="right"><a href="#readme-top">back to top</a></p>
  </br>

## Steps for Execution
 1. Clone the ``` 'Scheduler-SCHEDAY' ``` github repository.
  ```sh 
  git clone https://github.com/ankitacoder3/Efficient-Task-Scheduler-SCHEDAY.git 
  ```
 2. Navigate to the ``` 'SCHEDAY' ``` Directory in that.
  ```sh
  cd Efficient-Task-Scheduler-SCHEDAY
  cd SCHEDAY
  ```
  3. Open the ```SCHEDAY.py``` in python idle or terminal.  

  4. Run ``` SCHEDAY.py``` by selecting the ```run option``` in python idle, or by using the command prompt.
  ```sh
  python SCHEDAY.py
  ```
5. Output can be viewed on the SHELL (for python idle), or COMMAND LINE interface (for command prompt).

<p align="right"><a href="#readme-top">back to top</a></p>
  </br>
  
## Usage
There are several applications of this in different areas of life, such as-
1.	To plan events or activities for any person or customer.
2.	To schedule events for systems.
3.	To help people plan and prioritize their work, etc...

   <p align="right"><a href="#readme-top">back to top</a></p>
  </br>

## Screenshots
Below are few screenshots of the SCHEDAY application:
</br>
1.	SCHEDAY STARTING
    <BR>
      a. With default inputs
  	![Image_1a](./SCHEDAY/Screenshots/Image_1a.png)

  	<BR>
      b. With user-defined inputs
      
    ![Image_1b](./SCHEDAY/Screenshots/Image_1b.png)

2.	SCHEDAY MENU
   ![Image_3](./SCHEDAY/Screenshots/Image_2.png)
  	
3.	NEW TASK
    <BR>
      a. With default inputs
  	![Image_3a](./SCHEDAY/Screenshots/Image_3a.png)

  	<BR>
      b. With user-defined inputs
      
    ![Image_3b](./SCHEDAY/Screenshots/Image_3b.png)

   <BR>
      c. With hybrid input
      
  ![Image_3c](./SCHEDAY/Screenshots/Image_3c.png)
  	
4.	PENDING TASK SUMMARY
    <BR>
      a. With default inputs
  	![Image_4a](./SCHEDAY/Screenshots/Image_4a.png)
  	
5.	TASK DELETION
  	![Image_5](./SCHEDAY/Screenshots/Image_5.png)
   
6.	EXITING SCHEDAY
   ![Image_6](./SCHEDAY/Screenshots/Image_6.png)

7.	TASK RESCHEDULING
   ![Image_r1](./SCHEDAY/Screenshots/Image_r1.png)

</br>

Other screenschots can be found in the ```"./SCHEDAY/Screenshots/"``` folder.
</br>


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
