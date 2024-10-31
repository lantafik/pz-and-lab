import pandas as pd


def update(df):
    df = df.copy()
    df['average'] = df[['maths', 'physics', 'computer science']].mean(axis=1)
    df = df.sort_values(['average', 'name'], ascending=[False, True])
    return df

<<<<<<< HEAD


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = update(journal)
print(journal)
print(filtered)
=======
# Обычное сравнение
print("1. Самое обычное сравнение:")
a = fuzz.ratio('Привет мир', 'Привет мир')
print(a)

a = fuzz.ratio('Привет мир', 'Привт кир')
print(a)

#Частичное сравнение
print("2. Частичное сравнение")
a = fuzz.partial_ratio('Привет мир', 'Привет мир!')
print(a)

a = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, Привет мир')
print(a)

a = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, привет мир')
print(a)

#Сравнение по токену
print("3. Сравнение по токену")
a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш Привет')
print(a)

a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш любимый Привет')
print(a)

a = fuzz.token_sort_ratio('1 2 Привет наш мир', '1 мир наш 2 ПриВЕт')
print(a)

a = fuzz.token_set_ratio('Привет наш мир', 'мир мир наш наш наш ПриВЕт')
print(a)

#Продвинутое обычное сравнение
print('4. Продвинутое обычное сравнение')
a = fuzz.WRatio('Привет наш мир', '!ПриВЕт наш мир!')
print(a)

a = fuzz.WRatio('Привет наш мир', '!ПриВЕт, наш мир!')
print(a)
#Работа со списком
print("5. Работа со списком")
city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extract("Саратов", city, limit=2)
# Параметр limit по умолчанию имеет значение 5
print(a)

city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extractOne("Краногрск", city)
print(a)
>>>>>>> 855c6a52f0325bd39e2f5d251ab80d20baeba384
