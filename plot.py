# Using plotly.express
import plotly.express as px
import pandas as pd

df = pd.read_csv('listing_stats.csv')
# convert the 'date_hour' column to datetime format
df['date_hour']= pd.to_datetime(df['date_hour'])
fig = px.line(df, x='date_hour', y="lowest_price", markers=True)
fig.update_layout(showlegend=False, paper_bgcolor = 'rgba(0, 0, 0, 0)', plot_bgcolor = 'rgba(0, 0, 0, 0)' )
fig.add_vline(x='2022-08-25 10:20:00', line_width=3, line_dash="dash", line_color="red")
fig.add_vline(x='2022-08-25 15:40:00', line_width=3, line_dash="dash", line_color="red")
fig.update_traces(textposition='top center')
fig.add_annotation(x='2022-08-25 8:30:00', y=20,
            text="Buy before 10:30 am",
            showarrow=False)
fig.add_annotation(x='2022-08-25 17:15:00', y=20,
            text="and after 3:15 pm",
            showarrow=False)
fig.update_xaxes(linewidth = 2, linecolor ='black')
fig.update_yaxes(linewidth = 2, linecolor ='black')
fig.update_layout(
    title="Last Minute Mets Ticket Prices on SeetGeek (Game Against the Rockies, Thursday 8/26 7pm)",
    xaxis_title="Date and Time",
    yaxis_title="Lowest Ticket Price ($)")
fig.update_yaxes(range=[0, 25])
fig.write_html("plot.html")

