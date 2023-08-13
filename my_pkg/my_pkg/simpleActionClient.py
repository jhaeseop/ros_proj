import rclpy
import random
from rclpy.node import Node 
from my_interfaces.action import Fibonacci
from rclpy.action import ActionClient
import sys

class Simple_action_client(Node):
    def __init__(self):
        super().__init__('fibonacci_cli')
        self.cli = ActionClient(self, Fibonacci, 'fibonacci')

    def call_action(self, step):
        goal_msg = Fibonacci.Goal()
        goal_msg.step = int(step)
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
        self.get_logger().info(f'Feedback : {result.seq}')
        rclpy.shutdown()


    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Feedback : {feedback.temp_seq}')


def main():
    rclpy.init()
    node = Simple_action_client()
    try:
        node.call_action(sys.argv[1])
        rclpy.spin(node)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main':
    main()