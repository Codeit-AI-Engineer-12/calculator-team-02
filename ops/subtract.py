def subtract(a, b):
    """
    a를 b로 뺍니다.
    :param a: arg1
    :param b: arg2
    :return: a - b
    """
    try:
        return a - b
    except TypeError as e:
        raise TypeError(f"Argument is not numeric: {e}") from e
    except OverflowError as e:
        raise OverflowError(f"Result got overflowed: {e}") from e
