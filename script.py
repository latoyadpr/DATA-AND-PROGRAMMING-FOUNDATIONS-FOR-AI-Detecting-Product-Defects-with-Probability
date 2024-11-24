import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 7

## Task 2:
probability_exact_lam = stats.poisson.pmf(lam, lam)
print(probability_exact_lam)

## Task 3:
probability_good_day = stats.poisson.cdf(4, lam)
print(probability_good_day)

## Task 4:
probability_bad_day = 1 - stats.poisson.cdf(9, lam)
print(probability_bad_day)


### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(lam, size=365)

## Task 6:
print(year_defects[:20])

## Task 7:
expected_total_defects = lam * 365
print(expected_total_defects)


## Task 8:
total_defects = sum(year_defects)
print(total_defects)

## Task 9:
average_defects_per_day = np.mean(year_defects)
print(average_defects_per_day)

## Task 10:
max_defects = year_defects.max()
print(max_defects)

## Task 11:
probability_max_or_more = 1 - stats.poisson.cdf(max_defects - 1, lam)
print(probability_max_or_more)


### Extra Bonus ###
# Task 12
percentile_90_value = stats.poisson.ppf(0.90, lam)
print(percentile_90_value)

# Task 13