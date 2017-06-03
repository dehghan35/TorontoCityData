
# External Libraries and Modules
import matplotlib.pyplot as plt
import numpy as np
import gmplot
#######################################
# Adding the Classes path to sys path, to import classes/packages
import sys
sys.path.insert(0, "./Utility")
sys.path.insert(0, "./Modules/NearMeModule")
sys.path.insert(0, "./Modules/LocationModule")
sys.path.insert(0, "./Modules/POIModule")
#######################################
# Internal Classes and Modules
from IO import IO
from NearMe import NearMe
from LocationClass import LocationClass;
from SchoolClass import SchoolClass;
#######################################
#
#

school = SchoolClass('1');
print school.x;

school = SchoolClass('2');
print school.x;

# LocationObject = LocationClass();
# print LocationObject.LocationConverter("oiwjeoifjwojef");
