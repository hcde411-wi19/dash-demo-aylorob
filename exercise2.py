# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html


# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

# Data comes from summed data from my assignment 7
CarType = ["Sedan", "Sports Car", "SUV", "Wagon", "Minivan", "Pickup", "AWD", "RWD"]
CarNum = [234, 45, 59, 29, 20, 0, 78, 94]

app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': CarType, 'y': CarNum, 'type': 'bar', },

            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Usage of the BGT North of NE 70th per week day'
            }
        }
    )
])


if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)