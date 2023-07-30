from setuptools import setup
from glob import glob
import os


package_name = 'my_pkg'
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
            'simplepub = my_pkg.simplepublisher:main',
            'simplesub = my_pkg.simplesubscriber:main',
            'simpletimepub = my_pkg.simpletimepublisher:main',
            'simpletimesub = my_pkg.simpletimesubscriber:main',
            'messagepub = my_pkg.messagepublisher:main',
            'messagesub1 = my_pkg.messagesubscriber1:main',
            'messagesub2 = my_pkg.messagesubscriber2:main',
            'messagetimesub = my_pkg.messagetimesubscriber:main'
        ],
    },
)
