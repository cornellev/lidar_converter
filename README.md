# Lidar Converter

_Jason Klein, Daniel Sorokin_

ROS2 node to downsample incoming lidar data and send to the A&amp;A dashboard over WebSockets for visualization.

## Usage

Make sure that you have a source of LiDAR data, either live or rosbags. Currently, this repository is built around processing data from the [Unitree Robotics L1 LiDAR](https://github.com/unitreerobotics/unilidar_sdk/tree/main), a 3D lidar that publishes point clouds as [`sensor_msgs/msg/PointCloud2`](https://docs.ros2.org/foxy/api/sensor_msgs/msg/PointCloud2.html) messages.


