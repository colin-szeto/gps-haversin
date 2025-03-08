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
    

lon_bouy1 = -82.452822
lon_bouy2 = -82.452927
lon_bouy3 = -82.453066

destination_point(27.374223,lon_bouy3,270,7.292 )#N1
destination_point(27.374203,lon_bouy3,270,7.75  )#F1
destination_point(27.374053,lon_bouy3,270,8.934 )#F2
destination_point(27.374000,lon_bouy3,270,10.927)#f3
destination_point(27.373953,lon_bouy3,270,9.757 )#f4
destination_point(27.373953,lon_bouy3,270,8.24  )#f5
destination_point(27.373914,lon_bouy3,270,5.857 )#f6
destination_point(27.373914,lon_bouy3,270,4.037 )#f7
destination_point(27.373914,lon_bouy2,270,5.985 )#s1
destination_point(27.373731,lon_bouy1,270,1.963 )#s2
destination_point(27.373828,lon_bouy1,270,3.666 )#s3
destination_point(27.373931,lon_bouy1,270,1.963 )#s4
destination_point(27.374056,lon_bouy1,270,1.963 )#s5
destination_point(27.374056,lon_bouy1,270,4.963 )#s6
destination_point(27.373931,lon_bouy1,270,4.963 )#s7
destination_point(27.373828,lon_bouy1,270,3.666 )#s3
destination_point(27.373731,lon_bouy1,270,3.666 )#s2
destination_point(27.373828,lon_bouy1,270,3.666 )#s3
destination_point(27.373931,lon_bouy1,270,4.963 )#s7
destination_point(27.374056,lon_bouy1,270,4.963 )#s6
destination_point(27.373983,lon_bouy2,270,5.985 )#d1
destination_point(27.374078,lon_bouy2,270,3.825 )#g1
destination_point(27.374175,lon_bouy2,270,5.985 )#g2
destination_point(27.374205,lon_bouy2,270,3.825 )#g3
destination_point(27.374275,lon_bouy2,270,3.825 )#g4