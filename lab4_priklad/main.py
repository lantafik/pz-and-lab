import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

def methods(n):
    # Method 1: Using the random.randint()
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(1, 6))

    # Method 2: Using random.sample() #max 6
    res = random.sample(range(1, 7), 6)

    # Method 3: Using list comprehension + randrange()
    res = [random.randrange(1, 7, 1) for i in range(n)]

    # Method 4: using loop + randint()
    lis = []
    for _ in range(n):
        lis.append(random.randint(1, 6))

    # Method 5: Random Number Using Numpy
    m5 = list(np.random.randint(low=1, high=7, size=n))


    def count_rate(kub_data: list):
        """
        Возвращает частоту выпадания значений кубика,
        согласно полученным данным
        :param kub_data: данные эксперимента
        :return:
        """
        kub_rate = {}
        for i in kub_data:
            if i in kub_rate:
                continue
            else:
                kub_rate[i] = kub_data.count(i)
        for i in range(1, 7):
            if i not in kub_rate:
                kub_rate[i] = 0
        return kub_rate


    def sort_rate(counted_rate: dict):
        """
        Возвращает отсортированную частоту по ключу
        :param counted_rate: Наша неотсортированная частота
        :return:
        """
        sorted_rate = {}
        for key in sorted(counted_rate.keys()):
            sorted_rate[key] = counted_rate[key]
        return sorted_rate

    def crate_dataframe(sorted_date: dict):
        """
        Создание и преобразование данных в Pandas dataframe
        :param sorted_date: dict
        :return: pd.Dataframe
        """
        df = pd.DataFrame(sorted_date, index=[0])
        df = df.T
        df = df.rename(columns={0: 'Частота'})
        df.insert(0, 'Количество выпаданий', range(1, 1 + len(df)))
        return df

    def probability_solving(dataframe: pd.DataFrame):
        """
        Вычисление вероятности полученных результатов
        :param dataframe:
        :return:
        """
        sum_rate = dataframe['Частота'].sum()
        probability = []
        for i in dataframe['Частота']:
            probability.append(i / sum_rate)
        dataframe['Вероятность'] = probability
        return dataframe


    meths = [rand_list, res, lis, m5]
    for i in range(len(meths)):
        meths[i] = probability_solving(crate_dataframe(sort_rate(count_rate(meths[i]))))
        print(meths[i])

    labels = ['Rand List', 'Res', 'Lis', 'M5']
    colors = ['blue', 'green', 'red', 'purple']

    num_bars = len(meths[0])
    bar_width = 0.2
    x = np.arange(num_bars)

    fig, ax = plt.subplots(figsize=(10, 6))

    for i, df in enumerate(meths):
        x_values = df['Количество выпаданий']
        y_values = df['Вероятность']
        ax.bar(x + i * bar_width, y_values, width=bar_width, color=colors[i], label=labels[i])

    ax.set_xlabel('Количество выпадений')
    ax.set_ylabel('Вероятность')
    ax.set_title('Сравнение вероятностей')
    ax.set_xticks(x + bar_width * (len(meths) - 1) / 2)
    ax.set_xticklabels(x_values)
    ax.legend()

    plt.show()

    return meths


methods(int(input('Введите количество бросков')))
