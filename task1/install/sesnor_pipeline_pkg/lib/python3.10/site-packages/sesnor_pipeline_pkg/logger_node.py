import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3

class LoggerNode(Node):

	def __init__(self):
		super().__init__('logger_node')
		self.logger_subscriber = self.create_subscription(Vector3, 'publisher_data', self.messages, 10)
		self.get_logger().info("This is the logger node")

	def messages(self, msg:Vector3):
		msg.x = msg.x/3.0
		self.get_logger().info("Average = " + str(msg.x))

def main(args=None):
	rclpy.init(args=args)
	node = LoggerNode()
	rclpy.spin(node)
	rclpy.shutdown()
