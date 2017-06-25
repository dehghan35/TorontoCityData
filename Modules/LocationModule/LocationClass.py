########################### Location Class
########################### By: Ash Dehghan
########################### Date: 2017-05-30
# Imported Libraries:
import gmplot
import math
###########################
class LocationClass:

    def __init__(self):
        # Initializing the location based on Toronto's Long/Lat and city zoom
        self.GMPlotObject = gmplot.GoogleMapPlotter(43.653908,-79.384293,10);
        self.RadiusOfEarth = 6373.0;
        self.PI = 3.14159265359;

    ############################################################################
    def LocationConverter(self,input_location):
        Response = {};
        Status = False;
        Value = [None,None];
        ErrorMsg = None;
        if(isinstance(input_location, basestring)):
            try:
                Value = self.GMPlotObject.geocode(input_location);
                Status = True;
            except Exception as e:
                ErrorMsg = str(e);

        Response["Status"] = Status;
        Response["Value"] = Value;
        Response["ErrorMsg"] = ErrorMsg;
        return Response;
    ############################################################################

    ############################################################################
    def DistanceCalculater(self,input_PrimaryLocation,input_SecondaryLocations):
        Response = {};
        Status = False;
        Value = [];
        ErrorMsg = None;
        try:
            for i in range(0,len(input_SecondaryLocations)):
                TempList = [];
                lat1 = input_PrimaryLocation[0];
                lon1 = input_PrimaryLocation[1];
                lat2 = input_SecondaryLocations[i][0];
                lon2 = input_SecondaryLocations[i][1];

                dlon = lon2 - lon1;
                dlat = lat2 - lat1;
                a = (math.sin(dlat/2))**2 + math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2))**2
                c = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a) )
                d = self.RadiusOfEarth * c;

                # dLat = (lat2-lat1)*(self.PI/180);
                # dLon = (lon2-lon1)*(self.PI/180);
                # a = math.sin(dLat/2.0)*math.sin(dLat/2.0)+math.cos(lat1*(self.PI/180.0))*math.cos(lat2*(self.PI/180.0))*math.sin(dLon/2.0)*math.sin(dLon/2.0);
                # c = 2.0* math.atan2(math.sqrt(a),math.sqrt(1.0-a));
                # d = self.RadiusOfEarth*c;


                TempList.append(input_PrimaryLocation);
                TempList.append(input_SecondaryLocations[i]);
                TempList.append(d);
                Value.append(TempList);
            Status = True;
        except Exception as e:
             ErrorMsg = str(e);

        Response["Status"] = Status;
        Response["Value"] = Value;
        Response["ErrorMsg"] = ErrorMsg;
        return Response;
    ############################################################################

     ############################################################################
    def NumberAndDensityCalculater(self,input_PrimaryLocation,input_SecondaryLocations,input_Radius):
         Response = {};
         Status = False;
         Value = [None,None];
         ErrorMsg = None;
         print "Hello"

         FuncResponse = self.DistanceCalculater(input_PrimaryLocation,input_SecondaryLocations);
         print FuncResponse["Value"][0];
         exit(1);
         # Calculate the distance between the origin and all the latlong in the list

     ############################################################################


    # ############################################################################
    # def ClosestToLocationX(self,input_LocationX,input_ListOfLocations):
    #     Response = {};
    #     status = False;
    #     Value = [None,None];
    #     ErrorMsg = None;
    # ############################################################################










    # End Of File
