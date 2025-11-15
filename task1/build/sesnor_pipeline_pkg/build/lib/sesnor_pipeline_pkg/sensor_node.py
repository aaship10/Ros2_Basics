import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3

class SensorNode(Node):

	def __init__(self):
		super().__init__("sensor_data")
		self.declare_parameter('publish_rate', 2.0)
		self.publish_rate = self.get_parameter('publish_rate').get_parameter_value().double_value
		self.sensor_publisher = self.create_publisher(Vector3, 'sensor_data', 10)
		self.timer = self.create_timer(2, self.messages)
		self.get_logger().info("This is the sensor node") 

	def messages(self):
		msg = Vector3()
		msg.x = 3.0
		msg.y = 4.0
		msg.z = 5.0
		self.sensor_publisher.publish(msg)
		self.get_logger().info("x = " + str(msg.x) + " y = " + str(msg.y) + " z = " + str(msg.z))

def main(args=None):
	rclpy.init(args=args)
	node = SensorNode()
	rclpy.spin(node)
	rclpy.shutdown()
