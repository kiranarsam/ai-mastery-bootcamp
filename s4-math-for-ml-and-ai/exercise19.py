
data = [10, 30, 20, 50, 40]
mean = sum(data) / len(data)
print("Mean: ", mean)

sorted_data = sorted(data)
median = sorted_data[len(data) // 2] if len(data) % 2 != 0 else (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2
print("Median: ", median)

from statistics import mode

print("Mode: ", mode(data))


# Variance
variance = sum((x - mean) ** 2 for x in data) / len(data)
print("Variance: ", variance)

std_deviation = variance ** 0.5
print("Standard_Deviation: ", std_deviation)


from scipy.stats import stats

sample_mean = mean
z_score = 1.96

ci = (sample_mean - z_score * (std_deviation / len(data) ** 0.5),
      sample_mean + z_score * (std_deviation / len(data) ** 0.5))
print("95% Confidence Interval: ", ci)
