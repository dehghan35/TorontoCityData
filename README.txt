+++++++++++++++++++++++++++++
Ash Dehghan [2017-05-23]
+++++++++++++++++++++++++++++

+++++++++++++++++++++++++++++
Getting Requirements:
+++++++++++++++++++++++++++++
To install the dependencies, do the following:
- On Mac/Linux: sudo pip install -r requirements.txt
- Windows: Open terminal in admin mode and then type: pip install -r requirements.txt
Packages such as:
- numpy
- sqlite3
should already come with your Python install, if not install them manually using pip.


+++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++
  Class/Method Descriptions
+++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++

Location Class [LocationClass]

Location Convertor [LocationConvertor] (input_location)

Input: The input can be either a text string format of address, or a list of two elements, indicating a longitude/ Latitude. Ex: "123 Main St. West, Toronto" Or [23.1234,-65.32].

Output: An object with 3 elements.
			1- True/False indicating the method success.
			2- If True, the text format of address. If false, None.
			3- If True, a list of Long/Lat. If false, None.

Description: It converts lat/long to text address and text address into lat/long


Distance Calculator [DistanceCalculator]

Input: The input takes the format ([log,lat] ,[[long,lat],[long,lat],[long,lat]...]). The first element is the location everything is measured with respect to. The second list will contain a list of longitude/latitude.

Output: List of location 1, location 2, and distance between them.

Description: It calculates the distance between two points, or a single point and a list of points. It requires the locations to be in lat/long format. Distance is calculated in kilometers.


Density Calculator [DensityCalculator]

Input: The inputs are [long,lat] of main location, list of [long,lat] of secondary locations, and the radius in kilometers, within which we want to measure density.

Output: It returns a 4 elements object.
			1- True/False indicating the method success.
			2- If True, the Density. If False, None.
			3- If True, total number of objects. If False, None.
			4- If True, the area. If False, None.

Description: It calculates the density of the objects within a area.


Mapper

Input:

Output:

Description:



Near Me Class [NearMeClass]

Feature Builder
Report
Metric

Feature Class [FeatureClass]

Closest
Density In Radius X
Total Number In Radius X

School Class [SchoolClass] {Parent: FeatureClass} ** Implements all  FeatureClass methods

List All Schools
