import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import QoSHistoryPolicy, QoSReliabilityPolicy, QoSDurabilityPolicy
from std_msgs.msg import String
from rclpy.qos import qos_profile_sensor_data


class Sim_sub(Node):
    def __init__(self):
        super().__init__('simple_msub')
        qos_profile = QoSProfile(
            history=QoSHistoryPolicy.KEEP_ALL,
            reliability=QoSReliabilityPolicy.RELIABLE,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL)
        self.pub = self.create_subscription(String, 'message', self.sub, qos_profile_sensor_data)
        
    def sub(self, msg):
        self.get_logger().info(msg.data)
        #self.get_logger().error(msg.data)

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
    