#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist

def cmd_vel_pub():
    rospy.init_node('draw_circle', anonymous=False)  # 修正为 init_node
    cmd_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    twist = Twist()
    rospy.loginfo('Start control robot to draw a circle')
    
    while not rospy.is_shutdown():
        twist.linear.x = 0.2
        twist.angular.z = 0.4  # 修正为 angular.z
        cmd_pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':  # 修正为 '__main__'
    try:
        cmd_vel_pub()
    except rospy.ROSInterruptException:
        pass
