#! usr/bin/env python

import rospy
from plumbing_pub_sub.msg import Person

def MsgHandle(msg):
    rospy.loginfo("收到的话题消息：%s, %d, %.2f", msg.name, msg.age, msg.height)

def listener():
    rospy.init_node("woman")
    sub = rospy.Subscriber("xiangqin", Person, MsgHandle, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    listener()