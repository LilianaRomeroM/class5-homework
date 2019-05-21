import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

#creating Dataframe from Files
diabetes_df=pd.read_csv(filepath_or_buffer='~/Desktop/diabetes.csv',
                         sep=',',
                         header=0)
print(diabetes_df)
time.sleep(2)
print(diabetes_df.columns)
time.sleep(2)
print(diabetes_df.dtypes)
time.sleep(2)
print(diabetes_df.shape)
time.sleep(2)
print(diabetes_df.info())
time.sleep(2)
print(diabetes_df.describe())
time.sleep(2)
print(diabetes_df.corr())# -*- coding: utf-8 -*-
time.sleep(2)
plt.matshow(diabetes_df.corr())
plt.xticks(range(len(diabetes_df.columns)), diabetes_df.columns)
plt.yticks(range(len(diabetes_df.columns)), diabetes_df.columns)
plt.colorbar()
plt.show()
# Basic correlogram
sns.pairplot(diabetes_df)
plt.show()


os.makedirs('diabetesplots', exist_ok=True)

# Plotting line chart
plt.style.use("ggplot")
plt.plot(diabetes_df['BP'], color='blue', marker='o')
plt.title('BLOOD PRESSURE RANGE\nInitial info')
plt.xlabel('Samples')
plt.ylabel('Blood Pressure')
plt.savefig(f'diabetesplots/BP_to_see_plot.png', format='png')
plt.clf()

# Plotting TWO lines chart
fig, ax= plt.subplots()
ax.plot(diabetes_df.index, diabetes_df["BMI"], color='blue')
ax.set_xlabel("Samples")
ax.set_ylabel("Body Mass Index", color='blue')
ax.tick_params('y', colors='blue')
ax2 = ax.twinx()
ax2.plot(diabetes_df.index, diabetes_df['Y'], color='green')
ax2.set_ylabel('Diabetes progression after 1 year', color='green')
ax2.tick_params('y', colors='green')
ax.set_title('Body Mass Index and Diabetes progression')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/BMI_vs_Y_plot.png', format='png')
plt.clf()

# Plotting histogram
plt.hist(diabetes_df['AGE'], bins=10, histtype='bar', rwidth=0.6, color='b')
plt.title('AGE RANGE')
plt.xlabel('AGE')
plt.ylabel('COUNT')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/AGE_hist.png', format='png')
plt.clf()

#Plotting scatter with DataCamp tehcnique
fig, ax= plt.subplots()
ax.scatter(diabetes_df["AGE"], diabetes_df["Y"], c=diabetes_df.index)
ax.set_xlabel("AGE OF PATIENT")
ax.set_ylabel("DIABETES PROGRESSION AFTER 1 YEAR")
ax.set_title('AGE AND DIABETES PROGRESSION -1 YEAR-')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/AGEDC_vs_Y_scatter.png', format='png')
plt.clf()

#Plotting scatter with DataCamp tehcnique
fig, ax= plt.subplots()
ax.scatter(diabetes_df["S2"], diabetes_df["S4"], c=diabetes_df.index)
ax.set_xlabel("ldl")
ax.set_ylabel("tch")
ax.set_title('LDL AND TCH CORRELATION')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/LDL_TCH CORR.png', format='png')
plt.clf()


# Plotting scatterplot
plt.scatter(diabetes_df['AGE'], diabetes_df['Y'], color='b', marker='x', s=10)
plt.title('AGE AND DIABETES PROGRESSION -1 YEAR-')
plt.xlabel('AGE')
plt.ylabel('DIABETES PROGRESSION')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/progression_AGE.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(diabetes_df['AGE'], diabetes_df['SEX'], color='b', marker='v', s=10)
plt.title('AGE AND GENRE CORRELATION')
plt.xlabel('AGE')
plt.ylabel('GENRE')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/CORR_AGE_GENRE.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(diabetes_df['SEX'], diabetes_df['Y'], color='g')
plt.title('GENRE AND DIABETES PROGRESSION -1 YEAR-')
plt.xlabel('SEX')
plt.ylabel('DIABETES PROGRESSION')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/progression_SEX.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(diabetes_df['BMI'], diabetes_df['Y'], color='g')
plt.title('BODY MASS INDEX AND DIABETES PROGRESSION -1 YEAR-')
plt.xlabel('BMI')
plt.ylabel('DIABETES PROGRESSION')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/progression_BMI.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(diabetes_df['BP'], diabetes_df['Y'], color='g')
plt.title('BLOOD PRESSURE AND DIABETES PROGRESSION -1 YEAR-')
plt.xlabel('BP')
plt.ylabel('DIABETES PROGRESSION')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/progression_BP.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(diabetes_df['S1'], diabetes_df['Y'], color='g')
plt.title('TC AND DIABETES PROGRESSION -1 YEAR-')
plt.xlabel('S1')
plt.ylabel('DIABETES PROGRESSION')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/progression_S1.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(diabetes_df['S2'], diabetes_df['Y'], color='g')
plt.title('LDL AND DIABETES PROGRESSION -1 YEAR-')
plt.xlabel('S2')
plt.ylabel('DIABETES PROGRESSION')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/progression_S2.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(diabetes_df['S3'], diabetes_df['Y'], color='g')
plt.title('HDL AND DIABETES PROGRESSION -1 YEAR-')
plt.xlabel('S3')
plt.ylabel('DIABETES PROGRESSION')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/progression_S3.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(diabetes_df['S4'], diabetes_df['Y'], color='g')
plt.title('TCH AND DIABETES PROGRESSION -1 YEAR-')
plt.xlabel('S4')
plt.ylabel('DIABETES PROGRESSION')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/progression_S4.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(diabetes_df['S5'], diabetes_df['Y'], color='g')
plt.title('LTG AND DIABETES PROGRESSION -1 YEAR-')
plt.xlabel('S5')
plt.ylabel('DIABETES PROGRESSION')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/progression_S5.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(diabetes_df['S6'], diabetes_df['Y'], color='g')
plt.title('GLUCOSE AND DIABETES PROGRESSION -1 YEAR-')
plt.xlabel('S6')
plt.ylabel('DIABETES PROGRESSION')
fig.set_size_inches([8,8])
plt.savefig(f'diabetesplots/progression_S6.png', format='png')
plt.clf()
