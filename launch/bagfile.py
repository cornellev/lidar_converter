from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["ros2", "bag", "play", "bag/unilidar_3d/rosbags/bag_1"],
                name="bag",
            ),
            Node(
                package="lidar_converter",
                executable="lidar_converter",
                name="lidar_converter",
            ),
        ]
    )
