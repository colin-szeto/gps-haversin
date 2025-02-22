import math
from typing import Tuple

def destination_point(lat, lon, bearing, distance) -> Tuple[float, float]:
    """
    Calculate the destination point given a starting point, bearing, and distance in meters
    """
    # convert decimal degrees to radians
    lon, lat, bearing = map(math.radians, [lon, lat, bearing])

    distance = distance/1000

    # calculate the destination point
    lat2 = math.asin(math.sin(lat) * math.cos(distance/6371) + math.cos(lat) * math.sin(distance/6371) * math.cos(bearing))
    lon2 = lon + math.atan2(math.sin(bearing) * math.sin(distance/6371) * math.cos(lat), math.cos(distance/6371) - math.sin(lat) * math.sin(lat2))
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)
    print("{}, {}".format(lat2, lon2))
    return lat2, lon2
    
destination_point(27.37425599970764, -82.45286308975393,270,20)
destination_point(27.374340999707645, -82.45288009006511,270,15)
destination_point(27.37425599956146, -82.4530656346309,270,30)
destination_point(27.37434099937874, -82.45318390761393 ,90,3)

#scatterm(27.374340999375452, -82.45315352585905, 5, [0.3010, 0.7450, 0.9330]) % FTP 67 m out
destination_point(27.374340999375452, -82.45315352585905 ,180,3)
destination_point(27.374314019727276, -82.45315352585905 ,90,3)
