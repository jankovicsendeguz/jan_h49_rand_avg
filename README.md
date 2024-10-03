# `jan_h49_rand_avg` package
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)

A package két node-ból áll. A /gen_node véletlenszerű számokat generál és egy std_msgs/float32 topicban publikálja. Az /sum_node feliratkozik erre a topicra, összegzi az eddig kapott számokat, majd az átlagot egy másik std_msgs/float32 topicban publikálja.
Megvalósítás ROS 2 Humble alatt.

## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/jankovicsbendeguz/jan_h49_rand_avg
```

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select jan_h49_rand_avg --symlink-install
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source ~/ros2_ws/install/setup.bash
```
</details>

``` r
ros2 launch jan_h49_rand_avg launch_example1.launch.py
```
