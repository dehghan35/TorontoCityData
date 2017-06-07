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
        ############################################## Parse Data
        self.school_Internal_ID = [];
        self.school_Name = [];
        self.school_Address = [];
        self.school_PostalCode = [];
        self.school_LatLon = [];
        self.school_Municipality = [];
        self.school_City = [];
        self.ParseData();
        ############################################## Set Object Properties
        self.SetName('school');
        self.SetOrigin(input_LocationLonLat);
        self.SetRadiusFromOrigin(input_Radius);
        self.SetNumberAndDensityWithinRadius();
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
    def SetNumberAndDensityWithinRadius(self):
        # Extract the lat and long from the data
        print self.school_Name[0];
        pass;
    ############################################################################

    ############################################################################
    def SetClosestToOrigin(self):
        pass;

    ############################################################################

    ############################################################################
    def ParseData(self):
        for i in range (0,len(self.AllData)):
            self.school_Internal_ID.append(i);
            self.school_Name.append(self.AllData[i][0]);
            self.school_Address.append(self.AllData[i][1]);
            self.school_PostalCode.append(self.AllData[i][2]);
            self.school_Municipality.append(self.AllData[i][3]);
            self.school_City.append(self.AllData[i][4]);
            self.school_LatLon.append([self.AllData[i][5],self.AllData[i][6]]);



    ############################################################################


    # End
