# TELL
This is official repo for the paper Template-Driven LLM-Paraphrased Framework for Tabular Math Word Problem Generation. 

 - Paper link: arXiv
 - data link: [TABMWP-TELL](https://github.com/Jason8Kang/TELL/blob/main/Data/TABMWP-TELL.jsonl)

## Introduction
The rise of large language models (LLMs) has achieved unprecedented success in a variety of reasoning tasks. However, solving math word problems (MWPs) is still challenging, which is tasked as answering math questions based on heterogeneous tabular and textual data with mathematical reasoning ability. For various complex MWPs, training models usually require a large amount of data; nevertheless, the collection and annotation of MWPs are usually costly and time-consuming, resulting in the scarcity of public tabular MWP datasets.

## Overall Framework
<p align="center">
    <img src="./pictures/Framework03.png" width="800">
    <br>
</p>

## 25 TMWP templates of main question types

| Type | Template                                                                                                                       |
|------|--------------------------------------------------------------------------------------------------------------------------------|
| 1    | How many times does {count_value} appear in the stem-and-leaf plot?                                                            |
| 2    | How many numbers are at least {range_start} and at most {range_end}?                                                           |
| 3    | How many numbers are at least {range_start} but fewer than {range_end}?                                                        |
| 4    | How many numbers are greater than {range_start} but fewer than {range_end}?                                                    |
| 5    | How many numbers are greater than {range_start} and at most {range_end}?                                                       |
| 6    | How many numbers are fewer than {threshold}?                                                                                   |
| 7    | How many numbers are at most {threshold}?                                                                                      |
| 8    | How many numbers are at least {threshold}?                                                                                     |
| 9    | How many numbers are greater than {threshold}?                                                                                 |
| 10   | What is the smallest number in the dataset?                                                                                    |
| 11   | What is the largest number in the dataset?                                                                                     |
| 12   | How much money does {name} need to buy {number} {products}?                                                                    |
| 13   | How much money does {name} need to buy {number1} {product1s} and {number2} {product2s}?                                        |
| 14   | How much money does {name} need to buy {number1} {product1s}, {number2} {product2s}, and {number3} {product3s}?                |
| 15   | How much money will {name} have left if {gender} buys {number} {products}?                                                     |
| 16   | How much money will {name} have left if {gender} buys {number1} {product1s} and {number2} {product2s}?                         |
| 17   | How much money does {name} have left if {gender} buys {number1} {product1s}, {number2} {product2s}, and {number3} {product3s}? |
| 18   | Which category has more value for {column}, {row1} or {row2}?                                                                  |
| 19   | Which category has less value for {column}, {row1} or {row2}?                                                                  |
| 20   | What is the probability that a randomly selected item is {row} and {col}?                                                      |
| 21   | What fraction of {items} in the table belong to {category}?                                                                    |
| 22   | What is the mean of the numbers?                                                                                               |
| 23   | What is the median of the numbers?                                                                                             |
| 24   | What is the mode of the numbers?                                                                                               |
| 25   | What is the average of the numbers?                                                                                            |

The code for 25 problem templates is in Template folder. We use  Yi (Yi-Large-Turbo) to paraphrase the problems. The finally generated TABMWP-TELL is in Data folder.

## Experimental Setup
 In main experiments, we fine-tune three commonly used LLMs, including Mistral-7B, Qwen 2-7B, and Llama3-8B (Dubey et al. 2024) with the training set of TabMWP and TabMWP-TeLL, and the evaluations are conducted on the TabMWP test set. During the fine-tuning process, we set the number of epochs as 2, the batch size per device as 12, the gradient accumulation steps as 4, and the learning rate as 2e − 4. To achieve parameter-efficient fine-tuning, we adopt the QLoRA strategy with [XTuner](https://github.com/InternLM/xtuner/blob/main/README_zh-CN.md)
. All experiments are conducted on 8 NVIDIA GeForce RTX 3090 graphic cards.



## Citation












