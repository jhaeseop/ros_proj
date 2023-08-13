from setuptools import setup

package_name = 'move_turtle'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
        ],
    },
)
