from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    pkg = FindPackageShare('first_bot')
    return LaunchDescription([
        Node(package='robot_localization', executable='ekf_node', name='ekf_filter_node', output='screen', parameters=[PathJoinSubstitution([pkg, 'config', 'ekf.yaml'])]),
        Node(package='slam_toolbox', executable='async_slam_toolbox_node', name='slam_toolbox', output='screen', parameters=[PathJoinSubstitution([pkg, 'config', 'slam_toolbox.yaml'])]),
    ])
