import pandas as pd
import plotly.express as px

# Load the dataset
file_path = 'UN_food_security.csv'
data = pd.read_csv(file_path)

# Filter the dataset for 'Number of people undernourished (million)'
undernourished_data = data[data['Item'] == 'Number of people undernourished (million) (3-year average)'].copy()

# Convert 'Year' from range to single year (middle year of each range)
undernourished_data['Single Year'] = undernourished_data['Year'].apply(lambda x: int(x.split('-')[0]) + 1)

# Replace known non-numeric values with a numeric equivalent and convert 'Value' to float
undernourished_data['Value'] = pd.to_numeric(undernourished_data['Value'], errors='coerce').fillna(0)

# Create the bubble map
fig = px.scatter_geo(
    undernourished_data,
    locations="Area",
    locationmode='country names',
    size="Value",
    hover_name="Area",
    animation_frame="Single Year",
    title='Global Number of People Undernourished (Million) Over Time',
    color_discrete_sequence=["darkred"],
    size_max=100
)

# Show the figure
fig.update_traces(marker=dict(color='darkred'), selector=dict(mode='markers'))
fig.show()


