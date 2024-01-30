#! usr/bin/env python

import rospy
from  plumbing_pub_sub.msg import Person

def talker():
    rospy.init_node("man")
    pub = rospy.Publisher("xiangqin", Person, queue_size=10)

    p = Person(name = "阿赫里克", age=22, height=1.98)
    # p.name = "阿赫里克"
    # p.age = 22
    # p.height = 1.98

    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        p.age += 1

        pub .publish(p)
        rospy.loginfo("我叫%s，今年%d岁，身高：%.2f米", p.name, p.age, p.height)

        r.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass