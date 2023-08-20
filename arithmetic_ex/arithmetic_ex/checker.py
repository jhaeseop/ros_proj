import rclpy
import random
from rclpy.node import Node 
from my_interfaces.action import ArithmeticChecker
from rclpy.action import ActionClient
import sys
import argparse

class Checker_action_client(Node):
    def __init__(self):
        super().__init__('checker_cli')
        self.cli = ActionClient(self, ArithmeticChecker, 'arithmetic_checker')

    def call_action(self, step):
        goal_msg = ArithmeticChecker.Goal()
        goal_msg.goal_sum = float(step)
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
        self.get_logger().info(f'result all_formula : {result.all_formula}')
        self.get_logger().info(f'result total_sum : {result.total_sum}')
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Feedback : {feedback.formula}')


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-g',
        '--goal_total_sum',
        type=int,
        default=150,
        help='add total sum'
    )
    args = parser.parse_args()
    
    rclpy.init()
    node = Checker_action_client()
    try:
        node.call_action(args.goal_total_sum)
        rclpy.spin(node)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main':
    main()