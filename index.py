python
import pandas as pd
import matplotlib.pyplot as plt

# Load transportation dataset
transport_data = pd.read_csv("Public_Transportation_Utilization_Metrics.csv")

# Load healthcare dataset
healthcare_data = pd.read_csv("Healthcare_Facility_Utilization_Data.csv")

# Example analysis: Peak hours for public transportation
transport_data['hour'] = pd.to_datetime(transport_data['time_of_day']).dt.hour
peak_hours = transport_data.groupby('hour')['number_of_passengers'].sum()

# Plotting transportation peak hours
plt.figure(figsize=(10, 6))
peak_hours.plot(kind='bar', color='skyblue')
plt.title('Transportation Peak Hours')
plt.xlabel('Hour of the Day')
plt.ylabel('Total Passengers')
plt.xticks(rotation=45)
plt.show()

# Example analysis: Top 5 busiest healthcare facilities
busiest_facilities = healthcare_data.groupby('facility_name')['number_of_visits'].sum().nlargest(5)

# Plotting busiest facilities
plt.figure(figsize=(10, 6))
busiest_facilities.plot(kind='bar', color='salmon')
plt.title('Top 5 Busiest Healthcare Facilities')
plt.xlabel('Healthcare Facility')
plt.ylabel('Number of Visits')
plt.xticks(rotation=45)
plt.show()
