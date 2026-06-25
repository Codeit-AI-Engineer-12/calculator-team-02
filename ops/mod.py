def mod(a, b):
    """
    a를 b로 나머지 연산합니다.

    Args:
        a: 첫번째 숫자
        b: 두번째 숫자

    Returns:
        a를 b로 나머지 연산합니다.
    """
    try:
        return a % b
    except TypeError as e:
        raise TypeError(f"Argument is not numeric: {e}") from e
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"Cannot modulo by zero: {e}") from e