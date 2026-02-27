import csv

def read_files( data_files ):
    crime_list = []
    for item in data_files:
        with open(item) as cur_file:
            #temp = cur_file.readline()
            info = csv.reader(cur_file)
            for row in info:
                if row[6] == "False" or row[6] == "True":
                    try:
                        crime_list.append([float(row[8]), float(row[9]), row[7]])
                    except ValueError:
                        pass
                else:
                    try:
                        crime_list.append([float(row[9]), float(row[10]), row[8]])
                    except ValueError:
                        pass

    return crime_list
