from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription ([
		Node(
			package = 'robocon_vision_pkg',
			executable = 'test_node_1',
			name = 'camera_publisher',
			output = 'screen'
		),
		Node(
			package = 'robocon_vision_pkg',
			executable = 'test_node_2',
			name = 'zone_detector',
			output = 'screen'
		)
	])
