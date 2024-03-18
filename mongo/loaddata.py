from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['earthquake_db']
collection = db['earthquake_collection']

# Your data
data = {
    "features": [
        {
            "type": "Feature",
            "properties": {
                "mag": 2,
                "place": "54 km SW of Tatitlek, Alaska",
                "time": 1707964215011,
                "updated": 1707964353020,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak0242443akd",
                "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak0242443akd.geojson",
                "felt": None,
                "cdi": None,
                "mmi": None,
                "alert": None,
                "status": "automatic",
                "tsunami": 0,
                "sig": 62,
                "net": "ak",
                "code": "0242443akd",
                "ids": ",ak0242443akd,",
                "sources": ",ak,",
                "types": ",origin,phase-data,",
                "nst": None,
                "dmin": None,
                "rms": 0.85,
                "gap": None,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 2.0 - 54 km SW of Tatitlek, Alaska"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -147.3918,
                    60.5168,
                    19.7
                ]
            },
            "id": "ak0242443akd"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 0.67,
                "place": "5 km NW of Palomar Observatory, CA",
                "time": 1707964129780,
                "updated": 1707964484180,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ci40670456",
                "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci40670456.geojson",
                "felt": None,
                "cdi": None,
                "mmi": None,
                "alert": None,
                "status": "automatic",
                "tsunami": 0,
                "sig": 7,
                "net": "ci",
                "code": "40670456",
                "ids": ",ci40670456,",
                "sources": ",ci,",
                "types": ",nearby-cities,origin,phase-data,scitech-link,",
                "nst": 38,
                "dmin": 0.04541,
                "rms": 0.18,
                "gap": 33,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 0.7 - 5 km NW of Palomar Observatory, CA"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -116.8986667,
                    33.3876667,
                    13.38
                ]
            },
            "id": "ci40670456"
        },
{
      "type": "Feature",
      "properties": {
        "mag": 2.39,
        "place": "11 km ENE of Pāhala, Hawaii",
        "time": 1707963305280,
        "updated": 1707963962040,
        "tz": None,
        "url": "https://earthquake.usgs.gov/earthquakes/eventpage/hv74112096",
        "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv74112096.geojson",
        "felt": None,
        "cdi": None,
        "mmi": None,
        "alert": None,
        "status": "automatic",
        "tsunami": 0,
        "sig": 88,
        "net": "hv",
        "code": "74112096",
        "ids": ",us7000lzb0,hv74112096,",
        "sources": ",us,hv,",
        "types": ",origin,phase-data,",
        "nst": 52,
        "dmin": 0.09601,
        "rms": 0.180000007,
        "gap": 154,
        "magType": "ml",
        "type": "earthquake",
        "title": "M 2.4 - 11 km ENE of Pāhala, Hawaii"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -155.374664306641,
          19.2238330841064,
          32.25
        ]
      },
      "id": "hv74112096"
    },
    {
      "type": "Feature",
      "properties": {
        "mag": 0.85,
        "place": "5 km NNE of Moreno Valley, CA",
        "time": 1707963263570,
        "updated": 1707963641415,
        "tz": None,
        "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ci40670448",
        "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci40670448.geojson",
        "felt": None,
        "cdi": None,
        "mmi": None,
        "alert": None,
        "status": "automatic",
        "tsunami": 0,
        "sig": 11,
        "net": "ci",
        "code": "40670448",
        "ids": ",ci40670448,",
        "sources": ",ci,",
        "types": ",nearby-cities,origin,phase-data,scitech-link,",
        "nst": 33,
        "dmin": 0.04372,
        "rms": 0.2,
        "gap": 79,
        "magType": "ml",
        "type": "earthquake",
        "title": "M 0.9 - 5 km NNE of Moreno Valley, CA"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -117.2168333,
          33.9713333,
          12.77
        ]
      },
      "id": "ci40670448"
    },
    {
      "type": "Feature",
      "properties": {
        "mag": 0.93,
        "place": "10 km SSE of Big Bear City, CA",
        "time": 1707962814340,
        "updated": 1707963165624,
        "tz": None,
        "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ci40670440",
        "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci40670440.geojson",
        "felt": None,
        "cdi": None,
        "mmi": None,
        "alert": None,
        "status": "automatic",
        "tsunami": 0,
        "sig": 13,
        "net": "ci",
        "code": "40670440",
        "ids": ",ci40670440,",
        "sources": ",ci,",
        "types": ",nearby-cities,origin,phase-data,scitech-link,",
        "nst": 38,
        "dmin": 0.1211,
        "rms": 0.15,
        "gap": 59,
        "magType": "ml",
        "type": "earthquake",
        "title": "M 0.9 - 10 km SSE of Big Bear City, CA"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -116.821,
          34.1685,
          9.78
        ]
      },
      "id": "ci40670440"
    },
    {
      "type": "Feature",
      "properties": {
        "mag": 1.8,
        "place": "39 km SSE of Denali National Park, Alaska",
        "time": 1707962514512,
        "updated": 1707962724838,
        "tz": None,
        "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak024243x5uj",
        "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak024243x5uj.geojson",
        "felt": None,
        "cdi": None,
        "mmi": None,
        "alert": None,
        "status": "automatic",
        "tsunami": 0,
        "sig": 50,
        "net": "ak",
        "code": "024243x5uj",
        "ids": ",ak024243x5uj,",
        "sources": ",ak,",
        "types": ",origin,phase-data,",
        "nst": None,
        "dmin": None,
        "rms": 1.04,
        "gap": None,
        "magType": "ml",
        "type": "earthquake",
        "title": "M 1.8 - 39 km SSE of Denali National Park, Alaska"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -151.4247,
          63.2095,
          3.2
        ]
      },
      "id": "ak024243x5uj"
    },
    {
      "type": "Feature",
      "properties": {
        "mag": 3.34,
        "place": "1 km WSW of Jagual, Puerto Rico",
        "time": 1707962231630,
        "updated": 1707964700040,
        "tz": None,
        "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr71439953",
        "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr71439953.geojson",
        "felt": None,
        "cdi": None,
        "mmi": None,
        "alert": None,
        "status": "reviewed",
        "tsunami": 0,
        "sig": 172,
        "net": "pr",
        "code": "71439953",
        "ids": ",us7000lzay,pr71439953,",
        "sources": ",us,pr,",
        "types": ",origin,phase-data,",
        "nst": 14,
        "dmin": 0.1554,
        "rms": 0.13,
        "gap": 109,
        "magType": "md",
        "type": "earthquake",
        "title": "M 3.3 - 1 km WSW of Jagual, Puerto Rico"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -66.0115,
          18.1568333333333,
          76.19
        ]
      },
      "id": "pr71439953"
    },
    {
      "type": "Feature",
      "properties": {
        "mag": 2.11,
        "place": "4 km S of Pāhala, Hawaii",
        "time": 1707961253040,
        "updated": 1707961406930,
        "tz": None,
        "url": "https://earthquake.usgs.gov/earthquakes/eventpage/hv74110837",
        "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv74110837.geojson",
        "felt": None,
        "cdi": None,
        "mmi": None,
        "alert": None,
        "status": "automatic",
        "tsunami": 0,
        "sig": 68,
        "net": "hv",
        "code": "74110837",
        "ids": ",hv74110837,",
        "sources": ",hv,",
        "types": ",origin,phase-data,",
        "nst": 48,
        "dmin": 0.02079,
        "rms": 0.140000001,
        "gap": 104,
        "magType": "ml",
        "type": "earthquake",
        "title": "M 2.1 - 4 km S of Pāhala, Hawaii"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -155.481826782227,
          19.1646671295166,
          31.1900005340576
        ]
      },
      "id": "hv74110837"
    },
    {
      "type": "Feature",
      "properties": {
        "mag": 1.5,
        "place": "20 km NNE of Napa, CA",
        "time": 1707964790000,
        "updated": 1707964899999,
        "tz": None,
        "url": "https://earthquake.usgs.gov/earthquakes/eventpage/nc00000001",
        "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc00000001.geojson",
        "felt": None,
        "cdi": None,
        "mmi": None,
        "alert": None,
        "status": "automatic",
        "tsunami": 0,
        "sig": 35,
        "net": "nc",
        "code": "00000001",
        "ids": ",nc00000001,",
        "sources": ",nc,",
        "types": ",origin,phase-data,",
        "nst": 10,
        "dmin": 0.15,
        "rms": 0.08,
        "gap": 45,
        "magType": "md",
        "type": "earthquake",
        "title": "M 1.5 - 20 km NNE of Napa, CA"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -122.2708333,
          38.4111667,
          9.59
        ]
      },
      "id": "nc00000001"
    },
        # Add more earthquake features here...
    ]
}

# Insert each earthquake feature as a separate document
for feature in data['features']:
    collection.insert_one(feature)

print("Documents inserted successfully.")
