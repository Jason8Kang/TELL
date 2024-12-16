# TELL
This is official repo for the paper Template-Driven LLM-Paraphrased Framework for Tabular Math Word Problem Generation. This is overall framework.

<p align="center">
    <img src="./pictures/Framework03.png" width="800">
    <br>
</p>

## 25 TMWP templates of main question types

| Type | Template                                                                                                                                                                               |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | How many times does \verb|{count_value}| appear in the stem-and-leaf plot?                                                                                                             |
| 2    | How many numbers are at least \verb|{range_start}| and at most \verb|{range_end}|?                                                                                                     |
| 3    | How many numbers are at least \verb|{range_start}| but fewer than \verb|{range_end}|?                                                                                                  |
| 4    | How many numbers are greater than \verb|{range_start}| but fewer than \verb|{range_end}|?                                                                                              |
| 5    | How many numbers are greater than \verb|{range_start}| and at most \verb|{range_end}|?                                                                                                 |
| 6    | How many numbers are fewer than \verb|{threshold}|?                                                                                                                                    |
| 7    | How many numbers are at most \verb|{threshold}|?                                                                                                                                       |
| 8    | How many numbers are at least \verb|{threshold}|?                                                                                                                                      |
| 9    | How many numbers are greater than \verb|{threshold}|?                                                                                                                                  |
| 10   | What is the smallest number in the dataset?                                                                                                                                            |
| 11   | What is the largest number in the dataset?                                                                                                                                             |
| 12   | How much money does \verb|{name}| need to buy \verb|{number}| \verb|{products}|?                                                                                                       |
| 13   | How much money does \verb|{name}| need to buy \verb|{number1}| \verb|{product1s}| and \verb|{number2}| \verb|{product2s}|?                                                             |
| 14   | How much money does \verb|{name}| need to buy \verb|{number1}| \verb|{product1s}|, \verb|{number2}| \verb|{product2s}|, and \verb|{number3}| \verb|{product3s}|?                       |
| 15   | How much money will \verb|{name}| have left if \verb|{gender}| buys \verb|{number}| \verb|{products}|?                                                                                 |
| 16   | How much money will \verb|{name}| have left if \verb|{gender}| buys \verb|{number1}| \verb|{product1s}| and \verb|{number2}| \verb|{product2s}|?                                       |
| 17   | How much money does \verb|{name}| have left if \verb|{gender}| buys \verb|{number1}| \verb|{product1s}|, \verb|{number2}| \verb|{product2s}|, and \verb|{number3}| \verb|{product3s}|? |
| 18   | Which category has more value for \verb|{column}|, \verb|{row1}| or \verb|{row2}|?                                                                                                     |
| 19   | Which category has less value for \verb|{column}|, \verb|{row1}| or \verb|{row2}|?                                                                                                     |
| 20   | What is the probability that a randomly selected item is \verb|{row}| and \verb|{col}|?                                                                                                |
| 21   | What fraction of \verb|{items}| in the table belong to \verb|{category}|?                                                                                                              |
| 22   | What is the mean of the numbers?                                                                                                                                                       |
| 23   | What is the median of the numbers?                                                                                                                                                     |
| 24   | What is the mode of the numbers?                                                                                                                                                       |
| 25   | What is the average of the numbers?                                                                                                                                                    |

The code is in template folder.
