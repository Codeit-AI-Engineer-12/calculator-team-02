def root(a, b):
    """
    a를 b로 거듭제곱근합니다.
    :param a: arg1
    :param b: arg2
    :return: 거듭제곱근 연산 결과
    """
    try:
        if a < 0 and b % 2 == 0:
            raise ValueError("arg1 cannot be negative and arg2 must be odd")
        return a ** (1/b)
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"arg2 cannot be zero: {e}") from e
    except TypeError as e:
        raise TypeError(f"Argument is not numeric: {e}") from e
    except OverflowError as e:
        raise OverflowError(f"Numerical overflow: {e}") from e