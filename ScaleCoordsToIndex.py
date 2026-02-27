def latlon_to_grid(latitude, longitude, min_lat, max_lat, min_lon, max_lon, grid_size=25):

######################
# INCOMING LAT/LONG CONVERSION
######################

    lat_norm = (latitude - min_lat) / (max_lat - min_lat)
    lon_norm = (longitude - min_lon) / (max_lon - min_lon)

######################
# INDEXING CORRECT SIZE
######################

    lat_index = int(lat_norm * (grid_size - 1))
    lon_index = int(lon_norm * (grid_size - 1))

    lat_index = max(0, min(lat_index, grid_size - 1))
    lon_index = max(0, min(lon_index, grid_size - 1))

    return lat_index, lon_index