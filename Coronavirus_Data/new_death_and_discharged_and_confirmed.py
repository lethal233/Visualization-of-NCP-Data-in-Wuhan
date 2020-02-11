import csv
from datetime import datetime
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def graphing():
    filename = 'numbers.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, new_deaths, new_discharged, new_confirmed = [], [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y/%m/%d")
                death = int(row[7])
                confirmed = int(row[5])
                discharged = int(row[6])
            except ValueError:
                print(current_date, 'missing culmulated confirmed data')
            else:
                dates.append(current_date)
                new_deaths.append(death)
                new_discharged.append(discharged)
                new_confirmed.append(confirmed)

    fig = plt.figure(dpi=120, figsize=(9, 6))
    plt.plot(dates, new_deaths, label='新增死亡人数', c='#c20078', marker='.')
    plt.plot(dates, new_discharged, label='新增出院人数', c='#029386', marker='.')
    plt.plot(dates, new_confirmed, label='新增确诊人数',
             c='#03719c', markerfacecolor='#02d8e9', marker='.')
    for a, b in zip(dates, new_confirmed):
        plt.text(a, b, b, ha='center', va='bottom', fontsize='8')

    for a, b in zip(dates, new_discharged):
        plt.text(a, b, b, ha='left', va='bottom',
                 fontsize='8', rotation='45', alpha=0.5)

    for a, b in zip(dates, new_deaths):
        plt.text(a, b, b, ha='right', va='top',
                 fontsize='8', rotation='-45', alpha=0.5)

    # plt.title("武汉市日新增死亡/出院/确诊人数", bbox=dict(facecolor='g',
    #                                         edgecolor='blue', alpha=0.65), fontsize=24)

    plt.title("武汉市日新增死亡/出院/确诊人数", fontsize=24)
    plt.xlabel('日期', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("人数", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.legend(loc='best')
    plt.show()
    # fig.savefig('new_death_and_discharged_and_confirmed_cases.png')


if __name__ == "__main__":
    graphing()
