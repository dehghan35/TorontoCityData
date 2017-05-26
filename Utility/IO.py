# Imported Libraries:
import pandas as pd
import sqlite3
#######################################
class IO:

    def __init__(self):
        print "-------------------------------------------"
        print "Initializing the IO class."
        self.DataBaseNamePath = "";
        self.DataBaseConnection = None;

    # This method takes in a path/name to a csv file and uses pandas to read the file.
    # Input: String, file name/path, (ex: ./Data/ABC.csv)
    # Output: Dataframe
    def DataIO_CSV(self,input_FilePath):
        try:
            return pd.read_csv(input_FilePath, sep=',');
        except Exception as e:
            print "Error while reading the csv file!"
            exit(1);

    # This method takes in the path/name to a database and set the object database connection, else if it can not, it will exit with error.
    # Input: String, Database name and path (ex: ./Data/DataBase.db)
    def DataIO_DataBase(self,input_DataBaseNamePath):
        print "-------------------------------------------"
        print "Setting up the database object."
        self.DataBaseNamePath = input_DataBaseNamePath;
        try:
            self.DataBaseConnection = sqlite3.connect(self.DataBaseNamePath).cursor();
        except Exception as e:
            print "Unable to connect to the database!";
            exit(1);

    # This method will take in generic query and excecutes it and retruns all the results.
    # Input: String, query (ex: Select * From TableA)
    # Output: List
    def DataBase_Select_ReturnAll(self,input_Query):
        print "-------------------------------------------"
        print "Making a 'Select' query."
        Query = input_Query;
        try:
            self.DataBaseConnection.execute(Query);
            return self.DataBaseConnection.fetchall();
        except Exception as e:
            print "Error while excecuting the query!"
            exit(1);












    # End Of File
