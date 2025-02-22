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

#20241109 alpha
# destination_point(27.375039, -82.452516,270,38)   # gate 
# destination_point(27.375429, -82.452535,270,60)   # FTP 
# destination_point(27.375202, -82.452487,270,90)   # STC
# 
# destination_point(27.375428998812605, -82.45311225901862,180,8) # FTP 8 meters south
# # 27.375357053084137, -82.45311225901862 # 
# 
# destination_point(27.375202, -82.452487,270,80)   # STC


# 20241109 Bravo

#print("white white bouy on shore")
#print("27.374216,-82.452392")                   # white white on shore
#print("white white bouy 38 meter out")
#
#destination_point(27.374216,-82.452392,270,38)  # white white from shore: 27.374216,-82.452392
#print("\n FTP south:")
#
#destination_point(27.374272,-82.452449,270,67)  # FTP  south
#print("\n points around STC")
#
#destination_point(27.374141,-82.452444,270,90)  # west of STC
#destination_point(27.374141,-82.452444,270,67)  # east of STC
#
#print("5 meters north (west then east)")
## moving 5 meters north
#destination_point(27.374140997039902, -82.4533554509991,0,5)  # west of STC
#destination_point(27.374140998359522, -82.45312252463268,0,5)  # east of STC

#FTP 
destination_point(27.374424, -82.452476,270,67)  # FTP
destination_point(27.374159, -82.452455,270,38)  # gate 
destination_point(27.374159, -82.452455,270,0)   # gate on shore
destination_point(27.374128, -82.452452,270,92)  # STClight bouy
destination_point(27.374186, -82.452434,270,67)  # STC aroud Light tower



destination_point(27.37418599835952, -82.45311252490858,0,5)  # aroud Light power (5m north)

destination_point(27.37412799690688, -82.45338370535629,0,3) # light bouy 3m north
destination_point(27.37415497655505, -82.45338370535629,90,5) # light bouy 3m north

destination_point(27.374128, -82.452452,270,77)  # STC aroud Light tower

