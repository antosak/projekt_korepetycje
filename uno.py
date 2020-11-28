#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random


# constants
number_of_clients = 20
number_of_iterations = 5
fuel_consumption = 8  # l/100km
average_speed = 50  # km/h
fuel_cost = 4.20  # PlN/l


def read_data():
    data = pd.read_excel()


def create_new_world():
    all_the_clients = []
    for client in range(number_of_clients):
        all_the_clients.append(Client(1, 1, 1, 1, 1, 1))


class Client(object):
    def __init__(self, name, price, coordinates, prep_time, teaching_time, hour, day):
        self.name = name
        self.price = price
        self.coordinates = coordinates
        self.prep_time = prep_time
        self.teaching_time = teaching_time
        self.hour = hour
        self.day = day

    def add_client(self):
        pass

    def remove_client(self):
        pass
