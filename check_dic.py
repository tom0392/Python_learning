#!/bin/bash/python

fruit=["apple","orange","potato","apple"]
fruit_counts={}

for item in fruit:
	if item in fruit_counts:
		fruit_counts[item]=fruit_counts[item]+1
	else:
		fruit_counts[item]=1
print(fruit_counts)
		
