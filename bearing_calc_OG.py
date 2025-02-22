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
    
#destination_point(27.375189, -82.452475,270,80)
#destination_point(27.375188997039764, -82.45338645963143,0,5)
#destination_point(27.373553998684432, -82.45304263077614,180,5)

#20241109 Alpha
destination_point(27.375039, -82.452516,270,38)   # gate 
destination_point(27.375429, -82.452535,270,60)   # FTP 
destination_point(27.375202, -82.452487,270,90)   # STC

destination_point(27.375428998812605, -82.45311225901862,180,8) # FTP 8 meters south
# 27.375357053084137, -82.45311225901862 # 

destination_point(27.375202, -82.452487,270,80)   # STC
