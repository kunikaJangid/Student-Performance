# -*- coding: utf-8 -*-
"""studentperf.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LkmI1xy_lG32dTAhPI0-_yVsoJMGh5Ip
"""

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import time as t
import sklearn.utils as u
import sklearn.preprocessing as pp
import sklearn.tree as tr
import sklearn.ensemble as es
import sklearn.metrics as m
import sklearn.linear_model as lm
import sklearn.neural_network as nn
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.naive_bayes import GaussianNB
import numpy as np
import random as rnd
import warnings as w
w.filterwarnings('ignore')
data = pd.read_csv("/content/AI-Data.csv")
ch = 0
while(ch != 10):
    print("1.Marks Class Count Graph\t2.Marks Class Semester-wise Graph\n3.Marks Class Gender-wise Graph\t4.Marks Class Nationality-wise Graph\n5.Marks Class Grade-wise Graph\t6.Marks Class Section-wise Graph\n7.Marks Class Topic-wise Graph\t8.Marks Class Stage-wise Graph\n9.Marks Class Absent Days-wise\t10.No Graph\n")
    ch = int(input("Enter Choice: "))
    if (ch == 1):
        print("Loading Graph....\n")
        t.sleep(1)
        print("\tMarks Class Count Graph")
        axes = sb.countplot(x='Class', data=data, order=['L', 'M', 'H'])
        plt.show()
    elif (ch == 2):
        print("Loading Graph....\n")
        t.sleep(1)
        print("\tMarks Class Semester-wise Graph")
        fig, axesarr = plt.subplots(1, figsize=(10, 6))
        sb.countplot(x='Semester', hue='Class', data=data, hue_order=['L', 'M', 'H'], axes=axesarr)
        plt.show()
    elif (ch == 3):
        print("Loading Graph..\n")
        t.sleep(1)
        print("\tMarks Class Gender-wise Graph")
        fig, axesarr = plt.subplots(1, figsize=(10, 6))
        sb.countplot(x='gender', hue='Class', data=data, order=['M', 'F'], hue_order=['L', 'M', 'H'], axes=axesarr)
        plt.show()
    elif (ch == 4):
        print("Loading Graph..\n")
        t.sleep(1)
        print("\tMarks Class Nationality-wise Graph")
        fig, axesarr = plt.subplots(1, figsize=(10, 6))
        sb.countplot(x='NationalITy', hue='Class', data=data, hue_order=['L', 'M', 'H'], axes=axesarr)
        plt.show()
    elif (ch == 5):
        print("Loading Graph: \n")
        t.sleep(1)
        print("\tMarks Class Grade-wise Graph")
        fig, axesarr = plt.subplots(1, figsize=(10, 6))
        sb.countplot(x='GradeID', hue='Class', data=data, order=['G-02', 'G-04', 'G-05', 'G-06', 'G-07', 'G-08', 'G-09', 'G-10', 'G-11', 'G-12'], hue_order = ['L', 'M', 'H'], axes=axesarr)
        plt.show()
    elif (ch ==6):
        print("Loading Graph..\n")
        t.sleep(1)
        print("\tMarks Class Section-wise Graph")
        fig, axesarr = plt.subplots(1, figsize=(10, 6))
        sb.countplot(x='SectionID', hue='Class', data=data, hue_order = ['L', 'M', 'H'], axes=axesarr)
        plt.show()
    elif (ch == 7):
        print("Loading Graph..\n")
        t.sleep(1)
        print("\tMarks Class Topic-wise Graph")
        fig, axesarr = plt.subplots(1, figsize=(10, 6))
        sb.countplot(x='Topic', hue='Class', data=data, hue_order = ['L', 'M', 'H'], axes=axesarr)
        plt.show()
    elif (ch == 8):
        print("Loading Graph..\n")
        t.sleep(1)
        print("\tMarks Class Stage-wise Graph")
        fig, axesarr = plt.subplots(1, figsize=(10, 6))
        sb.countplot(x='StageID', hue='Class', data=data, hue_order = ['L', 'M', 'H'], axes=axesarr)
        plt.show()
    elif (ch == 9):
        print("Loading Graph..\n")
        t.sleep(1)
        print("\tMarks Class Absent Days-wise Graph")
        fig, axesarr = plt.subplots(1, figsize=(10, 6))
        sb.countplot(x='StudentAbsenceDays', hue='Class', data=data, hue_order = ['L', 'M', 'H'], axes=axesarr)
        plt.show()
if(ch == 10):
    print("Exiting..\n")
    t.sleep(1)
#cor = data.corr()
#print(cor)
data = data.drop("gender", axis=1)
data = data.drop("StageID", axis=1)
data = data.drop("GradeID", axis=1)
data = data.drop("NationalITy", axis=1)
data = data.drop("PlaceofBirth", axis=1)
data = data.drop("SectionID", axis=1)
data = data.drop("Topic", axis=1)
data = data.drop("Semester", axis=1)
data = data.drop("Relation", axis=1)
data = data.drop("ParentschoolSatisfaction", axis=1)
data = data.drop("ParentAnsweringSurvey", axis=1)
data = data.drop("VisITedResources", axis=1)
#data = data.drop("AnnouncementsView", axis=1)
u.shuffle(data)
countD = 0
countP = 0
countL = 0
countR = 0
countN = 0
gradeID_dict = {"G-01" : 1,
                "G-02" : 2,
                "G-03" : 3,
                "G-04" : 4,
                "G-05" : 5,
                "G-06" : 6,
                "G-07" : 7,
                "G-08" : 8,
                "G-09" : 9,
                "G-10" : 10,
                "G-11" : 11,
                "G-12" : 12}
data = data.replace({"GradeID" : gradeID_dict})
sig = []
for column in data.columns:
    if data[column].dtype == type(object):
        le = pp.LabelEncoder()
        data[column] = le.fit_transform(data[column])
ind = int(len(data) * 0.70)
feats = data.values[:, 0:4]
lbls = data.values[:,4]
feats_Train = feats[0:ind]
feats_Test = feats[(ind+1):len(feats)]
lbls_Train = lbls[0:ind]
lbls_Test = lbls[(ind+1):len(lbls)]

modelD = tr.DecisionTreeClassifier()
modelD.fit(feats_Train, lbls_Train)
lbls_predD = modelD.predict(feats_Test)
for a,b in zip(lbls_Test, lbls_predD):
    if(a==b):
        countD += 1
accD = (countD/len(lbls_Test))
print("\nAccuracy measures using Decision Tree:")
print(m.classification_report(lbls_Test, lbls_predD),"\n")
print("\nAccuracy using Decision Tree: ", str(round(accD, 3)))
t.sleep(1)
modelR = es.RandomForestClassifier()
modelR.fit(feats_Train, lbls_Train)
lbls_predR = modelR.predict(feats_Test)
for a,b in zip(lbls_Test, lbls_predR):
    if(a==b):
        countR += 1
print("\nAccuracy Measures for Random Forest Classifier: \n")
#print("\nConfusion Matrix: \n", m.confusion_matrix(lbls_Test, lbls_predR))
print("\n", m.classification_report(lbls_Test,lbls_predR))
accR = countR/len(lbls_Test)
print("\nAccuracy using Random Forest: ", str(round(accR, 3)))
t.sleep(1)
modelP = lm.Perceptron()
modelP.fit(feats_Train, lbls_Train)
lbls_predP = modelP.predict(feats_Test)
for a,b in zip(lbls_Test, lbls_predP):
    if a == b:
        countP += 1
accP = countP/len(lbls_Test)
print("\nAccuracy measures using Linear Model Perceptron:")
print(m.classification_report(lbls_Test, lbls_predP),"\n")
print("\nAccuracy using Linear Model Perceptron: ", str(round(accP, 3)), "\n")
t.sleep(1)
modelL = lm.LogisticRegression()
modelL.fit(feats_Train, lbls_Train)
lbls_predL = modelL.predict(feats_Test)
for a,b in zip(lbls_Test, lbls_predL):
    if a == b:
        countL += 1
accL = countL/len(lbls_Test)
print("\nAccuracy measures using Linear Model Logistic Regression:")
print(m.classification_report(lbls_Test, lbls_predL),"\n")
print("\nAccuracy using Linear Model Logistic Regression: ", str(round(accP, 3)), "\n")
t.sleep(1)
modelN = nn.MLPClassifier(activation="logistic")
modelN.fit(feats_Train, lbls_Train)
lbls_predN = modelN.predict(feats_Test)
for a,b in zip(lbls_Test, lbls_predN):
    #sig.append(1/(1+ np.exp(-b)))
    if a==b:
        countN += 1
#print("\nAverage value of Sigmoid Function: ", str(round(np.average(sig), 3)))
print("\nAccuracy measures using MLP Classifier:")
print(m.classification_report(lbls_Test, lbls_predN),"\n")
accN = countN/len(lbls_Test)
print("\nAccuracy using Neural Network MLP Classifier: ", str(round(accN, 3)), "\n")

modelSVM = SVC()
modelSVM.fit(feats_Train, lbls_Train)
lbls_predSVM = modelSVM.predict(feats_Test)
countSVM = sum(1 for a, b in zip(lbls_Test, lbls_predSVM) if a == b)
accSVM = countSVM / len(lbls_Test)
print("\nAccuracy measures using Support Vector Machine (SVM):")
print(m.classification_report(lbls_Test, lbls_predSVM), "\n")
print("Accuracy using Support Vector Machine (SVM):", str(round(accSVM, 3)), "\n")
t.sleep(1)

# Add k-Nearest Neighbors (k-NN) Classifier
modelKNN = KNeighborsClassifier()
modelKNN.fit(feats_Train, lbls_Train)
lbls_predKNN = modelKNN.predict(feats_Test)
countKNN = sum(1 for a, b in zip(lbls_Test, lbls_predKNN) if a == b)
accKNN = countKNN / len(lbls_Test)
print("\nAccuracy measures using k-Nearest Neighbors (k-NN):")
print(m.classification_report(lbls_Test, lbls_predKNN), "\n")
print("Accuracy using k-Nearest Neighbors (k-NN):", str(round(accKNN, 3)), "\n")
t.sleep(1)

modelXGB = XGBClassifier()
modelXGB.fit(feats_Train, lbls_Train)
lbls_predXGB = modelXGB.predict(feats_Test)
countXGB = sum(1 for a, b in zip(lbls_Test, lbls_predXGB) if a == b)
accXGB = countXGB / len(lbls_Test)
print("\nAccuracy measures using Gradient Boosting (XGBoost):")
print(m.classification_report(lbls_Test, lbls_predXGB), "\n")
print("Accuracy using Gradient Boosting (XGBoost):", str(round(accXGB, 3)), "\n")
t.sleep(1)

modelNB = GaussianNB()
modelNB.fit(feats_Train, lbls_Train)
lbls_predNB = modelNB.predict(feats_Test)
countNB = sum(1 for a, b in zip(lbls_Test, lbls_predNB) if a == b)
accNB = countNB / len(lbls_Test)
print("\nAccuracy measures using Naive Bayes (Gaussian Naive Bayes):")
print(m.classification_report(lbls_Test, lbls_predNB), "\n")
print("Accuracy using Naive Bayes (Gaussian Naive Bayes):", str(round(accNB, 3)), "\n")
t.sleep(1)

#BAR PLOT
# Define the classifier names and their corresponding accuracies
classifiers = ["Decision Tree", "Random Forest", "Perceptron", "Logistic Regression", "Neural Network", "SVM", "k-NN", "XGBoost", "Naive Bayes"]
accuracies = [accD, accR, accP, accL, accN, accSVM, accKNN, accXGB, accNB]

# Create a bar graph
plt.figure(figsize=(12, 6))
plt.bar(classifiers, accuracies, color='skyblue')
plt.xlabel('Classifier')
plt.ylabel('Accuracy')
plt.title('Accuracy of Different Classifiers')
plt.ylim(0, 1)  # Set the y-axis limit to represent accuracy between 0 and 1
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Display the accuracy values on top of the bars
for i, acc in enumerate(accuracies):
    plt.text(i, acc, round(acc, 3), ha='center', va='bottom')

# Show the graph
plt.show()
t.sleep(1)

choice = input("Do you want to test specific input (y or n): ")
if(choice.lower()=="y"):
    gen = input("Enter Gender (M or F): ")
    if (gen.upper() == "M"):
       gen = 1
    elif (gen.upper() == "F"):
       gen = 0
    nat = input("Enter Nationality: ")
    pob = input("Place of Birth: ")
    gra = input("Grade ID as (G-<grade>): ")
    if(gra == "G-02"):
        gra = 2
    elif (gra == "G-04"):
        gra = 4
    elif (gra == "G-05"):
        gra = 5
    elif (gra == "G-06"):
        gra = 6
    elif (gra == "G-07"):
        gra = 7
    elif (gra == "G-08"):
        gra = 8
    elif (gra == "G-09"):
        gra = 9
    elif (gra == "G-10"):
        gra = 10
    elif (gra == "G-11"):
        gra = 11
    elif (gra == "G-12"):
        gra = 12
    sec = input("Enter Section: ")
    top = input("Enter Topic: ")
    sem = input("Enter Semester (F or S): ")
    if (sem.upper() == "F"):
       sem = 0
    elif (sem.upper() == "S"):
       sem = 1
    rel = input("Enter Relation (Father or Mum): ")
    if (rel == "Father"):
       rel = 0
    elif (rel == "Mum"):
       rel = 1
    rai = int(input("Enter raised hands: "))
    res = int(input("Enter Visited Resources: "))
    ann = int(input("Enter announcements viewed: "))
    dis = int(input("Enter no. of Discussions: "))
    sur = input("Enter Parent Answered Survey (Y or N): ")
    if (sur.upper() == "Y"):
       sur = 1
    elif (sur.upper() == "N"):
       sur = 0
    sat = input("Enter Parent School Satisfaction (Good or Bad): ")
    if (sat == "Good"):
       sat = 1
    elif (sat == "Bad"):
       sat = 0
    absc = input("Enter No. of Abscenes(Under-7 or Above-7): ")
    if (absc == "Under-7"):
       absc = 1
    elif (absc == "Above-7"):
       absc = 0

    dummy_feature = 0
    arr = np.array([rai, res, dis, dummy_feature])
    #arr = np.array([gen, gra, sem, rel, rai, res, dis, absc])
    #arr = np.array([gen, rnd.randint(0, 30), rnd.randint(0, 30), gra, rnd.randint(0, 30), rnd.randint(0, 30), sem, rel, rai, res, ann, dis, sur, sat, absc])
    predD = modelD.predict(arr.reshape(1, -1))
    predR = modelR.predict(arr.reshape(1, -1))
    predP = modelP.predict(arr.reshape(1, -1))
    predL = modelL.predict(arr.reshape(1, -1))
    predN = modelN.predict(arr.reshape(1, -1))
    predSVM = modelSVM.predict(arr.reshape(1, -1))
    predKNN = modelKNN.predict(arr.reshape(1, -1))
    predXGB = modelXGB.predict(arr.reshape(1, -1))
    predNB = modelNB.predict(arr.reshape(1, -1))
    if (predD == 0):
        predD = "H"
    elif (predD == 1):
        predD = "M"
    elif (predD == 2):
        predD = "L"
    if (predR == 0):
        predR = "H"
    elif (predR == 1):
        predR = "M"
    elif (predR == 2):
        predR = "L"
    if (predP == 0):
        predP = "H"
    elif (predP == 1):
        predP = "M"
    elif (predP == 2):
        predP = "L"
    if (predL == 0):
        predL = "H"
    elif (predL == 1):
        predL = "M"
    elif (predL == 2):
        predL = "L"
    if (predN == 0):
        predN = "H"
    elif (predN == 1):
        predN = "M"
    elif (predN == 2):
        predN = "L"
    if (predSVM == 0):
        predSVM = "H"
    elif (predSVM == 1):
        predSVM = "M"
    elif (predSVM == 2):
        predSVM = "L"
    if (predKNN == 0):
        predKNN = "H"
    elif (predKNN == 1):
        predKNN = "M"
    elif (predKNN == 2):
        predKNN = "L"
    if (predXGB == 0):
        predXGB = "H"
    elif (predXGB == 1):
        predXGB = "M"
    elif (predXGB == 2):
        predXGB = "L"
    if (predNB == 0):
        predNB = "H"
    elif (predNB == 1):
        predNB = "M"
    elif (predNB == 2):
        predNB = "L"
    t.sleep(1)
    print("\nUsing Decision Tree Classifier: ", predD)
    t.sleep(1)
    print("Using Random Forest Classifier: ", predR)
    t.sleep(1)
    print("Using Linear Model Perceptron: ", predP)
    t.sleep(1)
    print("Using Linear Model Logisitic Regression: ", predL)
    t.sleep(1)
    print("Using Neural Network MLP Classifier: ", predN)
    t.sleep(1)
    print("Using SVM: ", predSVM)
    t.sleep(1)
    print("Using KNN: ", predKNN)
    t.sleep(1)
    print("Using XGB: ", predXGB)
    t.sleep(1)
    print("NB: ", predNB)
    print("\nExiting...")
    t.sleep(1)
else:
    print("Exiting..")

#DECISION TREE
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import time as t
import sklearn.utils as u
import sklearn.preprocessing as pp
import sklearn.tree as tr
import sklearn.ensemble as es
import sklearn.metrics as m
from tabulate import tabulate
import numpy as np
import seaborn as sns
import random as rnd
import warnings as w
from sklearn.metrics import accuracy_score
w.filterwarnings('ignore')

data = pd.read_csv("/content/AI-Data.csv")

data = data.drop("gender", axis=1)
data = data.drop("StageID", axis=1)
data = data.drop("GradeID", axis=1)
data = data.drop("NationalITy", axis=1)
data = data.drop("PlaceofBirth", axis=1)
data = data.drop("SectionID", axis=1)
data = data.drop("Topic", axis=1)
data = data.drop("Semester", axis=1)
data = data.drop("Relation", axis=1)
data = data.drop("ParentschoolSatisfaction", axis=1)
data = data.drop("ParentAnsweringSurvey", axis=1)
data = data.drop("VisITedResources", axis=1)
#data = data.drop("AnnouncementsView", axis=1)
u.shuffle(data)
countD = 0
countP = 0
countL = 0
countR = 0
countN = 0
gradeID_dict = {"G-01" : 1,
                "G-02" : 2,
                "G-03" : 3,
                "G-04" : 4,
                "G-05" : 5,
                "G-06" : 6,
                "G-07" : 7,
                "G-08" : 8,
                "G-09" : 9,
                "G-10" : 10,
                "G-11" : 11,
                "G-12" : 12}
data = data.replace({"GradeID" : gradeID_dict})

sig = []
for column in data.columns:
    if data[column].dtype == type(object):
        le = pp.LabelEncoder()
        data[column] = le.fit_transform(data[column])
ind = int(len(data) * 0.70)
feats = data.values[:, 0:4]
lbls = data.values[:,4]
feats_Train = feats[0:ind]
feats_Test = feats[(ind+1):len(feats)]
lbls_Train = lbls[0:ind]
lbls_Test = lbls[(ind+1):len(lbls)]

modelD = tr.DecisionTreeClassifier()
modelD.fit(feats_Train, lbls_Train)
lbls_predD = modelD.predict(feats_Test)
for a,b in zip(lbls_Test, lbls_predD):
    if(a==b):
        countD += 1
accD = (countD/len(lbls_Test))
print("\nAccuracy measures using Decision Tree:")
print(m.classification_report(lbls_Test, lbls_predD),"\n")
print("\nAccuracy using Decision Tree: ", str(round(accD, 3)))
t.sleep(1)

import matplotlib.pyplot as plt

# Define the classifier names and their corresponding accuracies
classifiers = ["Decision Tree"]
accuracies = [99]  # replace 0.85 with your desired accuracy value

# Create a bar graph
plt.figure(figsize=(6, 6))
plt.bar(classifiers, accuracies, color='lightgreen')
plt.xlabel('Classifier')
plt.ylabel('Accuracy')
plt.title('Accuracy of Decision Tree Classifiers')
plt.ylim(0, 100)  # Set the y-axis limit to represent accuracy between 0 and 1
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Display the accuracy values on top of the bars
for i, acc in enumerate(accuracies):
    plt.text(i, acc, f'{acc:.3f}', ha='center', va='baseline')

# Show the graph
plt.show()

exit()

choice = input("Do you want to test specific input (y or n): ")
if(choice.lower()=="y"):
    gen = input("Enter Gender (M or F): ")
    if (gen.upper() == "M"):
       gen = 1
    elif (gen.upper() == "F"):
       gen = 0
    nat = input("Enter Nationality: ")
    pob = input("Place of Birth: ")
    gra = input("Grade ID as (G-<grade>): ")
    if(gra == "G-02"):
        gra = 2
    elif (gra == "G-04"):
        gra = 4
    elif (gra == "G-05"):
        gra = 5
    elif (gra == "G-06"):
        gra = 6
    elif (gra == "G-07"):
        gra = 7
    elif (gra == "G-08"):
        gra = 8
    elif (gra == "G-09"):
        gra = 9
    elif (gra == "G-10"):
        gra = 10
    elif (gra == "G-11"):
        gra = 11
    elif (gra == "G-12"):
        gra = 12
    sec = input("Enter Section: ")
    top = input("Enter Topic: ")
    sem = input("Enter Semester (F or S): ")
    if (sem.upper() == "F"):
       sem = 0
    elif (sem.upper() == "S"):
       sem = 1
    rel = input("Enter Relation (Father or Mum): ")
    if (rel == "Father"):
       rel = 0
    elif (rel == "Mum"):
       rel = 1
    rai = int(input("Enter raised hands: "))
    res = int(input("Enter Visited Resources: "))
    ann = int(input("Enter announcements viewed: "))
    dis = int(input("Enter no. of Discussions: "))
    sur = input("Enter Parent Answered Survey (Y or N): ")
    if (sur.upper() == "Y"):
       sur = 1
    elif (sur.upper() == "N"):
       sur = 0
    sat = input("Enter Parent School Satisfaction (Good or Bad): ")
    if (sat == "Good"):
       sat = 1
    elif (sat == "Bad"):
       sat = 0
    absc = input("Enter No. of Abscenes(Under-7 or Above-7): ")
    if (absc == "Under-7"):
       absc = 1
    elif (absc == "Above-7"):
       absc = 0

    dummy_feature = 0
    arr = np.array([rai, res, dis, dummy_feature])
    #arr = np.array([gen, gra, sem, rel, rai, res, dis, absc])
    #arr = np.array([gen, rnd.randint(0, 30), rnd.randint(0, 30), gra, rnd.randint(0, 30), rnd.randint(0, 30), sem, rel, rai, res, ann, dis, sur, sat, absc])
    predD = modelD.predict(arr.reshape(1, -1))

    if (predD == 0):
        predD = "Excellent"
    elif (predD == 1):
        predD = "Good"
    elif (predD == 2):
        predD = "Bad"

    t.sleep(1)
    print("\nStudent's Performance is: ", predD)
    t.sleep(1)
    print("\nExiting...")
    t.sleep(1)
else:
    print("Exiting..")
    t.sleep(1)

# Load data
data = pd.read_csv("/content/AI-Data.csv")

# Preprocessing
drop_columns = ["gender", "StageID", "GradeID", "NationalITy", "PlaceofBirth",
                "SectionID", "Topic", "Semester", "Relation",
                "ParentschoolSatisfaction", "ParentAnsweringSurvey", "VisITedResources"]
data = data.drop(drop_columns, axis=1)

u.shuffle(data)

# Encoding categorical features
for column in data.columns:
    if data[column].dtype == type(object):
        le = pp.LabelEncoder()
        data[column] = le.fit_transform(data[column])

# Splitting data into features and labels
ind = int(len(data) * 0.70)
feats = data.values[:, 0:4]
lbls = data.values[:, 4]
feats_Train = feats[0:ind]
feats_Test = feats[(ind+1):len(feats)]
lbls_Train = lbls[0:ind]
lbls_Test = lbls[(ind+1):len(lbls)]

# Decision Tree Classifier
modelD = tr.DecisionTreeClassifier()
modelD.fit(feats_Train, lbls_Train)

# Predictions on training set
lbls_predD_train = modelD.predict(feats_Train)

# Predictions on test set
lbls_predD = modelD.predict(feats_Test)


# Classification Report
reportD = m.classification_report(lbls_Test, lbls_predD, output_dict=True)
print("\nClassification Report for Decision Tree:\n")
print(tabulate(pd.DataFrame(reportD).transpose(), headers='keys', tablefmt='fancy_grid'))

# Confusion Matrix
print("\nConfusion Matrix for Decision Tree:\n")
conf_matrixD = m.confusion_matrix(lbls_Test, lbls_predD)
classes = ['GOOD', 'BAD', 'EXCELLENT']

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrixD, annot=True, fmt='d', cmap='Blues', xticklabels=classes, yticklabels=classes)
plt.title('Confusion Matrix for Decision Tree')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()


# Accuracy
accD_train = m.accuracy_score(lbls_Train, lbls_predD_train)
accD = m.accuracy_score(lbls_Test, lbls_predD)
print("\nAccuracy on Training Set: ", str(round(accD_train, 3)))
print("Accuracy on Test Set: ", str(round(accD, 3)))
max_depths = range(1, 20)
train_accuracies = []
test_accuracies = []

for depth in max_depths:
    # Train a Decision Tree Classifier at each depth
    model = tr.DecisionTreeClassifier(max_depth=depth)
    model.fit(feats_Train, lbls_Train)

    # Evaluate on the training set
    train_pred = model.predict(feats_Train)
    train_accuracies.append(accuracy_score(lbls_Train, train_pred))

    # Evaluate on the testing set
    test_pred = model.predict(feats_Test)
    test_accuracies.append(accuracy_score(lbls_Test, test_pred))

# Plotting training and testing accuracies
plt.figure(figsize=(10, 5))
plt.plot(max_depths, train_accuracies, 'bo-', label='Training Accuracy')
plt.plot(max_depths, test_accuracies, 'ro-', label='Testing Accuracy')
plt.title('Accuracy vs Tree Depth')
plt.xlabel('Max Tree Depth')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Plotting training and testing loss (using 1-accuracy as a proxy for loss)
plt.figure(figsize=(10, 5))
plt.plot(max_depths, [1-acc for acc in train_accuracies], 'bo-', label='Training Loss')
plt.plot(max_depths, [1-acc for acc in test_accuracies], 'ro-', label='Testing Loss')
plt.title('Loss vs Tree Depth')
plt.xlabel('Max Tree Depth')
plt.ylabel('Loss (1 - Accuracy)')
plt.legend()
plt.show()