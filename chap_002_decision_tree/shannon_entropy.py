from math import log


def shannon_entropy(data_set):
    num_entries = len(data_set)  # len() 将获取二维数组的第一维个数
    label_counts = {}
    for feat_vec in data_set:
        current_label = feat_vec[-1]  # 获取最后一个值。
        # 为相同 label 出现次数做统计，记录在 label_counts 这个 dict 里。
        if current_label not in label_counts.keys():
            label_counts[current_label] = 0
        label_counts[current_label] += 1
    # 按照公式计算香农熵
    shannon_ent = 0.0
    for key in label_counts:
        prob = float(label_counts[key]) / num_entries
        shannon_ent -= prob * log(prob, 2)
    return shannon_ent


def create_dataset_1():
    data_set = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ]
    labels = ['no surfacing', 'flippers']
    return data_set, labels


def create_dataset_2():
    data_set = [
        [1, 1, 'maybe'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ]
    labels = ['no surfacing', 'flippers']
    return data_set, labels


if __name__ == '__main__':
    ds1, labels1 = create_dataset_1()
    shannon_ent_1 = shannon_entropy(ds1)
    print(shannon_ent_1)

    ds2, labels2 = create_dataset_2()
    shannon_ent_2 = shannon_entropy(ds2)
    print(shannon_ent_2)
