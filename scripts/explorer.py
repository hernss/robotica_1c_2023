#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class Explorer:

    def __init__(self):
        rospy.init_node('explorer_node', anonymous=True)
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.twist_msg = Twist()
        self.last_scan_time = rospy.Time.now()
        self.turn_start_time = None
        self.turn_duration = rospy.Duration.from_sec(1.0)

    def scan_callback(self, scan_msg):
        # check if a new scan has been received recently
        if (rospy.Time.now() - self.last_scan_time).to_sec() < 0.1:
            return

        # update the last scan time
        self.last_scan_time = rospy.Time.now()
        
        # find the closest point in the laser scan
        #closest_point = min(scan_msg.ranges)
        closest_point = min(scan_msg.ranges[350:360])
        if closest_point > 0.5:  # if we're close to an obstacle, stop
            self.twist_msg.linear.x = 0.2  # move forward
            self.twist_msg.angular.z = 0.0  # no turning
            self.turn_start_time = None  # reset turn timer
            rospy.loginfo("Long Forward")
        else:
            if self.turn_start_time is None:
                self.turn_start_time = rospy.Time.now()  # start turn timer
            elif (rospy.Time.now() - self.turn_start_time) > self.turn_duration:
                self.twist_msg.linear.x = 0.1  # move forward after turn timer expires
                self.twist_msg.angular.z = 0.0  # no turning
                self.turn_start_time = None  # reset turn timer
                rospy.loginfo("Forward")
            else:
                self.twist_msg.linear.x = 0.0  # stop
                self.twist_msg.angular.z = 0.35  # turn left
                rospy.loginfo("Turning")

        self.cmd_vel_pub.publish(self.twist_msg)

    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == '__main__':
    explorer = Explorer()
    explorer.run()