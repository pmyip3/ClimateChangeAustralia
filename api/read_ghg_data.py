import requests
import csv


def download(url):
    r = requests.get(url)
    data = r.text
    cr = csv.reader(data.splitlines(), delimiter=',')
    my_list = list(cr)
    data_list = []
    for i in range(25, len(my_list)):
        if len(my_list[i][0]) == 4:
            data_list.append(my_list[i])
    return data_list


def parse(data_list):
    cleaned_data = []
    for i in range(len(data_list)):
        # year, month, reading
        cleaned_data.append({
            "year": data_list[i][0],
            "month": data_list[i][1],
            "value": data_list[i][4]})
    print(cleaned_data)
    return cleaned_data


def lambda_handler(event, context):
    url = event['url']
    print(url)
    data = download(url)
    return parse(data)

url = 'http://capegrim.csiro.au/GreenhouseGas/data/CapeGrim_CO2_data_download.csv'
data = download(url)
parse(data)
