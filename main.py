import plotly.graph_objects as go
import plotly.figure_factory as ff
import random
import statistics
import csv
import pandas as pd
df = pd.read_csv('data.csv')
marksllist = df['math score'].tolist()
mean = statistics.mean(marksllist)
midean = statistics.median(marksllist)
mode = statistics.mode(marksllist)
sd = statistics.stdev(marksllist)
print(mean)
print(midean)
print(mode)
print(sd)
sd1start, sd1end = mean - sd, mean + sd
sd2start, sd2end = mean - (2*sd), mean + (2*sd)
sd3start, sd3end = mean - (3*sd), mean + (3*sd)
fig = ff.create_distplot([marksllist], ['Marks'], show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode='lines', name= 'mean'))
fig.add_trace(go.Scatter(x=[sd1start,sd1start], y=[0,0.17], mode='lines', name= 'sd1'))
fig.add_trace(go.Scatter(x=[sd1end,sd1end], y=[0,0.17], mode='lines', name= 'sd1'))
fig.add_trace(go.Scatter(x=[sd2start,sd2start], y=[0,0.17], mode='lines', name= 'sd2'))
fig.add_trace(go.Scatter(x=[sd2end,sd2end], y=[0,0.17], mode='lines', name= 'sd2'))
fig.add_trace(go.Scatter(x=[sd3start,sd3start], y=[0,0.17], mode='lines', name= 'sd3'))
fig.add_trace(go.Scatter(x=[sd3end,sd3end], y=[0,0.17], mode='lines', name= 'sd3'))

fig.show()
listofdatawithin1sd = [result for result in marksllist if result > sd1start and result < sd1end]
listofdatawinthin2sd = [result for result in marksllist if result > sd2start and result < sd2end]
listofdatawinthin3sd = [result for result in marksllist if result > sd3start and result < sd3end]
print('{}per ofdata lies within 1sd'.format(len(listofdatawithin1sd)*100.0/len(marksllist)))
print('{}per ofdata lies within 1sd'.format(len(listofdatawinthin2sd)*100.0/len(marksllist)))
print('{}per ofdata lies within 1sd'.format(len(listofdatawinthin3sd)*100.0/len(marksllist)))