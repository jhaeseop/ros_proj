import rclpy
from rclpy.node import Node
from std_msgs.msg import ArithmeticArgument


class Sim_sub(Node):
    def __init__(self):
        super().__init__('argument')
        self.pub = self.create_publisher(ArithmeticArgument, 'arithmetic_argument', 10)
        self.timer = self.create_timer(1, self.publisher)
        
    def publisher(self):
        msg = ArithmeticArgument()
        msg.stamp = self.get_clock().now().to_msg()
        msg.argument_a = 3.0
        msg.argument_b = 5.0
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Sim_sub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Keyboard Insterrupt!!')
    finally:
        node.destroy_node
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
    