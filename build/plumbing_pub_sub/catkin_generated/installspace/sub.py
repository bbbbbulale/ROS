#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def MsgHandle(msg):
    rospy.loginfo("Python subscriber订阅的数据：%s", msg.data)

def listener():
    # 初始化ROS节点
    rospy.init_node("subscriber")

    # 创建订阅者对象
    sub = rospy.Subscriber("mytopic", String, MsgHandle, queue_size=10)

    rospy.spin()


if __name__ == "__main__":
    listener()
