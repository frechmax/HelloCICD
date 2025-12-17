import folium

# Create a map centered at a specific location (e.g., Berlin)
m = folium.Map(location=[52.52, 13.405], zoom_start=10)

# Add a marker (optional)
folium.Marker([52.52, 13.405], popup="Berlin").add_to(m)

# Save the map to output/index.html
m.save('index.html')

