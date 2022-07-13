#!/usr/bin/env python
from __future__ import print_function
import cv2 as cv
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image


# def subscribe():
#     rospy.init_node('limo_pov_node', anonymous=False)
#     rospy.Subscriber("/camera/rgb/image_raw", Image, load_image)
#     rospy.spin()

def load_image(image_message):
    bridge = CvBridge()
    try:
        img = bridge.imgmsg_to_cv2(image_message, desired_encoding='passthrough')
        #opencv stores images as BGR, displays images as RGB

        cv.imshow('LIMO POV', img)
        cv.waitKey(0)
        cv.destroyAllWindows
    except:
        print("error")
    
    rospy.spin()
    
if __name__ == '__main__':
    rospy.init_node('limo_pov_node', anonymous=False)
    rospy.Subscriber("/camera/rgb/image_raw", Image, load_image)
