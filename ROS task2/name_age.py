#!/usr/bin/python

import rospy

from t2_requirement.msg import t2_message1

def main():
    rospy.init_node('name_age')
    pub = rospy.Publisher('input', t2_message, queue size = 10)
    r = rospy.Rate(1)
    msg = t2_message()
 
    while not ropsy.is_shutdown():
         msg.name = "Rohan"
         msg.age = 22
         pub.publish(msg)
         r.sleep()

if __name__ = "__main__":
    try:
       main()
    except rospy.ROSInterruptException:
       pass


