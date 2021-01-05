#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

df500 = pd.read_excel("Dat/RawData_iter_500.xlsx", index_col=0)
df1000 = pd.read_excel("Dat/RawData_iter_1000.xlsx", index_col=0)
df2000 = pd.read_excel("Dat/RawData_iter_2000.xlsx", index_col=0)
df4000 = pd.read_excel("Dat/RawData_iter_4000.xlsx", index_col=0)
df6000 = pd.read_excel("Dat/RawData_iter_6000.xlsx", index_col=0)
df8000 = pd.read_excel("Dat/RawData_iter_8000.xlsx", index_col=0)
df10000 = pd.read_excel("Dat/RawData_iter_10000.xlsx", index_col=0)


def better_first_chart():
    fig1, axs = plt.subplots(7, 3, figsize=(8.25, 11.75), sharey="row", sharex="col")
    fig1.suptitle("Porównanie składowych i ostatecznej funkcji celu", fontsize=16)
    fig1.subplots_adjust(top=0.95, left=0.1)
    szerokosc_paskow = 1
    axs[0, 0].hist(df500['Maximum income'], bins=20, rwidth=szerokosc_paskow)
    axs[0, 0].set_ylabel("500")
    axs[1, 0].hist(df1000['Maximum income'], bins=20, rwidth=szerokosc_paskow)
    axs[1, 0].set_ylabel("1000")
    axs[2, 0].hist(df2000['Maximum income'], bins=20, rwidth=szerokosc_paskow)
    axs[2, 0].set_ylabel("2000")
    axs[3, 0].hist(df4000['Maximum income'], bins=20, rwidth=szerokosc_paskow)
    axs[3, 0].set_ylabel("4000")
    axs[4, 0].hist(df6000['Maximum income'], bins=20, rwidth=szerokosc_paskow)
    axs[4, 0].set_ylabel("6000")
    axs[5, 0].hist(df8000['Maximum income'], bins=20, rwidth=szerokosc_paskow)
    axs[5, 0].set_ylabel("8000")
    axs[6, 0].hist(df10000['Maximum income'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 0].set_ylabel("10000")
    axs[6, 0].set_xlabel("Zysk")

    axs[0, 1].hist(df500['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[1, 1].hist(df1000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[2, 1].hist(df2000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[3, 1].hist(df4000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[4, 1].hist(df6000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[5, 1].hist(df8000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 1].hist(df10000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 1].set_xlabel("Czas")

    axs[0, 2].hist(df500['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[1, 2].hist(df1000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[2, 2].hist(df2000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[3, 2].hist(df4000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[4, 2].hist(df6000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[5, 2].hist(df8000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 2].hist(df10000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 2].set_xlabel("Funkcja celu")

    plt.savefig("Plots & Charts/objective functions comparison.png")
    plt.show()
    return fig1


a = better_first_chart()

"""
fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharey="row", sharex="row")
fig.suptitle("Całkowity zysk przy różnych liczbach iteracji algorytmu 500-4000", fontsize=16)
fig.subplots_adjust(top=0.90, left=0.1)
axs[0, 0].hist(df500['Maximum income'], bins=20, rwidth=0.9)
axs[0, 0].set_title("500")
axs[0, 0].set_ylabel("")
axs[0, 1].hist(df1000['Maximum income'], bins=20, rwidth=0.9)
axs[0, 1].set_title("1000")
axs[1, 0].hist(df2000['Maximum income'], bins=20, rwidth=0.9)
axs[1, 0].set_title("2000")
axs[1, 0].set_xlabel("Zysk")
axs[1, 1].hist(df4000['Maximum income'], bins=20, rwidth=0.9)
axs[1, 1].set_title("4000")
axs[1, 1].set_xlabel("Zysk")
axs[-1, 0].set_xlabel('.', color=(0, 0, 0, 0))
axs[-1, 0].set_ylabel('.', color=(0, 0, 0, 0))
# Make common axis labels
fig.text(0.5, 0.04, 'Zysk', va='center', ha='center')
fig.text(0.04, 0.5, 'Wystąpienia zysku na 1000 powtórzeń', va='center', ha='center', rotation='vertical')

plt.savefig("Plots & Charts/maximum income comparison.png")
plt.show()
"""

"""
fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axis
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.ylabel("Wystąpienia zysku na 1000 powtórzeń")
plt.subplots_adjust(left=0.08)
"""