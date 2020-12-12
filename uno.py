#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt
import pandas as pd
from copy import deepcopy
# constants
default_path = 'Tutoring.xlsx'
fuel_consumption = 8  # l/100km``
average_speed = 50  # km/h
fuel_cost = 4.20  # PlN/l
fuel_coeff = (fuel_consumption / 100) * fuel_cost  # useful thing
our_home = [5, 5]
waiting_threshold = 0.5


def read_data(path: str = default_path):
    data = pd.read_excel(path, index_col=0, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
    return data


def create_brave_new_world(source: str = default_path) -> list:
    """
    Returns list of instances of class Client in chronological order in a week.
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


class Client(object):
    """
    Somewhat surprisingly class Client represents a single date with a fool, not a fool itself.
    """
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


def legal_child(client_list, child, home_returns_vector) -> bool:
    """
    Checks whether a child (solution), that algorithm returned, is legal (within several severe limitations).
    :param client_list: list that function "create_brave_new_world" returns
    :param child: solution that algorithm (crossover or mutation) provides
    :param home_returns_vector: list that function "kappa_maker" provides
    :return: decision (bool) if new solution is legal
    """
    income = 0
    for i in range(0, len(child)):
        if child[i] == 1:
            income += client_list[i].price
    if income > 350:
        return False
    id_list = []
    for i in range(0, len(child)):
        if child[i] == 1:
            if client_list[i].name in id_list:
                return False
            else:
                id_list.append(client_list[i].name)
    days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    days_value_list = [0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(child)):
        if child[i] == 1:
            if i + 1 != len(child):
                if child[i + 1] == 1:
                    if home_returns_vector[i] == 0:
                        client_time = 0
                        client_time += client_list[i].teaching_time
                        client_time += (sqrt(
                            ((client_list[i + 1].coordinates[0] - client_list[i].coordinates[0]) ** 2) +
                            ((client_list[i + 1].coordinates[1] - client_list[i].coordinates[1]) ** 2))) / average_speed
                        if client_list[i + 1].hour < client_list[i].hour + client_time:
                            return False
                    else:
                        if client_list[i].day == client_list[i + 1].day:
                            client_time = 0
                            client_time += client_list[i].teaching_time
                            client_time += (sqrt(((client_list[i].coordinates[0] - our_home[0]) ** 2) +
                                                 ((client_list[i].coordinates[1] - our_home[1]) ** 2))) / average_speed
                            client_time += (sqrt(((client_list[i + 1].coordinates[0] - our_home[0]) ** 2) +
                                                 ((client_list[i + 1].coordinates[1] - our_home[
                                                     1]) ** 2))) / average_speed
                            if client_list[i + 1].hour < client_list[i].hour + client_time:
                                return False
                            j = days_list.index(client_list[i].day)
                            days_value_list[j] += client_list[i + 1].hour - (client_list[i].hour + client_time)
    last_coordinates = our_home
    total_time = 0
    for i in range(0, len(child)):
        if child[i] == 1:
            j = days_list.index(client_list[i].day)
            days_value_list[j] += client_list[i].teaching_time
            days_value_list[j] += (sqrt(((client_list[i].coordinates[0] - last_coordinates[0]) ** 2) +
                                        ((client_list[i].coordinates[1] - last_coordinates[1]) ** 2))) / average_speed
            last_coordinates = client_list[i].coordinates
            if home_returns_vector[i] == 1:
                last_coordinates = our_home
                days_value_list[j] += (sqrt(((client_list[i].coordinates[0] - last_coordinates[0]) ** 2) +
                                            ((client_list[i].coordinates[1] - last_coordinates[
                                                1]) ** 2))) / average_speed
    for days in days_value_list:
        if days > 4:
            return False
        total_time += days
    for i in range(0, len(child)):
        if child[i] == 1:
            total_time += client_list[i].prep_time
    if total_time > 28:
        return False
    return True


def kappa_maker(client_list, child):
    """
    Based on the solution says when we go back home
    :param client_list: list that function "create_brave_new_world" returns
    :param child: solution that algorithm (crossover or mutation) provides
    :return: binary vector, that says when we go back home
    """
    kappa = []
    for i in range(0, len(child)):
        if child[i] == 0:
            kappa.append(0)
        else:
            if i + 1 != len(child):
                if child[i + 1] == 1:
                    if client_list[i].day == client_list[i + 1].day:
                        client_time = 0
                        client_time += client_list[i].teaching_time
                        client_time += (sqrt(
                            ((client_list[i + 1].coordinates[0] - client_list[i].coordinates[0]) ** 2) +
                            ((client_list[i + 1].coordinates[1] - client_list[i].coordinates[1]) ** 2))) / average_speed
                        client_time = client_list[i + 1].hour - (client_list[i].hour + client_time)
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


def income_objective_function(solution: list, kappa: list, world: list):
    """
    :param solution: something that crossover or mutation spitted out
    :param kappa: information from "kappa maker" - when we go back home
    :param world: population
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


def time_objective_function(solution: list, kappa: list, world: list):
    """
    :param solution: something that crossover or mutation spitted out
    :param kappa: information from "kappa maker" - when we go back home
    :param world: population
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
    return result if result > 0.5 else 1000


def final_objective_function(solution, kappa, world) -> float:
    """
    :return: combination of income and time
    """
    return income_objective_function(solution, kappa, world) / (time_objective_function(solution, kappa, world))


def half_legality_test(child, max_ones):
    """
    Function prevents earning more than 350/week and simplifies calculations for large populations
    :param child: child
    :param max_ones: maximum number of ones (depends on input data)
    :return:
    """
    ones_ptr = []
    for i in range(len(child)):
        if child[i] == 1:
            ones_ptr.append(i)
    while np.sum(child) > max_ones:
        index = np.random.randint(low=0, high=len(ones_ptr))
        child[ones_ptr[index]] = (child[ones_ptr[index]] + 1) % 2
    return child


def crossover(par_1, par_2, current_iter, ptr_list, crossover_barrier, max_ones):
    """
    :param par_1: Parent No.1
    :param par_2: Parent No.2
    :param current_iter: Current iteration number
    :param ptr_list: List of pointers to week days
    :param crossover_barrier: number that says up to which iteration first type of crossover is more likely to happen
    :param max_ones: maximum number of ones (depends on input data)
    :return: Child No.1, Child No.2
    """
    parent_1 = deepcopy(par_1)
    parent_2 = deepcopy(par_2)

    if current_iter <= crossover_barrier:  # number of iter
        genome_length = len(parent_1) // 2
        child_1 = [parent_1[:genome_length]]
        child_1.extend([parent_2[genome_length:]])
        child_2 = [parent_2[:genome_length]]
        child_2.extend([parent_1[genome_length:]])
        child_1 = child_1[0] + child_1[1]
        child_2 = child_2[0] + child_2[1]
        child_1 = half_legality_test(child_1, max_ones)
        child_2 = half_legality_test(child_2, max_ones)
        return child_1, child_2

    elif current_iter > crossover_barrier:
        genome_length = ptr_list[np.random.randint(low=0, high=len(ptr_list))]

        child_1 = [parent_1[:genome_length]]
        child_1.extend([parent_2[genome_length:]])
        child_2 = [parent_2[:genome_length]]
        child_2.extend([parent_1[genome_length:]])
        child_1 = child_1[0] + child_1[1]
        child_2 = child_2[0] + child_2[1]
        child_1 = half_legality_test(child_1, max_ones)
        child_2 = half_legality_test(child_2, max_ones)
        return child_1, child_2


def mutation(parent, max_ones):
    """
    :param parent: Parent
    :param max_ones: maximum number of ones (depends on input data)
    :return: Child
    """
    number_of_cancer_cells = np.random.randint(low=1, high=3)
    child = deepcopy(parent)
    ones_ptr = []
    for i in range(len(child)):
        if child[i] == 1:
            ones_ptr.append(i)
    if np.random.randint(2, size=1) == 1:  # 50/50
        for i in range(number_of_cancer_cells):
            index = np.random.randint(low=0, high=len(child))
            child[index] = (child[index] + 1) % 2
            child = half_legality_test(child, max_ones)
    else:
        for i in range(number_of_cancer_cells):
            if len(ones_ptr) != 0:
                index = np.random.randint(low=0, high=len(ones_ptr))
                child[ones_ptr[index]] = (child[ones_ptr[index]] + 1) % 2
    return child


def definitly_not_a_random_member(max_ones, client_list):
    """
    Generates a random member-vector that will more likely pass legality test because we can not earn more than 350/week
    :param max_ones: maximum number of ones
    :param client_list: population
    :return:
    """
    population_member = np.zeros(len(client_list), dtype=int)
    number_of_ones = np.random.randint(low=1, high=max_ones)
    population_member[:number_of_ones] = 1
    np.random.shuffle(population_member)
    return population_member.tolist()
