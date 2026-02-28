import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    """
    TACTICAL OPERATION MASTER LAUNCH
    Brings up the entire Gökbörü architecture:
    1. Gazebo Simulation (Arena + UGV)
    2. Computer Vision (YOLO + Sign)
    3. Cyber Defense Daemon
    4. Mission Manager State Machine
    """
    
    pkg_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 1. Sim Environment
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_dir, 'sim', 'gokboru_gazebo.launch.py'))
    )

    # 2. Sub-System Bringup (Vision + Security)
    # Using the existing system_bringup snippet for modularity logic
    subsystems_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_dir, 'launch', 'system_bringup.launch.py'))
    )

    # 3. Dedicated ROS2 Bridge (The interface between our AI and ROS2 framework)
    ros2_bridge_node = TimerAction(
        period=5.0, # Let Gazebo and sensors settle
        actions=[
            LogInfo(msg="Spawning ROS2 Algorithm Bridge..."),
            Node(
                package='teknofest_insansiz_kara_araci',
                executable='ros2_bridge.py',
                name='gokboru_ros2_interface',
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        LogInfo(msg="====================================================="),
        LogInfo(msg="[GÖKBÖRÜ MASTER] INITIATING FULL TACTICAL OPERATION"),
        LogInfo(msg="====================================================="),
        gazebo_launch,
        subsystems_launch,
        ros2_bridge_node
    ])
