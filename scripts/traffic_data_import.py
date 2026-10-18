import requests
from src.config import RAW_DIR 

# NB: parameters and header guide found at https://ondata.github.io/guida-api-istat/
# url and header setting
url = "https://esploradati.istat.it/SDMXWS/rest/data/41_983"
headers = {'Accept': 'application/vnd.sdmx.data+csv;version=1.0.0'}

# setting of stringent parameters to better study the dataset
# params = {'startPeriod' : 2023, 'endPeriod' : 2024}
# traffic_raw = requests.get(url, headers=headers, params=params)
# print(len(traffic_raw.content))
# output of two years 2023-2024 is 2233124 which would be 2.13 MB
# since the data might be manageble in its interity, we can try to export the full csv
traffic_raw = requests.get(url, headers=headers)

output_file = RAW_DIR / "traffic_raw.csv"

# saving the data
if traffic_raw.status_code == 200:
    with open(output_file, "wb") as file:
        file.write(traffic_raw.content)
    # print confirmation in terminal if everything went ok
    print(f"Output saved in '{output_file}'")
else:
    # print error code in terminal, if something went wrong
    print(f"Errore code: {traffic_raw.status_code}")