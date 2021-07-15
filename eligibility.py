#!/usr/bin/python

import rospy

from t2_requirement.msg import t2_message2
from std_msgs.msg import String

name1 = String()
eligibility = String()

def callback(msg):
    if msg.age >= 18:
       msg.eligibility = 'Eligible'
    else
       msg.eligibility = 'Not eligible'
    eligibility.data = msg.eligibility
    
    
    rospy.loginfo(eligibility)

def main():
    rospy.init_node("Eligibility_node")
    pub = rospy.Publisher("eligible", Int16 , queue_size=1)
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
