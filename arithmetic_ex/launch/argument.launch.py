from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    param_dir = LaunchConfiguration(
        'param_dir',
        default=os.path.join(get_package_share_directory('arithmetic_ex'),
                             'param',
                             'argument.yaml')
    )
    return LaunchDescription([
        DeclareLaunchArgument('param_dir',
                              default_value=param_dir,
                              description='full path of parameter file'),
        Node(package='arithmetic_ex',
             executable='argument',
            #  parameters=[{'min_random_num': 10}, {'max_random_num': 50}],
            parameters=[param_dir],
             output='screen'),
        Node(package='arithmetic_ex',
             executable='argumentsub',
            #  parameters=[{'min_random_num': 10}, {'max_random_num': 50}],
            parameters=[param_dir],
             output='screen'),
    ])

