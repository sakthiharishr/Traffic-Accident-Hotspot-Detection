from geopy.geocoders import Nominatim

geolocator = Nominatim(
    user_agent="traffic_hotspot_project"
)

def get_location_name(lat, lon):

    try:

        location = geolocator.reverse(
            (lat, lon),
            timeout=10
        )

        address = location.raw.get(
            "address",
            {}
        )

        return (
            address.get("suburb")
            or address.get("neighbourhood")
            or address.get("village")
            or address.get("town")
            or address.get("city")
            or "Unknown"
        )

    except:

        return "Unknown"