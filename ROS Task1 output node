#!/usr/bin/python

import rospy

from t1_requirement.msg import t1_message
from std_msgs.msg import Int16

result = Int16()

def callback(msg):
    result.data = msg.a + msg.b
    rospy.loginfo(result)

def main():
    rospy.init_node("output_node")
    pub = rospy.Publisher("sum", Int16 , queue_size=1)
    sub = rospy.Subscriber("t1_message", t1_message, callback)
    r = rospy.Rate(1)

    while not rospy.is_shutdown():
         pub.publish(result)
         r.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
