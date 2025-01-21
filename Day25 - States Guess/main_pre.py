"""This would be a way to do it, but painful, as it is a list with comas etc... dirty data"""

#with open("weather_data.csv") as weather_csv:
#    data = weather_csv.readlines()
#    print(data)

"""import csv

with open("weather_data.csv") as weather_csv:
    data = csv.reader(weather_csv) #Create an object csv
    #print(data)   This shows the object created from csv.reader
    temperatures = []
    for row in data:
        temp = (row[1])
        if row[1] != "temp":
        #print(temp)
            temperatures.append(int(temp))

print(temperatures)"""



import pandas
"""same as above, but much easier with pandas!"""
data = pandas.read_csv("weather_data.csv")
#print(type(data))   #it will be <class 'pandas.core.frame.DataFrame'>
temp_list = (data["temp"]).to_list()
average = (data["temp"]).mean() #easier version, with methods
maximum = (data["temp"]).max() #easier version, with methods
#print(average)
#print(maximum)


"""converting the data csv to a dictionary objct"""
data_dict = data.to_dict()
#print(data_dict)

"""#what about get a hold of a row? first hols all the data table:
data[]
#search trought the column you want to search trought
data[data.temp]
#now, inside that column, want to check for the value == X"""
#print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
mondays_temp = monday.temp
#print((mondays_temp * 9/5) + 32)

"""Create a DataFrame from Scratch"""

#TODO - find the number of squirrels of each color   Gray, Cinnamon and Black   Column, Primary Fur Color
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")
squirrel_colors = squirrel_data["Primary Fur Color"]
total_colors = squirrel_colors.value_counts()
total_colors.to_csv("Squirrel_color_count.csv")




