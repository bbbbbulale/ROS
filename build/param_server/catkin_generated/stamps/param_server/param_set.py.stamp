# ! /usr/bin/env python
'''
    rospy.set_param("键", 值)
'''
import rospy

# 设置参数
def SetParam():
    rospy.set_param("nh_int", 10)
    rospy.loginfo("ros::param设置nh_int成功！")
    rospy.set_param("nh_double", 3.1415)
    rospy.loginfo("ros::param设置nh_double成功！")
    rospy.set_param("nh_bool", True)
    rospy.loginfo("ros::param设置nh_bool成功！")
    rospy.set_param("nh_string", "hello!")
    rospy.loginfo("ros::param设置nh_string成功！")
    rospy.set_param("nh_list", ["要", "鑫", "海"])
    rospy.loginfo("ros::param设置nh_list成功！")
    rospy.set_param("nh_dict", {"他":"男孩", "她":"女孩"})
    rospy.loginfo("ros::param设置nh_dict成功！")

# 修改参数
def ModifyParam():
    rospy.set_param("nh_string", "nani???")
    rospy.loginfo("ros::param修改nh_string成功！")
    
if __name__ == "__main__":
    rospy.init_node("param_set_node_")
    
    rospy.loginfo("-----正在设置参数-----")
    SetParam()
    rospy.loginfo("-----设置参数over-----\n")
    
    rospy.loginfo("-----正在修改参数-----")
    ModifyParam()
    rospy.loginfo("-----修改参数over-----\n")
    
