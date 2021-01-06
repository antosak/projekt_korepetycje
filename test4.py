#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is being used for collecting data from the main algorithm.
# Basically iterates over algorithm "repeat ="(1000) for 4000 generations and different population sizes.
# Prints it's state every 10 iterations and saves data to a file after all 1000 iterations.
# WARNING! Running whole program on just one thread can take approximately 210 hours.

from copy import deepcopy
from time import time

import numpy as np
import pandas as pd

import uno

begin = time()
barriers = [[400, 800], [800, 1600], [1200, 2400]]

for k in barriers:
    number_of_iterations = 4000
    client_list = uno.create_brave_new_world('Examples/Tutoring500nonlinear.xlsx')
    population_size = 50
    crossover_barrier = number_of_iterations // 10
    day_ptr_list = [0]
    for i in range(len(client_list)):
        if client_list[i].day == 'tuesday' and client_list[i - 1].day == 'monday':
            day_ptr_list.append(i)
        elif client_list[i].day == 'wednesday' and client_list[i - 1].day == 'tuesday':
            day_ptr_list.append(i)
        elif client_list[i].day == 'thursday' and client_list[i - 1].day == 'wednesday':
            day_ptr_list.append(i)
        elif client_list[i].day == 'friday' and client_list[i - 1].day == 'thursday':
            day_ptr_list.append(i)
        elif client_list[i].day == 'saturday' and client_list[i - 1].day == 'friday':
            day_ptr_list.append(i)
        elif client_list[i].day == 'sunday' and client_list[i - 1].day == 'saturday':
            day_ptr_list.append(i)

    repeat = 12
    min_final_average = []
    max_final_average = []
    avg_final_average = []
    min_repeats = []
    max_repeats = []
    avg_repeats = []
    initial_minimum_over_time = []

    for g in range(repeat):
        min_per_iter = []
        max_per_iter = []
        avg_per_iter = []
        start = time()
        current_population = []
        kappa_population = []
        evaluations = []
        max_ones = min(18, len(client_list))
        while len(current_population) < population_size:
            population_member = uno.definitely_not_a_random_member(max_ones, client_list)
            kappa = uno.kappa_maker(client_list, population_member)
            if uno.legal_child(client_list, population_member, kappa):
                current_population.append(population_member)
                kappa_population.append(kappa)
                evaluations.append(uno.final_objective_function(population_member, kappa, client_list))
        ######################
        min_per_iter.append(min(evaluations))
        max_per_iter.append(max(evaluations))
        avg_per_iter.append(sum(evaluations) / len(evaluations))
        ######################
        iter_barrier1, iter_barrier2 = k[0], k[1]

        for curr_iter in range(number_of_iterations):
            rand = np.random.random_sample()
            if curr_iter <= iter_barrier1:
                probability = 0.8
            elif curr_iter <= iter_barrier2:
                probability = 0.4
            else:
                probability = 0

            if rand > probability:  # chance for mutation increases over time
                parent = deepcopy(current_population[np.random.randint(low=0, high=len(current_population))])
                child_1 = uno.mutation(parent, max_ones)
                child_2 = None
                c1_kappa = uno.kappa_maker(client_list, child_1)
                c2_kappa = None
                while not uno.legal_child(client_list, child_1, c1_kappa):
                    parent = deepcopy(current_population[np.random.randint(low=0, high=len(current_population))])
                    child_1 = uno.mutation(parent, max_ones)
                    c1_kappa = uno.kappa_maker(client_list, child_1)
            else:
                parent_1 = deepcopy(current_population[np.random.randint(low=0, high=len(current_population))])
                parent_2 = deepcopy(current_population[np.random.randint(low=0, high=len(current_population))])
                child_1, child_2 = uno.crossover(parent_1, parent_2, curr_iter, day_ptr_list, crossover_barrier,
                                                 max_ones)
                c1_kappa = uno.kappa_maker(client_list, child_1)
                c2_kappa = uno.kappa_maker(client_list, child_2)
                while not (uno.legal_child(client_list, child_1, c1_kappa)
                           and uno.legal_child(client_list, child_2, c2_kappa)):
                    parent_1 = deepcopy(current_population[np.random.randint(low=0, high=len(current_population))])
                    parent_2 = deepcopy(current_population[np.random.randint(low=0, high=len(current_population))])
                    child_1, child_2 = uno.crossover(parent_1, parent_2, curr_iter, day_ptr_list, crossover_barrier,
                                                     max_ones)
                    c1_kappa = uno.kappa_maker(client_list, child_1)
                    c2_kappa = uno.kappa_maker(client_list, child_2)

            c1_eval = uno.final_objective_function(child_1, c1_kappa, client_list)
            minimum_value, minimum_ptr = min(evaluations), evaluations.index(min(evaluations))
            if c1_eval > minimum_value:
                current_population[minimum_ptr] = child_1
                kappa_population[minimum_ptr] = c1_kappa
                evaluations[minimum_ptr] = c1_eval
            if child_2 is not None:
                c2_eval = uno.final_objective_function(child_2, c2_kappa, client_list)
                minimum = (min(evaluations), evaluations.index(min(evaluations)))
                if c2_eval > minimum_value:
                    current_population[minimum_ptr] = child_2
                    kappa_population[minimum_ptr] = c2_kappa
                    evaluations[minimum_ptr] = c2_eval
            ######################
            min_per_iter.append(min(evaluations))
            max_per_iter.append(max(evaluations))
            avg_per_iter.append(sum(evaluations) / len(evaluations))
            ######################
        ######################
        min_repeats.append(min_per_iter)
        max_repeats.append(max_per_iter)
        avg_repeats.append(avg_per_iter)
        ######################

        if g % 0.01 == 0:
            print(repeat)

    min_temp = []
    max_temp = []
    avg_temp = []
    for i in range(number_of_iterations+1):
        for elem in min_repeats:
            min_temp.append(elem[i])
        for elem in max_repeats:
            max_temp.append(elem[i])
        for elem in avg_repeats:
            avg_temp.append(elem[i])
        min_final_average.append(sum(min_temp) / len(min_temp))
        max_final_average.append(sum(max_temp) / len(max_temp))
        avg_final_average.append(sum(avg_temp) / len(avg_temp))
        min_temp = []
        max_temp = []
        avg_temp = []

    total_time = time() - begin
    print(total_time)
    print("Finished")

    DATA = {
        'Minimum Fun': min_final_average,
        'Maximum Fun': max_final_average,
        'Average Fun': avg_final_average,
    }
    data_frame = pd.DataFrame(DATA, columns=['Minimum Fun', 'Maximum Fun', 'Average Fun'])

    if k == [400, 800]:
        data_frame.to_excel('Dat/RawData_prob1020.xlsx', header=True)
    elif k == [800, 1600]:
        data_frame.to_excel('Dat/RawData_prob2040.xlsx', header=True)
    elif k == [1200, 2400]:
        data_frame.to_excel('Dat/RawData_prob3060.xlsx', header=True)
