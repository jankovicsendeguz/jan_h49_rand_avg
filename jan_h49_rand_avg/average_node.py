# random_average/average_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class AverageCalculator(Node):

    def __init__(self):
        super().__init__('average_node')
        self.subscription = self.create_subscription(
            Float32,
            'random_numbers',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Float32, 'average_value', 10)
        self.numbers = []
    
    def listener_callback(self, msg):
        self.numbers.append(msg.data)
        average = sum(self.numbers) / len(self.numbers)
        average_msg = Float32()
        average_msg.data = average
        self.publisher_.publish(average_msg)
        self.get_logger().info(f'Received: {msg.data}, Current Average: {average}')


def main(args=None):
    rclpy.init(args=args)
    average_calculator = AverageCalculator()
    rclpy.spin(average_calculator)
    average_calculator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
