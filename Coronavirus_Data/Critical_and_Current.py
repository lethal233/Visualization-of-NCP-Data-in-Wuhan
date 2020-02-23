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

        dates, current, critical = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y/%m/%d")
                current_people = int(row[10])
                critical_people = int(row[2])
            except ValueError:
                print(current_date, 'missing culmulated confirmed data')
            else:
                dates.append(current_date)
                current.append(current_people)
                critical.append(critical_people)

    fig = plt.figure(dpi=120, figsize=(9, 6))
    plt.plot(dates, critical,
             label='现有重症人数', c='#c20078', marker='.')
    plt.plot(dates, current, label='现有确诊人数', c='#029386', marker='.')

    for a, b in zip(dates, current):
        plt.text(a, b, b, ha='center', va='bottom',
                 fontsize='8')
    for a, b in zip(dates, critical):
        plt.text(a, b, b, ha='center', va='top', fontsize='8')

    plt.title("武汉市现有重症/确诊人数", fontsize=24)
    plt.xlabel('日期', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("人数", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.legend(loc='best')
    plt.show()
    # fig.savefig('culmulated_current_people_and_critical_people_cases.png')


if __name__ == "__main__":
    graphing()
