#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import time

# constants
default_path = 'Tutoring.xlsx'
number_of_clients = 20
number_of_iterations = 5
fuel_consumption = 8  # l/100km
average_speed = 50  # km/h
fuel_cost = 4.20  # PlN/l
our_home = (0, 0)


def read_data(path: str = default_path):
    data = pd.read_excel(path, index_col=0, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
    return data


def create_brave_new_world(source: str = default_path):
    all_the_clients = []
    data = read_data(source)
    for index, row in data.iterrows():
        all_the_clients.append(Client(index, row['Price'], (row['X_'], row['Y_']), row['Preparation_Time'], row['Lesson_Duration'], row['Lesson_Start_Time'],
                                      row['Lesson_Day']))

    return all_the_clients


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


example = (0, 1, 0, 1, 1)
world = create_brave_new_world()


def objective_function(current_solution=example):
    income = []
    last_visit = our_home
    for elem in world:
        income = 0
    result = np.dot(current_solution, )
    return result
