def overlap(i1, i2):
    """
    :type i1: List[]
    :type i1: List[]
    :rtype: boolean
    """
    front = i1
    end = i2

    if i1[0] > i2[0]:
        front = i2
        end = i1

    return (front[0] <= end[0] and front[1] >= end[1]) or \
        (front[0] <= end[0] and front[1] > end[0]) or \
        (front[1] == end[0])
