# FRA502_service_robot : Phase III: Final presentation 

## name : student ID
นายรัศพัชร์ ลีลาวัฒนเกียรติ : 62340500044

## How to run the robot
1. run ros master
~~~~~
roscore
~~~~~
2. run gazebo
~~~~~
roslaunch project_sim gazebo.launch 
~~~~~
3. run rviz and amcl file
~~~~~
roslaunch project_sim amcl.launch 
~~~~~
4. run speech file
~~~~~
rosrun project_sim speech.py 
~~~~~

## My process
1. create world and obstacle in gazebo __In this step avoid to move the door and window through the wall__ 
2. create robot model in gazebo, in this case I choose differntial drive robot __In this step, I learn and know that how xacro better than URDF file. If I have time or I have opportunity, I will use function include to seperate the code. It will easier to debug
3. Set up the laser scanner. In this case I use hokuyo scanner becuase, It show how to use in tutorial and a lot of people use it. So it easy to find the debug.
4. Set up the teleop key board. This is useful in next step, to create the map in Gmapping.
5. Create a map using Gmapping, to run this file
~~~~~
roslaunch project_sim gmapping.launch
~~~~~
6. Create navigation using amcl __Before set the 2d goal, set the 2d position estimate first and try to set robot position in rviz to the same with gazebo__
7. Rus speech file. In this case the logic is just if-else logic, But IF I have the time or oppotunity, I will try touse state machine logic
## Problem and challenges in this project
1. ไม่สามารถลง ubuntu ได้ในวันแรกและต้องลง window ใหม่เนื่องจากลง ubuntu ผิดวิธี
2. พบจอ error เกี่ยว audio เยอะมาก
3. การทำ position estimate ยังไม่ดีเท่าที่ควร คาดว่าอาจจะเป็นเพราะการตั้ง position ใน rviz ไม่ตรงกับ gazebo
