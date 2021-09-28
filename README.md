<h1>Basic Info/Disclaimer</h1>
This code intends to simulate the costs of a negative income tax (NIT) if implemented in the United States.

The data used (the relevent aspects being the household income level at each percentile in 2020) comes from: https://dqydj.com/average-median-top-household-income-percentiles/. Note that the three rightmost columns in the data file are not used by this code. <br></br>
This code should by no means be used as an end all, be all for the costs of a NIT. It is based off of rough estimates, so take with a grain of salt. The code is also easy to break because it doesn't check for valid input (yet). 

<h1>About the Negative Income Tax</h1>
The NIT is a welfare program which can be used to guarantee income. Unlike a Universal basic income, the payments phase out as income increases, so a greater poverty reduction is achieved with a smaller total cost. Unlike means-tested welfare, recipients do not face a "welfare cliff" in which increasing their earnings can sometimes lower their income <br></br>
The NIT can be implemented using two parameters: a threshold and a percentage. Under the NIT, each household which makes an income lower than the threshold would recieve payments. The NIT works by first substracting the recipients household income from the threshold, and then multiplying this result by the percentage. <br></br>As an example, If an NIT program had a threshold of $40,000 and a percent of 50, a household making $30,000 would recieve $5,000, equal to $40,000 - $30,000 * 0.5. A household making $0, would recieve $40,000 - $0 * 0.5, or $20,000. 

<h1>Algorithms used</h1>
The first algorithm uses the data to estimate the percentage of households at or below a given income level. This algorithm first figures out the two percentiles (and the corresponding incomes) from the data set the given income lies between. If w represents the lower of the two percentiles, x represents the given income, y represents the income associated with the lower percentile, z represents the income associated with the higher percentile, the income percentile of a household can be estimated with:<br></br>

P = w + (x - y) / (z - y) 








