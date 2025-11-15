import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import numpy as np

class ZoneDetector(Node):

	def __init__(self):
		super().__init__("zone_detector")
		self.camera_subscriber = self.create_subscription(Image, 'arena_camera/image_raw', self.messages, 10)
		self.get_logger().info("This is the zone detection camera")
		self.cap = None

	def messages(self, msg):
		bridge = CvBridge()
		frame = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		lower_blue = np.array([100, 150, 0])
		upper_blue = np.array([140, 255, 255])
		mask = cv2.inRange(hsv, lower_blue, upper_blue)
		contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		for contour in contours:
			if cv2.contourArea(contour) > 500:
				x, y, w, h = cv2.boundingRect(contour)
				cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		lower_green = np.array([35, 40, 40])
		upper_green = np.array([85, 255, 255])
		mask = cv2.inRange(hsv, lower_green, upper_green)
		contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		for contour in contours:
			if cv2.contourArea(contour) > 100:
				x, y, w, h = cv2.boundingRect(contour)
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		lower_red = np.array([0, 100, 100])
		upper_red = np.array([10, 255, 255])
		mask = cv2.inRange(hsv, lower_red, upper_red)
		contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		for contour in contours:
			if cv2.contourArea(contour) > 100:
				x, y, w, h = cv2.boundingRect(contour)
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2) 

		cv2.imshow("colourss targeted", frame)
		cv2.waitKey(1)

	def messages_destroy(self):
		self.cap.release()
		cv2.destroyAllWindows()

def main(args=None):
	rclpy.init(args=args)
	node = ZoneDetector()
	rclpy.spin(node)
	node.messages_destroy()
	rclpy.shutdown()
