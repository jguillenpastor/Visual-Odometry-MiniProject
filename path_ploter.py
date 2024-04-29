import pandas as pd
import utm
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_csv('../DJIFlightRecord_2021-03-18_[13-04-51]-TxtLogToCsv.csv',encoding='latin1')

# Extract latitude and longitude columns
latitude_column = 'OSD.latitude'
longitude_column = 'OSD.longitude'

# Convert latitude and longitude to UTM
utm_coords = []
for index, row in df.iterrows():
    lat = row[latitude_column]
    lon = row[longitude_column]
    utm_coords.append(utm.from_latlon(lat, lon))

# Split UTM coordinates into UTM Easting and Northing
utm_easting, utm_northing, _, _ = zip(*utm_coords)

# Plot UTM path
plt.figure(figsize=(10, 8))
plt.plot(utm_easting, utm_northing, marker='.', linestyle='-')
plt.xlabel('UTM Easting (m)')
plt.ylabel('UTM Northing (m)')
plt.title('UTM Path')
plt.grid(True)
plt.show()
