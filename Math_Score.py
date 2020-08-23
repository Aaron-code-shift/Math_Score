import csv
import pandas as pd 
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("maths_score.csv")
data = df['Math_score'].tolist()

mean = statistics.mean(data)
stdev = statistics.stdev(data)
print( mean , stdev)

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0 , counter):
      randomIndex = random.randint(0 , len(data) -1)
      value = data[randomIndex]
      dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

meanList = []

for i in range(0 , 1000):
    SetOfMean = randomSetOfMean(100)
    meanList.append(SetOfMean)

staDev = statistics.stdev(meanList)
mean1 = statistics.mean(meanList)
print( mean1 , staDev)


stdev1s , stdev1e = mean1 - staDev , mean1 + staDev
stdev2s , stdev2e = mean1 - (2 *staDev) , mean1 +(2 * staDev)
stdev3s , stdev3e = mean1 - (3 *staDev) , mean1 +(3 * staDev)

print(stdev1s , stdev1e)
print(stdev2s , stdev2e)
print(stdev3s , stdev3e)

#fig = ff.create_distplot([meanList] , ["Maths Score"] , show_hist = False)
#fig.add_trace(go.Scatter(x = [mean1 , mean1] , y = [0 , 0.20] , mode = 'lines' , name = 'Mean'))
#fig.add_trace(go.Scatter(x = [stdev1s , stdev1s] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev1s'))
#fig.add_trace(go.Scatter(x = [stdev1e , stdev1e] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev1e'))
#fig.add_trace(go.Scatter(x = [stdev2s , stdev2s] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev2s'))
#fig.add_trace(go.Scatter(x = [stdev2e , stdev2e] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev2e'))
#fig.add_trace(go.Scatter(x = [stdev3s , stdev3s] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev3s'))
#fig.add_trace(go.Scatter(x = [stdev3e , stdev3e] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev3e'))

#fig.show()
#df = pd.read_csv("maths_score1.csv")
#data = df['Math_score'].tolist()
###meanofsample1 = statistics.mean(data)
#print(meanofsample1)
#fig = ff.create_distplot([data] , ["Maths Score"] , show_hist = False)
#fig.add_trace(go.Scatter(x = [mean , mean] , y = [0 , 0.17] , mode = 'lines' , name = 'Mean'))
#fig.add_trace(go.Scatter(x = [meanofsample1 , meanofsample1] , y = [0 , 0.17] , mode = 'lines' , name = 'Mean Of Sample 1'))
#fig.add_trace(go.Scatter(x = [stdev1e , stdev1e] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev1e'))
#fig.show()

#df = pd.read_csv("maths_score2.csv")
#data = df['Math_score'].tolist()
#meanofsample2 = statistics.mean(data)
#print(meanofsample2)
#fig = ff.create_distplot([data] , ["Maths Score"] , show_hist = False)
#fig.add_trace(go.Scatter(x = [mean , mean] , y = [0 , 0.17] , mode = 'lines' , name = 'Mean'))
#fig.add_trace(go.Scatter(x = [meanofsample2 , meanofsample2] , y = [0 , 0.17] , mode = 'lines' , name = 'Mean Of Sample 2'))
#fig.add_trace(go.Scatter(x = [stdev1e , stdev1e] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev1e'))
#fig.add_trace(go.Scatter(x = [stdev2e , stdev2e] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev2e'))
#fig.show()

df = pd.read_csv("maths_score3.csv")
data = df['Math_score'].tolist()
meanofsample3 = statistics.mean(data)
print(meanofsample3)
fig = ff.create_distplot([data] , ["Maths Score"] , show_hist = False)
fig.add_trace(go.Scatter(x = [mean , mean] , y = [0 , 0.17] , mode = 'lines' , name = 'Mean'))
fig.add_trace(go.Scatter(x = [meanofsample3 , meanofsample3] , y = [0 , 0.17] , mode = 'lines' , name = 'Mean Of Sample 3'))
fig.add_trace(go.Scatter(x = [stdev1e , stdev1e] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev1e'))
fig.add_trace(go.Scatter(x = [stdev2e , stdev2e] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev2e'))
fig.add_trace(go.Scatter(x = [stdev3e , stdev3e] , y = [0 , 0.17] , mode = 'lines' , name = 'Stdev3e'))
fig.show()
