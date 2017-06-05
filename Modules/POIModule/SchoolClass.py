########################### School Class
########################### By: Ash Dehghan
########################### Date: 2017-06-03
# Imported Libraries:
from POIParentClass import POIParentClass;
from IO import IO;
from LocationClass import LocationClass;
###########################

class SchoolClass(POIParentClass):

    ###################################################### Define the Properties
    Name = None;
    Origin = None;
    RadiusFromOrigin = None;
    DensityWithinRadius = None;
    NumberWithinRadius = None;
    ClosestToOrigin = None;
    ############################################################################

    ############################################################################
    def __init__(self,input_LocationLonLat,input_Radius):
        ############################################## Get Config Data
        with open("./Config/DataBasePathName.txt") as f:
            content = f.readlines();
        content = [x.strip() for x in content];
        DataBasePath = content[0];
        ############################################## Utility:
        self.DataBase = IO();
        self.Location = LocationClass();
        self.DataBase.DataIO_DataBase(DataBasePath);
        ############################################## Get all data once
        Query = "Select * From school;";
        self.AllData  = self.DataBase.DataBase_Select_ReturnAll(Query);
        ############################################## Set Object Properties
        self.SetName('school');
        self.SetOrigin(input_LocationLonLat);
        self.SetRadiusFromOrigin(input_Radius);
        self.SetDensityWithinRadius(self.RadiusFromOrigin);
    ############################################################################


    ############################################################################
    def SetName(self,input_Name):
        self.Name = input_Name;
    ############################################################################

    ############################################################################
    def SetOrigin(self,input_LocationLonLat):
        self.Origin = input_LocationLonLat;
    ############################################################################

    ############################################################################
    def SetRadiusFromOrigin(self,input_Radius):
        self.RadiusFromOrigin = input_Radius;
    ############################################################################

    ############################################################################
    def SetDensityWithinRadius(self,self_RadiusFromOrigin):
        # Get data from database on all SchoolClass
        pass;
    ############################################################################

    ############################################################################
    def SetNumberWithinRadius(self):
        pass;

    ############################################################################

    ############################################################################
    def SetClosestToOrigin(self):
        pass;

    ############################################################################






    # End
