#!/usr/bin/python

import rospy

from t2_requirement.msg import t2_message2
from std_msgs.msg import String
    
   

def main():
    rospy.init_node("Result_node")
    pub = rospy.Publisher("result", String , queue_size=10)
    sub = rospy.Subscriber("t2_message", t2_message, callback)
    r = rospy.Rate(1)

    while not rospy.is_shutdown():
         pub.publish(eligibility)
         r.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
