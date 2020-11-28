#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import uno

client_list = uno.create_brave_new_world()

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


