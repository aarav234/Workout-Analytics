# ==============importing libraries==================
import numpy as np
import matplotlib.pyplot as plt 
import numpy as np
from datetime import datetime
import pandas as pd

# ==============opening file========================= 
file = open("my_workout.txt", "r")
lst = file.readlines()

# ===============Required Variables==================
bestSet = {}
volumeDict = {}
chest = {}
legs = {}
shoulders = {}
arms = {}
back = {}
# ===================================================


for i in range(len(lst)):
    lst[i] = lst[i].rstrip()
for i in range(len(lst)):
    if lst[i].lower().__contains__("in"):
        j = i+1
        try:
            while not lst[j].lower().__contains__("in"):
                index = lst[j].find("*") 
                repIndex = index - 2
                weightIndex = index + 2
                try:
                    # =============Converting pounds to kgs==============
                    if lst[i].lower().__contains__("pounds"):
                        index = lst[j].find("*") + 2
                        weightInPounds = int(lst[j][weightIndex:])
                        weightInKgs = str(int(weightInPounds*0.453592))
                        lst[j] = lst[j][:weightIndex] + weightInKgs
                    # ===================================================
                    # ==============Finding the best set of each workout=============
                    maxvalue = 0
                    indexOfIn = lst[i].lower().find('in ')
                    if lst[i][:indexOfIn] in list(bestSet.keys()):
                        maxvalue = bestSet.get(lst[i][:indexOfIn])

                    if not lst[j].lower().__contains__("warm up"):
                        reps = int(lst[j][:(repIndex + 1)])
                        weight = int(lst[j][weightIndex:])
                        if weight > maxvalue:
                            maxvalue = weight
                except ValueError:
                    pass
                
                bestSet[lst[i][:indexOfIn]] = maxvalue

                # ===============================================================
                j += 1
        except IndexError:
            pass

for i in range(len(lst)):
    # ====================Finding date====================
    if lst[i].__contains__("/"):
    # ====================================================
        j = i+1
        volume = 0
        while True:
            try:
                if lst[j].__contains__("/"):
                    break
                # =================Finding all workout lines in code==================
                if lst[j].__contains__("*"):
                # ====================================================================

                # ===============Finding reps and weight =============================
                    index = lst[j].find("*") 
                    repIndex = index - 2
                    weightIndex = index + 2
                    if lst[j].lower().__contains__("warm"):
                        reps = int(lst[j][10:(repIndex + 1)])
                    else:
                        reps = int(lst[j][:(repIndex + 1)])
                    weight = float(lst[j][weightIndex:])
                # =====================================================================
                    product = reps * weight
                    volume += product

            except IndexError:
                break
            finally:
                j += 1
        # ===============Assigning to volume dict =====================================
        volumeDict[lst[i]] = [lst[i+1], volume]
        # =============================================================================

        if lst[i+1].lower().__contains__("chest"):
            chest[lst[i]] = volume
        elif lst[i+1].lower().__contains__("shoulder"):
            shoulders[lst[i]] = volume
        elif lst[i+1].lower().__contains__("back"):
            back[lst[i]] = volume
        elif lst[i+1].lower().__contains__("leg"):
            legs[lst[i]] = volume
        else:
            arms[lst[i]] = volume

# =================creating the Best Set bar plot=====================

exercise = list(bestSet.keys())
weight = list(bestSet.values())
  
fig = plt.figure(figsize = (20, 10))

p1 = plt.bar(exercise, weight, color ='maroon', 
        width = 0.3)
 
plt.xlabel("Type of exercise")
plt.ylabel("Weight")
plt.title("Best set")
plt.xticks(fontsize = 4)
plt.bar_label(p1, fontsize = 10)
plt.show()
# =====================================================================

# ========================creating Volume over time plot====================
date = list(volumeDict.keys())
excercise_type = [i[0] for i in list(volumeDict.values())]
vol = [i[1] for i in list(volumeDict.values())]

p1 = plt.plot(date, vol)

plt.xlabel("Date")
plt.ylabel("Volume")
plt.title("Volume Lifted")

for i, (xi, yi) in enumerate(zip(date, vol)):
    plt.annotate(excercise_type[i], (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center', fontsize = "10")
plt.show()
#  =========================================================================

# ==================Creating volume per excercise day analytic ========================
format = '%d/%m/%Y'
chest_date = [datetime.strptime(i, format).date() for i in list(chest.keys())]
chest_vol = list(chest.values())
legs_date = [datetime.strptime(i, format).date() for i in list(legs.keys())]
legs_vol = list(legs.values())
arms_date = [datetime.strptime(i, format).date() for i in list(arms.keys())]
arms_vol = list(arms.values())
shoulders_date = [datetime.strptime(i, format).date() for i in list(shoulders.keys())]
shoulders_vol = list(shoulders.values())
back_date = [datetime.strptime(i, format).date() for i in list(back.keys())]
back_vol = list(back.values())

dataframe1 = pd.DataFrame({'date_of_week': chest_date,
                          'volume': chest_vol})
dataframe2 = pd.DataFrame({'date_of_week': legs_date,
                          'volume': legs_vol})
dataframe3 = pd.DataFrame({'date_of_week': back_date,
                          'volume': back_vol})
dataframe4 = pd.DataFrame({'date_of_week': arms_date,
                          'volume': arms_vol})
dataframe5 = pd.DataFrame({'date_of_week': shoulders_date,
                          'volume': shoulders_vol})



plt.plot(dataframe1.date_of_week, dataframe1.volume, dataframe2.date_of_week, dataframe2.volume, dataframe3.date_of_week, dataframe3.volume, dataframe4.date_of_week, dataframe4.volume, dataframe5.date_of_week, dataframe5.volume)

# Giving title to the chart using plt.title
plt.title('Exercise volume by Date')

# Formatting x-axis tick labels
plt.xticks(rotation=30, ha='right')
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d/%m/%Y'))

for i, (xi, yi) in enumerate(zip(chest_date, chest_vol)):
    plt.annotate(yi, (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center', fontsize = "10")
for i, (xi, yi) in enumerate(zip(legs_date, legs_vol)):
    plt.annotate(yi, (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center', fontsize = "10")
for i, (xi, yi) in enumerate(zip(back_date, back_vol)):
    plt.annotate(yi, (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center', fontsize = "10")
for i, (xi, yi) in enumerate(zip(arms_date, arms_vol)):
    plt.annotate(yi, (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center', fontsize = "10")
for i, (xi, yi) in enumerate(zip(shoulders_date, shoulders_vol)):
    plt.annotate(yi, (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center', fontsize = "10")

plt.legend(["chest", "legs", "back", "arms", "shoulders"])

# Providing x and y label to the chart
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()
# =====================================================================================
# ================closing file====================
file.close()
# ================================================
