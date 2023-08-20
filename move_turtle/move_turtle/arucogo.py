import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from ros2_aruco_interfaces.msg import ArucoMarkers
from math import sqrt

MAX_LIN_VEL = 0.22
MAX_ANG_VEL = 2.84

class Move_straight(Node):
    def __init__(self):
        super().__init__('straight')
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.odometery_sub = self.create_subscription(Odometry, 'odom', self.odom_sub, 10)
        self.aruco_marker_sub = self.create_subscription(ArucoMarkers, 'aruco_markers', self.aruco_sub, 10)
        self.update_timer = self.create_timer(0.1, self.update)
        self.origin_x = 0.0
        self.origin_y = 0.0
        self.x = 0.0
        self.y = 0.0
        self.moving = False
        self.distance = 0.0

    def odom_sub(self, data):
        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y

    def aruco_sub(self, submsg):
        self.distance = submsg.poses[0].position.z - 0.05
        self.get_logger().info(f'{submsg.poses[0].position.z}')
        self.origin_x = self.x
        self.origin_y = self.y
        self.moving = True
    
    def update(self):
        msg = Twist()
        if self.moving:
            # self.get_logger().info(f'{self.origin_x}, {self.origin_y}')
            # self.get_logger().info(f'elapse: {self.elapsed_dist()}')
            if self.elapsed_dist() < self.distance:
                msg.linear.x = 0.1
                self.pub.publish(msg)
            else:
                msg.linear.x = 0.0
                self.pub.publish(msg)
        else:
            msg.linear.x = 0.0
            self.pub.publish(msg) # stop move

    def elapsed_dist(self):
        # calcurate and return elapsed distance
        return sqrt(pow((self.x - self.origin_x), 2) + pow((self.y - self.origin_y), 2))

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
    node = Move_straight()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('keyboard Interrupt!!')
    finally:
        # stop code
        msg = Twist()
        msg.linear.x = 0.0
        node.pub.publish(msg)
        
        node.destroy_node
        rclpy.shutdown()

if __name__ == '__main__':
    main()