import json

# Data for locations.json
locations_data = [
    {"id": "loc_01", "latitude": 37.7749, "longitude": -122.4194},
    {"id": "loc_02", "latitude": 34.0522, "longitude": -118.2437},
    {"id": "loc_03", "latitude": 40.7128, "longitude": -74.0060},
    {"id": "loc_04", "latitude": 27.8749, "longitude": 122.4194},
    {"id": "loc_05", "latitude": 57.2749, "longitude": -112.4344},
    {"id": "loc_06", "latitude": 14.0522, "longitude": -119.2531},
    {"id": "loc_07", "latitude": 64.0522, "longitude": -108.2330},
    {"id": "loc_08", "latitude": 24.0522, "longitude": -168.2197}
]

# Data for metadata.json
metadata_data = [
    {"id": "loc_01", "type": "restaurant", "rating": 4.5, "reviews": 120},
    {"id": "loc_02", "type": "hotel", "rating": 4.2, "reviews": 200},
    {"id": "loc_03", "type": "cafe", "rating": 4.7, "reviews": 150},
    {"id": "loc_04", "type": "restaurant", "rating": 4.1, "reviews": 500},
    {"id": "loc_05", "type": "restaurant", "rating": 3.7, "reviews": 110},
    {"id": "loc_06", "type": "hotel", "rating": 4.0, "reviews": 700},
    {"id": "loc_07", "type": "hotel", "rating": 2.0, "reviews": 900},
    {"id": "loc_08", "type": "cafe", "rating": 4.5, "reviews": 750}
]

# Save to JSON files
with open('locations.json', 'w') as f:
    json.dump(locations_data, f, indent=4)

with open('metadata.json', 'w') as f:
    json.dump(metadata_data, f, indent=4)

print("JSON files created successfully!")
