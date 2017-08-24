import plotly.plotly as py
import plotly.graph_objs as go
import csv
import pandas as pd
import math

# loading the scraped dataset
data = pd.read_csv("World.csv")
df_2007 = data
df_2007 = df_2007.sort_values(['Quand','Quand1'])
slope = 2.666051223553066e-05
hover_text = []
bubble_size = []

# appending the hover text for each character
for index, row in df_2007.iterrows():
    hover_text.append('Victim: {Victime}<br>'.format(Victime=row['Victime']) +
                      'House: {Maison}<br>'.format(Maison=row['Maison'])+
                      'Killer: {Tueur}<br>'.format(Tueur=row['Tueur'])+
                      'Method: {Technique}<br>'.format(Technique=row['Technique'])+
                      'Motive: {Raison}'.format(Raison=row['Raison']))

    bubble_size.append(50)

df_2007['text'] = hover_text
df_2007['size'] = bubble_size

# creating a bubble group for each season for clarity purposes

trace0 = go.Scatter(
    x=1+df_2007['Quand'][df_2007['Quand1'] == ' Season 2'],
    y=df_2007['Hauteur'][df_2007['Quand1'] == ' Season 2'],
    mode='markers',
    name='Season 2',
    text=df_2007['text'][df_2007['Quand1'] == ' Season 2'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_2007['Size'][df_2007['Quand1'] == ' Season 2'],
        line=dict(
            width=2
        ),
    )
)

trace1 = go.Scatter(
    x=1+df_2007['Quand'][df_2007['Quand1'] == ' Season 3'],
    y=df_2007['Hauteur'][df_2007['Quand1'] == ' Season 3'],
    mode='markers',
    name='Season 3',
    text=df_2007['text'][df_2007['Quand1'] == ' Season 3'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_2007['Size'][df_2007['Quand1'] == ' Season 3'],
        line=dict(
            width=2
        ),
    )
)


trace2 = go.Scatter(
    x=1+df_2007['Quand'][df_2007['Quand1'] == ' Season 4'],
    y=df_2007['Hauteur'][df_2007['Quand1'] == ' Season 4'],
    mode='markers',
    name='Season 4',
    text=df_2007['text'][df_2007['Quand1'] == ' Season 4'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_2007['Size'][df_2007['Quand1'] == ' Season 4'],
        line=dict(
            width=2
        ),
    )
)


trace3 = go.Scatter(
    x=1+df_2007['Quand'][df_2007['Quand1'] == ' Season 5'],
    y=df_2007['Hauteur'][df_2007['Quand1'] == ' Season 5'],
    mode='markers',
    name='Season 5',
    text=df_2007['text'][df_2007['Quand1'] == ' Season 5'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_2007['Size'][df_2007['Quand1'] == ' Season 5'],
        line=dict(
            width=2
        ),
    )
)

trace4 = go.Scatter(
    x=1+df_2007['Quand'][df_2007['Quand1'] == ' Season 1'],
    y=df_2007['Hauteur'][df_2007['Quand1'] == ' Season 1'],
    mode='markers',
    name='Season 1',
    text=df_2007['text'][df_2007['Quand1'] == ' Season 1'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_2007['Size'][df_2007['Quand1'] == ' Season 1'],
        line=dict(
            width=2
        ),
    )
)

# setting the axis, labels and colors
data = [trace0, trace1, trace2, trace3, trace4]
layout = go.Layout(
    title='Game Of Thrones Project',
    xaxis=dict(
        title='Episode of Death',
        gridcolor='rgb(255, 255, 255)',
        range=[0, 60],
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Deaths in Episode',
        gridcolor='rgb(255, 255, 255)',
        range=[0, 60],
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
    # setting hovermode to closest in order to allow easier exploration
    hovermode='closest',
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='Game Of Thrones Project')