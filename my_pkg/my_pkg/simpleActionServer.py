import rclpy
from rclpy.node import Node
from my_interfaces.action import Fibonacci
from rclpy.action import ActionServer
import time

class Fibonacci_action_server(Node):
    def __init__(self):
        super().__init__('fibonacci_server')
        self.action_server = ActionServer(self, Fibonacci, 'fibonacci', self.excute_callback)
    
    def excute_callback(self, goal_handle):
        feedback_msg = Fibonacci.Feedback()
        feedback_msg.temp_seq = [0, 1]
        result = Fibonacci.Result()
        
        self.get_logger().info('request[Goal] is accepted!!')
        
        for i in range(1, goal_handle.request.step):
            feedback_msg.temp_seq.append(feedback_msg.temp_seq[i] + feedback_msg.temp_seq[i-1])
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)
        goal_handle.succeed()
        result.seq = feedback_msg.temp_seq
        return result

def main():
    rclpy.init()
    node = Fibonacci_action_server()
    try:
        rclpy.spin(node)
    except:
        node.destroy_node()
        rclpy.shutdown()
    

if __name__ == '__main__':
    main()
    
    