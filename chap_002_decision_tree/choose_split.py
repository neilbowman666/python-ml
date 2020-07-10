from chap_002_decision_tree.data_set import create_dataset_1
from chap_002_decision_tree.shannon_entropy import shannon_entropy
from chap_002_decision_tree.split_dataset import split_data_set


def choose_best_feature_to_split(data_set):
    """
    从最佳的特征以拆分成决策树
    尽量选择与原始香农熵相差大的子集作为拆分依据
    :param data_set:
    :return:
    """
    num_features = len(data_set[0]) - 1
    base_entropy = shannon_entropy(data_set)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_features):
        feat_list = [example[i] for example in data_set]
        unique_values = set(feat_list)
        new_entropy = 0.0
        for value in unique_values:
            sub_data_set = split_data_set(data_set, i, value)
            prob = len(sub_data_set) / float(len(data_set))
            new_entropy += prob * shannon_entropy(sub_data_set)  # 计算期望
        info_gain = base_entropy - new_entropy
        # print("base_entropy={}, new_entropy={}, info_gain=base_entropy-new_entropy={}, i={}".format(
        #     base_entropy,
        #     new_entropy,
        #     info_gain,
        #     i
        # ))
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature


if __name__ == '__main__':
    ds1, labels1 = create_dataset_1()
    print(choose_best_feature_to_split(ds1))
