import Parameters as params                       ## Import project-wide parameters
from ScaleCoordsToIndex import latlon_to_grid     ## Convert from latitude/longitude to indexes for the crime map
from Crime_Data import Data_Compiler as DataComp  ## Function to read the crime data

#############################
### Made by: Jhon Kiselev ###
#############################
def createCrimeMap( flag=False, year='2023' ):

    ## Important parameters
    crime_map = []
    file_crime_map = []
    if flag and year == '2023':
        file_crime_map = DataComp.read_files(params.data_files[0:2])
    elif flag:
        file_crime_map = DataComp.read_files(params.data_files[2:])
    else:
        file_crime_map = DataComp.read_files(params.data_files)

    grid_size = params.CRIME_MAP_WIDTH

    ## Initialize the crime map array
    for y in range(0, grid_size):
        temp_list = []
        for x in range(0, grid_size):
            temp_list.append({})
        crime_map.append(temp_list)

    ## Go through the points from file_crime_map and load them into crime_map
    ## point -> [lat, long, crime_type]
    for point in file_crime_map:
        lat = point[0]
        long = point[1]
        crime_type = point[2]

        ## Getting the x and y indexes for the array
        y, x = latlon_to_grid(float(lat), float(long),
                              params.MinLat, params.MaxLat,
                              params.MinLong, params.MaxLong,
                              grid_size)

        ## Add the point to crime_map
        if crime_type in crime_map[y][x].keys():
            crime_map[y][x][crime_type] += 1
        else:
            crime_map[y][x][crime_type] = 1

    return crime_map

#print(createCrimeMap())