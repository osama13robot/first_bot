import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg = FindPackageShare('first_bot'); use_sim_time = LaunchConfiguration('use_sim_time'); world = LaunchConfiguration('world')
    robot_description = Command(['xacro ', PathJoinSubstitution([pkg, 'description', 'robot.urdf.xacro'])])
    gz = IncludeLaunchDescription(PythonLaunchDescriptionSource([FindPackageShare('ros_gz_sim'), '/launch/gz_sim.launch.py']), launch_arguments={'gz_args': ['-r ', world]}.items())
    rsp = Node(package='robot_state_publisher', executable='robot_state_publisher', parameters=[{'robot_description': robot_description, 'use_sim_time': use_sim_time}], output='screen')
    bridge = Node(package='ros_gz_bridge', executable='parameter_bridge', arguments=['/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock', '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan', '/imu/data@sensor_msgs/msg/Imu[gz.msgs.IMU', '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry', '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist'], output='screen')
    spawn = Node(package='ros_gz_sim', executable='create', arguments=['-topic', 'robot_description', '-name', 'first_bot', '-x', '0', '-y', '0', '-z', '0.15'], output='screen')
    return LaunchDescription([DeclareLaunchArgument('use_sim_time', default_value='true'), DeclareLaunchArgument('world', default_value=PathJoinSubstitution([pkg, 'worlds', 'navigation_arena.world'])), gz, rsp, bridge, spawn])
