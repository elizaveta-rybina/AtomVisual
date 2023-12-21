import plotly.express as px
import plotly.graph_objects as go

def create_map(nuclear_plants):

    fig = px.scatter_geo(
        nuclear_plants,
        lat='Latitude',
        lon='Longitude',
        title='Карта ядерных электростанций с указанием статуса',
        hover_name='Name',
        size='Capacity',
        custom_data=['Name', 'Country', 'Capacity'],
        projection='equirectangular',
        color='Status',
        size_max=12  # Максимальный размер точки
    )

    fig.add_trace(go.Choropleth(locations=['ATA'],
            z=[0],
            colorscale=[[0,'rgba(0,0,0,0)'], [1,'rgba(0,0,0,0)']],
            marker_line_color='rgba(0,0,0,0)',
            showlegend=False,
            showscale=False)
    )
    
    fig.update_traces(
        hovertemplate='<b>%{customdata[0]}</b><br>Страна: %{customdata[1]}<br>Мощность: %{customdata[2]} МВт',
        selector=dict(type='scattergeo')
    )

    fig.update_geos(projection_type="natural earth", lataxis_range=[-59, 80], showland=True, landcolor="white", showcountries=True, showframe=False, bgcolor="rgba(0,0,0,0)")

    fig.update_layout(
        title={
        'text': '<span style="text-decoration: underline;">Карта ядерных электростанций с указанием статуса</span>',
        'x': 0.5,
        'font': {
            'color': 'white',
        }
        },
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
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        height=550,
        coloraxis_colorbar=dict(
        title='Мощность',
        thicknessmode="pixels", thickness=30,
        lenmode="pixels", len=800,
        yanchor="top", y=1,
        ticks="inside",
        ticksuffix=" MW",
        ticklen=10
    ))

    return fig