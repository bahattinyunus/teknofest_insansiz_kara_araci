import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Robot Controller Baslatildi...')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.5  # 0.5 m/s hiz
        msg.angular.z = 0.1 # 0.1 rad/s donus
        self.publisher_.publish(msg)
        self.get_logger().info('Komut Gonderildi: Linear=%.2f, Angular=%.2f' % (msg.linear.x, msg.angular.z))

def main(args=None):
    rclpy.init(args=args)
    robot_controller = RobotController()
    try:
        rclpy.spin(robot_controller)
    except KeyboardInterrupt:
        pass
    robot_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
