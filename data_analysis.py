#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Width of histogram bars (number from  0 to 1)
szerokosc_paskow = 1


# Histogram, three objective functions in terms of number of iterations
def first_test():
    df500 = pd.read_excel("Dat/RawData_iter_500.xlsx", index_col=0)
    df1000 = pd.read_excel("Dat/RawData_iter_1000.xlsx", index_col=0)
    df2000 = pd.read_excel("Dat/RawData_iter_2000.xlsx", index_col=0)
    df4000 = pd.read_excel("Dat/RawData_iter_4000.xlsx", index_col=0)
    df6000 = pd.read_excel("Dat/RawData_iter_6000.xlsx", index_col=0)
    df8000 = pd.read_excel("Dat/RawData_iter_8000.xlsx", index_col=0)
    df10000 = pd.read_excel("Dat/RawData_iter_10000.xlsx", index_col=0)

    fig1, axs = plt.subplots(7, 3, figsize=(8.25, 11.75), sharey="row", sharex="col")
    fig1.suptitle("Porównanie składowych i ostatecznej funkcji celu (1000 powtórzeń)", fontsize=16)
    fig1.subplots_adjust(top=0.95, left=0.1)

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
    axs[6, 0].set_xlabel("Zysk [PLN]", fontsize=12)

    axs[0, 1].hist(df500['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[1, 1].hist(df1000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[2, 1].hist(df2000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[3, 1].hist(df4000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[4, 1].hist(df6000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[5, 1].hist(df8000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 1].hist(df10000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 1].set_xlabel("Czas [h]", fontsize=12)

    axs[0, 2].hist(df500['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[1, 2].hist(df1000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[2, 2].hist(df2000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[3, 2].hist(df4000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[4, 2].hist(df6000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[5, 2].hist(df8000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 2].hist(df10000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 2].set_xlabel("Funkcja celu [PLN/h]", fontsize=12)

    plt.savefig("Plots & Charts/objective functions comparison.png")
    plt.show()
    return fig1


# Minimal, average, maximum solution (out of total population size 50) throughout iterations
def second_test():
    data4000 = pd.read_excel("Dat/RawData_oneiter_4000.xlsx", index_col=0)
    data10000 = pd.read_excel("Dat/RawData_oneiter_10000.xlsx", index_col=0)
    fig, axs = plt.subplots(1, 2, figsize=(10, 6), sharey='row')
    fig.suptitle("Zachowanie się granicznych i średniego rozwiązania", fontsize=16)

    axs[0].plot(data4000["Minimum Fun"], color="red", label="Minimum")
    axs[0].plot(data4000["Average Fun"], color="blue", label="Średnia")
    axs[0].plot(data4000["Maximum Fun"], color='green', label="Maksimum")
    axs[0].set_ylabel("Funkcja celu [PLN/h]", fontsize=12)
    axs[0].set_xlabel("Iteracja", fontsize=12)
    axs[1].plot(data10000["Minimum Fun"], color="red", label="Minimum")
    axs[1].plot(data10000["Average Fun"], color="blue", label="Średnia")
    axs[1].plot(data10000["Maximum Fun"], color='green', label="Maksimum")
    axs[1].set_xlabel("Iteracja", fontsize=12)
    plt.legend(fontsize=16)
    plt.savefig("Plots & Charts/max average min.png")
    plt.show()
    return fig


# Histogram, three objective functions in terms of population size (25, 50, 75, 100)
def third_test():
    df25 = pd.read_excel("Dat/RawData_popsize25.xlsx", index_col=0)
    df50 = pd.read_excel("Dat/RawData_popsize50.xlsx", index_col=0)
    df75 = pd.read_excel("Dat/RawData_popsize75.xlsx", index_col=0)
    df100 = pd.read_excel("Dat/RawData_popsize100.xlsx", index_col=0)

    fig1, axs = plt.subplots(4, 3, figsize=(8.25, 6.75), sharey="row", sharex="col")
    fig1.suptitle("Porównanie składowych i ostatecznej funkcji celu (1000 powtórzeń)", fontsize=16)
    fig1.subplots_adjust(top=0.95, left=0.1)

    axs[0, 0].hist(df25['Maximum income'], bins=20, rwidth=szerokosc_paskow)
    axs[0, 0].set_ylabel("25")
    axs[1, 0].hist(df50['Maximum income'], bins=20, rwidth=szerokosc_paskow)
    axs[1, 0].set_ylabel("50")
    axs[2, 0].hist(df75['Maximum income'], bins=20, rwidth=szerokosc_paskow)
    axs[2, 0].set_ylabel("75")
    axs[3, 0].hist(df100['Maximum income'], bins=20, rwidth=szerokosc_paskow)
    axs[3, 0].set_ylabel("100")
    axs[3, 0].set_xlabel("Zysk [PLN]", fontsize=12)

    axs[0, 1].hist(df25['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[1, 1].hist(df50['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[2, 1].hist(df75['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[3, 1].hist(df100['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 1].set_xlabel("Czas [h]", fontsize=12)

    axs[0, 2].hist(df25['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[1, 2].hist(df50['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[2, 2].hist(df75['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[3, 2].hist(df100['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 2].set_xlabel("Funkcja celu [PLN/h]", fontsize=12)

    plt.savefig("Plots & Charts/pop_size and objective functions.png")
    plt.show()

    return fig1


# DO NOT RUN until data arrives
# a = third_test()

def controversial_test():
    df4000 = pd.read_excel("Dat/RawData_iter_4000.xlsx", index_col=0)

    fig = plt.figure(figsize=(9.6, 7.2))
    ax = fig.add_subplot(111)
    ax.set_title("Zależność końcowego najlepszego rozwiązania od początkowego najlepszego rozwiązania", fontweight='bold')
    ax.scatter(df4000["Initial maximum"], df4000["Final maximum"], s=5)
    plt.grid()
    z = np.polyfit(df4000["Initial maximum"], df4000["Final maximum"], 1)
    p = np.poly1d(z)
    ax.plot(df4000["Initial maximum"], p(df4000["Initial maximum"]), "r")
    txt = "Linia trendu: y=%.2fx+%.2f" % (z[0], z[1])
    ax.annotate(txt, xy=(29, 39.3), xytext=(27, 44.5), fontsize=14,
                arrowprops=dict(facecolor='black', shrink=0.05))
    ax.set_xlabel("Początkowe maksimum [PLN/h]")
    ax.set_ylabel("Końcowy wynik [PLN/h]")
    plt.savefig("Plots & Charts/yahoooy.png")
    plt.show()
    return fig


# a = controversial_test()
