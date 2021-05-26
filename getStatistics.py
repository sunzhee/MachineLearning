"""
Get Statistics

Write a function that takes in a list of
numbers and returns a dictionary containing
the following statistics about the numbers:
the mean, median, mode, sample variance,
sample standard deviation, and 95%
condence interval for the mean.
Note that:
You can assume that the given list
contains a large-enough number of
samples from a population to use a zscore of 1.96 .
If there's more than one mode, your
function can return any of them.
You shouldn't use any libraries.
Your output values will automatically
be rounded to the fourth decimal.



Sample Input
input_list = [2, 1, 3, 4, 4, 5, 6, 7]



Sample Output
{
 "mean": 4.0,
 "median": 4.0,
 "mode": 4.0,
 "sample_variance": 4.0,
 "sample_standard_deviation": 2.0,
 "mean_confidence_interval": [2.6141, 5.3859
}

"""
# 各种数值定义，和计算方法
def get_statistics(input_list):
    sortedInput = sorted(input_list)
    inputLength = len(sortedInput)

    mean = sum(sortedInput) / inputLength

    # 这是总长度为奇数的情况，如果是偶数则不对，我们在下面重新计算偶数情况
    middleIndex = (inputLength - 1) // 2
    median = sortedInput[middleIndex]
    # 偶数的情况
    if inputLength % 2 == 0:
        middleNumber1 = sortedInput[middleIndex]
        middleNumber2 = sortedInput[middleIndex + 1]
        median = (middleNumber1 + middleNumber2) / 2
    
    numberCounts = {x: sortedInput.count(x) for x in set(sortedInput)}
    mode = max(numberCounts.keys(), key=lambda uniqueNumber: numberCounts[uniqueNumber])

    sample_variance = sum([(number - mean) ** 2 / (inputLength - 1) for number in sortedInput])

    sample_standard_deviation = sample_variance ** 0.5

    mean_standard_error = sample_standard_deviation / inputLength ** 0.5
    z_score_standard_error = 1.96 * mean_standard_error
    mean_confidence_interval = [mean - z_score_standard_error, mean + z_score_standard_error]

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }

