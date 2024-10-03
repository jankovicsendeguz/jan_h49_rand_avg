from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='jan_h49_rand_avg',
            executable='random_generator_node',
            name='random_generator',
            output='screen'
        ),
        Node(
            package='jan_h49_rand_avg',
            executable='average_node',
            name='average_node',
            output='screen'
        ),
    ])
