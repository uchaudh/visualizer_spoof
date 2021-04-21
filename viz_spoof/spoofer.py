#! usr/bin/env python3

import rclpy
from rclpy.node import Node
from novatel_gps_msgs.msg import Inspva
from deep_orange_msgs.msg import PtReport, BrakeTempReport, CtReport, RcToCt
from raptor_dbw_msgs.msg import BrakeCmd, AcceleratorPedalCmd, SteeringCmd
import numpy as np
import math
import csv

class Test(Node):


    def __init__(self):
        super().__init__("Visualizer_Node")
        self.pt_pub =  self.create_publisher(PtReport, '/pt_report', 100)
        # self.braketemp_pub = self.create_publisher(BrakeTempReport, '/raptor_dbw_interface/brake_2_report',100)
        self.ct_pub = self.create_publisher(CtReport, '/ct',100)
        self.rc2ct_pub = self.create_publisher(RcToCt, '/rc2ct',100)
        self.brakecmd_pub = self.create_publisher(BrakeCmd,'/raptor_dbw_interface/brake_cmd',100)
        self.accelcmd_pub = self.create_publisher(AcceleratorPedalCmd,'/raptor_dbw_interface/accelerator_pedal_cmd',100)
        self.steeringcmd_pub = self.create_publisher(SteeringCmd,'/raptor_dbw_interface/steering_cmd',100)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0


    def timer_callback(self):
        pt_report = PtReport()
        pt_report.engine_oil_pressure = 80.00
        pt_report.engine_coolant_temperature = 77.00
        pt_report.transmission_oil_pressure = 64.00
        pt_report.transmission_oil_temperature = 43.00
        pt_report.fuel_pressure = 110.00

        ct_report = CtReport()
        ct_report.track_cond_ack = 8
        ct_report.ct_state = 11

        rc2ct_report = RcToCt()
        rc2ct_report.track_cond = 8

        brake_cmd = BrakeCmd()
        brake_cmd.pedal_cmd = 60.00

        accel_cmd = AcceleratorPedalCmd()
        accel_cmd.pedal_cmd = 24.00

        steering_cmd = SteeringCmd()
        steering_cmd.angle_cmd = 250.00

        self.pt_pub.publish(pt_report)
        self.ct_pub.publish(ct_report)
        self.rc2ct_pub.publish(rc2ct_report)
        self.brakecmd_pub.publish(brake_cmd)
        self.accelcmd_pub.publish(accel_cmd)
        self.steeringcmd_pub.publish(steering_cmd)

        self.i += 1


def main(args=None):
    rclpy.init()
    test_node = Test()
    rclpy.spin(test_node)
    rclpy.shutdown()
    
if __name__  == '__main__':
    main()