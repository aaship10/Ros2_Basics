from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'sesnor_pipeline_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', 'sesnor_pipeline_pkg', 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		"test_node = sesnor_pipeline_pkg.sensor_node:main",
		"test_node_2 = sesnor_pipeline_pkg.processor_node:main",
		"test_node_3 = sesnor_pipeline_pkg.logger_node:main"
        ],
    },
)
