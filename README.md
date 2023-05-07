# robotica_1c_2023

<h2> Proyecto 2023 - Travado - Sobral</h2>

> Step-by-step guide:

{my_robot_controller} = > Your own pkg name. 

--------

* *<h3>Exportar la variable global al bashrc*</h3>
    * echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc

* *<h3>Terminal 1 - GAZEBO:*</h3>
    * roslaunch turtlebot3_gazebo turtlebot3_house.launch

* *<h3>Terminal 2 - RVIZ* </h3>
    * roslaunch turtlebot3_slam turtlebot3_slam.launch  slam_methods:=gmapping

* *<h3>Terminal 3 - Simulador de potencia WIFI*</h3>
    * rosrun my_robot_controller fake_wifi_transmiter.py


* *<h3>Terminal 4 - Heat Map*</h3>
    * rosrun my_robot_controller make_heat_map.py 


