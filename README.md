# Robotica - UTN - FRBA

<h2> Proyecto 1C-2023 - Travado - Sobral</h2>

> Step-by-step guide:

{my_robot_controller} = > Your own pkg name. 

--------

## Instalacion de ROS Noetic

Para la instalacion de ros noetic seguir el tutorial disponible en la pagina oficial de ros 

```
http://wiki.ros.org/noetic/Installation/Ubuntu
```

## Instalacion del modelo TurtleBot3 

### Instalacion  de las dependencias

```
sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
ros-noetic-rosserial-python ros-noetic-rosserial-client \
ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
```

### Instalacion de los paquetes de TurtleBot3

```
sudo apt install ros-noetic-dynamixel-sdk
sudo apt install ros-noetic-turtlebot3-msgs
sudo apt install ros-noetic-turtlebot3
sudo apt install ros-noetic-explore-lite
```
### Instalacion del simulador de TurtleBot3

```
mkdir ~/catkin_ws 
cd ~/catkin_ws/src
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/catkin_ws && catkin_make
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source devel/setup.bash
```

### Instalacion de los controladores del robot

```
cd ~/catkin_ws/src
mkdir my_robot_controller
cd my_robot_controller
rm -rf *
git clone https://github.com/hernss/robotica_1c_2023 .
cd ~/catkin_ws && catkin_make
```

### Cargar configuracion de visualizacion de RVIZ

```
cd /opt/ros/noetic/share/turtlebot3_slam/rviz
sudo mv turtlebot3_gmapping.rviz turtlebot3_gmapping_backup.rviz
sudo cp ~/catkin_ws/src/my_robot_controller/rviz/turtlebot3_gmapping.rviz .
```

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
