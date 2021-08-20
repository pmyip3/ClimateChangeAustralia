import requests
import csv


def download(url):
    r = requests.get(url)
    data = r.content.decode('utf-8', errors='ignore')
    cr = csv.reader(data.splitlines(), delimiter=',')
    my_list = list(cr)
    row_counter = 0
    data_list = []
    for row in my_list:
        if row_counter > 25 and len(row[0]) == 4:
            data_list.append(row)
        row_counter += 1

    return data_list


def parse(data_list):
    cleaned_data = []
    for i in range(len(data_list)):
        # year, month, reading
        cleaned_data.append([data_list[i][0], data_list[i][1], data_list[i][4]])


def lambda_handler(event, context):
    # url = 'http://capegrim.csiro.au/GreenhouseGas/data/CapeGrim_CO2_data_download.csv'
    url = event['url']
    print(url)
    data = download(url)
    parse(data)

