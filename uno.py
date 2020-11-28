#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt
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
fuel_coeff = (fuel_consumption / 100) * fuel_cost  # useful thing
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


def legal_child(Client_list, child, home_returns_vector) -> bool:
    income = 0
    for i in range(0, len(child)):
        if child[i] == 1:
            income += Client_list[i].price
    if income > 350:
        return False
    coordinate_list = []
    for i in range(0, len(child)):
        if child[i] == 1:
            if Client_list[i].coordinates in coordinate_list:
                return False
            else:
                coordinate_list.append(Client_list[i].coordinates)
    days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    days_value_list = [0, 0, 0, 0, 0, 0, 0]
    last_coordinates = our_home
    total_time = 0
    for i in range(0, len(child)):
        if child[i] == 1:
            j = days_list.index(Client_list[i].day)
            days_value_list[j] += Client_list[i].teaching_time
            days_value_list[j] += (sqrt(((Client_list[i].coordinates[0] - last_coordinates[0]) ** 2) +
                                        ((Client_list[i].coordinates[1] - last_coordinates[1]) ** 2)))/average_speed
            last_coordinates = Client_list[i].coordinates
            if home_returns_vector[i] == 1:
                last_coordinates = our_home
                days_value_list[j] += (sqrt(((Client_list[i].coordinates[0] - last_coordinates[0]) ** 2) +
                                            ((Client_list[i].coordinates[1] - last_coordinates[1]) ** 2)))/average_speed
    for days in days_value_list:
        if days > 4:
            return False
        total_time += days
    for i in range(0, len(child)):
        if child[i] == 1:
            total_time += Client_list[i].prep_time
    if total_time > 28:
        return False
    return True


def kappa_maker(Client_list, child):
    kappa = []
    for i in range(0, len(child)):
        if child[i] == 0:
            kappa.append(0)
        else:
            if i+1 != len(child):
                if child[i+1] == 1:
                    if Client_list[i].day == Client_list[i+1].day:
                        kappa.append(0)
                    else:
                        kappa.append(1)
            else:
                kappa.append(1)
    return kappa


example_sol = (0, 1, 0, 1, 1)
example_kappa = (1, 0, 0, 0, 1)
world = create_brave_new_world()


def objective_function(current_solution=example_sol, kappa=example_kappa):
    income = []
    last_visit = our_home
    kappa_counter = 0
    for elem in world:
        income.append(elem.price - np.sqrt((elem.coordinates[0] - last_visit[0])**2 + (elem.coordinates[1] - last_visit[1])**2)*fuel_coeff
                      - kappa[kappa_counter]*np.sqrt((our_home[0] - last_visit[0])**2 + (our_home[1] - last_visit[1])**2)*fuel_coeff)
        if current_solution[kappa_counter] == 1:
            last_visit = elem.coordinates
        kappa_counter += 1
    result = np.dot(current_solution, income)
    return result


res = objective_function()
