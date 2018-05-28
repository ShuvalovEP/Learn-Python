import csv

fields = ['ID', 'Name', 'Longitude_WGS84', 'Latitude_WGS84', 'Street', 'AdmArea',
          'District', 'RouteNumbers', 'StationName', 'Direction', 'Pavilion', 
          'OperatingOrgName', 'EntryState', 'global_id', 'geoData']


data_list = []
street_list = []

def get_data_csv():
    with open('data-398-2018-05-25.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, fields, delimiter=';')
        for row in reader:
            data_list.append(row)


get_data_csv()


for row in data_list:
    street_list.append({row['Street']:row['StationName']})
