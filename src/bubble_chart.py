import pandas as pd
import altair as alt

def bubble_chart_gen(data, x, y):
    """
    Generate the bubble chart.

    Parameters
    ----------
    data : pandas dataframe
        Dataframe containing the data to plot.
    x : string
        Column name to plot on the x-axis.
    y : string
        Column name to plot on the y-axis.
    
    Results
    -------
    chart : html of altair Chart
        The generated bubble chart converted to html
    """

    chart = alt.Chart(
        data=data,
        title="Top 15 Actors from the best rated movies"
    ).encode(
        x=alt.X(x,
                title="",
                axis=None),
        y=alt.Y(y,
                title="",
                sort='-x'),
        size=alt.Size(x,
                  legend=None),
        color=x
    ).mark_circle(
    )

    return chart