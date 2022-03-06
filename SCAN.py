# #!pip install --upgrade metpy
# #!pip install netCDF4
import xarray as xr
import pandas as pd

nc_files_array = []  #
nc_file_names = []  #

print("Enter Dataset Year [start yaer, end year]")
start_year = int(input("Start Year: 2012"))
end_year = int(input("End Year: 2013"))

#print("Enter Months to be included separated by comma e.g 1,2,3,4")
print("January")
months = input("1,2")
months = list(months)

dname = "temperature"

print("1. Salt Data, 2 Temp Data 3. ice_force 4. Ocean_eta_t 5. Ocean Force 6. Ocean Temp")
choice = int(input("Choice 2"))
print(choice)

if choice == 1:
    dname = "ocean_salt_"
elif choice == 2:
    dname = "ocean_temp_"
elif choice == 3:
    dname = "ice_force_"
elif choice == 4:
    dname = "ocean_eta_t_"
elif choice == 5:
    dname = "ocean_force_"
elif choice == 6:
    dname = "atm_flux_diag_"
else:
    print("Illegal Choice")
    exit()

year_array = []
year_list = []
while start_year <= end_year:
    year_list.append(start_year)
    start_year = start_year + 1

print(year_list)

for year in year_list:
    print("Year " + str(year))
    year_array.append(str(year))
    month = 0
year = str(year)
for month in months:
    month = int(month)
    if month > 9:
        year_name = year + "_"
else:
    year_name = year + "_0"

temp = year_name + str(month)
remote_path = "https://dapds00.nci.org.au/thredds/fileServer/gb6/BRAN/BRAN_2016/OFAM/" + dname + "" + temp + ".nc"
file_name = "atm_flux_diag_" + temp + ".nc"
nc_files_array.append(remote_path)
nc_file_names.append(file_name)
print("Created URL " + remote_path)
print("Created File Name " + file_name)
temp = ""
year_name = ""
month = month + 1

file_name="20110101032000-ABOM-L3S_GHRSST-SSTskin-AVHRR_D-6d_night.nc"
remote_path="http://thredds.aodn.org.au/thredds/catalog/IMOS/SRS/SST/ghrsst/L3S-6d/ngt/2011/20110101032000-ABOM-L3S_GHRSST-SSTskin-AVHRR_D-6d_night.nc"
 #"/thredds/fileServer/IMOS/SRS/SST/ghrsst/L3S-6d/ngt/2011/20110101032000-ABOM-L3S_GHRSST-SSTskin-AVHRR_D-6d_night.nc"

import urllib
nc_files_array.append(remote_path)
nc_file_names.append(file_name)
print("Created URL " + remote_path)
print("Created File Name " + file_name)

nc_files_array

# +
pole=nc_files_array[0]
#pole2=nc_files_array[1]

string_list = list(pole)
string_list[-7] = "6"
new_string = "".join(string_list)

#string_list2 = list(pole2)
#string_list2[-7] = "6"
#new_string2 = "".join(string_list2)
print(new_string+'\n')#+new_string2)
# -



# +
file_index = 0
print("Retriving file from " + nc_files_array[file_index])
urllib.request.urlretrieve(nc_files_array[file_index], nc_file_names[file_index])

ds = xr.open_dataset(nc_file_names[file_index])
df = ds.to_dataframe()
df.to_csv(nc_file_names[file_index] + '.csv')
# -

nc_file_names

file_index = 0
for year in year_list:
    counter = 0
print("Year ==>" + str(year))
while counter < 1:
    print("Retriving file from " + nc_files_array[file_index])
    urllib.request.urlretrieve(nc_files_array[file_index], nc_file_names[file_index])

    ds = xr.open_dataset(nc_file_names[file_index])
    df = ds.to_dataframe()
    df.to_csv(nc_file_names[file_index] + '.csv')
    counter = counter + 1
file_index = file_index + 1



## convertion part
""
for dataset_file in nc_file_names:
    print("Current File "+dataset_file)
    ds = xr.open_dataset(dataset_file)
    df = ds.to_dataframe()
    df.to_excel(dataset_file+'.csv',sheet_name='Sheet_name_1')

# +
import netCDF4 as nc
fn = 'ocean_salt_2016_02.nc'
ds = nc.Dataset(fn)

from matplotlib import pyplot as plt
import netCDF4

url='https://dapds00.nci.org.au/thredds/fileServer/gb6/BRAN/BRAN_2016/OFAM/atm_flux_diag_2016_01.nc'
vname = 'Tx_1211'
station = 0

nc = netCDF4.Dataset(url)
h = nc.variables[vname]
times = nc.variables['time']
jd = netCDF4.num2date(times[:],times.units)
hs = pd.Series(h[:,station],index=jd)

fig = plt.figure(figsize=(12,4))
ax = fig.add_subplot(111)
hs.plot(ax=ax,title='%s at %s' % (h.long_name,nc.id))
ax.set_ylabel(h.units)

ds = xr.open_dataset(r'ocean_salt_2016_02.nc')
df = ds.to_dataframe()
df.to_csv(nc_file_names[file_index] + '.csv')
#counter = counter + 1
