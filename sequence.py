def syracuse_sequence(n):
    """
    Function to build Syracuse sequence
    :param n: number for building sequence
    :return: list of sequence
    """
    p_list = list()
    p_list.append(n)
    if n == 0:
        return []
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            p_list.append(int(n))
        else:
            n = n * 3 + 1
            p_list.append(int(n))
    return p_list


def syracuse_max(n):
    """
    Function to find maximal element in Syracuse sequence
    :param n: number for building sequence
    :return: maximal element in Syracuse sequence
    """
    p_list = syracuse_sequence(n)
    max_n = 0
    for i in p_list:
        if i > max_n:
            max_n = i
    return max_n
