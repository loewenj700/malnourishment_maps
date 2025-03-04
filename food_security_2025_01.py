import pandas as pd
import plotly.express as px

# Load dataset
file_path = 'UN_food_security.csv'
data = pd.read_csv(file_path)

# Filter for 'Prevalence of undernourishment (percent) (3-year average)'
undernourishment_data = data[data['Item'] == 'Prevalence of undernourishment (percent) (3-year average)'].copy()

# Convert 'Year' from range to middle year (e.g., '2000-2002' -> 2001)
undernourishment_data['Single Year'] = undernourishment_data['Year'].apply(lambda x: int(x.split('-')[0]) + 1)

# Clean 'Value' column by replacing leading comparison operators like '<' or '>' with just the numeric part
undernourishment_data['Value'] = undernourishment_data['Value'].astype(str).str.replace(r'^[><=]+', '', regex=True).astype(float)

# Create choropleth map with slider
fig = px.choropleth(
    undernourishment_data,
    locations="Area",
    locationmode="country names",
    color="Value",
    hover_name="Area",
    animation_frame="Single Year",
    color_continuous_scale=px.colors.sequential.RdBu_r,
    title='Global Prevalence of Undernourishment (%) Over Time',
    labels={'Value': 'Undernourishment (%)'}
)

# Show map
fig.show()

