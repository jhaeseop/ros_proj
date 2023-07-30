import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Header


class Sim_sub(Node):
    def __init__(self):
        super().__init__('tmsub')
        self.create_subscription(String, 'message', self.sub, 10)
        self.create_subscription(Header, 'time', self.time_sub, 10)
        
    def sub(self, msg):
        self.get_logger().info(f'Recieved message: {msg.data}')
        
    def time_sub(self, msg):
        self.get_logger().info(f'Recieved message: {msg.stamp.sec}, {msg.stamp.nanosec}')

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
    