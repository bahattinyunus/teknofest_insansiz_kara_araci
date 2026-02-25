import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Simulated package name assuming teknofest_insansiz_kara_araci is built as a ROS package
    # For standalone launch, we'll use absolute/relative paths based on the workspace
    pkg_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    world_file = os.path.join(pkg_dir, 'sim', 'worlds', 'tactical_arena.world')
    urdf_file = os.path.join(pkg_dir, 'sim', 'ika_base.urdf')

    # Start Gazebo client and server with the custom tactical world
    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', world_file, '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    # Robot State Publisher to broadcast TF frames
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}]
    )

    # Spawn the UGV entity in the Gazebo Engine
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'gokboru_sotm', '-x', '0', '-y', '0', '-z', '0.5'],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        node_robot_state_publisher,
        spawn_entity,
    ])
