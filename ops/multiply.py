def multiply(a, b):
    """
    두 자연수를 곱한 결과를 반환한다.

    Args:
        a (int): 첫 번째 수
        b (int): 두 번째 수

    Returns:
        int: 곱셈 결과
    """

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("자연수(정수)만 입력 가능합니다.")

    if a < 0 or b < 0:
        raise ValueError("자연수(0 이상)만 입력 가능합니다.")

    return a * b
