def add(a, b):
    """
    두 자연수를 더하는 함수

    Args:
        a (int): 첫 번째 자연수
        b (int): 두 번째 자연수

    Raises:
        TypeError: _description_
        ValueError: _description_

    Returns:
        int: a와 b를 더한 합계
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("자연수(정수)만 입력 가능합니다.")
    if a < 0 or b < 0:
        raise ValueError("자연수(0 이상)만 입력 가능합니다.")
    return a + b
