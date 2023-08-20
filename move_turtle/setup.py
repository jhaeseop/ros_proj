from setuptools import setup
import os
from glob import glob

package_name = 'move_turtle'
share_dir = 'share/' + package_name

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (share_dir + '/launch', glob(os.path.join('launch', '*.launch.py')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros2',
    maintainer_email='jhaeseop@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mt = move_turtle.moveTurtle:main',
            'mt2 = move_turtle.moveTurtle2:main',
            'mt3 = move_turtle.moveTurtle_0806:main',
            'mt4 = move_turtle.moveTurtle2_0806:main',
            'tb3_image_sub = move_turtle.imagesub:main',
            'gostraight = move_turtle.gostraight:main',
            'arucogo = move_turtle.arucogo:main',
            'rotate = move_turtle.rotate:main',
        ],
    },
)
