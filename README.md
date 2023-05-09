# Robotica - UTN - FRBA

<h2> Proyecto 1C-2023 - Travado - Sobral</h2>

> Step-by-step guide:

{my_robot_controller} = > Your own pkg name. 

--------
## Cargar configuracion de visualizacion de RVIZ

    cd /opt/ros/noetic/share/turtlebot3_slam/rviz
    sudo mv turtlebot3_gmapping.rviz turtlebot3_gmapping_backup.rviz
    sudo cp ~/catkin_ws/src/my_robot_controller/rviz/turtlebot3_gmapping.rviz .


# Orden de ejecucion de nodos

### Exportar la variable global al bashrc
    echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc

### Terminal 1 - **GAZEBO:**
    roslaunch turtlebot3_gazebo turtlebot3_house.launch

### Terminal 2 - **RVIZ**
    roslaunch turtlebot3_slam turtlebot3_slam.launch  slam_methods:=gmapping

### Terminal 3 - **Navigation**
    roslaunch turtlebot3_navigation move_base.launch 

### Terminal 4 - **Simulador de potencia WIFI**
    rosrun my_robot_controller fake_wifi_transmiter.py

### Terminal 5 - **Heat Map**
    rosrun my_robot_controller make_heat_map.py 

### Terminal 6 - **Nodo de Exploracion**</h3>
    roslaunch explore_lite explore.launch

# Resultado final

![heatmap](./rviz/rviz%20heat%20map.png)

[Video de funcionamiento](https://frbautneduar-my.sharepoint.com/:v:/g/personal/htravado_frba_utn_edu_ar/ES7OqQve1ZNOpxuKj6dg2I0B7qUQzcsdTQUmzsvLAOy5EA?e=7VyChX) <- hay que acceder con cuenta de UTN.BA

[Video funcionamiento - Mirror](https://github.com/hernss/robotica_1c_2023/blob/main/Misc/Video%20funcionamiento.mp4)
