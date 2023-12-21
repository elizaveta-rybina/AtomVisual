import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def create_histogram_station(nuclear_plants):
    nuclear_plants['ConstructionStartAt'] = pd.to_datetime(nuclear_plants['ConstructionStartAt'], errors='coerce')
    nuclear_plants['ConstructionStartYear'] = nuclear_plants['ConstructionStartAt'].dt.year
    grouped_data = nuclear_plants.groupby(['ConstructionStartYear', 'Status']).size().reset_index(name='Count')
    color_map = {
        'Operational': '#94C343',
        'Suspended Construction': '#F97B4D',
        'Under Construction': '#B2A5A0',
        'Shutdown': '#CC3856',
    }

    fig = px.bar(
        grouped_data, 
        x='ConstructionStartYear',
        y='Count', 
        color='Status',
        labels={'Count': 'Количество станций', 'ConstructionStartYear': 'Год'},
        color_discrete_map=color_map
    )

    fig.update_layout(
        title={
        'text': '<span style="text-decoration: underline;">Строительство атомных станций по годам с разделением по статусу</span>',
        'x': 0.5,
        'font': {
            'color': 'white'
        }},
        legend=go.layout.Legend(
            title='Status',
            borderwidth=1,
            bordercolor="white",
            traceorder='normal',
            font=dict(
                color='white'
            ),
            y=1
        ),
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            tickfont=dict(
                color='white'  # Установка белого цвета текста на оси X
            ),
            showgrid=False,  # Убрать сетку на оси X
            title=dict(
                text='Год',
                font=dict(
                    color='white'  # Установить белый цвет для заголовка оси X
                )
            )
        ),
        yaxis=dict(
            tickfont=dict(
                color='white'  # Установка белого цвета текста на оси Y
            ),
            title=dict(
                text='Количество станций',
                font=dict(
                    color='white'  # Установить белый цвет для заголовка оси X
                )
            )
        ),
        legend_title='Статус',
        paper_bgcolor='rgba(0,0,0,0)')
    
    fig.add_annotation(
        x=1986,
        y=5,
        text="Авария на Чернобыльской АЭС",
        showarrow=True,
        arrowhead=1,
        font=dict(
            color="white",
            size=14
        ),
        arrowcolor="white"
    )

    fig.add_annotation(
        x=2011,
        y=4,
        text="Авария на АЭС Фукусима-1",
        showarrow=True,
        arrowhead=1,
        font=dict(
            color="white",
            size=14
        ),
        arrowcolor="white"
    )

    return fig


def create_histogram_weapon(nuclear_test):

    fig = px.bar(
        nuclear_test, 
        x='Year', 
        y='nuclear_weapons_tests', 
        color='Entity',
        labels={'nuclear_weapons_tests': 'Ядерные испытания'},
        title='Изменение количества ядерных испытаний разных стран по годам')


    fig.update_layout(
        title={
        'text': '<span style="text-decoration: underline;">Изменение количества ядерных испытаний разных стран по годам</span>',
        'x': 0.5,
        'font': {
            'color': 'white'
        }},
        legend=go.layout.Legend(
            title='Status',
            borderwidth=1,
            bordercolor="white",
            traceorder='normal',
            font=dict(
                color='white'
            ),
            y=1
        ),
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            tickfont=dict(
                color='white'  # Установка белого цвета текста на оси X
            ),
            showgrid=False,  # Убрать сетку на оси X
            title=dict(
                text='Год',
                font=dict(
                    color='white'  # Установить белый цвет для заголовка оси X
                )
            )
        ),
        yaxis=dict(
            tickfont=dict(
                color='white'  # Установка белого цвета текста на оси Y
            ),
            title=dict(
                text='Ядерные испытания',
                font=dict(
                    color='white'  # Установить белый цвет для заголовка оси X
                )
            )
        ),
        legend_title='Статус',
        paper_bgcolor='rgba(0,0,0,0)')
    
    fig.add_annotation(
        x=1959,
        y=0,
        text="Мораторий СССР, США и Великобритании",
        showarrow=True,
        arrowhead=1,
        font=dict(
            color="white",
            size=14
        ),
        arrowcolor="white"
    )

    fig.add_annotation(
        x=1996,
        y=3,
        text="Договор о запрете ядерных испытаний",
        showarrow=True,
        arrowhead=1,
        font=dict(
            color="white",
            size=14
        ),
        arrowcolor="white"
    )

    fig.add_annotation(
        x=1963,
        y=47,
        text="Договор о ограничении ядерных испытаний",
        showarrow=True,
        arrowhead=1,
        font=dict(
            color="white",
            size=14
        ),
        arrowcolor="white"
    )

    return fig

