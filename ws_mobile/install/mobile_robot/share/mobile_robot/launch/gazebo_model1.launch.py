import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    robotXacroName = 'differential_drive_robot'
    robotXacroName1 = 'differential_drive_robot1'
    namePackage = 'mobile_robot'
    modelFileRelativePath = 'model/robot.xacro'
    modelFileRelativePath1 = 'model/robot1.xacro'
    worldFileRelativePath = 'model/empty_world.world'
    
    pathModelFile = os.path.join(get_package_share_directory(namePackage), modelFileRelativePath)
    pathModelFile1 = os.path.join(get_package_share_directory(namePackage), modelFileRelativePath1)
    pathWorldFile = os.path.join(get_package_share_directory(namePackage), worldFileRelativePath)
    
    robotDescription = xacro.process_file(pathModelFile).toxml()
    robot1Description = xacro.process_file(pathModelFile1).toxml()
    
    gazebo_rosPackageLaunch = PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'))
    
    gazeboLaunch = IncludeLaunchDescription(
        gazebo_rosPackageLaunch,
        launch_arguments={'world': pathWorldFile}.items()
    )
    
    spawnModelNode = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', robotXacroName],
        output='screen'
    )
    
    nodeRobotStatePublisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robotDescription, 'use_sim_time': True}]
    )

    nodeRobotStatePublisher1 = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot1Description, 'use_sim_time': True}],
        namespace=robotXacroName1  # To distinguish the second robot
    )
    
    spawnModelNode1 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', robotXacroName1 + '/robot_description',
            '-entity', robotXacroName1,
            '-x', '1.0',  # Set x position
            '-y', '2.0',  # Set y position
            '-z', '0.5',  # Set z position (height)
            '-R', '0.0',  # Roll orientation
            '-P', '0.0',  # Pitch orientation
            '-Y', '1.57'  # Yaw orientation
        ],
        output='screen'
    )
    
    launchDescriptionObject = LaunchDescription()
    
    launchDescriptionObject.add_action(gazeboLaunch)
    launchDescriptionObject.add_action(spawnModelNode)
    launchDescriptionObject.add_action(nodeRobotStatePublisher)
    launchDescriptionObject.add_action(nodeRobotStatePublisher1)
    launchDescriptionObject.add_action(spawnModelNode1)
    
    return launchDescriptionObject
