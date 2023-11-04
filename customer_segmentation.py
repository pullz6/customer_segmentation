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

test_df =  pd.read_csv("test.csv")
train_df =  pd.read_csv("train.csv")

train_copy = train_df.copy()

label_encoder = preprocessing.LabelEncoder()

print(train_df['Segmentation'].unique())

train_copy['Gender']= label_encoder.fit_transform(train_copy['Gender']) 
train_copy['Ever_Married']= label_encoder.fit_transform(train_copy['Ever_Married'])
train_copy['Graduated']= label_encoder.fit_transform(train_copy['Graduated'])
train_copy['Spending_Score']= label_encoder.fit_transform(train_copy['Spending_Score'])
train_copy['Profession']= label_encoder.fit_transform(train_copy['Profession']) 
train_copy['Var_1']= label_encoder.fit_transform(train_copy['Var_1']) 
train_copy['Segmentation']= label_encoder.fit_transform(train_copy['Segmentation']) 

#Filling missing values
train_copy['Work_Experience']=train_copy['Work_Experience'].fillna(train_copy['Work_Experience'].mean())
train_copy['Family_Size']=train_copy['Family_Size'].fillna(train_copy['Family_Size'].mean())

#Kmeans clustering
train_cols = train_copy.columns 
ms = MinMaxScaler()
train_Knn = ms.fit_transform(train_copy) 
print(train_Knn)
train_Knn = pd.DataFrame(train_Knn , columns=[train_cols])
print(train_Knn)

cs = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 'auto', random_state = 0)
    kmeans.fit(train_Knn)
    cs.append(kmeans.inertia_)
plt.plot(range(1, 11), cs)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('CS')
plt.show()

#Hierarchial Clustering
plt.figure(1, figsize = (16 ,8))
dendrogram = sch.dendrogram(sch.linkage(train_copy, method  = "ward"))

plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()

