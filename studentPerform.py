import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")
mScore_list = df["math score"].to_list()
rScore_list = df["reading score"].to_list()
mScore_mean = statistics.mean(mScore_list)
rScore_mean = statistics.mean(rScore_list)
mScore_mode = statistics.mode(mScore_list)
rScore_mode = statistics.mode(rScore_list)
mScore_median = statistics.median(mScore_list)
rScore_median = statistics.median(rScore_list)

print("mean, median, and mode of height is {},{},and{}".format(mScore_mean,mScore_median,mScore_mode))
print("mean, median, and mode of weight is {},{},and{}".format(rScore_mean,rScore_median,rScore_mode))
mScore_std_deviation = statistics.stdev(mScore_list)
rScore_std_deviation = statistics.stdev(rScore_list)
mScore_first_std_deviation_start,mScore_first_std_deviation_end = mScore_mean-mScore_std_deviation,mScore_mean+mScore_std_deviation
mScore_second_std_deviation_start,mScore_second_std_deviation_end = mScore_mean-(2*mScore_std_deviation),mScore_mean+(2*mScore_std_deviation)
mScore_third_std_deviation_start,mScore_third_std_deviation_end = mScore_mean-(3*mScore_std_deviation),mScore_mean+(3*mScore_std_deviation)
rScore_first_std_deviation_start,rScore_first_std_deviation_end = rScore_mean-rScore_std_deviation,rScore_mean+rScore_std_deviation
rScore_second_std_deviation_start,rScore_second_std_deviation_end = rScore_mean-(2*rScore_std_deviation),rScore_mean+(2*rScore_std_deviation)
rScore_third_std_deviation_start,rScore_third_std_deviation_end = rScore_mean-(3*rScore_std_deviation),rScore_mean+(3*rScore_std_deviation)
mScore_list_of_data_within_1_std_deviation = [result for result in mScore_list if result > mScore_first_std_deviation_start and result < mScore_first_std_deviation_end]
mScore_list_of_data_within_2_std_deviation = [result for result in mScore_list if result > mScore_second_std_deviation_start and result < mScore_second_std_deviation_end]
mScore_list_of_data_within_3_std_deviation = [result for result in mScore_list if result > mScore_third_std_deviation_start and result < mScore_third_std_deviation_end]
rScore_list_of_data_within_1_std_deviation = [result for result in rScore_list if result > rScore_first_std_deviation_start and result < rScore_first_std_deviation_end]
rScore_list_of_data_within_2_std_deviation = [result for result in rScore_list if result > rScore_second_std_deviation_start and result < rScore_second_std_deviation_end]
rScore_list_of_data_within_3_std_deviation = [result for result in rScore_list if result > rScore_third_std_deviation_start and result < rScore_third_std_deviation_end]
print("{}% of data for height lies within 1 standard deviation".format(len(mScore_list_of_data_within_1_std_deviation)*100.0/len(mScore_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(mScore_list_of_data_within_2_std_deviation)*100.0/len(mScore_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(mScore_list_of_data_within_3_std_deviation)*100.0/len(mScore_list)))
print("{}% of data for weight lies within 1 standard deviation".format(len(rScore_list_of_data_within_1_std_deviation)*100.0/len(rScore_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(rScore_list_of_data_within_2_std_deviation)*100.0/len(rScore_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(rScore_list_of_data_within_3_std_deviation)*100.0/len(rScore_list)))
fig = ff.create_distplot([mScore_list],["math socre"],show_hist=False)
fig.show()