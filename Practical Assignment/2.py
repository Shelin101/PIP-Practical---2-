import statistics
import pandas as pd
sr = pd.Series([10, 50, 80, 70, 49, 23, 11, 4])
mean = sr.mean()
median = sr.median()
mode = sr.mode()
range1 = sr.max() - sr.min()
stdeviation = sr.std(axis=0, skipna=True)
print(mean)
print(median)
print(mode)
print(range1)
print(stdeviation)
print("Variance is %s"
      % (statistics.variance(sr)))
