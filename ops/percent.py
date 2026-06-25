def percent(a: int | float, b: int | float) -> float:
    """
    a의 b%를 구합니다.

    Args:
        a: 대상 숫자
        b: %

    Returns:
        a의 b% 연산 결과
    """
    return a / 100 * b