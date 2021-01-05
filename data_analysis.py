#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd


def better_first_chart():
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
    axs[6, 0].set_xlabel("Zysk", fontsize=12)

    axs[0, 1].hist(df500['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[1, 1].hist(df1000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[2, 1].hist(df2000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[3, 1].hist(df4000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[4, 1].hist(df6000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[5, 1].hist(df8000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 1].hist(df10000['Suboptimal teaching time'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 1].set_xlabel("Czas", fontsize=12)

    axs[0, 2].hist(df500['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[1, 2].hist(df1000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[2, 2].hist(df2000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[3, 2].hist(df4000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[4, 2].hist(df6000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[5, 2].hist(df8000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 2].hist(df10000['Final maximum'], bins=20, rwidth=szerokosc_paskow)
    axs[6, 2].set_xlabel("Funkcja celu", fontsize=12)

    plt.savefig("Plots & Charts/objective functions comparison.png")
    plt.show()
    return fig1


def second_test():
    data4000 = pd.read_excel("Dat/RawData_oneiter_4000.xlsx", index_col=0)
    data10000 = pd.read_excel("Dat/RawData_oneiter_10000.xlsx", index_col=0)
    fig, axs = plt.subplots(1, 2, figsize=(10, 6), sharey='row')
    fig.suptitle("Zachowanie granicznych i średniego rozwiązania", fontsize=16)

    axs[0].plot(data4000["Minimum Fun"], color="red", label="Minimum")
    axs[0].plot(data4000["Average Fun"], color="blue", label="Średnia")
    axs[0].plot(data4000["Maximum Fun"], color='green', label="Maksimum")
    axs[0].set_ylabel("Funkcja celu", fontsize=12)
    axs[0].set_xlabel("Iteracja", fontsize=12)
    axs[1].plot(data10000["Minimum Fun"], color="red", label="Minimum")
    axs[1].plot(data10000["Average Fun"], color="blue", label="Średnia")
    axs[1].plot(data10000["Maximum Fun"], color='green', label="Maksimum")
    axs[1].set_xlabel("Iteracja", fontsize=12)
    plt.legend(fontsize=16)
    plt.savefig("Plots & Charts/max average min.png")
    plt.show()
    return fig
