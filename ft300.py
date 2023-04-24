#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Echo client program

import socket
import csv


class Ft300:

    def __init__(self, csv_file):
        # HOST = raw_input("Enter IP address of UR controller:") # The remote host
        # HOST = '192.168.10.52'
        self.UR5 = "192.168.10.52"
        self.PORT = 63351 # The same port as used by the server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.encoding = 'utf-8'
        self.f = open(csv_file, "w")

    def connect(self):
        self.s.connect((self.UR5, self.PORT))

    def get_ft_data(self):
        """Get FT300 force and torque value

        :return: float list
        """
        data = self.s.recv(1024)
        data = data.decode(self.encoding)
        data = data.replace("(", "")
        data = data.replace(")", "\n")
        self.ft_str = data
        ft_list = [float(data.split(",")[0]), float(data.split(",")[1]),
                   float(data.split(",")[2]), float(data.split(",")[3]),
                   float(data.split(",")[4]), float(data.split(",")[5])]
        return ft_list

    def write_to_csv(self):
        self.write(self.ft_str)

    def disconnect(self):
        self.s.close

