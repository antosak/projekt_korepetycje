#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt
import pandas as pd
import random

# constants
default_path = 'Tutoring.xlsx'
number_of_clients = 20
number_of_iterations = 5
fuel_consumption = 8  # l/100km
average_speed = 50  # km/h
fuel_cost = 4.20  # PlN/l
fuel_coeff = (fuel_consumption / 100) * fuel_cost  # useful thing
our_home = (0, 0)
waiting_threshold = 0.5


def read_data(path: str = default_path):
    data = pd.read_excel(path, index_col=0, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
    return data


# Returns list of instances of class Client in chronological order in a week.
def create_brave_new_world(source: str = default_path) -> list:
    """
    :param source: path to a file that provides data
    :return: ordered list of all the meetings and information about them
    """
    all_the_clients = []
    data = read_data(source)
    for index, row in data.iterrows():
        all_the_clients.append(
            Client(index, row['Price'], (row['X_'], row['Y_']), row['Preparation_Time'], row['Lesson_Duration'],
                   row['Lesson_Start_Time'],
                   row['Lesson_Day']))

    return all_the_clients


# Somewhat surprisingly class Client represents a single date with a fool, not a fool itself.
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


# Checks whether a child (solution), that algorithm returned, is legal (within several severe limitations).
def legal_child(Client_list, child, home_returns_vector) -> bool:
    """
    :param client_list: list that function "create_brave_new_world" returns
    :param child: solution that algorithm (crossover or mutation) provides
    :param home_returns_vector: list that function "kappa_maker" provides
    :return: decision (bool) if new solution is legal
    """
    income = 0
    for i in range(0, len(child)):
        if child[i] == 1:
            income += Client_list[i].price
    if income > 350:
        return False
    id_list = []
    for i in range(0, len(child)):
        if child[i] == 1:
            if Client_list[i].name in id_list:
                return False
            else:
                id_list.append(Client_list[i].name)
    days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    days_value_list = [0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(child)):
        if child[i] == 1:
            if i+1 != len(child):
                if child[i+1] == 1:
                    if home_returns_vector[i] == 0:
                        client_time = 0
                        client_time += Client_list[i].teaching_time
                        client_time += (sqrt(((Client_list[i+1].coordinates[0] - Client_list[i].coordinates[0]) ** 2) +
                                        ((Client_list[i+1].coordinates[1] - Client_list[i].coordinates[1]) ** 2)))/average_speed
                        if Client_list[i+1].hour < Client_list[i].hour + client_time:
                            return False
                    else:
                        if Client_list[i].day == Client_list[i + 1].day:
                            client_time = 0
                            client_time += Client_list[i].teaching_time
                            client_time += (sqrt(((Client_list[i].coordinates[0] - our_home[0]) ** 2) +
                                                 ((Client_list[i].coordinates[1] - our_home[1]) ** 2)))/average_speed
                            client_time += (sqrt(((Client_list[i+1].coordinates[0] - our_home[0]) ** 2) +
                                                 ((Client_list[i+1].coordinates[1] - our_home[1]) ** 2)))/average_speed
                            if Client_list[i + 1].hour < Client_list[i].hour + client_time:
                                return False
                            j = days_list.index(Client_list[i].day)
                            days_value_list[j] += Client_list[i + 1].hour - (Client_list[i].hour + client_time)
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


# Based on the solution says when we go back home
def kappa_maker(Client_list, child):
    """
    :param client_list: list that function "create_brave_new_world" returns
    :param child: solution that algorithm (crossover or mutation) provides
    :return: binary vector, that says when we go back home
    """
    kappa = []
    for i in range(0, len(child)):
        if child[i] == 0:
            kappa.append(0)
        else:
            if i+1 != len(child):
                if child[i+1] == 1:
                    if Client_list[i].day == Client_list[i+1].day:
                        client_time = 0
                        client_time += Client_list[i].teaching_time
                        client_time += (sqrt(((Client_list[i + 1].coordinates[0] - Client_list[i].coordinates[0]) ** 2) +
                                             ((Client_list[i + 1].coordinates[1] - Client_list[i].coordinates[1]) ** 2))) / average_speed
                        client_time = Client_list[i + 1].hour - (Client_list[i].hour + client_time)
                        if client_time <= waiting_threshold:
                            kappa.append(0)
                        else:
                            kappa.append(1)
                    else:
                        kappa.append(1)
                else:
                    kappa.append(1)
            else:
                kappa.append(1)
    return kappa


example_sol = (0, 1, 0, 1, 1)
example_kappa = (1, 0, 0, 0, 1)
world = create_brave_new_world()


def income_objective_function(solution: list = example_sol, kappa: list = example_kappa):
    """
    :param solution: something that crossover or mutation spitted out
    :param kappa: information from "kappa maker" - when we go back home
    :return: real number that tells how good in terms of income the solution is
    """
    income = []
    last_visit = our_home
    counter = 0
    for elem in world:
        income.append(elem.price - np.sqrt(
            (elem.coordinates[0] - last_visit[0]) ** 2 + (elem.coordinates[1] - last_visit[1]) ** 2) * fuel_coeff
                      - kappa[counter] * np.sqrt(
            (our_home[0] - last_visit[0]) ** 2 + (our_home[1] - last_visit[1]) ** 2) * fuel_coeff)
        if solution[counter] == 1:
            last_visit = elem.coordinates
        counter += 1
    result = np.dot(solution, income)
    return result


def time_objective_function(solution: list = example_sol, kappa: list = example_kappa):
    """
    :param solution: solution: something that crossover or mutation spitted out
    :param kappa: information from "kappa maker" - when we go back home
    :return: real number that tells how good in terms of time the solution is
    """
    time_spent = []
    last_visit = our_home
    counter = 0
    for elem in world:
        time_spent.append(elem.prep_time + elem.teaching_time + np.sqrt(
            (elem.coordinates[0] - last_visit[0]) ** 2 + (elem.coordinates[1] - last_visit[1]) ** 2) / average_speed
                          + kappa[counter] * np.sqrt(
            (our_home[0] - last_visit[0]) ** 2 + (our_home[1] - last_visit[1]) ** 2) / average_speed)
        if solution[counter] == 1:
            last_visit = elem.coordinates
        counter += 1
    result = np.dot(solution, time_spent)
    return result


def final_objective_function() -> float:
    """
    :return: combination of income and time
    """
    return income_objective_function() / (time_objective_function() + 1)


res = final_objective_function()  # the more the better!

# number that says up to which iteration first type of crossover is more likely to happen
crossover_barrier = 2


def crossover(parent_1, parent_2, current_iter, ptr_list):
    if current_iter <= crossover_barrier:  # number of iter
        genome_length = len(parent_1) // 2

        child_1 = [parent_1[:genome_length]]
        child_1.extend([parent_2[genome_length:]])
        child_2 = [parent_2[:genome_length]]
        child_2.extend([parent_1[genome_length:]])
        return child_1, child_2

    elif current_iter > crossover_barrier:
        genome_length = ptr_list[random.randint(0, len(ptr_list))]

        child_1 = [parent_1[:genome_length]]
        child_1.extend([parent_2[genome_length:]])
        child_2 = [parent_2[:genome_length]]
        child_2.extend([parent_1[genome_length:]])
        return child_1, child_2

# TODO ile bitów neogwać?


def mutation(parent):
    number_of_cells = len(parent)//15+1
    child = parent
    for i in range(number_of_cells):
        cancer = random.randint(0, len(parent))
        if child[cancer] == 1:
            child[cancer] = 0
        else:
            child[cancer] = 1
    return child
