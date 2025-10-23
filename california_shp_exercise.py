import os
import matplotlib.pyplot as plt
import geopandas as gpd

fp = os.path.join('data','gbif_sus_scrofa_california')
fp
 
#looking at the data in pigs
pigs = gpd.read_file(fp)
pigs.head()

# Check in #1
#importing the shapefile
shp_file = os.path.join('data','ca_state_boundary')
cali = gpd.read_file(shp_file)

#checking type of data of pigs
print(type(pigs))

#checking the data type of the geom column
print(type(pigs.geometry))

#check the data type of the gbifID column
print(type(pigs.gbifID))

#check the data type of each column
print(pigs.dtypes)

#check-in number #2
print(type(cali))

#access the CRS of the GeoDataframe
pigs.crs

# Examine CRS details
print('Ellipsoid: ', pigs.crs.ellipsoid)
print('Datum: ', pigs.crs.datum)
print('Is geographic?: ', pigs.crs.is_geographic)
print('Is projected?: ', pigs.crs.is_projected)

# Obtain the geographic extent of the geo-dataframe
pigs.total_bounds

# check-in #3
# crs
cali.crs
# extent
cali.total_bounds

### Data Wrangling

# examine pig observation by year
pigs['year'].value_counts().sort_index()

# select data from 2020 onwards
pigs_recent = pigs[pigs['year'] >= 2020]
pigs_recent

# check the length of the og dataframe
print("total number of observations: ", len(pigs))

# check length of the recent dataframe
print("total number of pig obervations since 2020 onwards ", len(pigs_recent))

pigs_recent.plot()


# Initialize empty figure (fig) and axis (ax)
fig, ax = plt.subplots()

# Display figure
plt.show()