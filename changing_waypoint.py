# Original coordinates for 5 meters south
lat_5m, lon_5m = 27.3753209854926, -82.4530253880068

# Create a point and move it 5 meters south
original_point_5m = Point(lat_5m, lon_5m)
destination_point_5m = geodesic(meters=5).destination(original_point_5m, 180)  # 180° is south

# Extract the new coordinates
new_lat_5m, new_lon_5m = destination_point_5m.latitude, destination_point_5m.longitude

(new_lat_5m, new_lon_5m)