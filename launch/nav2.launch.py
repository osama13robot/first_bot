from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    nav2 = FindPackageShare('nav2_bringup')
    pkg = FindPackageShare('first_bot')
    return LaunchDescription([IncludeLaunchDescription(PythonLaunchDescriptionSource(PathJoinSubstitution([nav2, 'launch', 'navigation_launch.py'])), launch_arguments={'params_file': PathJoinSubstitution([pkg, 'config', 'nav2_params.yaml']), 'use_sim_time': 'true'}.items())])
