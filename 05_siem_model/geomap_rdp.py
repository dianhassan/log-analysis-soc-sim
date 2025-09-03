import pandas as pd
import folium

# Load parsed logs (adjust path if needed)
df = pd.read_csv("rdp_parsed_out/parsed_logs.csv")

# Convert lat/lon to numbers
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
df = df.dropna(subset=["latitude", "longitude"])

# Center map on average coords
map_center = [df["latitude"].mean(), df["longitude"].mean()]
m = folium.Map(location=map_center, zoom_start=2, tiles="CartoDB positron")

# Add red dots for each failed attempt
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=5,
        popup=f"""
        <b>Source IP:</b> {row['sourcehost']}<br>
        <b>User:</b> {row['username']}<br>
        <b>Country:</b> {row['country']}<br>
        <b>Time:</b> {row['timestamp']}
        """,
        color="red",
        fill=True,
        fill_color="red"
    ).add_to(m)

# Save as HTML (interactive map)
m.save("reports/rdp_geomap.html")
print("✅ Interactive geomap saved to reports/rdp_geomap.html")
