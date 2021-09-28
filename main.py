NUM_HOUSEHOLDS_US = 120756048


# returns index of the "lower" data point the user inputed income is between
def binary_search(income: float, data: list[list[float]]) -> int:
    l, r = 0, len(data) - 1
    res = -1
    while l <= r:
        mid = l + (r - l) // 2
        if data[mid][1] > income:
            r = mid - 1

        else:
            res = mid
            l = mid + 1

    return res


# returns the percent of households at a given income threshold
def households_at_threshold(l_index: int, income: float, data: list[list[float]]) -> float:
    return (data[l_index][0] +
            (data[l_index + 1][0] - data[l_index][0]) * (income - data[l_index][1]) / (
                        data[l_index + 1][1] - data[l_index][1])) / 100


# calculates the amount a NIT at a certain threshold and percent will cost
def calculate_cost(threshold: float, percent: float, data: list[list[float]]) -> float:
    res = 0.0
    prev_percent = 0.0
    for i in range(0, int(threshold), 100):
        curr = households_at_threshold(binary_search(i, data), float(i), data)
        res += (curr - prev_percent) * NUM_HOUSEHOLDS_US * ((threshold - i) * percent)
        prev_percent = curr

    return res


def main():
    f = open("data.txt", "r")
    data = []
    for line in f:
        data.append([float(line[0: line.index("%")]),
                    float(line[line.index("$")+1: line.index("\t", line.index("%")+2)])])

    f.close()

    threshold = float(input("What threshold do you want the NIT to apply to?"))
    percent = float(input("What percent of the threshold minus the income should the NIT give?"))

    cost = round(calculate_cost(threshold, percent / 100, data), 2)
    print("A NIT guaranteeing " + str(percent) + "% of a threshold of $"
          + str(threshold) + " would cost: $" + f'{cost:,}')


main()
