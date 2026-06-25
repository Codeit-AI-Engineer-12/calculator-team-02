def floor_divide(a, b):
    """
    정수 나눗셈(몫)을 수행하는 함수

    Args:
        a (int or float): 나눠지는 수
        b (int or float): 나누는 수

    Returns:
        int: a를 b로 나눈 몫

    Raises:
        ValueError: b가 0일 경우
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")

    return a // b
