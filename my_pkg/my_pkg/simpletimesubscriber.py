import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import QoSHistoryPolicy, QoSReliabilityPolicy, QoSDurabilityPolicy
from std_msgs.msg import String
from rclpy.qos import qos_profile_sensor_data
from std_msgs.msg import Header

class Sim_time_sub(Node):
    def __init__(self):
        super().__init__('simple_time_sub')
        self.pub = self.create_subscription(Header, 'time', self.sub, 10)
        
    def sub(self, msg):
        # msg.stamp.nanosec
        # msg.stamp.sec
        # msg.frame_id
        self.get_logger().info(f'Recieved time: {msg.stamp.sec}, {msg.stamp.nanosec}')
        self.get_logger().info(f'Recieved frame_id: {msg.frame_id}')

def main():
    rclpy.init()
    node = Sim_time_sub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Keyboard Insterrupt!!')
    finally:
        node.destroy_node
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
    