from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([
		Node(
			package = 'sesnor_pipeline_pkg',
			executable = 'test_node',
			name = 'sensor_node',
			output = 'screen',
			parameters = [{'publish_rate': 2.0}]
		),

		Node(
			package = 'sesnor_pipeline_pkg',
			executable = 'test_node_2',
			name = 'processor_node',
			output = 'screen'
		),

		Node(
			package = 'sesnor_pipeline_pkg',
			executable = 'test_node_3',
			name = 'logger_node',
			output = 'screen'
		)
	])
