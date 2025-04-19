import folium
from gpx_parser import parse_gpx_file

def create_map(gpx_path, output_html="route_map.html"):
    df = parse_gpx_file(gpx_path)


    # get firstt point to be the centre of the map
    start_lat = df['latitude'].iloc[0]
    start_lon = df['longitude'].iloc[0]
    fmap = folium.Map(location=[start_lat, start_lon], zoom_start=16)

    # draw the route Polyline
    coordinates = df[['latitude', 'longitude']].values.tolist()
    folium.PolyLine(locations=coordinates, color='blue', weight=4).add_to(fmap)

    # mark the start point
    folium.Marker(location=coordinates[0], popup="Start", icon=folium.Icon(color='green')).add_to(fmap)
    # mark the end point
    folium.Marker(location=coordinates[-1], popup="End", icon=folium.Icon(color='red')).add_to(fmap)

    # save the map to html
    fmap.save(output_html)
    print(f"✅ 地圖已儲存：{output_html}")