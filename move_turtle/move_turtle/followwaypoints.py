import rclpy
import random
from rclpy.node import Node 
from nav2_msgs.action import FollowWaypoints 
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped
import sys

class FollowWaypoints1(Node):
    def __init__(self):
        super().__init__('follow_waypoints')
        self.cli = ActionClient(self, FollowWaypoints, 'FollowWaypoints')

    def call_action(self, points):
        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = points
        self.cli.wait_for_server()
        self.send_goal_future = self.cli.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self.send_goal_future.add_done_callback(self.goal_response_callback)
        
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected!!')
            return
        self.get_logger().info('Goal accepted!!')
        self.get_result_future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)
        
    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Feedback : {result.missed_waypoints}')
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Feedback : {feedback.current_waypoints}')


def main():
    rclpy.init()
    node = FollowWaypoints1()
    try:
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp =  node.get_clock().now().to_msg()
        pose.pose.orientation.w = 1.0   #theta
        pose.pose.position.z = 0.0
        pose.pose.position.x = 0.376
        pose.pose.position.y = 1.49        
        node.call_action([pose])
        rclpy.spin(node)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main':
    main()