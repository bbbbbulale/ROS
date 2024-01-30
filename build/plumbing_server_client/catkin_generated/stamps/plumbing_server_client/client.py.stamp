#! usr/bin/env python
import rospy, sys
from plumbing_server_client.srv import *

def isInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
    
def client_addTwoInts(num1 , num2):
    rospy.init_node("myClient_py")
    client = rospy.ServiceProxy("add_two_ints", AddInts)

    client.wait_for_service()
    # rospy.wait_for_service("add_two_ints") 法2
    try:
        # 三种请求方法
        # ack = client(num1, num2) # 法1
        # ack = client.call(num1, num2) # 法2
        req = AddIntsRequest(num1, num2)
        ack = client.call(req) # 法3

        # -1为error code
        if ack.sum == -1:  
            rospy.loginfo("%s, 不支持请求小于0的参数！", ack)
        else:
            rospy.loginfo("%s", ack)
    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s", e)

if __name__ == "__main__": 
    # 必须两个int型参数
    if len(sys.argv)!=3 or not isInt(sys.argv[1]) or not isInt(sys.argv[2]):
        rospy.logwarn("Error Params")
        sys.exit(1)
    else:
        client_addTwoInts(int(sys.argv[1]), int(sys.argv[2]))