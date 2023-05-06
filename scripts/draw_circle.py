#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node("draw_circle_node")
    rospy.loginfo("Draw circle running")

    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        # Publish cmd velocity
        msg = Twist()
        msg.linear.x = 3.0
        msg.angular.z = 1.5
        pub.publish(msg)
        rate.sleep()
        
