#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is being used for collecting data from the main algorithm.
# Prints main parameters of the result for every generation and saves that in an Excel file.

from copy import deepcopy

import numpy as np
import pandas as pd

import uno

number_of_iterations = 4000
client_list = uno.create_brave_new_world('Examples/Tutoring500nonlinear.xlsx')
population_size = 100
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

minimum_over_time = []
maximum_over_time = []
avg_over_time = []
minimum_income_over_time = []
maximum_income_over_time = []
avg_income_over_time = []
minimum_time = []
maximum_time = []
avg_time = []

current_population = []
kappa_population = []
evaluations = []
test_counter = 1

max_ones = min(18, len(client_list))
while len(current_population) < population_size:
    population_member = uno.definitely_not_a_random_member(max_ones, client_list)
    kappa = uno.kappa_maker(client_list, population_member)
    if uno.legal_child(client_list, population_member, kappa):
        current_population.append(population_member)
        kappa_population.append(kappa)
        evaluations.append(uno.final_objective_function(population_member, kappa, client_list))

    test_counter += 1

print(test_counter, '\n')

print('initial score: ', max(evaluations))
print('initial min: ', min(evaluations), '\n')

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
        child_1, child_2 = uno.crossover(parent_1, parent_2, curr_iter, day_ptr_list, crossover_barrier, max_ones)
        c1_kappa = uno.kappa_maker(client_list, child_1)
        c2_kappa = uno.kappa_maker(client_list, child_2)
        while not (uno.legal_child(client_list, child_1, c1_kappa)
                   and uno.legal_child(client_list, child_2, c2_kappa)):
            parent_1 = deepcopy(current_population[np.random.randint(low=0, high=len(current_population))])
            parent_2 = deepcopy(current_population[np.random.randint(low=0, high=len(current_population))])
            child_1, child_2 = uno.crossover(parent_1, parent_2, curr_iter, day_ptr_list, crossover_barrier, max_ones)
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

    income_table = []
    minimum_income = 0
    maximum_income = 0
    minimum_value, minimum_ptr = min(evaluations), evaluations.index(min(evaluations))
    maximum_value, maximum_ptr = max(evaluations), evaluations.index(max(evaluations))
    for member in current_population:
        income = 0
        for i in range(0, len(member)):
            if member[i] == 1:
                income += client_list[i].price
        income_table.append(income)

    for i in range(0, len(current_population[minimum_ptr])):
        if current_population[minimum_ptr][i] == 1:
            minimum_income += client_list[i].price

    for i in range(0, len(current_population[maximum_ptr])):
        if current_population[maximum_ptr][i] == 1:
            maximum_income += client_list[i].price

    minimum_over_time.append(minimum_value)
    maximum_over_time.append(maximum_value)
    avg_over_time.append(sum(evaluations) / len(evaluations))
    minimum_income_over_time.append(minimum_income)
    maximum_income_over_time.append(maximum_income)
    avg_income_over_time.append(sum(income_table) / len(current_population))
    minimum_time.append(minimum_income / minimum_value)
    maximum_time.append(maximum_income / maximum_value)
    avg_time.append((sum(income_table) / len(current_population)) / (sum(evaluations) / len(evaluations)))

ones_ptr = []
for i in range(len(current_population[evaluations.index(max(evaluations))])):
    if current_population[evaluations.index(max(evaluations))][i] == 1:
        ones_ptr.append(i)

income = 0
for elem in ones_ptr:
    income += client_list[elem].price
print('Total number of clients:', np.sum(current_population[evaluations.index(max(evaluations))], axis=0))
print("Your clients' numbers: ", ones_ptr)
print('Objective function value: ', max(evaluations))
print("Your total income for this week: ", income)

DATA = {
    'Minimum Fun': minimum_over_time,
    'Maximum Fun': maximum_over_time,
    'Average Fun': avg_over_time,
    'Minimum income': minimum_income_over_time,
    'Maximum income': maximum_income_over_time,
    'Average income': avg_income_over_time,
    'Minimum time': minimum_time,
    'Maximum time': maximum_time,
    'Average time': avg_time,

}
data_frame = pd.DataFrame(DATA, columns=['Minimum Fun', 'Maximum Fun', 'Average Fun', 'Minimum income',
                                         'Maximum income', 'Average income', 'Minimum time', 'Maximum time',
                                         'Average time'])

if population_size == 25:
    data_frame.to_excel('Dat/RawData_pop25.xlsx', header=True)
elif population_size == 50:
    data_frame.to_excel('Dat/RawData_pop50.xlsx', header=True)
elif population_size == 75:
    data_frame.to_excel('Dat/RawData_pop75.xlsx', header=True)
elif population_size == 100:
    data_frame.to_excel('Dat/RawData_pop_100.xlsx', header=True)
