from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription ([
		Node(
			package = 'action_demo_pkg',
			executable = 'test_node_1',
			name = 'goal_client',
			output = 'screen'
		),
		Node(
			package = 'action_demo_pkg',
			executable = 'test_node_2',
			name = 'goal_tracker_server',
			output = 'screen'
		)
	])
