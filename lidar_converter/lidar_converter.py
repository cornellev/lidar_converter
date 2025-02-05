import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2

class LidarConverter(Node):
    def __init__(self):
        super().__init__("lidar_converter")
        self.unilidar_sub = self.create_subscription(PointCloud2, "unilidar/cloud", self.callback, 10)

    def callback(self, msg):
        self.get_logger().info("received a message!")
        self.get_logger().info(msg)
        

def main():
    rclpy.init()
    nh = LidarConverter()
    rclpy.spin(nh)
    nh.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()