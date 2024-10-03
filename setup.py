from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'jan_h49_rand_avg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jankovicsbendeguz',
    maintainer_email='jankovicsbendeguz@gmail.com',
    description='ROS 2 csomag ami számokat generál, majd azokat átlagolja',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           'random_generator_node = jan_h49_rand_avg.random_generator_node:main',
            'average_node = jan_h49_rand_avg.average_node:main',
        ],
    },
)
