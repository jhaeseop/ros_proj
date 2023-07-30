from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='my_pkg',
             node_executable='messagepub',
             output='screen'),
        Node(package='my_pkg',
             node_executable='simpletimepub',
             output='screen'),
        Node(package='my_pkg',
             node_executable='messagesub1',
             output='screen'),
        Node(package='my_pkg',
             node_executable='messagesub2',
             output='screen'),
        Node(package='my_pkg',
             node_executable='messagetimesub',
             output='screen')
    ])

