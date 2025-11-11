import matplotlib.pyplot as plt #Импорт всех необходимых библиотек
import docx
import re
from collections import Counter
import pandas as pd


#открываем наш документ docx
f = docx.Document("D:\Загрузки\lion.docx")
#пустая переменная для текста
text = []
#Отделяем каждый абзац и вносим его в переменную с конца
for paragraph in f.paragraphs:
    text.append(paragraph.text)
#Обьеденим все абзацы
text = ' '.join(text)
#Теперь отделяем каждое слово, убирая знаки препинания, а также делаем все слова с маленькой буквы, чтобы поиск был правильнее,
#т.к если слово с большой буквы, то он будет считать именно его(отдельно от слова, которое с маленькой,т.е из-за разного регистра
#будет считать как два разных слова)
words = re.findall(r'\b\w+\b', text.lower())

#Считаем все слова, у каждого слова будет значение его кол-ва повторений
nwords = Counter(words)
#Общее число слов в тексте
vsego_words = sum(nwords.values())
#Создаем dataframe, значения каждого слово и его число повторений
df_words = pd.DataFrame(nwords.items(), columns=['Слово', 'Частота'])
#Рассчитываем проценты и добавляем для каждого слова процнты его частоты встречи
df_words['Процент'] = (df_words['Частота'] / vsego_words) * 100

#Записываем нашу таблицу в существующий пустой файл xlsx для экселя
writer = pd.ExcelWriter('D:\учеба\ОМП\sasa.xlsx', engine='openpyxl')
#Тут убираем колонку индексов, т.к в этом нет небходимости, в excel есть своя нумерация строк
df_words.to_excel(writer, 'Sheet1', index = False)
writer.close()

#Считаем теперь все русские буквы, делаем их в нижний регистр
letters = re.findall(r'[а-яА-ЯёЁ]', text.lower())
#Считаем все буквы, у каждой буквы будет значение ее кол-ва повторений
nletters = Counter(letters)
#создаем dataframe для буквы с двумя колоннами. Буква и ее частота
df_letters = pd.DataFrame(nletters.items(), columns=['Буква', 'Частота'])

#Создаем гистограмму из нашего dataframe-а
#Размер столбиков
plt.figure(figsize=(10, 6))
#Используемые значения для букв и частоты, а также цвет граифка
plt.bar(df_letters['Буква'], df_letters['Частота'], color='green')
#Название графика
plt.title('Частота встречаемости букв')
#Колонки 
plt.xlabel('Буквы')
#Частота повторения
plt.ylabel('Частота')
#Отрисовка вертикальных линий для удобства просмотра
plt.grid(axis='y')

# Отображаем гистограмму для букв
plt.tight_layout()
#вывод графика
plt.show()



