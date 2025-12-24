from setuptools import setup
import os
from glob import glob

package_name = 'teknofest_insansiz_kara_araci'

setup(
    name=package_name,
    version='4.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'sim'), glob('sim/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Bahattin Yunus',
    maintainer_email='bahattinyunus@example.com',
    description='Teknofest IKA Elite Guide',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mission_manager = scripts.mission_manager:main',
            'teleop = scripts.control.teleop_example:main',
        ],
    },
)
