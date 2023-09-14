import matplotlib.pyplot as plt
import sqlite3
import datetime
connection = sqlite3.connect('climate.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM ClimateData")
results = cursor.fetchall()
# Check results - database table
print(results)

years = []
co2 = []
temp = []

for result in results:
    years.append(result[0])
    co2.append(result[1])
    temp.append(result[2])
# Check arrays
print('years: ', years, 'co2: ', co2, 'temp: ', temp)


# years = []
# co2 = []
# temp = []

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)")
# CORRECTION MADE: Change order to perform save action
plt.savefig("co2_temp_1.png")
plt.show() 

