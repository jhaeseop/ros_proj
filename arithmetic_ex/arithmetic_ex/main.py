import rclpy
from rclpy.node import Node
from my_interfaces.msg import ArithmeticArgument
from my_interfaces.srv import ArithmeticOperator
from my_interfaces.action import ArithmeticChecker
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.action import ActionServer
import time
import random


class Calculator(Node):
    def __init__(self):
        super().__init__('msub')
        self.create_subscription(ArithmeticArgument, 'arithmetic_argument', self.sub, 10)
        self.create_service(ArithmeticOperator, 
                            'arithmetic_operator',
                            self.get_arithmetic_operator,
                            callback_group=ReentrantCallbackGroup())
        self.arithmetic_action_server = ActionServer(self, ArithmeticChecker, 'arithmetic_checker', self.execute_callback)
        self.argument_a = 0.0
        self.argument_b = 0.0
        self.argument_result = 0.0
        self.arthmetic_result = 0.0
        self.argument_formula = ''
        self.argument_symbol = ['+','-', '*', '/']
        self.argument_operator = 1

    def sub(self, msg):
        self.get_logger().info(f'Recieved time: {msg.stamp.sec}, {msg.stamp.nanosec}')
        self.get_logger().info(f'Recieved message: {msg.argument_a}, {msg.argument_b}')
        self.argument_a = msg.argument_a
        self.argument_b = msg.argument_b
        
        if self.argument_operator == ArithmeticOperator.Request.PLUS:
            self.arithmetic_result = self.argument_a + self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.MINUS:
            self.arithmetic_result = self.argument_a - self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.MULTIPLY:
            self.arithmetic_result = self.argument_a * self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.DIVISION:
            if self.argument_b == 0:
                self.arithmetic_result = 0.0
            else:
                self.arithmetic_result = self.argument_a / self.argument_b
        self.get_logger().info(f'Receiving Service {self.argument_operator}')
        self.argument_result = self.arithmetic_result
        self.argument_formula = f'{self.argument_a} {self.argument_symbol[self.argument_operator-1]} {self.argument_b} = {self.arthmetic_result}'
        self.argument_result = self.arithmetic_result
        
    def get_arithmetic_operator(self, request, response):
        self.argument_operator = request.arithmetic_operator
        if self.argument_operator == ArithmeticOperator.Request.PLUS:
            self.arithmetic_result = self.argument_a + self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.MINUS:
            self.arithmetic_result = self.argument_a - self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.MULTIPLY:
            self.arithmetic_result = self.argument_a * self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.DIVISION:
            if self.argument_b == 0:
                self.arithmetic_result = 0.0
            else:
                self.arithmetic_result = self.argument_a / self.argument_b
        self.get_logger().info(f'Receiving Service {self.argument_operator}')
        response.arithmetic_result = self.arithmetic_result
        return response
    
    def execute_callback(self, goal_handle):
        feedback = ArithmeticChecker.Feedback()
        feedback.formula = []
        total_sum = 0
        goal_sum = goal_handle.request.goal_sum
        while total_sum < goal_sum:
            total_sum += self.argument_result
            feedback.formula.append(self.argument_formula)
            goal_handle.publish_feedback(feedback)
            time.sleep(1)
        goal_handle.succeed()
        result = ArithmeticChecker.Result()
        result.all_formula = feedback.formula
        result.total_sum = total_sum
        return result
    


def main():
    rclpy.init()
    node = Calculator()
    excutor = MultiThreadedExecutor(num_threads=4)
    excutor.add_node(node)

    try:
        excutor.spin()
    except KeyboardInterrupt:
        print('Keyboard Insterrupt!!')
    finally:
        excutor.shutdown()
        node.destroy_node
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
    