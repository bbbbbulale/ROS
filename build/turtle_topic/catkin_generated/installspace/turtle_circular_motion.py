#!/usr/bin/env python3
import rospy, sys
from geometry_msgs.msg import Twist, Vector3

def MsgInit():
    msg = Twist(linear=Vector3(1.0, 0.0, 0.0), angular=Vector3(0.0, 0.0, 1.0))
    # or
    # msg = Twist()
    # msg.linear= Vector3(1.0, 0.0, 0.0)
    # msg.angular = Vector3(0.0, 0.0, 1.0)
    return msg
    
if __name__ == "__main__":
    rospy.init_node("turtle_circular_motion_node_p")
    pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=100)
    
    rate = rospy.Rate(1)
    msg = MsgInit()
    
    rospy.loginfo("argc:%d  argv:%s", len(sys.argv), sys.argv[1:])
    if len(sys.argv) >= 3:
        msg.linear.x = float(sys.argv[1])
        msg.angular.z = float(sys.argv[2])
        if len(sys.argv) == 4:
            rate.hz = float(sys.argv[3])
    
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()