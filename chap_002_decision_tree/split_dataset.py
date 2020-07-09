from chap_002_decision_tree.data_set import create_dataset_1, create_dataset_2, create_dataset_3


def split_data_set(data_set, axis, value):
    """
    切分数据集：摘取目标位置为指定特征的新数据划分方案
    :param data_set: 二维数组数据集
    :param axis: 目标位置，如：0
    :param value: 目标位置的特征值，如：0 或 1
    :return:
    """
    ret_data_set = []
    for feat_vec in data_set:
        # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print("feat_vec is {}".format(feat_vec, ))
        # print("feat_vec[axis={}]={}, value={}, {}".format(
        #     axis, feat_vec[axis], value,
        #     "matching" if feat_vec[axis] == value else "not matching"))
        if feat_vec[axis] == value:
            # 这里已经将目标位置的数字排除
            reduced_feat_vec = feat_vec[:axis]
            reduced_feat_vec.extend(feat_vec[axis + 1:])
            # print("reduced_feat_vec is {}".format(reduced_feat_vec))
            # print("extending reduced_feat_vec for feat_vec[axis+1={}:] = {}".format(axis + 1, feat_vec[axis + 1:]))
            ret_data_set.append(reduced_feat_vec)
    # print("===================================================================")
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
    ds3, labels3 = create_dataset_3()
    res00 = split_data_set(ds1, 0, 1)
    res01 = split_data_set(ds1, 0, 0)
    res10 = split_data_set(ds2, 0, 1)
    res11 = split_data_set(ds2, 0, 0)
    res3 = split_data_set(ds3, 2, 1)
    print(res00)
    print(res01)
    print(res10)
    print(res11)
    print(res3)
