from numpy import tile, array
import operator


def create_data_set():
    """
    创建数据集及为其标定标签

    numpy.array() 数组有下面的属性：
    ndim        int32 数组维度
    shape       tuple 数组各维度大小
    size        元素总数
    dtype       元素数据类型
    itemsize    元素字节大小
    data        包含数组元素的缓冲区，一般用于索引访问素组元素

    :return:
    """
    _group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    _labels = ['A', 'A', 'B', 'B']
    return _group, _labels


def euclidean_knn_classify(in_x, data_set, labels, k):
    """
    欧几里得距离 KNN 核心检测函数

    KNN 算法优点：精度高、异常值不敏感、无数据输入假定；
    KNN 算法缺点：算法复杂度高、空间复杂度高；
    适用范围：数值型、标称型。

    :param in_x: 待测试数据
    :param data_set: 已有数据集
    :param labels: 已有数据集的标签
    :param k: 临近深度：有几个与之相近
    :return: 结果
    """
    data_set_size = data_set.shape[0]  # 这里传入一个矩阵，获取矩阵的行数
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set  # tile 构造一个只包含待测点的矩阵，减去已有的测试数据集中的所有点，得到待测点与所有点的坐标差
    # 关于 tile 的用法，参考：https://www.jianshu.com/p/4b74a367833c
    # 或者：https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.tile.html
    sq_diff_mat = diff_mat ** 2  # 双星号做乘方运算，这里算的是 diff_mat 的二次方。坐标差算二次方，这里是要计算欧几里得距离。
    sq_distances = sq_diff_mat.sum(axis=1)  # 坐标差矩阵行内求和，得到一个单列矩阵。
    distances = sq_distances ** 0.5  # 双星号做乘方运算，这里算的是 sq_distances 的 0.5 次方，也就是开根号。
    sorted_dist_indices = distances.argsort()  # 获取数组中从小到大的数据的索引值
    class_count = {}
    for i in range(k):  # 数据集中前 k 个距离近的数据数据有投票权
        vote_i_label = labels[sorted_dist_indices[i]]  # 按照从小到大的索引值去找最小的值，即找距离最近的前 k 个依次投票
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1  # 统计数据集中前 k 近的各个标签的投票结果
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    # operator.itemgetter(1) 表示 map 中按值排序：https://www.cnblogs.com/zhoufankui/p/6274172.html
    return sorted_class_count[0][0]


if __name__ == '__main__':
    group, labels = create_data_set()
    result = euclidean_knn_classify([0, 0], group, labels, 3)
    print(result)
