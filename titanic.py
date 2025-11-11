import pandas as pd
import matplotlib.pyplot as plt

#Читаем наш файл parquet, далее конвертируем его в csv и сохраняем в эту же папку без индексов, 
#т.к в excel строки и так пронумерованы
df = pd.read_parquet('D:\учеба\ОМП\\titanic.parquet')
df.to_csv('D:\учеба\ОМП\\titanic.csv', index=False)

#По условию задания читаем уже созданный нами файл csv
df = pd.read_csv('D:\учеба\ОМП\\titanic.csv')
#Задаем данные для гистограммы
#Выделяем из таблицы класс и выживших(в таблице выжившие это 1, 0 - погибшие)
#size считает все строки, unstack преобразует все эти данные в новую таблицу, а в пустые значения закидывает нули
survive = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)
#Вычисляем выживаемость каждого класса
survive_percentage = survive.div(survive.sum(axis=1), axis=0) * 100
#Тип нашего графика bar это столбцы, stacked это чтобы выжившие и не выжившие в одном классе были на одном столбце, а не два рядом
#И размер наших фигур
survive_percentage.plot(kind='bar', stacked=True, figsize=(10, 6))

# Настраиваем заголовок и метки
plt.title('Выживаемость пассажиров Титаника')
plt.xlabel('Класс билета')
#Наши классы выравниваем на оси х, чтобы не были наклонены под 90 градусов
plt.xticks(rotation=0)
#Легенда к графику(обозначение какой цвет что значит)
plt.legend(['Не выжили', 'Выжили'])

# Настройка оси Y на проценты
#Добавляем значение в процентах на ось y
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))
plt.ylim(0, 100)
#Для красоты добавляем линий по процентам
plt.grid(axis='y')
# Отображаем гистограмму
plt.tight_layout()
plt.show()