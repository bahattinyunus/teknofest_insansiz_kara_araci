import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    """
    MASTER BRINGUP LAUNCH FILE (GÖKBÖRÜ SOTM)
    Initializes perception, AI fusion, and mission management asynchronously 
    using ROS 2 launch capabilities.
    """
    
    # 1. Perception Node (Computer Vision / YOLO)
    perception_node = Node(
        package='teknofest_insansiz_kara_araci',
        executable='yolo_inference.py',
        name='yolo_vision_core',
        output='screen',
        parameters=[{'use_tensorrt': True}]
    )

    # 2. Guardian Anomaly Detector (Security Layer)
    guardian_node = Node(
        package='teknofest_insansiz_kara_araci',
        executable='anomaly_detector.py',
        name='guardian_anomaly_agent',
        output='screen'
    )

    # 3. Mission Manager (Core logic delayed to allow sensors to boot)
    mission_manager_node = TimerAction(
        period=3.0, # Wait 3 seconds for sensors and AI to initialize
        actions=[
            LogInfo(msg="Sensors nominal. Initializing Mission Manager Core..."),
            Node(
                package='teknofest_insansiz_kara_araci',
                executable='mission_manager.py',
                name='gokboru_mission_manager',
                output='screen'
            )
        ]
    )

    # Note: In a real environment, you'd integrate the LiDAR drivers and NAV2 here.

    return LaunchDescription([
        LogInfo(msg="[GÖKBÖRÜ MASTER] Starting System Architecture..."),
        perception_node,
        guardian_node,
        mission_manager_node
    ])
