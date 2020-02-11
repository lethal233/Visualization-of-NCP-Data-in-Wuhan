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

        dates, death_rates, discharged_rates = [], [], []

        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y/%m/%d")
                death = float(row[8])
                discharged = float(row[9])
            except ValueError:
                print(current_date, 'missing culmulated confirmed data.')
            else:
                dates.append(current_date)
                death_rates.append(death)
                discharged_rates.append(discharged)

    # fig = plt.figure(dpi=96, figsize=(10, 6))
    fig = plt.figure(dpi=120, figsize=(9, 6))
    plt.plot(dates, death_rates, label='死亡率', c='#c20078', marker='.')
    plt.plot(dates, discharged_rates, label='治愈率', c='#029386', marker='.')

    # for a, b in zip(dates, death_rates):
    #     plt.text(a, b, b, ha='center', va='bottom', fontsize='8')

    # for a, b in zip(dates, discharged_rates):
    #     plt.text(a, b, b, ha='center', va='top', fontsize='8')

    plt.title("武汉市日死亡/治愈出院比例", fontsize=24)
    plt.xlabel('日期', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("比例", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.legend(loc='best')
    plt.show()
    # fig.savefig('death_and_discharged_rates.png')


if __name__ == "__main__":
    graphing()
