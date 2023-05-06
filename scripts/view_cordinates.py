#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry


def odom_callback(msg: Odometry):
    rospy.loginfo("[" + str(msg.pose.pose.position.x) + ", " + str(msg.pose.pose.position.y))


if __name__ == '__main__':
    rospy.init_node("turtle_pose_subscriber")
    
    sub = rospy.Subscriber("/odom", Odometry, callback=odom_callback)
    
    rospy.loginfo("Subscriber running")

    rospy.spin()
            