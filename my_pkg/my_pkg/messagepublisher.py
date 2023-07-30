import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Sim_pub(Node):
    def __init__(self):
        super().__init__('mpub')
        self.pub = self.create_publisher(String, 'message', 10)
        self.pub2 = self.create_publisher(String, 'message2', 10)
        self.create_timer(1, self.publisher)
        self.create_timer(0.5, self.publisher2)
        self.count = 0
        
    def publisher(self):
        msg = String()
        msg.data = 'message -> hello' + str(self.count)
        self.pub.publish(msg)
        self.count += 1
        
    def publisher2(self):
        msg = String()
        msg.data = 'message2 -> hello' + str(self.count)
        self.pub2.publish(msg)
        self.count += 1

def main():
    rclpy.init()
    node = Sim_pub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Keyboard Insterrupt!!')
    finally:
        node.destroy_node
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
    