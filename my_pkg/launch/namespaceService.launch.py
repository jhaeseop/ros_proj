from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
import os


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'ros_namespace',
            default_value=os.environ['ROS_NAMESPACE']),
        Node(package='my_pkg',
             namespace='/jhs',
             executable='simplesss',
             output='screen'),
    ])

