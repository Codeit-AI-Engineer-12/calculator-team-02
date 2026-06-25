def power(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("자연수(정수)만 입력 가능합니다.")
    if a < 0 or b < 0:
        raise ValueError("자연수(0 이상)만 입력 가능합니다.")
    if a == 0 and b == 0:
        raise ValueError("0의 0승은 정의되지 않습니다.")
    return a**b
