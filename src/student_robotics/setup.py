from setuptools import setup

package_name = 'student_robotics'

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
    maintainer='Edward Haynes',
    maintainer_email='student@unibe.ch',
    description='Student robotics package',
    license='MIT',
    entry_points={
        'console_scripts': [
            'circle_motion = student_robotics.circle_motion:main',
            'odom_monitor = student_robotics.odom_monitor:main',
        ],
    },
)
