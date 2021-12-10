#!/usr/bin/env python3
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import speech_recognition as sr
from subprocess import call


r = sr.Recognizer()


def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    with sr.Microphone() as source:
        print("I am Ready ?")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    data = r.recognize_google(audio)
    data = data.lower()
    print("Robot thinks you said " + data)
    place = ""
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    if 'bedroom' in data:
        goal.target_pose.pose.position.x = -3.0
        goal.target_pose.pose.position.y = -1.5
        goal.target_pose.pose.orientation.w =  1
        client.send_goal(goal) 
        place="bedroom"       

    elif 'working room' in data:
        goal.target_pose.pose.position.x = 0.0
        goal.target_pose.pose.position.y = -1.5
        goal.target_pose.pose.orientation.w =  1
        client.send_goal(goal)
        place="working room"

    elif 'kitchen' in data:
        goal.target_pose.pose.position.x = 0.0
        goal.target_pose.pose.position.y = -3.0
        goal.target_pose.pose.orientation.w =  1
        client.send_goal(goal)
        place="kitchen"

    elif 'toilet' in data:
        goal.target_pose.pose.position.x = -2.0
        goal.target_pose.pose.position.y = -3.0
        goal.target_pose.pose.orientation.w = 1
        client.send_goal(goal)
        place="toilet"

    else:
        print("No Task")

    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result(),place

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        while not rospy.is_shutdown():
            result,pl = movebase_client()
            if result:
                rospy.loginfo("I'M HERE!, finish!")
                text="Reached to" + pl


    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")