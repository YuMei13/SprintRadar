from gpx_parser import parse_gpx_file

df = parse_gpx_file("data/sprintradar_test_sample.gpx")
print(df.head())