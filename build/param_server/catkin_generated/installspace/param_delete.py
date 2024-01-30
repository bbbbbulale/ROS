#!/usr/bin/env python3
'''
    rospy.delete_param("键")
    键存在时，可以删除成功，键不存在时，会抛出异常
'''
import rospy

# 删除参数
def DeleteParam():
    try:
        rospy.delete_param("nh_int")
        rospy.loginfo("删除nh_int成功！")
    except Exception as e:
        rospy.loginfo("删除nh_int失败！")
        
if __name__ == "__main__":
    rospy.init_node("param_delete_node_")

    rospy.loginfo("-----正在删除参数-----")
    DeleteParam()
    rospy.loginfo("-----删除参数over-----\n")
