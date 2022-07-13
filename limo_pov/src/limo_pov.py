#!/usr/bin/env python
from __future__ import print_function
import cv2 as cv
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image

rospy.init_node('limo_pov_node', anonymous=False)
rospy.Subscriber("/camera/rgb/image_raw", Image, load_image)

def load_image(image_message):
    bridge = CvBridge()
    try:
        img = bridge.imgmsg_to_cv2(image_message, desired_encoding='passthrough')
        cv.imshow('LIMO POV', img)

        # Convert to GRB colour space
        # GRB_img = img[:, :, [2, 0, 1]]
        # cv.imshow("LIMO's WACKY POV", GRB_img)
        
        cv.waitKey(0)
        cv.destroyAllWindows
    except:
        print("error")
    

while not rospy.is_shutdown():
    rospy.spin()

#FINAL
# #!/usr/bin/env python
# from __future__ import print_function
# import cv2 as cv
# from cv_bridge import CvBridge
# import rospy
# from sensor_msgs.msg import Image

# rospy.init_node('limo_pov_node', anonymous=False)

# def load_image(image_message):
#     bridge = CvBridge()
#     try:
#         img = bridge.imgmsg_to_cv2(image_message, desired_encoding='passthrough')
#         cv.imshow('LIMO POV', img)

#         # Convert to GRB colour space
#         GRB_img = img[:, :, [2, 0, 1]]
#         cv.imshow("LIMO's WACKY POV", GRB_img)
        
#         cv.waitKey(0)
#         cv.destroyAllWindows
#     except:
#         print("error")
    
# sub = rospy.Subscriber("/camera/rgb/image_raw", Image, load_image)
# while not rospy.is_shutdown():
#     rospy.spin()
    