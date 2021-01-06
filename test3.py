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

popsize = [25, 50, 75, 100]

begin = time()
for k in popsize:
    number_of_iterations = 4000
    client_list = uno.create_brave_new_world('Examples/Tutoring500nonlinear.xlsx')
    population_size = k
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

    repeat = 1
    initial_minimum_over_time = []
    initial_maximum_over_time = []
    initial_avg_over_time = []
    final_minimum_over_time = []
    final_maximum_over_time = []
    final_avg_over_time = []
    maximum_income_over_time = []
    minimum_income_over_time = []
    avg_income_over_time = []
    maximum_time = []
    avg_time = []

    calculating_time_per_iteration = []

    for g in range(repeat):
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
        initial_minimum_over_time.append(min(evaluations))
        initial_maximum_over_time.append(max(evaluations))
        initial_avg_over_time.append(sum(evaluations) / len(evaluations))
        ######################
        probability = 0.8
        for curr_iter in range(number_of_iterations):
            rand = np.random.random_sample()
            if rand > probability / (curr_iter + 1):  # chance for mutation increases over time
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
        final_minimum_over_time.append(min(evaluations))
        final_maximum_over_time.append(max(evaluations))
        final_avg_over_time.append(sum(evaluations) / len(evaluations))
        ######################
        income_table = []
        for member in current_population:
            income = 0
            for i in range(0, len(member)):
                if member[i] == 1:
                    income += client_list[i].price
            income_table.append(income)
        minimum_income_over_time.append(min(income_table))
        maximum_income_over_time.append(max(income_table))
        avg_income_over_time.append(sum(income_table) / len(income_table))
        calculating_time_per_iteration.append(time() - start)
        maximum_time.append(max(income_table) / max(evaluations))
        avg_time.append((sum(income_table) / len(income_table)) / (sum(evaluations) / len(evaluations)))
        if g % 0.01 == 0:
            print(repeat)

    total_time = time() - begin
    print(total_time)
    print("Finished")

    DATA = {
        'Initial minimum': initial_minimum_over_time,
        'Initial maximum': initial_maximum_over_time,
        'Initial average': initial_avg_over_time,
        'Final minimum': final_minimum_over_time,
        'Final maximum': final_maximum_over_time,
        'Final average': final_avg_over_time,
        'Minimum income': minimum_income_over_time,
        'Maximum income': maximum_income_over_time,
        'Average income': avg_income_over_time,
        'Iteration time': calculating_time_per_iteration,
        'Suboptimal teaching time': maximum_time,
        'Average teaching time': avg_time
    }
    data_frame = pd.DataFrame(DATA, columns=['Initial minimum', 'Initial maximum', 'Initial average', 'Final minimum',
                                             'Final maximum', 'Final average', 'Minimum income', 'Maximum income',
                                             'Average income', 'Iteration time', 'Suboptimal teaching time',
                                             'Average teaching time'])

    if population_size == 25:
        data_frame.to_excel('Dat/RawData_popsize25.xlsx', header=True)
    elif population_size == 50:
        data_frame.to_excel('Dat/RawData_popsize50.xlsx', header=True)
    elif population_size == 75:
        data_frame.to_excel('Dat/RawData_popsize75.xlsx', header=True)
    elif population_size == 100:
        data_frame.to_excel('Dat/RawData_popsize100.xlsx', header=True)
