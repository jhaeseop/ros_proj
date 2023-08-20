import rclpy
from rclpy.node import Node
from my_interfaces.msg import ArithmeticArgument
from rcl_interfaces.msg import SetParametersResult


class Argument_sub(Node):
    def __init__(self):
        super().__init__('msub')
        self.create_subscription(ArithmeticArgument, 'arithmetic_argument', self.sub, 10)
        
    def sub(self, msg):
        self.get_logger().info(f'Recieved time: {msg.stamp.sec}, {msg.stamp.nanosec}')
        self.get_logger().info(f'Recieved message: {msg.argument_a}, {msg.argument_b}')

def main():
    rclpy.init()
    node = Argument_sub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Keyboard Insterrupt!!')
    finally:
        node.destroy_node
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
    