import math

incheon = [25.0, 27.5, 24.0, 29.0, 28.2, 25.0, 26.4, 28.0, 24.0, 28.0]
daegu = [27.2, 30.2, 25.0, 36.2, 35.1, 28.2, 30.1, 25.1, 23.2, 34.1]

# 최고값
max_incheon = max(incheon)
max_daegu = max(daegu)
print("인천 최고값: %f" %max_incheon)
print("대구 최고값: %f" %max_daegu)

# 최저값
min_incheon = min(incheon)
min_daegu = min(daegu)
print("인천 최저값: %f" %min_incheon)
print("대구 최저값: %f" %min_daegu)

# 평균
mean_incheon = sum(incheon) / len(incheon)
mean_daegu = sum(daegu) / len(daegu)
print("인천 평균: %f" %mean_incheon)
print("대구 평균: %f" %mean_daegu)

# 분산
vsum_incheon = 0
for x in incheon:
    vsum_incheon = vsum_incheon + (x - mean_incheon)**2
var_incheon = vsum_incheon / len(incheon)
vsum_daegu = 0
for x in daegu:
    vsum_daegu = vsum_daegu + (x - mean_daegu)**2
var_daegu = vsum_daegu / len(daegu)
print("인천 분산: %f" %var_incheon)
print("대구 분산: %f" %var_daegu)

# 표준편차
std_incheon = math.sqrt(var_incheon)
std_daegu = math.sqrt(var_daegu)
print("인천 표준편차: %f" %std_incheon)
print("대구 표준편차: %f" %std_daegu)