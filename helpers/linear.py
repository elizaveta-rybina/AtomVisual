import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def create_linear(nuclear_number):
    fig = px.line(
        nuclear_number, 
        x='Year', 
        y='nuclear_weapons_stockpile', 
        color='Entity',
        line_group='Entity', 
        labels={'nuclear_weapons_stockpile': 'Ядерные запасы'},
        height=600
    )

    fig.update_traces(line=dict(width=4))

    fig.update_layout(
        title={
        'text': '<span style="text-decoration: underline;">Изменение ядерных запасов разных стран по годам</span>',
        'x': 0.5,
        'font': {
            'color': 'white'
        }},
        plot_bgcolor='rgba(0,0,0,0)',
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
                text='Ядерные запасы',
                font=dict(
                    color='white'  # Установить белый цвет для заголовка оси X
                )
            )
        ),
        legend_title='Страна', 
        showlegend=True,
        height=500,
        paper_bgcolor='rgba(0,0,0,0)'
    )

    # fig.add_annotation(
    #     x=1986,
    #     y=40159,
    #     text="Договор о ликвидации ракет средней и меньшей дальности",
    #     showarrow=True,
    #     arrowhead=1,
    #     font=dict(
    #         color="white",
    #         size=14
    #     ),
    #     arrowcolor="white"
    # )

    return fig
