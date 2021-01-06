#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file contains the main algorithm.

from copy import deepcopy

import numpy as np

import uno

print('Preparing data ...')
number_of_iterations = 4000
client_list = uno.create_brave_new_world('Examples/Tutoring500nonlinear.xlsx')
population_size = min(2 * len(client_list), 50)
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

print('Calculating ...\n ETC. ', 0.024 * number_of_iterations, '[s]\n')
probability = 0.8
for curr_iter in range(number_of_iterations):
    rand = np.random.random_sample()
    if rand > probability/(curr_iter+1):  # chance for mutation increases over time
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

ones_ptr = []
for i in range(len(current_population[evaluations.index(max(evaluations))])):
    if current_population[evaluations.index(max(evaluations))][i] == 1:
        ones_ptr.append(i)

income = 0
for elem in ones_ptr:
    income += client_list[elem].price
print('Total number of clients:', np.sum(current_population[evaluations.index(max(evaluations))], axis=0))
print("Customer numbers: ", ones_ptr)
print('Objective function value: ', max(evaluations))
print("Your total income for this week: ", income)
