import plotly.graph_objects as go
import matplotlib
import numpy as np
import os
import math
import base64
from PIL import Image
from io import BytesIO

import maptoken
import Parameters as params
# Made by Anderson Squires
# Convert heatmap to base64 PNG
def encode_png(arr):
    buffer = BytesIO()
    Image.fromarray(arr).save(buffer, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode()

# 10×10 kilometer square conversion
def lon_to_mx(lon): return lon * 20037508.34 / 180
def lat_to_my(lat): return math.log(math.tan((math.pi/4) + (math.radians(lat)/2))) * 20037508.34 / math.pi
def mx_to_lon(mx): return mx * 180 / 20037508.34
def my_to_lat(my): return math.degrees(2 * math.atan(math.exp(my * math.pi / 20037508.34)) - math.pi/2)

def getCrimeCountArray( crime_map, crime_type='' ):
    crime_count = []
    for y in range(params.CRIME_MAP_HEIGHT):
        temp = []
        for x in range(params.CRIME_MAP_WIDTH):
            num = 0
            d = crime_map[y][x]
            if crime_type in d.keys():
                num += d[crime_type]
            elif crime_type == '':
                num += sum(d.values())

            temp.append(num)
        crime_count.append(temp)
    return crime_count

def generateHeatMap( crime_map, crime_type='', year_flag=False, year='2023' ):

    # Generate title for map
    year_title = ''
    if year_flag and year == '2023':
        year_title = '2023 '
    elif year_flag:
        year_title = '2024 '
    else:
        year_title = '2023 & 2024 '

    crime_label = (params.CRIME_TYPES[crime_type] + ' ') if crime_type != '' else ''

    # Set Mapbox token
    os.environ["MAPBOX_ACCESS_TOKEN"] = maptoken.maptoken

    # Colormap
    plasma = matplotlib.colormaps.get_cmap("plasma")

    # 25×25 heatmap (0.4 km per cell for a 10 km square)
    z = getCrimeCountArray(crime_map, crime_type)
    z_np = np.array(z)
    z_log = np.log1p(z)
    z_norm = (z_log - z_log.min()) / (z_log.max() - z_log.min())
    rgb_img = (plasma(z_norm)[:, :, :3] * 255).astype(np.uint8)

    # Upscale heatmap to 256×256
    rgb_img = np.array(Image.fromarray(rgb_img).resize((256, 256), Image.NEAREST))

    # Convert heatmap to base64 PNG
    encoded_heatmap = encode_png(rgb_img)

    # TRUE geographic centroid of Syracuse
    lat0 = 43.048122
    lon0 = -76.147424

    # Convert center to meters
    mx = lon_to_mx(lon0)
    my = lat_to_my(lat0)

    # Half-size of the box in meters
    half = 5000

    # Corners in meters (mx and my being meters)
    corners_m = [
        (mx - half, my + half),
        (mx + half, my + half),
        (mx + half, my - half),
        (mx - half, my - half)
    ]

    # Convert corners back to lat/lon
    coordinates = [[mx_to_lon(x), my_to_lat(y)] for x, y in corners_m]


    fig = go.Figure()

    # Dummy trace to activate Mapbox
    fig.add_trace(go.Scattermapbox(lat=[lat0], lon=[lon0], mode="markers",
                                   marker=dict(size=1, opacity=0)))
    fig.add_trace(go.Heatmap(
        z=z,
        colorscale="Plasma",
        showscale=True,
        opacity=0,
        hoverinfo="skip"
    ))
    fig.update_layout(
        mapbox=dict(
            accesstoken=os.environ["MAPBOX_ACCESS_TOKEN"],
            style="streets",
            center=dict(lat=lat0, lon=lon0),
            zoom=11.8,
            layers=[
                dict(
                    sourcetype="image",
                    source=encoded_heatmap,
                    coordinates=coordinates,
                    opacity=0.50,
                    below=""
                )
            ]
        ),
        width=700,
        height=700,
        title=year_title + crime_label + "Crime Density Overlay (10km x 10km)"
    )
    # shows our map in a browser
    fig.show(renderer="browser")