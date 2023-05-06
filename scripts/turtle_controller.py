#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(msg : Pose):
    cmd = Twist()
    if msg.x > 10.0 or msg.x < 1.0 or msg.y < 1.0 or msg.y > 10.0:
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = 0

    pub.publish(cmd)

if __name__ == '__main__':
    rospy.init_node("turtle_controller")
    
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)


    rospy.loginfo("Subscriber running")

    rospy.spin()
            