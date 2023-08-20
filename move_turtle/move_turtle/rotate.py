import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import sqrt
import numpy as np

MAX_LIN_VEL = 0.22
MAX_ANG_VEL = 2.84

def euler_from_quaternion(quaternion):
    """
    Converts quaternion (w in last place) to euler roll, pitch, yaw
    quaternion = [x, y, z, w]
    Bellow should be replaced when porting for ROS 2 Python tf_conversions is done.
    """
    x = quaternion.x
    y = quaternion.y
    z = quaternion.z
    w = quaternion.w

    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = np.arctan2(sinr_cosp, cosr_cosp)

    sinp = 2 * (w * y - z * x)
    pitch = np.arcsin(sinp)

    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = np.arctan2(siny_cosp, cosy_cosp)

    return roll, pitch, yaw

class Move_rotate(Node):
    def __init__(self):
        super().__init__('straight')
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.odometery_sub = self.create_subscription(Odometry, 'odom', self.odom_sub, 10)
        self.origin_theta = 0.0
        self.x = 0.0
        self.y = 0.0

    def odom_sub(self, data):
        self.theta = euler_from_quaternion(data.pose.pose.orientation)[2]
        self.get_logger().info(f'theta : {self.theta}')

    def rotate(self, theta):
        msg = Twist()
        rclpy.spin_once(self)
        if theta > self.theta:
            msg.angular.z = 0.5
        else:
            msg.angular.z = -0.5
        self.origin_theta = theta
        print(self.origin_theta)

        while rclpy.ok():
            rclpy.spin_once(self)
            self.pub.publish(msg)
            if abs(self.elapsed_theta()) < 0.1:
                break
            
        msg.angular.z = 0.0
        self.pub.publish(msg) # stop move

    def elapsed_theta(self):
        # calcurate and return elapsed theta
        return self.origin_theta - self.theta

    def restrain(self, msg):
        if msg.linear.x < - MAX_LIN_VEL:
            msg.linear.x = - MAX_LIN_VEL
        elif msg.linear.x > MAX_LIN_VEL:
            msg.linear.x = MAX_LIN_VEL
        if msg.angular.z < - MAX_ANG_VEL:
            msg.angular.z = - MAX_ANG_VEL
        elif msg.angular.z > MAX_ANG_VEL:
            msg.angular.z = MAX_ANG_VEL
        return msg


def main():
    rclpy.init()
    node = Move_rotate()
    try:
        dist = float(input("input theta(radian): "))
        node.rotate(dist)
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('keyboard Interrupt!!')
    finally:
        node.destroy_node
        rclpy.shutdown()

if __name__ == '__main__':
    main()