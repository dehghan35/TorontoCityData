# Imported Libraries:
import gmplot
#######################################
class NearMe:

    def __init__(self,input_MyLocation):
        print "-------------------------------------------"
        print "Initializing the Near Me Object . . ."

        # Initializing the location based on Toronto's Long/Lat and city zoom
        self.MyLocation = gmplot.GoogleMapPlotter(43.653908,-79.384293,10);
        self.MyLatLong = [];
        # Check the type of the input object and set the Lat/Long for that location
        if(isinstance(input_MyLocation, basestring)):
            self.MyLatLong = self.MyLocation.geocode("40 King St West, Toronto");
        elif(isinstance(input_MyLocation, list)):
            if():
                self.MyLatLong = input_MyLocation;
            else:
                print "The Lat/Long you have inputted is not correct!"
                exit(1);
        else:
            print "You must either enter a long/lat or an address . . .";
            exit(1);










    # End Of File
