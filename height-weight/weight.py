import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import pandas as pd

# reading data
df = pd.read_csv('height-weight.csv')
weight = df ['Weight(Pounds)'].to_list()

# mean & sd
mean = statistics.mean(weight)
std_deviation = statistics.stdev(weight)
median = statistics.median(weight)
mode = statistics.mode(weight)

# sd1 range, sd2 range, sd3 range
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

# plot chart with lines for each range & mean
fig = ff.create_distplot([weight], ["Weight"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.034], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.034], mode="lines", name="SD Start 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.034], mode="lines", name="SD End 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.034], mode="lines", name="SD Start 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.034], mode="lines", name="SD End 2"))
fig.show()

# printing calculations
sd1 = [result for result in weight if result > first_std_deviation_start and result < first_std_deviation_end]
sd2 = [result for result in weight if result > second_std_deviation_start and result < second_std_deviation_end]
sd3 = [result for result in weight if result > third_std_deviation_start and result < third_std_deviation_end]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_deviation))
print("{}% of data lies within 1 standard deviation".format(len(sd1)*100.0/len(weight)))
print("{}% of data lies within 2 standard deviations".format(len(sd2)*100.0/len(weight)))
print("{}% of data lies within 3 standard deviations".format(len(sd3)*100.0/len(weight)))