import os
import random
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    namePackage = 'mobile_robot'
    modelFileRelativePath = 'model/robot.xacro'
    worldFileRelativePath = 'model/empty_world.world'
    
    pathModelFile = os.path.join(get_package_share_directory(namePackage), modelFileRelativePath)
    pathWorldFile = os.path.join(get_package_share_directory(namePackage), worldFileRelativePath)
    
    robotDescription = xacro.process_file(pathModelFile).toxml()
    
    gazebo_rosPackageLaunch = PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'))
    
    gazeboLaunch = IncludeLaunchDescription(
        gazebo_rosPackageLaunch,
        launch_arguments={'world': pathWorldFile}.items()
    )
    
    launchDescriptionObject = LaunchDescription()
    
    launchDescriptionObject.add_action(gazeboLaunch)
    
    for i in range(10):
        robotName = f'differential_drive_robot_{i}'
        
        x_position = random.uniform(-5.0, 5.0)
        y_position = random.uniform(-5.0, 5.0)
        z_position = 0.5
        yaw_orientation = random.uniform(0.0, 3.14)  # Yaw angle in radians
        
        spawnModelNode = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-topic', 'robot_description',
                '-entity', robotName,
                '-x', str(x_position),
                '-y', str(y_position),
                '-z', str(z_position),
                '-R', '0.0',
                '-P', '0.0',
                '-Y', str(yaw_orientation)
            ],
            output='screen'
        )
        
        nodeRobotStatePublisher = Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robotDescription, 'use_sim_time': True}],
            namespace=robotName
        )
        
        launchDescriptionObject.add_action(spawnModelNode)
        launchDescriptionObject.add_action(nodeRobotStatePublisher)
    
    return launchDescriptionObject
