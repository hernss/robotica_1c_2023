# robotica_1c_2023

Proyecto 2023 - Travado - Sobral

Exportar la variable global al bashrc
echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc

Terminal 1 - GAZEBO
roslaunch turtlebot3_gazebo turtlebot3_house.launch

Terminal 2 - RVIZ
roslaunch turtlebot3_slam turtlebot3_slam.launch  slam_methods:=gmapping

Terminal 3 - Simulador de potencia WIFI
rosrun my_robot_controller fake_wifi_transmiter.py 

Terminal 4 - Heat Map
rosrun my_robot_controller make_heat_map.py 

