# график scatter
import plotly.express as px
from pandas import DataFrame

# данные для визуализации
df = DataFrame({'Perihelion': [0.46, 1.07, 1.47, 2.06, 7.4, 13.53, 27.48, 44.52]})
df['Number'] = [1, 2, 3, 4, 5, 6, 7, 8]
# коэффициент радиуса планет
df['Radius'] = [0.24, 0.6, 0.64, 0.33, 7.1, 6.02, 2.6, 2.5]
# типы планеты
df['Types'] = ['', '', '', '', '', '', '', '']
df.loc[:4, 'Types'] = 'Земная группа'
df.loc[4:, 'Types'] = 'Планеты-гиганты'
# масса планет (на 10 в 24 степени килограмм)
df['Масса'] = [0.33, 4.87, 5.97, 0.64, 1898.6, 568.46, 86.81, 102.43]
# орбитальная скорость (км/с)
df['Скорость'] = [47.36, 35.02, 29.78, 24.13, 13.07, 9.69, 6.81, 5.43]

# цвет планет
Меркурий = '#74563a'
Венера = '#bfc1c0'
Земля = '#384a5e'
Марс = '#8c2222'
Юпитер = '#ffaa4d'
Сатурн = '#9d9772'
Уран = '#acbecc'
Нептун = '#90bbea'
df['Планеты'] = ['Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун']

# создать график
fig = px.scatter(df,
                 x='Perihelion',
                 y='Number',
                 size='Radius',
                 color='Планеты',
                 hover_name='Types',
                 hover_data=['Масса', 'Скорость'])

# показать график в HTML
fig.write_html('graph.html', auto_open=True)
