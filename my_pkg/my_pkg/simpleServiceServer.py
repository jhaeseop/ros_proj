import rclpy
from rclpy.node import Node 
from my_interfaces.srv import TwoIntAdd

class Simple_service_server(Node):
    def __init__(self):
        self.cnt = 0
        super().__init__('twonumber')
        self.srv = self.create_service(TwoIntAdd, 'addtwoint', self.twonumber_callback)
        self.timer = self.create_timer(1, self.test)

    def twonumber_callback(self, request, response):
        print(type(request))
        self.get_logger().info(f'incomming data{request.a}, {request.b}')
        response.rn =  request.a + request.b
        # response.rn = 10 
        return response
        

    def test(self):
        self.get_logger().info( f'a {self.cnt}')
        self.cnt += 1

def main(args = None):
    rclpy.init(args = args)
    node = Simple_service_server()
    try:
        rclpy.spin(node)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main':
    main()