import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import random

class ActionClient(Node):

	def __init__(self):
		super().__init__("goal_client")
		self.client_publisher = self.create_publisher(Point, 'action_data', 10)
		self.timer = self.create_timer(10, self.messages)
		self.get_logger().info("This is the action client node")

	def messages(self):
		msg = Point()
		msg.x = float(random.randint(0,100))
		msg.y = float(random.randint(0,100))
		self.client_publisher.publish(msg)
		self.get_logger().info("given x-value = " + str(msg.x) + " Given y-value = " + str(msg.y))

def main(args=None):
	rclpy.init(args=args)
	node = ActionClient()
	rclpy.spin(node)
	rclpy.shutdown()
