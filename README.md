# First Bot — ROS 2 Autonomous RC-Style Simulation

A deeper starting point for a miniature, 3D-printable robot platform. The first milestone provides a four-wheel RC-style chassis, Gazebo sensors, and a bounded navigation arena for mapping and Nav2 work.

## Current simulation

- Four independently modeled rubber wheels and printable box chassis
- Gazebo differential-drive plugin with `/cmd_vel` and `/odom`
- 2D lidar: `/scan`, 720 samples, 12 m range
- RGB/depth camera: `/camera/rgbd/...`
- IMU: `/imu/data`
- Simulated wheel odometry and TF
- Arena with boundary walls and obstacles

Dimensions are in metres. The nominal chassis is 420 x 300 x 100 mm and wheel diameter is 150 mm. These dimensions are intended as a simulation reference for a future CAD/STL package; validate mechanical tolerances, fasteners, motor mounts, and center of gravity before printing.

## Build and run

```bash
# In a ROS 2 workspace containing this repository
colcon build --symlink-install --packages-select first_bot
source install/setup.bash
ros2 launch first_bot sim.launch.py
```

In a second terminal, start localization and mapping:

```bash
source install/setup.bash
ros2 launch first_bot autonomy.launch.py
```

After saving a map, start Nav2 (in a new terminal):

```bash
ros2 launch first_bot nav2.launch.py
```

Drive it from another terminal:

```bash
source install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Inspect sensors:

```bash
ros2 topic echo /scan
ros2 topic echo /imu/data
ros2 topic list
```

## Roadmap

1. Add a dedicated RViz configuration and map-save workflow.
2. Add controller-independent wheel joints and realistic motor limits.
3. Create parametric CAD/STL files for chassis plates, wheel hubs, sensor mast, and battery tray.
4. Add camera optical frames and point-cloud/depth-image topics.
5. Add automated launch tests and simulation smoke tests.
6. Add realistic friction, noise, IMU bias, lidar dropout, and wheel-slip models.
7. Add route scenarios and autonomy evaluation metrics.

This package is simulation-first. The CAD design and physical dimensions must be reviewed against the selected motors, wheels, battery, electronics, and printer before manufacturing.
