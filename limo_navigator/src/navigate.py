#!/usr/bin/env python
import rospy
import actionlib
import tf
import roslib
from nav_msgs.msg import Odometry
from move_base_msgs.msg import *

rospy.init_node('limo_navigator_node')
client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
rospy.loginfo('Connecting to move_base...')
client.wait_for_server()
rospy.loginfo('Connected to move_base')

def set_goal(point):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "odom"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = point[0]
    goal.target_pose.pose.position.y = point[1]
    quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0, point[2])
    goal.target_pose.pose.orientation.x = quaternion[0]
    goal.target_pose.pose.orientation.y = quaternion[1]
    goal.target_pose.pose.orientation.z = quaternion[2]
    goal.target_pose.pose.orientation.w = quaternion[3]

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr('Action server not available!')
        rospy.signal_shutdown('Action server not available!')
    else:
        return client.get_result

def main():

    point = (0, 0.8, 0.2)
    set_goal(point)
    print "1st point reached"

    point = (0.5, 0.4, 0.2)
    # point = (-1.5, 0.3, 0.2)
    set_goal(point)
    print "2nd point reached"

    point = (0.5, 0.7, 0.2)
    # point = (-3, 0.5, 0.2)
    set_goal(point)
    print "3rd point reached"

    point = (0.3, 0.4, 0.2)
    set_goal(point)
    print "4th point reached"

main()