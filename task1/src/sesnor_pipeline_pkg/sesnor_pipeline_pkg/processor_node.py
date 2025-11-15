import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3

class ProcessorNode(Node):

	def __init__(self):
		super().__init__('processor_node')
		self.processor_node_ = self.create_subscription(Vector3, 'sensor_data', self.messages, 10)
		self.processor_publisher = self.create_publisher(Vector3, 'publisher_data', 10)
		self.get_logger().info("This is the Processor Node")

	def messages(self, msg : Vector3):
		msg.x = msg.x + msg.y + msg.z
		self.processor_publisher.publish(msg)
		self.get_logger().info("Sum = " + str(msg.x))


def main(args=None):
	rclpy.init(args=args)
	node = ProcessorNode()
	rclpy.spin(node)
	rclpy.shutdown()

