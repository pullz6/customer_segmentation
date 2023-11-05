#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 17:26:47 2023

@author: pulsaragunawardhana
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing 
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import AgglomerativeClustering 
import scipy.cluster.hierarchy as sch
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

test_df =  pd.read_csv("test.csv")
train_df =  pd.read_csv("train.csv")

train_copy = train_df.copy()

label_encoder = preprocessing.LabelEncoder()
train_copy['Gender']= label_encoder.fit_transform(train_copy['Gender']) 
train_copy['Ever_Married']= label_encoder.fit_transform(train_copy['Ever_Married'])
train_copy['Graduated']= label_encoder.fit_transform(train_copy['Graduated'])
train_copy['Spending_Score']= label_encoder.fit_transform(train_copy['Spending_Score'])
train_copy['Profession']= label_encoder.fit_transform(train_copy['Profession']) 
train_copy['Var_1']= label_encoder.fit_transform(train_copy['Var_1']) 
train_copy['Segmentation']= label_encoder.fit_transform(train_copy['Segmentation']) 

#Filling missing values for the training set
train_copy['Work_Experience']=train_copy['Work_Experience'].fillna(train_copy['Work_Experience'].mean())
train_copy['Family_Size']=train_copy['Family_Size'].fillna(train_copy['Family_Size'].mean())

test_df['Gender']= label_encoder.fit_transform(test_df['Gender']) 
test_df['Ever_Married']= label_encoder.fit_transform(test_df['Ever_Married'])
test_df['Graduated']= label_encoder.fit_transform(test_df['Graduated'])
test_df['Spending_Score']= label_encoder.fit_transform(test_df['Spending_Score'])
test_df['Profession']= label_encoder.fit_transform(test_df['Profession']) 
test_df['Var_1']= label_encoder.fit_transform(test_df['Var_1']) 

#Filling missing values for the testing set
test_df['Work_Experience']=test_df['Work_Experience'].fillna(test_df['Work_Experience'].mean())
test_df['Family_Size']=test_df['Family_Size'].fillna(test_df['Family_Size'].mean())

# #Kmeans clustering
# train_cols = train_copy.columns 
# ms = MinMaxScaler()
# train_Knn = ms.fit_transform(train_copy) 
# print(train_Knn)
# train_Knn = pd.DataFrame(train_Knn , columns=[train_cols])
# print(train_Knn)

# cs = []
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 'auto', random_state = 0)
#     kmeans.fit(train_Knn)
#     cs.append(kmeans.inertia_)
# plt.plot(range(1, 11), cs)
# plt.title('The Elbow Method')
# plt.xlabel('Number of clusters')
# plt.ylabel('CS')
# plt.show()

# #Hierarchial Clustering
# plt.figure(1, figsize = (16 ,8))
# dendrogram = sch.dendrogram(sch.linkage(train_copy, method  = "ward"))

# plt.title('Dendrogram')
# plt.xlabel('Customers')
# plt.ylabel('Euclidean distances')
# plt.show()

#K-nearest neighbours 
knn = KNeighborsClassifier(n_neighbors=5)
x_train = train_copy.loc[:, train_copy.columns != 'Segmentation']
x_train = x_train.values.tolist()
y_train = train_copy.Segmentation
y_train = y_train.values.tolist()
x_test = test_df.values.tolist()

#fitting the model
knn.fit(x_train, y_train) 
y_pred = knn.predict(x_test)
test_df['Predicted Segmenation'] = y_pred

train_copy_plot = train_copy.groupby(['Segmentation'])['Spending_Score'].sum().reset_index()

# sort it by spending score and make a horizontal bar plot!
train_copy_plot.sort_values(['Spending_Score'], ascending=False).plot(kind='barh', y='Spending_Score', x='Segmentation', title ="Spending Score on Train Set",color=['r', 'g', 'm', 'b',],legend=False)

#do the above for the test set as well
test_df_plot = test_df.groupby(['Predicted Segmenation'])['Spending_Score'].sum().reset_index()

# sort it by spending score and make a horizontal bar plot!
test_df_plot.sort_values(['Spending_Score'], ascending=False).plot(kind='barh', y='Spending_Score', x='Predicted Segmenation', title ="Spending Score on Test Set",color=['r', 'g', 'm', 'b',],legend=False)


