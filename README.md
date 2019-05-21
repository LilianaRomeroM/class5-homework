# class5-homework

This homework is only a testing of matplotlib library graphics (and 1 short Seaborn test), using the Diabetes dataset.

Dataset
Dataset used in this homework is part of Scikit-learn datasets (toydatasets)
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes

Files included in this repository

Code:  
dataset-processor.py

Dataset:  
diabetes.csv

Graphics:
Folder: diabetesplots
Note: Some files in this folder have information not related/applicable to this dataset, since they are created only for testing purposes.  In addition, they are provided only for information; the code includes the creation of the same directory during execution.

Install:

Supported Python3 version

Libraries imported for this exercise:

•	os
•	numpy
•	pandas
•	matplotlib.pyplot
•	seaborn
•	time

Code:  

The code used in this homework is inside dataset-processor.py

How to Run:

To run this homework it is recommended to use Anaconda, which provides support for executing .py files in a friendly-user enviro (Spyder-Jupyter Notebook).
In order to run the code, you can:
1)	Download the diabetes.csv file included in the repository and send it to your Desktop, or
2)	You can move the diabetes.csv to another folder; if you do so, you need to edit the line 9 on the .py file, in order to appropriately locate your .csv file path.


diabetes_df=pd.read_csv(filepath_or_buffer='~/Desktop/diabetes.csv',
                         sep=',',
                         header=0)


After making sure you have this defined, you can run the file from your editor or terminal.


License

MIT License
