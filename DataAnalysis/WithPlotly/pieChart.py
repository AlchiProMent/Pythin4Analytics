# круговая диаграмма
import plotly.express as px

# получить набор счетов из ресторана
df = px.data.tips()

# круговая диаграмма
fig = px.pie(df, names='day', values='tip')

# показать в браузере
fig.write_html('graph.html', auto_open=True)
