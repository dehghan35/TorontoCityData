########################### Point Of Interest (POI) Class
########################### By: Ash Dehghan
########################### Date: 2017-06-03
# Imported Libraries:
from abc import ABCMeta, abstractmethod, abstractproperty
###########################

class POIParentClass:
    __metaclass__ = ABCMeta;

    ###################################################### Abstract Properties
    @abstractproperty
    def Name(self): pass
    @abstractproperty
    def Origin(self): pass
    @abstractproperty
    def RadiusFromOrigin(self): pass
    @abstractproperty
    def DensityWithinRadius(self): pass
    @abstractproperty
    def NumberWithinRadius(self): pass
    @abstractproperty
    def ClosestToOrigin(self): pass


    ###################################################### Abstract Methods
    @abstractmethod
    def __init__(self):pass
    @abstractmethod
    def SetName(self):pass
    @abstractmethod
    def SetOrigin(self):pass
    @abstractmethod
    def SetRadiusFromOrigin(self):pass
    @abstractmethod
    def SetDensityWithinRadius(self):pass
    @abstractmethod
    def SetNumberWithinRadius(self):pass
    @abstractmethod
    def SetClosestToOrigin(self):pass




    # End
