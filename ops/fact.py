def fact(x: int) -> int:
    """
    x를 팩토리얼 계산합니다.

    Args:
        x: 팩토리얼 연산 숫자

    Returns:
        팩토리얼 연산 결과

    Raises:
        ValueError: x는 0이나 음수가 될 수 없습니다.
    """
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers or zero.")

    if x is not int:
        print("x is not int, calculator will convert it to int")
        x = int(x)

    result = 1
    for i in range(1, x + 1):
        result *= i
    return result