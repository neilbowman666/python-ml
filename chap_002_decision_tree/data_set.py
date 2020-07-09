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


def create_dataset_3():
    data_set = [
        [1, 1, 1, 'maybe'],
        [1, 1, 1, 'yes'],
        [1, 0, 0, 'no'],
        [0, 1, 1, 'no'],
        [0, 1, 0, 'no'],
    ]
    labels = ['no surfacing', 'flippers', 'swimming']
    return data_set, labels
