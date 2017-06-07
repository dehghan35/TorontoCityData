########################### Location Class
########################### By: Ash Dehghan
########################### Date: 2017-05-30
# Imported Libraries:
import gmplot
###########################
class LocationClass:

    def __init__(self):
        # Initializing the location based on Toronto's Long/Lat and city zoom
        self.GMPlotObject = gmplot.GoogleMapPlotter(43.653908,-79.384293,10);
        self.RadiusOfEarth = 6371;

    ############################################################################
    def LocationConverter(self,input_location):
        Response = {};
        status = False;
        Value = [None,None];
        ErrorMsg = None;
        if(isinstance(input_location, basestring)):
            try:
                Value = self.GMPlotObject.geocode(input_location);
                status = True;
            except Exception as e:
                ErrorMsg = str(e);

        Response["status"] = status;
        Response["Value"] = Value;
        Response["ErrorMsg"] = ErrorMsg;
        return Response;
    ############################################################################


    # ############################################################################
    # def DistanceCalculater(self,input_PrimaryLocation,input_SecondaryLocations):
    #     Response = {};
    #     status = False;
    #     Value = [];
    #     ErrorMsg = None;
    #     for i in range(0,len(input_SecondaryLocations)):
    #         print input_SecondaryLocations(i);
    # ############################################################################

    # ############################################################################
    # def DensityCalculater(self,input_PrimaryLocation,input_SecondaryLocations,input_Radius):
    #     Response = {};
    #     status = False;
    #     Value = [None,None];
    #     ErrorMsg = None;
    # ############################################################################
    #
    # ############################################################################
    # def ClosestToLocationX(self,input_LocationX,input_ListOfLocations):
    #     Response = {};
    #     status = False;
    #     Value = [None,None];
    #     ErrorMsg = None;
    # ############################################################################








    # End Of File
