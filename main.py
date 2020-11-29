#!/usr/bin/python
# -*- coding: utf-8 -*-

import uno
import numpy as np

number_of_iterations = 1000
client_list = uno.create_brave_new_world('Tutoring4.xlsx')
population_size = min(2 * len(client_list), 50)
crossover_barrier = number_of_iterations // 10
data = uno.read_data('Tutoring4.xlsx')
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
test_counter = 0
max_ones = min(35, len(client_list))
while len(current_population) < population_size:
    population_member = np.random.randint(2, size=len(client_list))
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
    if rand > probability/(curr_iter+1):  # chance for mutation increases over time
        parent = current_population[np.random.randint(low=0, high=len(current_population))]
        child_1 = uno.mutation(parent)
        child_2 = None
        c1_kappa = uno.kappa_maker(client_list, child_1)
        c2_kappa = None
        while not uno.legal_child(client_list, child_1, c1_kappa):
            parent = current_population[np.random.randint(low=0, high=len(current_population))]
            child_1 = uno.mutation(parent)
            c1_kappa = uno.kappa_maker(client_list, child_1)
    else:
        parent_1 = current_population[np.random.randint(low=0, high=len(current_population))]
        parent_2 = current_population[np.random.randint(low=0, high=len(current_population))]
        child_1, child_2 = uno.crossover(parent_1, parent_2, curr_iter, day_ptr_list, crossover_barrier)
        c1_kappa = uno.kappa_maker(client_list, child_1)
        c2_kappa = uno.kappa_maker(client_list, child_2)
        while not uno.legal_child(client_list, child_1, c1_kappa) or not uno.legal_child(client_list, child_2, c2_kappa):
            parent_1 = current_population[np.random.randint(low=0, high=len(current_population))]
            parent_2 = current_population[np.random.randint(low=0, high=len(current_population))]
            child_1, child_2 = uno.crossover(parent_1, parent_2, curr_iter, day_ptr_list, crossover_barrier)
            c1_kappa = uno.kappa_maker(client_list, child_1)
            c2_kappa = uno.kappa_maker(client_list, child_2)

    c1_eval = uno.final_objective_function(child_1, c1_kappa, client_list)
    minimum = (min(evaluations), evaluations.index(min(evaluations)))
    if c1_eval > minimum[0]:
        current_population[minimum[1]] = child_1
        kappa_population[minimum[1]] = c1_kappa
        evaluations[minimum[1]] = c1_eval
    if child_2 is not None:
        c2_eval = uno.final_objective_function(child_2, c2_kappa, client_list)
        minimum = (min(evaluations), evaluations.index(min(evaluations)))
        if c2_eval > minimum[0]:
            current_population[minimum[1]] = child_2
            kappa_population[minimum[1]] = c2_kappa
            evaluations[minimum[1]] = c2_eval

print('final score: ', max(evaluations))
print('final min: ', min(evaluations))
