
# External Libraries and Modules
import matplotlib.pyplot as plt
import numpy as np

import gmplot
#######################################
# Adding the Classes path to sys path, to import classes/packages
import sys
sys.path.insert(0, "./Classes")
#######################################
# Internal Classes and Modules
from IO import IO
#######################################

# Set up a databse connection
IO = IO();
IO.DataIO_DataBase('../Data/TransitData.db');
AA = IO.DataBase_Select_ReturnAll("Select stop_lat,stop_lon From stops Where stop_id in (Select stop_id From stop_times Where trip_id = '34597099')");



LAT = [];
LON = [];
for i in range(0,len(AA)):
    LAT.append(AA[i][0]);
    LON.append(AA[i][1]);

gmap = gmplot.GoogleMapPlotter(LAT[0], LON[1], 15)
gmap.plot(LAT, LON, 'cornflowerblue', edge_width=10)
gmap.scatter(LAT, LON, '#3B0B39', size=40, marker=True)

print gmap.geocode("40 King St West, Toronto")

gmap.draw("mymap.html")
