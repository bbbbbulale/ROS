#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    # 初始化ROS节点
    rospy.init_node("publisher")
    # 创建发布者对象
    pub = rospy.Publisher("mytopic", String, queue_size=10)
    # 编写发布逻辑并发布数据
    msg = String()
    count = 0

    rate = rospy.Rate(1)
    rospy.sleep(1)

    while not rospy.is_shutdown():
        count += 1
        msg.data = "hello Python" + str(count)

        pub.publish(msg)
        rospy.loginfo("发布的数据是：%s \n", msg.data)

        rate.sleep()


if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass