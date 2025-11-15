import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2

class CameraPublisher(Node):

	def __init__(self):
		super().__init__("camera_publisher")
		self.camera_publisher_ = self.create_publisher(Image, 'arena_camera/image_raw', 10)
		self.timer = self.create_timer(0.001, self.messages)
		self.cap = cv2.VideoCapture(0)
		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
		self.get_logger().info("This is the camera publisher")

	def messages(self):
		ret, frame = self.cap.read()
		if not ret:
			self.get_logger().info("Camera failed")
			return
		cv2.imshow("original view", frame)
		bridge = CvBridge()
		image = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
		self.camera_publisher_.publish(image)
		cv2.waitKey(1)

	def destroy_messages(self):
		self.cap.release()
		cv2.destroyAllWindows()


def main(args=None):
	rclpy.init(args=args)
	node = CameraPublisher()
	rclpy.spin(node)
	node.destroy_messages()
	rclpy.shutdown()
