from chap_002_decision_tree.data_set import create_dataset_1, create_dataset_2


def split_data_set(data_set, axis, value):
    """
    切分数据集
    :param data_set: 二维数组数据集
    :param axis: 0
    :param value: 0 或 1
    :return:
    """
    ret_data_set = []
    for feat_vec in data_set:
        if feat_vec[axis] == value:
            reduced_feat_vec = feat_vec[:axis]
            reduced_feat_vec.extend(feat_vec[axis + 1:])
            ret_data_set.append(reduced_feat_vec)
    return ret_data_set


def _test_append_and_extend():
    a = [1, 2, 3]
    b = [4, 5, 6]
    print("a is: {}".format(a))
    print("b is: {}".format(b))
    _a = a[:]
    _a.append(b)
    print("a.append(b) is: {}".format(_a))
    _a = a[:]
    _a.extend(b)
    print("a.extend(b) is: {}".format(_a))


if __name__ == '__main__':
    # _test_append_and_extend()
    ds1, labels1 = create_dataset_1()
    ds2, labels2 = create_dataset_2()
    res00 = split_data_set(ds1, 0, 1)
    res01 = split_data_set(ds1, 0, 0)
    res10 = split_data_set(ds2, 0, 1)
    res11 = split_data_set(ds2, 0, 0)
    print(res00)
    print(res01)
    print(res10)
    print(res11)
