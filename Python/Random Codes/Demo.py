# Import module
from geopy.geocoders import Nominatim
import os
import glob
import pandas as pd
from time import sleep
import reverse_geocoder as rg

# getting folder location input
# Folder_path = input(r'Enter 1st Row CSV Folder Path :: ')

# # read all the files in the folder
# all_files = glob.glob(os.path.join(Folder_path, "1ST ROW FILE CSV*.csv"))
# for file_ in all_files:

#         file_name = file_.split("\\")      # split file name
#         print("Working on File: ",file_name[-1])

#         # read the CSV files
#         df = pd.read_csv(file_, encoding='utf-8', low_memory=False)

#         # Get latitude and longitude from CSV
#         coordinates = list(zip(df['latitude'],df['longitude']))



# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

Latitude = "25.594095"
Longitude = "85.137566"


# Get location with geocode
location = geolocator.reverse(Latitude+","+Longitude, addressdetails=True)

data = location.raw
#print(data)
data = data['address']
address = str(data)
print(address)


# street = district = postalCode= state = country = countryCode = ""

# district    =str(data['state_district'])
# postalCode  =str(data['postcode'])
# state       =str(data['state'])
# country     =str(data['country'])
# countryCode =str(data['country_code']).upper()

# address = street +' '+ district  +' '+  postalCode  +' '+  state  +' '+  country  +' '+  countryCode
# print("Address:",address)
# print("\nLocation of the given Latitude and Longitude:")
# print("All Details: ",location)
