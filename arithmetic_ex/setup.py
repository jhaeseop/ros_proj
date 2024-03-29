from setuptools import setup
from setuptools import find_packages
import glob, os

package_name = 'arithmetic_ex'
share_dir = 'share/' + package_name

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (share_dir + '/param', glob.glob(os.path.join('param', '*.yaml'))),
        (share_dir + '/launch', glob.glob(os.path.join('launch', '*.launch.py'))),
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
            'argument = arithmetic_ex.argument:main',
            'argumentsub = arithmetic_ex.argumentsub:main',
            'operator = arithmetic_ex.operator:main',
            'main = arithmetic_ex.main:main',
            'checker = arithmetic_ex.checker:main',
        ],
    },
)
