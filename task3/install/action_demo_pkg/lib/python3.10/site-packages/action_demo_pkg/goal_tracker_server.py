import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

class ActionDemo(Node):

	def __init__(self):
		super().__init__("action_demo")
		#self.action_subscribe = self.create_subscription(Point, 'action_data', self.messages_store, 10)
		self.declare_parameter('x_value', 0.0)
		self.declare_parameter('y_value', 0.0)
		self.action_subscribe = self.create_subscription(Point, 'action_data', self.messages_store, 10)
		self.x_value = self.get_parameter('x_value').get_parameter_value().double_value
		self.y_value = self.get_parameter('y_value').get_parameter_value().double_value
		self.last_msg = None
		self.timer = self.create_timer(0.1, self.messages)
		self.get_logger().info("This is the action server node")

	def messages_store(self, msg=None):
		self.last_msg = msg
	def messages(self):

		if self.last_msg:
			if self.last_msg.x > self.x_value:
				self.x_value+=1
			if self.last_msg.x < self.x_value:
				self.x_value-=1
			if self.last_msg.y > self.y_value:
				self.y_value += 1
			if self.last_msg.y < self.y_value:
				self.y_value -= 1
			self.get_logger().info("X-value = " + str(self.x_value) + " Y-value = " + str(self.y_value))

			if self.x_value == self.last_msg.x and self.y_value == self.last_msg.y:
				self.get_logger().info("Goal Completed")
				self.last_msg = None



def main(args=None):
	rclpy.init(args=args)
	node = ActionDemo()
	rclpy.spin(node)
	rclpy.shutdown()
