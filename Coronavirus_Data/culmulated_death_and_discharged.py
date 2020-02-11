import csv
from datetime import datetime

from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def graphing():
    filename = 'numbers.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, culmulated_deaths, culmulated_discharged = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y/%m/%d")
                death = int(row[4])
                discharged = int(row[3])
            except ValueError:
                print(current_date, 'missing culmulated confirmed data')
            else:
                dates.append(current_date)
                culmulated_deaths.append(death)
                culmulated_discharged.append(discharged)

    fig = plt.figure(dpi=120, figsize=(9, 6))
    plt.plot(dates, culmulated_discharged,
             label='累计出院人数', c='#029386', marker='.')
    plt.plot(dates, culmulated_deaths, label='累计死亡人数', c='#c20078', marker='.')

    for a, b in zip(dates, culmulated_deaths):
        plt.text(a, b, b, ha='center', va='bottom',
                 fontsize='8', rotation='-45')
    for a, b in zip(dates, culmulated_discharged):
        plt.text(a, b, b, ha='center', va='top', fontsize='8', rotation='45')

    plt.title("武汉市日累计死亡/出院人数", fontsize=24)
    plt.xlabel('日期', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("人数", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.legend(loc='best')
    plt.show()
    # fig.savefig('culmulated_death_and_discharged_cases.png')


if __name__ == "__main__":
    graphing()
