def minimum(a, b):
    """두 자연수를 입력받아 더 작은 값을 반환합니다."""
    if a <= 0 or b <= 0:
        raise ValueError("자연수만 입력할 수 있습니다.")
    return min(a, b)