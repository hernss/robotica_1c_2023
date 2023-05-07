#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
from nav_msgs.msg import OccupancyGrid
import numpy as np
from std_msgs.msg import Float64
from rosgraph_msgs.msg import Clock


last_clock = 0
last_seq = -1

def map_callback(map: OccupancyGrid):
    rospy.loginfo("Res:" + str(map.info.resolution) + " time:" + str(map.info.map_load_time))

def clock_callback(clock: Clock):
    global last_clock
    last_clock = clock.clock

def odom_callback(odom: Odometry):
    global last_seq
    global last_clock
    global msg
    global heat_map_pub

    last_seq += 1
    msg.header.seq = last_seq
    msg.header.stamp = last_clock
    
    x = int(odom.pose.pose.position.x)
    y = int(odom.pose.pose.position.y)

    points_list = get_area(x, y)

    rospy.loginfo("X: " + str(x) + " Y:" + str(y))

    for point in points_list:
        msg.data[point] = 100
        

    heat_map_pub.publish(msg)

def get_area(x, y, radius = 0.5, center = 76615, escale = 20, cols = 384, rows = 384):
    ret_list = []
    punto_central = int(center + (y * escale * 384) + (x * escale))
   

    pixel_radius = int(radius*escale)
    #pixel_radius = 3

    for i in range(pixel_radius):
        # Descarto el 0
        if i == 0:
            ret_list.append(punto_central)
        else:
            ret_list.append(punto_central+i)
            ret_list.append(punto_central-i)
        
        for j in range(pixel_radius-i):
            if j == 0:
                ret_list.append(punto_central+cols*i)
                ret_list.append(punto_central-cols*i)
            else:
                ret_list.append(punto_central+cols*i-j)
                ret_list.append(punto_central-cols*i-j)
                ret_list.append(punto_central+cols*i+j)
                ret_list.append(punto_central-cols*i+j)

    return ret_list


if __name__ == '__main__':
    rospy.init_node("map_subscriber")
    rospy.loginfo("Heat map generator running")

    

    # frecuencia de actualizacion del mapa
    #rate = rospy.Rate(1)

    # Los datos para cargar el mensaje los deberia sacar el /map que esta generando el slam
    msg = OccupancyGrid()
    # header
    msg.header.frame_id = "map"
    # map.info
    msg.info.map_load_time.secs = 0
    msg.info.map_load_time.nsecs = 0
    msg.info.resolution = 0.05
    msg.info.height = 384
    msg.info.width = 384
    msg.info.origin.position.x = -10
    msg.info.origin.position.y = -10
    msg.info.origin.position.z = 0
    msg.info.origin.orientation.x = 0
    msg.info.origin.orientation.y = 0
    msg.info.origin.orientation.z = 0
    msg.info.origin.orientation.w = 0
    # data
    for i in range(msg.info.height*msg.info.width):
        msg.data.append(-1)

    #sub = rospy.Subscriber("/map", OccupancyGrid, callback=map_callback)
    clock_sub = rospy.Subscriber("/clock", Clock, callback=clock_callback)
    odom_sub = rospy.Subscriber("/odom", Odometry, callback=odom_callback)

    heat_map_pub = rospy.Publisher("/heat_map", OccupancyGrid, queue_size=10)

    rospy.spin()
     