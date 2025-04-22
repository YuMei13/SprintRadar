import base64
import io
import dash
from dash import dcc, html, Output, Input
import plotly.graph_objects as go
import gpxpy

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2("Upload GPX data"),
    dcc.Upload(
        id='upload-gpx',
        children=html.Div(['drag or choose GPX data']),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=True
    ),
    dcc.Graph(id='map')
])

def parse_gpx(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    gpx_file = io.StringIO(decoded.decode('utf-8'))
    gpx = gpxpy.parse(gpx_file)
    latitudes = []
    longitudes = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                latitudes.append(point.latitude)
                longitudes.append(point.longitude)
    return latitudes, longitudes

@app.callback(
    Output('map', 'figure'),
    Input('upload-gpx', 'contents'),
    Input('upload-gpx', 'filename')
)
def update_map(list_of_contents, list_of_names):
    if list_of_contents is not None:
        fig = go.Figure()
        for contents, name in zip(list_of_contents, list_of_names):
            latitudes, longitudes = parse_gpx(contents)
            fig.add_trace(go.Scattermapbox(
                lat=latitudes,
                lon=longitudes,
                mode='lines',
                name=name
            ))
        fig.update_layout(
            mapbox_style="open-street-map",
            mapbox_zoom=10,
            mapbox_center={"lat": latitudes[0], "lon": longitudes[0]},
            margin={"r":0,"t":0,"l":0,"b":0}
        )
        return fig
    return go.Figure()

# if __name__ == '__main__':
#     app.run_server(debug=True)
