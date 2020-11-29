#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import uno
import numpy as np
number_of_iterations = 5
client_list = uno.create_brave_new_world('Tutoring3.xlsx')
population_size = 3*len(client_list)

day_ptr_list = [0]
for i in range(len(client_list)):
    if client_list[i].day == 'tuesday' and client_list[i-1].day == 'monday':
        day_ptr_list.append(i)
    elif client_list[i].day == 'wednesday' and client_list[i-1].day == 'tuesday':
        day_ptr_list.append(i)
    elif client_list[i].day == 'thursday' and client_list[i-1].day == 'wednesday':
        day_ptr_list.append(i)
    elif client_list[i].day == 'friday' and client_list[i-1].day == 'thursday':
        day_ptr_list.append(i)
    elif client_list[i].day == 'saturday' and client_list[i-1].day == 'friday':
        day_ptr_list.append(i)
    elif client_list[i].day == 'sunday' and client_list[i-1].day == 'saturday':
        day_ptr_list.append(i)

current_population = []
kappa_population = []
test_counter = 0
while len(current_population) < population_size:
    population_member = np.random.randint(2, size=len(client_list))
    kappa = uno.kappa_maker(client_list, population_member)
    if uno.legal_child(client_list, population_member, kappa):
        current_population.append(population_member)
        kappa_population.append(kappa)
    test_counter += 1

print(test_counter)

for curr_iter in range(number_of_iterations):
    rand = np.random.random_sample()
    genetic_operation = ''
    if rand > 0.8:
        parent = np.random.randint(low=0, high=len(current_population))
    else:
        parent_1 = np.random.randint(low=0, high=len(current_population))
        parent_2 = np.random.randint(low=0, high=len(current_population))
