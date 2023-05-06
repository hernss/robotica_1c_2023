#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
import numpy as np
from std_msgs.msg import Float64

def getRSSI(x, y):
    # Datos del transmisor
    transmiter_location_x = 0
    transmiter_location_y = 0
    transmiter_power = 1 #30dBm
    wave_length = 0.125
    escale = 1

    # Calculo la distancia al cuadrado
    dist_square = ((x - transmiter_location_x)**2 + (y- transmiter_location_y)**2)

    # https://es.wikipedia.org/wiki/Propagaci%C3%B3n_por_espacio_libre
    power = (transmiter_power * wave_length)/ ((4*np.pi)**2 * dist_square)

    return power


def odom_callback(msg: Odometry):
    pub = rospy.Publisher("/rssi_level", Float64, queue_size=10)
    power = getRSSI(msg.pose.pose.position.x, msg.pose.pose.position.y)
    pub.publish(power)


if __name__ == '__main__':
    rospy.init_node("turtle_pose_subscriber")
    
    sub = rospy.Subscriber("/odom", Odometry, callback=odom_callback)
    
    rospy.loginfo("Subscriber running")

    rospy.spin()
            