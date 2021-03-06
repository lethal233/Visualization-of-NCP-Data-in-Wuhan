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

        dates, culmulated_confirmed = [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y/%m/%d")
                data = int(row[1])
            except ValueError:
                print(current_date, 'missing culmulated confirmed data')
            else:
                dates.append(current_date)
                culmulated_confirmed.append(data)

    # fig = plt.figure(dpi=96, figsize=(10, 6))
    fig = plt.figure(dpi=120, figsize=(9, 6))
    plt.plot(dates, culmulated_confirmed,
             label='累计确诊人数', c='#1fa774', marker='.')

    for a, b in zip(dates, culmulated_confirmed):
        plt.text(a, b, b, ha='center', va='bottom', fontsize='8')

    plt.title("武汉市日累计确诊人数", fontsize=24)
    plt.xlabel('日期', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("人数", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.legend(loc='best')
    plt.show()
    # fig.savefig('culmulated_cases.png')


if __name__ == "__main__":
    graphing()
