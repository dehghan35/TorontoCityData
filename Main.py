import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import gmplot

conn = sqlite3.connect('./Data/TransitData.db')
c = conn.cursor()
c.execute("Select stop_lat,stop_lon From stops Where stop_id in (Select stop_id From stop_times Where trip_id = '34597099')");
AA = c.fetchall();

LAT = [];
LON = [];
for i in range(0,len(AA)):
    LAT.append(AA[i][0]);
    LON.append(AA[i][1]);

gmap = gmplot.GoogleMapPlotter(LAT[0], LON[1], 16)
gmap.plot(LAT, LON, 'cornflowerblue', edge_width=10)
gmap.scatter(LAT, LON, '#3B0B39', size=40, marker=False)


gmap.draw("mymap.html")
