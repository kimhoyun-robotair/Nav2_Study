import rclpy
from rclpy.node import Node
import rclpy.subscription

class FastTimerNode(Node):
    def __init__(self):
        super().__init__("fast_timer_node")
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        self.count += 1
        self.get_logger().info(f"Fast Count: {self.count}")

def main(args=None):
    rclpy.init(args=args)
    fast_tiemr = FastTimerNode()
    rclpy.spin(fast_tiemr)
    fast_tiemr.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
