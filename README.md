# A robot in ros2 (robot operating system)

This repo contains the source code for a robot simulation in ros2 using Gazebo simulator.


#Build

The build and run of this project is very simple.
* First of all install ros2 and gazebo ros2 documentation will be enough.
* using linux terminal or windows cmd type:
```
mkdir ws_ros
cd ws_ros
mkdir src
cd src
git clone https://github.com/Uzair-90/robot-simulation.git
cd ../../
colcon build
source install/setup.bash #this will depend whether you are using bash or some other terminal
ros2 launch mobile_sim robot.launch.py #check the folder for launch file name and simulation directory name.

```

Above is the so simple method to build and run this project.

For any issues post your comment.
