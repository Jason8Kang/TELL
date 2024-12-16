import random
import json

# 定义一个函数来生成随机的茎叶图数据
def generate_stem_leaf_data(min_value, max_value, num_samples):
    stem = []
    leaf = []
    for _ in range(num_samples):
        value = random.randint(min_value, max_value)
        stem.append(value // 10)
        leaf.append(value % 10)
    return stem, leaf

# 定义一个函数来格式化表格输出
def format_table(stem, leaf):
    new_stem = []
    new_leaf = []
    table = "Stem | Leaf\n"
    unique_stems = sorted(set(stem))
    for s in unique_stems:
        leaves = sorted([leaf[i] for i in range(len(stem)) if stem[i] == s])
        table += f"{s} | {', '.join(map(str, leaves))}\n"
        new_stem.extend([s]*len(leaves))
        new_leaf.extend(leaves)
    return table.strip(), new_stem, new_leaf

def generate_random_upper(numbers):
    if random.random()<0.15:
        threshold = random.randint(0, min(numbers) + 1)
    elif random.random()<0.3:
        threshold = random.randint(max(numbers), 99)
    else:
        threshold = random.randint(min(numbers), max(numbers))
    return threshold

def generate_random_lower(numbers):
    if random.random()<0.3:
        threshold = random.randint(0, min(numbers) + 1)
    elif random.random()<0.15:
        threshold = random.randint(max(numbers), 99)
    else:
        threshold = random.randint(min(numbers), max(numbers))
    return threshold

# 定义一个函数来创建问题
def create_questions(stem, leaf, times=10):
    '''生成九类问题:>, >=, <, <=, a<x<b, a<=x<b, a<x<=b, a<=x<=b, min, max, ='''
    questions = []
    numbers = [s * 10 + l for s, l in zip(stem, leaf)]
    table, stem, leaf = format_table(stem, leaf)
    print(f"new Stem: {stem}")
    print(f"new Leaf: {leaf}")
    min_value = min(numbers)
    max_value = max(numbers)

    def add_question(question, solution, answer):
        questions.append({
            "question": question,
            "choices": None,
            "table_title": "Stem-Leaf Plot",
            "table": table,
            "solution": "\n".join(solution),
            "answer": answer
        })

    def count_occurrences(condition):
        return sum(1 for n in numbers if condition(n))

    for i in range(times):
        # 统计特定数值的出现次数
        if random.random() < 0.1:
            count_value = random.randint(min_value, max_value)
        else:
            count_value = random.choice(numbers)

        answer = count_occurrences(lambda n: n == count_value)
        add_question(
            f"How many times does {count_value} appear in the stem-and-leaf plot?",
            [
                f"To determine how many times {count_value} appears in the stem-and-leaf plot, follow these steps:",
                f"1. **Identify the Relevant Stem and Leaf**: For the number {count_value}, the stem is {count_value // 10} and the leaf is {count_value % 10}.",
                f"2. **Count the Occurrences**: Count the total number of occurrences of the leaf {count_value % 10} in the stem {count_value // 10} row.",
                f"Therefore, exactly **{answer} items** have exactly {count_value}."
            ],
            answer
        )

        # 统计数值范围
        # 统计数值范围 (range_start <= n <= range_end)
        # range_start = random.randint(min(numbers), max(numbers) - 1)
        # range_end = random.randint(range_start, max(numbers))
        range_start = random.randint(0, max(numbers))
        range_end = random.randint(range_start, 99)
        counts = [
            sum(1 for j in range(len(stem)) if stem[j] == i and range_start <= i * 10 + leaf[j] <= range_end)
            for i in range(range_start // 10, range_end // 10 + 1)
        ]
        range_answer = sum(counts)
        if len(counts) > 1:
            counts_str = " + ".join(map(str, counts))
            total_count_str = f"{counts_str} = {range_answer}"
        else:
            total_count_str = f"{range_answer}"
        add_question(
            f"How many numbers are at least {range_start} and at most {range_end}?",
            [
                f"To determine how many numbers are at least {range_start} and at most {range_end} from the given stem-and-leaf plot, follow these steps:",
                f"1. **Identify the Relevant Stems**: Stems from {range_start // 10} to {range_end // 10} represent numbers between {range_start} and {range_end}.",
                f"2. **Analyze the Leaves**:",
                *[
                    f"- For stem {i}, count the leaves {[leaf[j] for j in range(len(stem)) if stem[j] == i and range_start <= i * 10 + leaf[j] <= range_end]} and there are {counts[idx]} leaves."
                    for idx, i in enumerate(range(range_start // 10, range_end // 10 + 1))
                ],
                f"3. **Aggregate the Counts**: Total count = {total_count_str}.",
                f"Therefore, there are exactly **{range_answer}** numbers between {range_start} and {range_end}."
            ],
            range_answer
        )


        # 统计数值范围 (range_start <= n < range_end)
        # range_start = random.randint(min(numbers), max(numbers) - 1)
        # range_end = random.randint(range_start + 1, max(numbers))
        range_start = random.randint(0, max(numbers))
        range_end = random.randint(range_start, 99)
        counts = [
            sum(1 for j in range(len(stem)) if stem[j] == i and range_start <= i * 10 + leaf[j] < range_end)
            for i in range(range_start // 10, range_end // 10 + 1)
        ]
        range_answer = sum(counts)
        if len(counts) > 1:
            counts_str = " + ".join(map(str, counts))
            total_count_str = f"{counts_str} = {range_answer}"
        else:
            total_count_str = f"{range_answer}"
        add_question(
            f"How many numbers are at least {range_start} but fewer than {range_end}?",
            [
                f"To determine how many numbers are at least {range_start} but fewer than {range_end} from the given stem-and-leaf plot, follow these steps:",
                f"1. **Identify the Relevant Stems**: Stems from {range_start // 10} to {range_end // 10} represent numbers between {range_start} and {range_end}.",
                f"2. **Analyze the Leaves**:",
                *[
                    f"- For stem {i}, count the leaves {[leaf[j] for j in range(len(stem)) if stem[j] == i and range_start <= i * 10 + leaf[j] < range_end]} and there are {counts[idx]} leaves."
                    for idx, i in enumerate(range(range_start // 10, range_end // 10 + 1))
                ],
                f"3. **Aggregate the Counts**: Total count = {total_count_str}.",
                f"Therefore, there are exactly **{range_answer}** numbers between {range_start} and {range_end}."
            ],
            range_answer
        )


        # 统计数值范围 (range_start < n < range_end)
        # range_start = random.randint(min(numbers), max(numbers) - 1)
        # range_end = random.randint(range_start + 1, max(numbers))
        range_start = random.randint(0, max(numbers))
        range_end = random.randint(range_start, 99)
        counts = [
            sum(1 for j in range(len(stem)) if stem[j] == i and range_start < i * 10 + leaf[j] < range_end)
            for i in range(range_start // 10, range_end // 10 + 1)
        ]
        range_answer = sum(counts)
        if len(counts) > 1:
            counts_str = " + ".join(map(str, counts))
            total_count_str = f"{counts_str} = {range_answer}"
        else:
            total_count_str = f"{range_answer}"
        add_question(
            f"How many numbers are greater than {range_start} but fewer than {range_end}?",
            [
                f"To determine how many numbers are greater than {range_start} but fewer than {range_end} from the given stem-and-leaf plot, follow these steps:",
                f"1. **Identify the Relevant Stems**: Stems from {range_start // 10} to {range_end // 10} represent numbers between {range_start} and {range_end}.",
                f"2. **Analyze the Leaves**:",
                *[
                    f"- For stem {i}, count the leaves {[leaf[j] for j in range(len(stem)) if stem[j] == i and range_start < i * 10 + leaf[j] < range_end]} and there are {counts[idx]} leaves."
                    for idx, i in enumerate(range(range_start // 10, range_end // 10 + 1))
                ],
                f"3. **Aggregate the Counts**: Total count = {total_count_str}.",
                f"Therefore, there are exactly **{range_answer}** numbers between {range_start} and {range_end}."
            ],
            range_answer
        )


        # 统计数值范围 (range_start < n <= range_end)
        # range_start = random.randint(min(numbers), max(numbers) - 1)
        # range_end = random.randint(range_start, max(numbers))
        range_start = random.randint(0, max(numbers))
        range_end = random.randint(range_start, 99)
        counts = [
            sum(1 for j in range(len(stem)) if stem[j] == i and range_start < i * 10 + leaf[j] <= range_end)
            for i in range(range_start // 10, range_end // 10 + 1)
        ]
        range_answer = sum(counts)
        if len(counts) > 1:
            counts_str = " + ".join(map(str, counts))
            total_count_str = f"{counts_str} = {range_answer}"
        else:
            total_count_str = f"{range_answer}"
        add_question(
            f"How many numbers are greater than {range_start} and at most {range_end}?",
            [
                f"To determine how many numbers are greater than {range_start} and at most {range_end} from the given stem-and-leaf plot, follow these steps:",
                f"1. **Identify the Relevant Stems**: Stems from {range_start // 10} to {range_end // 10} represent numbers between {range_start} and {range_end}.",
                f"2. **Analyze the Leaves**:",
                *[
                    f"- For stem {i}, count the leaves {[leaf[j] for j in range(len(stem)) if stem[j] == i and range_start < i * 10 + leaf[j] <= range_end]} and there are {counts[idx]} leaves."
                    for idx, i in enumerate(range(range_start // 10, range_end // 10 + 1))
                ],
                f"3. **Aggregate the Counts**: Total count = {total_count_str}.",
                f"Therefore, there are exactly **{range_answer}** numbers between {range_start} and {range_end}."
            ],
            range_answer
        )


        # 统计数值范围 (n < threshold)        
        # threshold = random.randint(min(numbers), max(numbers))
        threshold = generate_random_upper(numbers)
            
        counts = [
            sum(1 for j in range(len(stem)) if stem[j] == i and i * 10 + leaf[j] < threshold)
            for i in range(min(stem), threshold // 10 + 1)
        ]
        range_answer = sum(counts)
        if len(counts) > 1:
            counts_str = " + ".join(map(str, counts))
            total_count_str = f"{counts_str} = {range_answer}"
        else:
            total_count_str = f"{range_answer}"
        add_question(
            f"How many numbers are fewer than {threshold}?",
            [
                f"To determine how many numbers are fewer than {threshold} from the given stem-and-leaf plot, follow these steps:",
                f"1. **Identify the Relevant Stems**: Stems from {min(stem)} to {threshold // 10} represent numbers fewer than {threshold}.",
                f"2. **Analyze the Leaves**:",
                *[
                    f"- For stem {i}, count the leaves {[leaf[j] for j in range(len(stem)) if stem[j] == i and i * 10 + leaf[j] < threshold]} and there are {counts[idx]} leaves."
                    for idx, i in enumerate(range(min(stem), threshold // 10 + 1))
                ],
                f"3. **Aggregate the Counts**: Total count = {total_count_str}.",
                f"Therefore, there are exactly **{range_answer}** numbers fewer than {threshold}."
            ],
            range_answer
        )


        # 统计数值范围 (n <= threshold)
        # threshold = random.randint(min(numbers), max(numbers))
        threshold = generate_random_upper(numbers)
        counts = [
            sum(1 for j in range(len(stem)) if stem[j] == i and i * 10 + leaf[j] <= threshold)
            for i in range(min(stem), threshold // 10 + 1)
        ]
        range_answer = sum(counts)
        if len(counts) > 1:
            counts_str = " + ".join(map(str, counts))
            total_count_str = f"{counts_str} = {range_answer}"
        else:
            total_count_str = f"{range_answer}"
        add_question(
            f"How many numbers are at most {threshold}?",
            [
                f"To determine how many numbers are at most {threshold} from the given stem-and-leaf plot, follow these steps:",
                f"1. **Identify the Relevant Stems**: Stems from {min(stem)} to {threshold // 10} represent numbers at most {threshold}.",
                f"2. **Analyze the Leaves**:",
                *[
                    f"- For stem {i}, count the leaves {[leaf[j] for j in range(len(stem)) if stem[j] == i and i * 10 + leaf[j] <= threshold]} and there are {counts[idx]} leaves."
                    for idx, i in enumerate(range(min(stem), threshold // 10 + 1))
                ],
                f"3. **Aggregate the Counts**: Total count = {total_count_str}.",
                f"Therefore, there are exactly **{range_answer}** numbers at most {threshold}."
            ],
            range_answer
        )


        # 统计数值范围 (n >= threshold)
        threshold = generate_random_lower(numbers)
        counts = [
            sum(1 for j in range(len(stem)) if stem[j] == i and i * 10 + leaf[j] >= threshold)
            for i in range(threshold // 10, max(stem) + 1)
        ]
        range_answer = sum(counts)
        if len(counts) > 1:
            counts_str = " + ".join(map(str, counts))
            total_count_str = f"{counts_str} = {range_answer}"
        else:
            total_count_str = f"{range_answer}"
        add_question(
            f"How many numbers are at least {threshold}?",
            [
                f"To determine how many numbers are at least {threshold} from the given stem-and-leaf plot, follow these steps:",
                f"1. **Identify the Relevant Stems**: Stems from {threshold // 10} to {max(stem)} represent numbers at least {threshold}.",
                f"2. **Analyze the Leaves**:",
                *[
                    f"- For stem {i}, count the leaves {[leaf[j] for j in range(len(stem)) if stem[j] == i and i * 10 + leaf[j] >= threshold]} and there are {counts[idx]} leaves."
                    for idx, i in enumerate(range(threshold // 10, max(stem) + 1))
                ],
                f"3. **Aggregate the Counts**: Total count = {total_count_str}.",
                f"Therefore, there are exactly **{range_answer}** numbers at least {threshold}."
            ],
            range_answer
        )


        # 统计数值范围 (n > threshold)
        threshold = generate_random_lower(numbers)
        counts = [
            sum(1 for j in range(len(stem)) if stem[j] == i and i * 10 + leaf[j] > threshold)
            for i in range(threshold // 10, max(stem) + 1)
        ]
        range_answer = sum(counts)
        if len(counts) > 1:
            counts_str = " + ".join(map(str, counts))
            total_count_str = f"{counts_str} = {range_answer}"
        else:
            total_count_str = f"{range_answer}"
        add_question(
            f"How many numbers are greater than {threshold}?",
            [
                f"To determine how many numbers are greater than {threshold} from the given stem-and-leaf plot, follow these steps:",
                f"1. **Identify the Relevant Stems**: Stems from {threshold // 10} to {max(stem)} represent numbers greater than {threshold}.",
                f"2. **Analyze the Leaves**:",
                *[
                    f"- For stem {i}, count the leaves {[leaf[j] for j in range(len(stem)) if stem[j] == i and i * 10 + leaf[j] > threshold]} and there are {counts[idx]} leaves."
                    for idx, i in enumerate(range(threshold // 10, max(stem) + 1))
                ],
                f"3. **Aggregate the Counts**: Total count = {total_count_str}.",
                f"Therefore, there are exactly **{range_answer}** numbers greater than {threshold}."
            ],
            range_answer
        )


    # 寻找最小值
    add_question(
        "What is the smallest number in the dataset?",
        [
            f"The smallest number is the smallest stem and leaf combination in the stem-and-leaf plot.",
            f"1. **Find the Minimum Stem**: The smallest stem is {min_value // 10}.",
            f"2. **Find the Minimum Leaf**: The smallest leaf in the stem {min_value // 10} is {min_value % 10}.",
            f"Therefore, the smallest number is **{min_value}**."
        ],
        min_value
    )

    # 寻找最大值
    add_question(
        "What is the largest number in the dataset?",
        [
            f"The largest number is the largest stem and leaf combination in the stem-and-leaf plot.",
            f"1. **Find the Maximum Stem**: The largest stem is {max_value // 10}.",
            f"2. **Find the Maximum Leaf**: The largest leaf in the stem {max_value // 10} is {max_value % 10}.",
            f"Therefore, the largest number is **{max_value}**."
        ],
        max_value
    )

    return questions

def generate_stem_leaf_exercise(args):

    # 生成数据
    min_value = 0
    max_value = 99

    f_w=open(args.output_file_path, 'w')
    for i in range(args.tree_number):
        num_samples = random.randint(8, 50)
        stem, leaf = generate_stem_leaf_data(min_value, max_value, num_samples)
        print(f"org Stem: {stem}")
        print(f"org Leaf: {leaf}")

        # 创建问题
        questions = create_questions(stem, leaf, args.question_number)
        # 打印生成的问题和解答    
        for i, question in enumerate(questions):
            f_w.write(json.dumps(question, ensure_ascii=False) + '\n') # indent=2, 
            f_w.flush()  # 立即将结果写入文件
    f_w.close()

def main():
    import argparse
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description='create stem and leaf exercise by rules.')

    # 添加参数
    parser.add_argument('--tree-number', type=int, default=100 ,help='number of tree, including stem and leaf.')
    parser.add_argument('--question-number', type=int, default=10, help="number of questions in a stem and leaf")
    parser.add_argument('--output-file-path', type=str, help='the path of output file.')

    # 解析命令行参数
    args = parser.parse_args()
    generate_stem_leaf_exercise(args)


if __name__ == "__main__":
    main()
