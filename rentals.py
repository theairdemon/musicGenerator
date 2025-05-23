import requests
from bs4 import BeautifulSoup
from datetime import datetime
from collections import defaultdict
import os
import json

STATE_FIPS = {
    'Alabama': '01',
    'Alaska': '02',
    'Arizona': '04',
    'Arkansas': '05',
    'California': '06',
    'Colorado': '08',
    'Connecticut': '09',
    'Delaware': '10',
    'Florida': '12',
    'Georgia': '13',
    'Hawaii': '15',
    'Idaho': '16',
    'Illinois': '17',
    'Indiana': '18',
    'Iowa': '19',
    'Kansas': '20',
    'Kentucky': '21',
    'Louisiana': '22',
    'Maine': '23',
    'Maryland': '24',
    'Massachusetts': '25',
    'Michigan': '26',
    'Minnesota': '27',
    'Mississippi': '28',
    'Missouri': '29',
    'Montana': '30',
    'Nebraska': '31',
    'Nevada': '32',
    'New Hampshire': '33',
    'New Jersey': '34',
    'New Mexico': '35',
    'New York': '36',
    'North Carolina': '37',
    'North Dakota': '38',
    'Ohio': '39',
    'Oklahoma': '40',
    'Oregon': '41',
    'Pennsylvania': '42',
    'Rhode Island': '44',
    'South Carolina': '45',
    'South Dakota': '46',
    'Tennessee': '47',
    'Texas': '48',
    'Utah': '49',
    'Vermont': '50',
    'Virginia': '51',
    'Washington': '53',
    'West Virginia': '54',
    'Wisconsin': '55',
    'Wyoming': '56'
}

def get_median_rent(state):
    fips = STATE_FIPS[state]
    url = f"https://api.census.gov/data/2022/acs/acs5"
    params = {"get":"NAME,B25031_003E","for":f"state:{fips}"}
    r = requests.get(url, params=params).json()
    # r[0] is header row
    return float(r[1][1]) * 2

def get_quarterly_climate(lat, lon, year=None):
    year = year or datetime.utcnow().year
    start = f"{year}-01-01"
    end   = f"{year}-12-31"
    url = "https://climate-api.open-meteo.com/v1/climate"
    params = {
        "latitude": lat, "longitude": lon,
        "start_date": start, "end_date": end,
        "daily": "temperature_2m_mean,relative_humidity_2m_mean",
        "models": "EC_Earth3P_HR",
        "timezone": "auto"
    }
    data = requests.get(url, params=params).json()["daily"]
    times = data["time"]
    temps = data["temperature_2m_mean"]
    hums  = data["relative_humidity_2m_mean"]
    quarters = defaultdict(lambda: {"temp":[], "hum":[]})
    for t, tm, hm in zip(times, temps, hums):
        m = int(t.split('-')[1])
        q = (m-1)//3 + 1
        quarters[q]["temp"].append(tm)
        quarters[q]["hum"].append(hm)
    return {q:{"avg_temp":sum(d["temp"])/len(d["temp"]),
               "avg_humidity":sum(d["hum"])/len(d["hum"])}
            for q,d in quarters.items()}

def get_state_legislature(state):
    page = f"{state} State Legislature"
    url = "https://en.wikipedia.org/w/api.php"
    params = {"action":"parse","page":page,
              "prop":"text","format":"json","formatversion":"2"}
    html = requests.get(url, params=params).json()["parse"]["text"]
    soup = BeautifulSoup(html, "html.parser")
    box = soup.find("table", class_="infobox")
    result = {}
    if box:
        for row in box.find_all("tr"):
            th = row.find("th")
            td = row.find("td")
            if th and td:
                key = th.get_text(strip=True)
                val = td.get_text(" ", strip=True)
                if key.lower() in ("seats", "seats2"):
                    result[key] = val
    return result

# approximate geographic centroids for each state (lat, lon)
STATE_COORDINATES = {
    'Alabama': (32.806671, -86.791130),
    'Alaska': (61.370716, -152.404419),
    'Arizona': (33.729759, -111.431221),
    'Arkansas': (34.969704, -92.373123),
    'California': (36.116203, -119.681564),
    'Colorado': (39.059811, -105.311104),
    'Connecticut': (41.597782, -72.755371),
    'Delaware': (39.318523, -75.507141),
    'Florida': (27.766279, -81.686783),
    'Georgia': (33.040619, -83.643074),
    'Hawaii': (21.094318, -157.498337),
    'Idaho': (44.240459, -114.478828),
    'Illinois': (40.349457, -88.986137),
    'Indiana': (39.849426, -86.258278),
    'Iowa': (42.011539, -93.210526),
    'Kansas': (38.526600, -96.726486),
    'Kentucky': (37.668140, -84.670067),
    'Louisiana': (31.169546, -91.867805),
    'Maine': (44.693947, -69.381927),
    'Maryland': (39.063946, -76.802101),
    'Massachusetts': (42.230171, -71.530106),
    'Michigan': (43.326618, -84.536095),
    'Minnesota': (45.694454, -93.900192),
    'Mississippi': (32.741646, -89.678696),
    'Missouri': (38.456085, -92.288368),
    'Montana': (46.921925, -110.454353),
    'Nebraska': (41.125370, -98.268082),
    'Nevada': (38.313515, -117.055374),
    'New Hampshire': (43.452492, -71.563896),
    'New Jersey': (40.298904, -74.521011),
    'New Mexico': (34.840515, -106.248482),
    'New York': (42.165726, -74.948051),
    'North Carolina': (35.630066, -79.806419),
    'North Dakota': (47.528912, -99.784012),
    'Ohio': (40.388783, -82.764915),
    'Oklahoma': (35.565342, -96.928917),
    'Oregon': (44.572021, -122.070938),
    'Pennsylvania': (40.590752, -77.209755),
    'Rhode Island': (41.680893, -71.511780),
    'South Carolina': (33.856892, -80.945007),
    'South Dakota': (44.299782, -99.438828),
    'Tennessee': (35.747845, -86.692345),
    'Texas': (31.054487, -97.563461),
    'Utah': (40.150032, -111.862434),
    'Vermont': (44.045876, -72.710686),
    'Virginia': (37.769337, -78.169968),
    'Washington': (47.400902, -121.490494),
    'West Virginia': (38.491226, -80.954453),
    'Wisconsin': (44.268543, -89.616508),
    'Wyoming': (42.755966, -107.302490),
}

if __name__ == "__main__":
    cache_file = 'state_data_cache.json'
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            all_data = json.load(f)
    else:
        all_data = {}
        for state in STATE_FIPS:
            print("Getting info for " + state + "...")
            lat, lon = STATE_COORDINATES[state]
            rent = get_median_rent(state)
            climate = get_quarterly_climate(lat, lon)
            all_data[state] = {
                'median_rent': rent,
                'climate': climate
            }
        with open(cache_file, 'w') as f:
            json.dump(all_data, f)

    # print out results for each state
    red_states = {'Alabama', 'North Carolina', 'Texas', 'Tennessee', 'Florida', 'Kentucky', 'Lousiana', 'Mississippi', 'West Virginia'}
    boring_states = {'Arkansas', 'Illinois', 'Indiana', 'Kansas', 'Missouri', 'Nebraska', 'Ohio', 'Oklahoma'}

    for state, data in all_data.items():
        print_extra = True
        printout = f"{state}:\n"

        if state in red_states:
            # print(f"{state} is too conservative.")
            print_extra = False

        if state in boring_states and print_extra:
            # print(f"{state} is too boring.")
            print_extra = False

        if data['median_rent'] > 2500 and print_extra:
            # print(f"{state} is expensive.")
            print_extra = False
        
        printout += f"  Median 1-BR rent: ${data['median_rent']:.0f}/mo\n"

        for q, stats in sorted(data['climate'].items()):
            if stats['avg_temp'] < -2 and print_extra:
                # print(f"{state} gets too cold.")
                print_extra = False
            if stats['avg_humidity'] < 40 and print_extra:
                # print(f"{state} gets too dry.")
                print_extra = False

            printout += f"  Q{q} • Avg Temp: {stats['avg_temp']:.1f}°C, Avg Humidity: {stats['avg_humidity']:.0f}%\n"
        # print("  State legislature composition:", data['politics'])
        if print_extra:
            print(printout)
            print("-" * 50)

