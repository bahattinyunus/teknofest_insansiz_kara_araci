from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Perception Node
        Node(
            package='ika_scripts',
            executable='sign_detection.py',
            name='perception_engine'
        ),
        # Mission Manager
        Node(
            package='ika_scripts',
            executable='mission_manager.py',
            name='mission_manager',
            parameters=[{'use_sim_time': True}]
        ),
        # AI Fusion (Elite)
        Node(
            package='ika_scripts',
            executable='advanced_ai_fusion.py',
            name='tactical_ai'
        )
    ])
