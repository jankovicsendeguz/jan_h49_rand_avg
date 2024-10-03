# random_average/random_generator_node.py

import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import Float32

class RandomNumberPublisher(Node):

    def __init__(self):
        super().__init__('random_generator_node')
        self.publisher_ = self.create_publisher(Float32, 'random_numbers', 10)
        self.timer = self.create_timer(1.0, self.publish_random_number)

    def publish_random_number(self):
        random_number = random.uniform(0, 100)
        msg = Float32()
        msg.data = random_number
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {random_number}')


def main(args=None):
    rclpy.init(args=args)
    random_number_publisher = RandomNumberPublisher()
    rclpy.spin(random_number_publisher)
    random_number_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
