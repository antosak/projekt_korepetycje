#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

df500 = pd.read_excel("Dat/RawData_iter_500.xlsx", index_col=0)
df1000 = pd.read_excel("Dat/RawData_iter_1000.xlsx", index_col=0)
df2000 = pd.read_excel("Dat/RawData_iter_2000.xlsx", index_col=0)
df4000 = pd.read_excel("Dat/RawData_iter_4000.xlsx", index_col=0)
df6000 = pd.read_excel("Dat/RawData_iter_6000.xlsx", index_col=0)
df8000 = pd.read_excel("Dat/RawData_iter_8000.xlsx", index_col=0)
df10000 = pd.read_excel("Dat/RawData_iter_10000.xlsx", index_col=0)

fig_size = (12.8, 9.6)

fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharey="row", sharex="row")
fig.suptitle("Całkowity zysk przy różnych liczbach iteracji algorytmu ", fontsize=16)
fig.subplots_adjust(top=0.90, left=0.1)
axs[0, 0].hist(df500['Maximum income'], bins=20, rwidth=0.9)
axs[0, 0].set_title("500")
axs[0,0].set_ylabel("")
axs[0, 1].hist(df1000['Maximum income'], bins=20, rwidth=0.9)
axs[0, 1].set_title("1000")
axs[1, 0].hist(df4000['Maximum income'], bins=20, rwidth=0.9)
axs[1, 0].set_title("4000")
axs[1, 0].set_xlabel("Zysk")
axs[1, 1].hist(df10000['Maximum income'], bins=20, rwidth=0.9)
axs[1, 1].set_title("10000")
axs[1, 1].set_xlabel("Zysk")
axs[-1, 0].set_xlabel('.', color=(0, 0, 0, 0))
axs[-1, 0].set_ylabel('.', color=(0, 0, 0, 0))
# Make common axis labels
fig.text(0.5, 0.04, 'Zysk', va='center', ha='center')
fig.text(0.04, 0.5, 'Wystąpienia zysku na 1000 powtórzeń', va='center', ha='center', rotation='vertical')
"""
fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axis
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.ylabel("Wystąpienia zysku na 1000 powtórzeń")
plt.subplots_adjust(left=0.08)
"""
plt.savefig("Plots & Charts/maximum income comparison.png")
plt.show()
