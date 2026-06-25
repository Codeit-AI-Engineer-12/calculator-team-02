def floor_divide(a, b):
    """
    정수 나눗셈을 수행하는 함수

    Args:
        a (int): 나눠지는 수
        b (int): 나누는 수

    Raises:
        ValueError: 나누는 수가 0일 경우

    Returns:
        int: 정수 나눗셈의 결과
    """
    if b == 0:
        raise ValueError("0으로는 나눌 수 없습니다.")
    return a // b
