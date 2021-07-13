#!/usr/bin/python

import rospy

from t1_requirement.msg import t1_message

def main():
    rospy.init_node("input_node")
    pub = rospy.Publisher("sum", t1_message, queue_size = 1)
    r = rospy.Rate(1)

    msg = t1_message()
    while not rospy.is_shutdown():
         msg.x = 2
         msg.y = 3
         pub.publish(msg)
         r.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass

    
