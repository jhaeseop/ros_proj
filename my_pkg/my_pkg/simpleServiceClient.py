import rclpy
import random
from rclpy.node import Node 
from my_interfaces.srv import TwoIntAdd

class Simple_service_client(Node):
    def __init__(self):
        super().__init__('twonumber_cli')
        self.client = self.create_client(TwoIntAdd, 'addtwoint')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.msg = TwoIntAdd.Request()
    
    def call_service(self):
        print('??')
        self.msg.a = random.randint(0,200)
        self.msg.b = random.randint(0,200)
        print('massage sending')
        self.future = self.client.call_async(self.msg)
        rclpy.spin_until_future_complete(self, self.future)
        print('meassage done')
        return self.future.result()

def main():
    rclpy.init()
    node = Simple_service_client()
    try:
        response = node.call_service()
        node.get_logger().info( f'Recived message : {response.rn}')
        # rclpy.spin(node)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main':
    main()