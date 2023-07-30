import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.clock import Clock, ClockType
from rclpy.qos import QoSHistoryPolicy, QoSReliabilityPolicy, QoSDurabilityPolicy
from std_msgs.msg import String
from rclpy.qos import qos_profile_sensor_data
from std_msgs.msg import Header


class Sim_time_pub(Node):
    def __init__(self):
        super().__init__('tpub')
        self.pub = self.create_publisher(Header, 'time', 10)
        self.create_timer(1, self.publisher)
        self.id = 0
        # self.clock = Clock(clock_type=ClockType.SYSTEM_TIME)

        
    def publisher(self):
        msg = Header()
        msg.stamp = self.get_clock().now().to_msg()
        msg.frame_id = str(self.id)
        self.id += 1
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Sim_time_pub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Keyboard Insterrupt!!')
    finally:
        node.destroy_node
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
    