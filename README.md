# Ros2_Basics
🤖 ROS 2 Robotics Fundamentals Tasks
This repository contains solutions for the first three fundamental tasks of a ROS 2 training assignment, focusing on core concepts like node communication, parameter handling, vision integration, and the ROS 2 Action system.

# 🚀 Project Overview
The goal of this project is to build a foundational understanding of the Robot Operating System 2 (ROS 2) by implementing practical robotic software components, including:

Data Pipeline: Setting up standard Publisher-Subscriber communication (ros2 topic).
Computer Vision: Integrating OpenCV with ROS 2 using cv_bridge for real-time image processing.
Goal Tracking: Implementing an Action Server/Client system (ros2 action) for robust, long-running tasks.

# ✅ Implemented Tasks
This repository includes the following three tasks, each residing in its own dedicated folder:
1. ROS 2 Topics & Node Communication
  Folder: task1
  Concept: Demonstrates the core Publisher-Subscriber pattern and dynamic parameter handling.
  Pipeline: Sensor Node -> Processor Node -> Logger Node
    Sensor Node: Publishes fake IMU/encoder data (geometry_msgs/Vector3).
    Key Feature: Exposes a parameter named publish_rate (default 2 Hz) that can be changed live via ros2 param set.
    Processor Node: Subscribes to sensor data and computes a simple value (e.g., vector length).
    Logger Node: Subscribes to the processed value and prints it to the terminal.
 Launch File: sesnor_pipeline_pkg.launch.py (It is not a typing error, I have named it that way)

2. ROS 2 + OpenCV Vision for Arena Detection
  Folder: task2
  Concept: Demonstrates the integration of OpenCV for computer vision tasks with ROS 2, using cv_bridge to convert between ROS 2 sensor_msgs/Image and OpenCV image formats.
  Node:
    camera_publisher.py: Publishes frames from the webcam or a video to the topic /arena_camera/image_raw at a parameterized rate (default 10 Hz)
    zone_detector.py: Subscribes to the image topic, uses HSV color filtering to detect colored zones (e.g., Red, Green, Blue) , draws bounding boxes , and displays the processed view.
  Launch File: robocon_vision_pkg.launch.py

4. Action Server-Client System
  Folder: task3
  Concept: Implements the ROS 2 Action system, which is crucial for handling long-running, interruptible tasks like navigation (nav2).
  Nodes:
    goal_tracker_server.py: Action Server. Receives a target coordinate (x, y) , sends feedback every second, and returns a result ("Goal Completed") upon reaching the goal
    goal_client.py: Action Client. Sends random (x, y) goals every 10 seconds , displays the live feedback updates , and logs the final result.
  Launch: action_demo_pkg.launch.py

# Build the Workspace
1. Clone the Repository:
git clone https://github.com/aaship10/Ros2_Basics.git
cd Ros2_Basics

2. Source your ROS 2 environment:
source /opt/ros/<your_distro>/setup.bash

3. Copy the package folders into your ROS 2 workspace (src folder): Assuming you have a workspace named ros2_ws:
cp -r task1 task2 task3 ~/ros2_ws/src/

4. Build the packages from your workspace root:
cd ~/ros2_ws
colcon build

5. Source the workspace:
source install/setup.bash

6. Running the Tasks
Task        Command                                            
Task 1      ros2 launch task1 sesnor_pipeline_pkg.launch.py    
Task 2      ros2 launch task2 robocon_vision_pkg.launch.py     
Task 3      ros2 launch task3 action_demo_pkg.launch.py        
