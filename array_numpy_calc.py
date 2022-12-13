#numpy calculation method 
import numpy as np 

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

grades_sum = grades.sum()
grades_min = grades.min()
grades_max = grades.max()
grade_mean = grades.mean()
grade_std = grades.std()

print(grades_sum,grades_min,grades_max,grade_mean,grade_std)


