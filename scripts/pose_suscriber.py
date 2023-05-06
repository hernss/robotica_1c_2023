#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(msg : Pose):
    rospy.loginfo(msg.x)


if __name__ == '__main__':
    rospy.init_node("turtle_pose_subscriber")
    
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    
    rospy.loginfo("Subscriber running")

    rospy.spin()
            