import pandas as pd


def update(df):
    df = df.copy()
    df['average'] = df[['maths', 'physics', 'computer science']].mean(axis=1)
    df = df.sort_values(['average', 'name'], ascending=[False, True])
    return df



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