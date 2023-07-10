from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('rosbag_path', default_value='rosbag'),
        DeclareLaunchArgument('topics', default_value='-a'),

        ExecuteProcess(
            cmd=['ros2', 'bag', 'record', '-o',
                 LaunchConfiguration('rosbag_path'), LaunchConfiguration('topics')],
            output='screen'
        ),
    ])
