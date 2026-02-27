## Lists for mix and max latitudes and longitudes of different files
MinLatArr = [43.001275504, 42.9851158380001, 42.9854399870001, 42.9851158380001]
MinLongArr = [-76.129295959, -76.198941034, -76.199029614, -76.2026881469999]
MaxLatArr = [43.1139420000001, 43.1139420000001, 43.0838724320001, 43.1139420000001]
MaxLongArr = [-76.111874999, -76.075872943, -76.075872943, -76.075872943]

MinLong = -76.2026881469999
MaxLong = -76.075872943
MinLat = 42.9851158380001
MaxLat = 43.1139420000001

CRIME_MAP_WIDTH = 25  ## Sets grid size
CRIME_MAP_HEIGHT = 25 ## Currently not used

## List of file names
data_files = ["Crime_Data/Crime_Data_2023-1.csv", "Crime_Data/Crime_Data_2023-2.csv", "Crime_Data/Crime_Data_2024-1.csv", "Crime_Data/Crime_Data_2024-2.csv"]

## All crime types
CRIME_TYPES = {'LARCENY':'Larceny',
               'CRIMINAL MISCHIEF':'Criminal Mischief',
               'SIMPLE ASSAULT':'Simple Assault',
               'MV THEFT':'Motor Vehicle Theft',
               'BURGLARY':'Burglary',
               'OFFN AGAINST FAMILY':'Offence Against Family',
               'AGGRAVATED ASSAULT':'Aggravated Assault'}