def subtract(a: int | float, b: int | float) -> int | float:
    """
    a를 b로 뺍니다.

    Args:
        a: 첫번째 숫자 (int or float)
        b: 두번째 숫자 (int or float)

    Returns:
        a에서 b를 뺀 연산 결과
    """
    try:
        return a - b
    except TypeError as e:
        raise TypeError(f"Argument is not numeric: {e}") from e
    except OverflowError as e:
        raise OverflowError(f"Result got overflowed: {e}") from e
