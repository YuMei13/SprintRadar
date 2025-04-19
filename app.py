# from gpx_parser import parse_gpx_file

# df = parse_gpx_file("data/sprintradar_test_sample.gpx")
# print(df.head())

from map_plotter import create_map

# test data to draw map
create_map("data/sprintradar_test_sample.gpx", output_html="route_map.html")