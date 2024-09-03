#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

# Create a subscriber
class PoseSubscriberNode(Node):

    def __init__(self):
        super().__init__("pose_subscriber") # the name of the node
        self.pose_subscriber_ = self.create_subscription(
            Pose, # type
            "/turtle1/pose", # name of the topic
            self.pose_callback,
            10 # queue
        )

    def pose_callback(self, msg: Pose):
        self.get_logger().info("(" + str(msg.x) + " , " + str(msg.y) + ")")


def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node=node)
    rclpy.shutdown()