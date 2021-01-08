#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Width of histogram bars (number from  0 to 1)
bars_width = 1


# Histogram, three objective functions in terms of number of iterations
def first_test():
    df500 = pd.read_excel("../Dat/RawData_iter_500.xlsx", index_col=0)
    df1000 = pd.read_excel("../Dat/RawData_iter_1000.xlsx", index_col=0)
    df2000 = pd.read_excel("../Dat/RawData_iter_2000.xlsx", index_col=0)
    df4000 = pd.read_excel("../Dat/RawData_iter_4000.xlsx", index_col=0)
    df6000 = pd.read_excel("../Dat/RawData_iter_6000.xlsx", index_col=0)
    df8000 = pd.read_excel("../Dat/RawData_iter_8000.xlsx", index_col=0)
    df10000 = pd.read_excel("../Dat/RawData_iter_10000.xlsx", index_col=0)

    fig1, axs = plt.subplots(7, 3, figsize=(8.25, 11.75), sharey="row", sharex="col")
    fig1.suptitle("Porównanie składowych i ostatecznej funkcji celu", fontsize=16)
    fig1.subplots_adjust(top=0.95, bottom=0.05)
    fig1.text(0.02, 0.5, 'Liczba iteracji', va='center', rotation='vertical', fontsize=14)

    axs[0, 0].hist(df500['Maximum income'], bins=20, rwidth=bars_width)
    axs[0, 0].set_ylabel("500")
    axs[1, 0].hist(df1000['Maximum income'], bins=20, rwidth=bars_width)
    axs[1, 0].set_ylabel("1000")
    axs[2, 0].hist(df2000['Maximum income'], bins=20, rwidth=bars_width)
    axs[2, 0].set_ylabel("2000")
    axs[3, 0].hist(df4000['Maximum income'], bins=20, rwidth=bars_width)
    axs[3, 0].set_ylabel("4000")
    axs[4, 0].hist(df6000['Maximum income'], bins=20, rwidth=bars_width)
    axs[4, 0].set_ylabel("6000")
    axs[5, 0].hist(df8000['Maximum income'], bins=20, rwidth=bars_width)
    axs[5, 0].set_ylabel("8000")
    axs[6, 0].hist(df10000['Maximum income'], bins=20, rwidth=bars_width)
    axs[6, 0].set_ylabel("10000")
    axs[6, 0].set_xlabel("Przychód [PLN]", fontsize=12)

    axs[0, 1].hist(df500['Suboptimal teaching time'], bins=20, rwidth=bars_width)
    axs[1, 1].hist(df1000['Suboptimal teaching time'], bins=20, rwidth=bars_width)
    axs[2, 1].hist(df2000['Suboptimal teaching time'], bins=20, rwidth=bars_width)
    axs[3, 1].hist(df4000['Suboptimal teaching time'], bins=20, rwidth=bars_width)
    axs[4, 1].hist(df6000['Suboptimal teaching time'], bins=20, rwidth=bars_width)
    axs[5, 1].hist(df8000['Suboptimal teaching time'], bins=20, rwidth=bars_width)
    axs[6, 1].hist(df10000['Suboptimal teaching time'], bins=20, rwidth=bars_width)
    axs[6, 1].set_xlabel("Czas [h]", fontsize=12)

    axs[0, 2].hist(df500['Final maximum'], bins=20, rwidth=bars_width)
    axs[1, 2].hist(df1000['Final maximum'], bins=20, rwidth=bars_width)
    axs[2, 2].hist(df2000['Final maximum'], bins=20, rwidth=bars_width)
    axs[3, 2].hist(df4000['Final maximum'], bins=20, rwidth=bars_width)
    axs[4, 2].hist(df6000['Final maximum'], bins=20, rwidth=bars_width)
    axs[5, 2].hist(df8000['Final maximum'], bins=20, rwidth=bars_width)
    axs[6, 2].hist(df10000['Final maximum'], bins=20, rwidth=bars_width)
    axs[6, 2].set_xlabel("Funkcja celu [PLN/h]", fontsize=12)

    plt.savefig("../Plots & Charts/objective functions comparison.png")
    plt.show()
    return fig1


# Minimal, average, maximum solution (out of total population size 50) throughout iterations (NOT INCLUDED)
def second_test():
    data4000 = pd.read_excel("../Dat/RawData_oneiter_4000.xlsx", index_col=0)
    data10000 = pd.read_excel("../Dat/RawData_oneiter_10000.xlsx", index_col=0)
    fig, axs = plt.subplots(2, 1, figsize=(8.25, 6), sharey='row')
    fig.suptitle("Zachowanie się granicznych i średniego rozwiązania", fontsize=16)
    fig.text(0.02, 0.5, 'Funkcja celu [PLN/h]', va='center', rotation='vertical', fontsize=14)

    axs[0].plot(data4000.iloc[10:]["Minimum Fun"], color="red", label="Minimum")
    axs[0].plot(data4000["Average Fun"], color="blue", label="Średnia")
    axs[0].plot(data4000["Maximum Fun"], color='green', label="Maksimum")
    axs[0].grid()
    axs[1].plot(data10000.iloc[13:]["Minimum Fun"], color="red", label="Minimum")
    axs[1].plot(data10000["Average Fun"], color="blue", label="Średnia")
    axs[1].plot(data10000["Maximum Fun"], color='green', label="Maksimum")
    axs[1].set_xlabel("Iteracja", fontsize=14)
    axs[1].grid()
    plt.legend(fontsize=16)
    plt.savefig("../Plots & Charts/max average min.png")
    plt.show()
    return fig


# Histogram, three objective functions in terms of population size (25, 50, 75, 100)
def third_test_hist():
    df25 = pd.read_excel("../Dat/RawData_popsize25.xlsx", index_col=0)
    df50 = pd.read_excel("../Dat/RawData_popsize50.xlsx", index_col=0)
    df75 = pd.read_excel("../Dat/RawData_popsize75.xlsx", index_col=0)
    df100 = pd.read_excel("../Dat/RawData_popsize100.xlsx", index_col=0)

    fig1, axs = plt.subplots(4, 3, figsize=(9.5, 6.75), sharey="row", sharex="col")
    fig1.suptitle("Porównanie funkcji celu dla różnych wielkości populacji", fontsize=16)
    fig1.subplots_adjust(top=0.93, left=0.1)
    fig1.text(0.01, 0.5, 'Wielkość populacji', va='center', rotation='vertical', fontsize=14)

    axs[0, 0].hist(df25['Maximum income'], bins=20, rwidth=bars_width)
    axs[0, 0].set_ylabel("25")
    axs[1, 0].hist(df50['Maximum income'], bins=20, rwidth=bars_width)
    axs[1, 0].set_ylabel("50")
    axs[2, 0].hist(df75['Maximum income'], bins=20, rwidth=bars_width)
    axs[2, 0].set_ylabel("75")
    axs[3, 0].hist(df100['Maximum income'], bins=20, rwidth=bars_width)
    axs[3, 0].set_ylabel("100")
    axs[3, 0].set_xlabel("Przychód [PLN]", fontsize=12)

    axs[0, 1].hist(df25['Suboptimal teaching time'], bins=20, rwidth=bars_width)
    axs[1, 1].hist(df50['Suboptimal teaching time'], bins=20, rwidth=bars_width)
    axs[2, 1].hist(df75['Suboptimal teaching time'], bins=20, rwidth=bars_width)
    axs[3, 1].hist(df100['Suboptimal teaching time'], bins=20, rwidth=bars_width)
    axs[3, 1].set_xlabel("Czas [h]", fontsize=12)

    axs[0, 2].hist(df25['Final maximum'], bins=20, rwidth=bars_width)
    axs[1, 2].hist(df50['Final maximum'], bins=20, rwidth=bars_width)
    axs[2, 2].hist(df75['Final maximum'], bins=20, rwidth=bars_width)
    axs[3, 2].hist(df100['Final maximum'], bins=20, rwidth=bars_width)
    axs[3, 2].set_xlabel("Funkcja celu [PLN/h]", fontsize=12)

    plt.savefig("../Plots & Charts/pop_size and objective functions.png")
    plt.show()

    return fig1


# Plot without first 500 iterations
def third_test_plot():
    data1020 = pd.read_excel("../Dat/RawData_popsize_2_25.xlsx", index_col=0)
    data2040 = pd.read_excel("../Dat/RawData_popsize_2_50.xlsx", index_col=0)
    data3060 = pd.read_excel("../Dat/RawData_popsize_2_75.xlsx", index_col=0)
    data4590 = pd.read_excel("../Dat/RawData_popsize_2_100.xlsx", index_col=0)

    fig, axs = plt.subplots(4, 1, figsize=(8.25, 12), sharex='col')
    fig.suptitle("Wynik algorytmu dla różnych rozmiarów populacji", fontsize=18)
    fig.text(0.04, 0.5, 'Rozmiar populacji', va='center', rotation='vertical', fontsize=14)
    fig.subplots_adjust(top=0.95, bottom=0.05)

    axs[0].plot(data1020.iloc[500:]["Minimum Fun"], color="red", label="Minimum")
    axs[0].plot(data1020.iloc[500:]["Average Fun"], color="blue", label="Średnia")
    axs[0].plot(data1020.iloc[500:]["Maximum Fun"], color='green', label="Maksimum")
    axs[0].set_ylabel("25")
    axs[0].set_ylim([21, 42])
    axs[0].grid()
    axs[1].plot(data2040.iloc[500:]["Minimum Fun"], color="red", label="Minimum")
    axs[1].plot(data2040.iloc[500:]["Average Fun"], color="blue", label="Średnia")
    axs[1].plot(data2040.iloc[500:]["Maximum Fun"], color='green', label="Maksimum")
    axs[1].set_ylabel("50")
    axs[1].set_ylim([21, 42])
    axs[1].grid()
    axs[2].plot(data3060.iloc[500:]["Minimum Fun"], color="red", label="Minimum")
    axs[2].plot(data3060.iloc[500:]["Average Fun"], color="blue", label="Średnia")
    axs[2].plot(data3060.iloc[500:]["Maximum Fun"], color='green', label="Maksimum")
    axs[2].set_ylabel("75")
    axs[2].set_ylim([21, 42])
    axs[2].grid()
    axs[3].plot(data4590.iloc[500:]["Minimum Fun"], color="red", label="Minimum")
    axs[3].plot(data4590.iloc[500:]["Average Fun"], color="blue", label="Średnia")
    axs[3].plot(data4590.iloc[500:]["Maximum Fun"], color='green', label="Maksimum")
    axs[3].set_ylabel("100")
    axs[3].grid()
    axs[3].set_ylim([21, 42])
    axs[3].set_xlabel("Iteracja", fontsize=14)
    plt.legend(fontsize=16)

    plt.savefig("../Plots & Charts/populacja wykres bez pierwszych 500.png")
    plt.show()

    return fig


# Plot with first 500
def third_test_plot_vel_2():
    data1020 = pd.read_excel("../Dat/RawData_popsize_2_25.xlsx", index_col=0)
    data2040 = pd.read_excel("../Dat/RawData_popsize_2_50.xlsx", index_col=0)
    data3060 = pd.read_excel("../Dat/RawData_popsize_2_75.xlsx", index_col=0)
    data4590 = pd.read_excel("../Dat/RawData_popsize_2_100.xlsx", index_col=0)

    fig, axs = plt.subplots(4, 1, figsize=(8.25, 12), sharex='col')
    fig.suptitle("Wynik algorytmu dla różnych rozmiarów populacji", fontsize=18)
    fig.text(0.04, 0.5, 'Rozmiar populacji', va='center', rotation='vertical', fontsize=14)
    fig.subplots_adjust(top=0.95, bottom=0.05)

    axs[0].plot(data1020["Minimum Fun"], color="red", label="Minimum")
    axs[0].plot(data1020["Average Fun"], color="blue", label="Średnia")
    axs[0].plot(data1020["Maximum Fun"], color='green', label="Maksimum")
    axs[0].set_ylabel("25")
    axs[0].set_ylim([0, 44])
    axs[0].grid()
    axs[1].plot(data2040["Minimum Fun"], color="red", label="Minimum")
    axs[1].plot(data2040["Average Fun"], color="blue", label="Średnia")
    axs[1].plot(data2040["Maximum Fun"], color='green', label="Maksimum")
    axs[1].set_ylabel("50")
    axs[1].set_ylim([0, 44])
    axs[1].grid()
    axs[2].plot(data3060["Minimum Fun"], color="red", label="Minimum")
    axs[2].plot(data3060["Average Fun"], color="blue", label="Średnia")
    axs[2].plot(data3060["Maximum Fun"], color='green', label="Maksimum")
    axs[2].set_ylabel("75")
    axs[2].set_ylim([0, 44])
    axs[2].grid()
    axs[3].plot(data4590["Minimum Fun"], color="red", label="Minimum")
    axs[3].plot(data4590["Average Fun"], color="blue", label="Średnia")
    axs[3].plot(data4590["Maximum Fun"], color='green', label="Maksimum")
    axs[3].set_ylabel("100")
    axs[3].grid()
    axs[3].set_ylim([0, 44])
    axs[3].set_xlabel("Iteracja", fontsize=14)
    plt.legend(fontsize=16)

    plt.savefig("../Plots & Charts/populacja wykres.png")
    plt.show()

    return fig


# Probability of crossover and mutation
def fourth_test():
    data1020 = pd.read_excel("../Dat/RawData_prob1020.xlsx", index_col=0)
    data2040 = pd.read_excel("../Dat/RawData_prob2040.xlsx", index_col=0)
    data3060 = pd.read_excel("../Dat/RawData_prob3060.xlsx", index_col=0)
    data4590 = pd.read_excel("../Dat/RawData_prob4590.xlsx", index_col=0)
    data00 = pd.read_excel("../Dat/RawData_prob00.xlsx", index_col=0)

    fig, axs = plt.subplots(5, 1, figsize=(8.25, 12), sharex='col')
    fig.suptitle("Wynik algorytmu dla różnych progów zmiany operatorów", fontsize=18)
    fig.text(0.02, 0.5, 'Progi zmiany operatora krzyżowania, mutacji', va='center', rotation='vertical', fontsize=14)
    fig.subplots_adjust(top=0.95, bottom=0.05)

    axs[0].plot(data1020.iloc[13:]["Minimum Fun"], color="red", label="Minimum")
    axs[0].plot(data1020["Average Fun"], color="blue", label="Średnia")
    axs[0].plot(data1020["Maximum Fun"], color='green', label="Maksimum")
    axs[0].set_ylabel("400, 800")
    axs[0].grid()
    axs[1].plot(data2040.iloc[13:]["Minimum Fun"], color="red", label="Minimum")
    axs[1].plot(data2040["Average Fun"], color="blue", label="Średnia")
    axs[1].plot(data2040["Maximum Fun"], color='green', label="Maksimum")
    axs[1].set_ylabel("800, 1600")
    axs[1].grid()
    axs[2].plot(data3060.iloc[13:]["Minimum Fun"], color="red", label="Minimum")
    axs[2].plot(data3060["Average Fun"], color="blue", label="Średnia")
    axs[2].plot(data3060["Maximum Fun"], color='green', label="Maksimum")
    axs[2].set_ylabel("1200, 2400")
    axs[2].grid()
    axs[3].plot(data4590.iloc[13:]["Minimum Fun"], color="red", label="Minimum")
    axs[3].plot(data4590["Average Fun"], color="blue", label="Średnia")
    axs[3].plot(data4590["Maximum Fun"], color='green', label="Maksimum")
    axs[3].set_ylabel("1800, 3600")
    axs[3].grid()
    axs[4].plot(data00.iloc[15:]["Minimum Fun"], color="red", label="Minimum")
    axs[4].plot(data00["Average Fun"], color="blue", label="Średnia")
    axs[4].plot(data00["Maximum Fun"], color='green', label="Maksimum")
    axs[4].set_ylabel("Tylko mutacja")
    axs[4].set_xlabel("Iteracja", fontsize=14)
    axs[4].grid()

    plt.legend(fontsize=16)

    plt.savefig("../Plots & Charts/prawdopodobieństwa.png")
    plt.show()

    return fig


# Probability of crossover and mutation without first 500 iterations
def fourth_test_vel2():
    data1020 = pd.read_excel("../Dat/RawData_prob1020.xlsx", index_col=0)
    data2040 = pd.read_excel("../Dat/RawData_prob2040.xlsx", index_col=0)
    data3060 = pd.read_excel("../Dat/RawData_prob3060.xlsx", index_col=0)
    data4590 = pd.read_excel("../Dat/RawData_prob4590.xlsx", index_col=0)
    data00 = pd.read_excel("../Dat/RawData_prob00.xlsx", index_col=0)

    fig, axs = plt.subplots(5, 1, figsize=(8.25, 12), sharex='col')
    fig.suptitle("Wynik algorytmu dla różnych progów zmiany operatorów", fontsize=18)
    fig.text(0.02, 0.5, 'Progi zmiany operatora krzyżowania, mutacji', va='center', rotation='vertical', fontsize=14)
    fig.subplots_adjust(top=0.95, bottom=0.05)

    axs[0].plot(data1020.iloc[500:]["Minimum Fun"], color="red", label="Minimum")
    axs[0].plot(data1020.iloc[500:]["Average Fun"], color="blue", label="Średnia")
    axs[0].plot(data1020.iloc[500:]["Maximum Fun"], color='green', label="Maksimum")
    axs[0].set_ylabel("400, 800")
    axs[0].grid()
    axs[1].plot(data2040.iloc[500:]["Minimum Fun"], color="red", label="Minimum")
    axs[1].plot(data2040.iloc[500:]["Average Fun"], color="blue", label="Średnia")
    axs[1].plot(data2040.iloc[500:]["Maximum Fun"], color='green', label="Maksimum")
    axs[1].set_ylabel("800, 1600")
    axs[1].grid()
    axs[2].plot(data3060.iloc[500:]["Minimum Fun"], color="red", label="Minimum")
    axs[2].plot(data3060.iloc[500:]["Average Fun"], color="blue", label="Średnia")
    axs[2].plot(data3060.iloc[500:]["Maximum Fun"], color='green', label="Maksimum")
    axs[2].set_ylabel("1200, 2400")
    axs[2].grid()
    axs[3].plot(data4590.iloc[500:]["Minimum Fun"], color="red", label="Minimum")
    axs[3].plot(data4590.iloc[500:]["Average Fun"], color="blue", label="Średnia")
    axs[3].plot(data4590.iloc[500:]["Maximum Fun"], color='green', label="Maksimum")
    axs[3].set_ylabel("1800, 3600")
    axs[3].grid()
    axs[4].plot(data00.iloc[500:]["Minimum Fun"], color="red", label="Minimum")
    axs[4].plot(data00.iloc[500:]["Average Fun"], color="blue", label="Średnia")
    axs[4].plot(data00.iloc[500:]["Maximum Fun"], color='green', label="Maksimum")
    axs[4].set_ylabel("Tylko mutacja")
    axs[4].set_xlabel("Iteracja", fontsize=14)
    axs[4].grid()
    plt.legend(fontsize=16)

    plt.savefig("../Plots & Charts/prawdopodobieństwa bez pierwszych 500.png")
    plt.show()

    return fig


# Influence of initial population on final solution
def controversial_test():
    df4000 = pd.read_excel("../Dat/RawData_iter_4000.xlsx", index_col=0)

    fig, axs = plt.subplots(2, 1, figsize=(8.25, 9))
    fig.subplots_adjust(top=0.95, bottom=0.05)

    axs[0].set_title("Końcowego najlepsze rozwiązanie a początkowe najlepsze rozwiązanie", fontweight='bold')
    axs[0].scatter(df4000["Initial maximum"], df4000["Final maximum"], s=5)
    axs[0].grid()
    z = np.polyfit(df4000["Initial maximum"], df4000["Final maximum"], 1)
    p = np.poly1d(z)
    axs[0].plot(df4000["Initial maximum"], p(df4000["Initial maximum"]), "r")
    txt = "Linia trendu: y=%.2fx+%.2f" % (z[0], z[1])
    axs[0].annotate(txt, xy=(29, 39.3), xytext=(27, 44.5), fontsize=14,
                    arrowprops=dict(facecolor='black', shrink=0.05))
    axs[0].set_xlabel("Początkowe najlepsze rozwiązanie [PLN/h]")
    axs[0].set_ylabel("Końcowe najlepsze rozwiązanie [PLN/h]")

    axs[1].set_title("Końcowe średnie rozwiązanie a początkowe średnie rozwiązanie", fontweight='bold')
    axs[1].scatter(df4000["Initial average"], df4000["Final average"], s=5)
    axs[1].grid()
    z = np.polyfit(df4000["Initial average"], df4000["Final average"], 1)
    p = np.poly1d(z)
    axs[1].plot(df4000["Initial average"], p(df4000["Initial average"]), "r")
    txt = "y=%.2fx+%.2f" % (z[0], z[1])
    axs[1].annotate(txt, xy=(16, 37.3), xytext=(15, 42.5), fontsize=14,
                    arrowprops=dict(facecolor='black', shrink=0.05))
    axs[1].set_xlabel("Początkowe średnie rozwiązanie [PLN/h]")
    axs[1].set_ylabel("Końcowe średnie rozwiązanie [PLN/h]")

    plt.savefig("../Plots & Charts/yahoooy.png")
    plt.show()
    return fig


def optimized_performance():
    data1020 = pd.read_excel("../Dat/RawData_final.xlsx", index_col=0)

    fig, axs = plt.subplots(1, 1, figsize=(8, 6), sharex='col')
    fig.suptitle("Wynik algorytmu dla wybranych najlepszych parametrów", fontsize=18)

    axs.plot(data1020.iloc[500:]["Minimum Fun"], color="red", label="Minimum")
    axs.plot(data1020.iloc[500:]["Average Fun"], color="blue", label="Średnia")
    axs.plot(data1020.iloc[500:]["Maximum Fun"], color='green', label="Maksimum")
    axs.set_ylabel("Funkcja celu [PLN/h]", fontsize=14)
    axs.set_ylim([27, 44])
    axs.grid()
    axs.set_xlabel("Iteracja", fontsize=14)

    plt.legend(loc="lower right", fontsize=16)

    plt.savefig("../Plots & Charts/optymalność.png")
    plt.show()

    return fig
