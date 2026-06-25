def avg(a: int | float, b: int | float) -> float:
    """
    a와 b의 평균값을 계산합니다.

    Args:
        a: 첫번째 숫자
        b: 두번째 숫자

    Returns:
        a와 b의 평균값
    """
    try:
        return (a + b) / 2
    except TypeError as e:
        raise TypeError(f"Argument is not numeric: {e}") from e
    except OverflowError as e:
        raise OverflowError(f"Numerical overflow: {e}") from e