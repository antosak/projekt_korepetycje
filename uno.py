#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
print("Hello world")


def create_new_world():
    pass


class Client(object):
    def __init__(self, price, coordinates, prep_time, teaching_time, hour):
        self.price = price
        self.coordinates = coordinates
        self.prep_time = prep_time
        self.teaching_time = teaching_time
        self.hour = hour

    def add_client(self):
        pass

    def remove_client(self):
        pass

