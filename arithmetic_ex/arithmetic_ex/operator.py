import rclpy
import random
import time
from rclpy.node import Node 
from my_interfaces.srv import ArithmeticOperator

class Operator(Node):
    def __init__(self):
        super().__init__('operator')
        self.client = self.create_client(ArithmeticOperator, 'arithmetic_operator')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.msg = ArithmeticOperator.Request()
    
    def call_service(self):
        self.msg.arithmetic_operator = random.randint(1, 4)
        self.future = self.client.call_async(self.msg)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()
    

def main():
    rclpy.init()
    node = Operator()
    try:
        while rclpy.ok():
            # rclpy.spin_once(node)
            response = node.call_service()
            input('Press Enter ofr next service call')
            node.get_logger().info( f'Recived message : {response.arithmetic_result}')
    except:
        node.destroy_node()
        rclpy.shutdown()



if __name__ == '__main':
    main()