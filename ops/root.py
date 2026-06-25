def root(a: int | float, b: int | float) -> float | complex:
    """
    a를 b로 거듭제곱근합니다.
    
    Args:
        a: 첫번째 숫자
        b: 두번째 숫자
        
    Returns:
        a를 b로 거듭제곱근(root) 연산한 결과

    Raises:
        ValueError: a가 음수이고 b가 짝수인 경우
    """
    try:
        if a < 0 and b % 2 == 0:
            raise ValueError("arg1 cannot be negative and arg2 must be odd")
        return a ** (1 / b)
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"arg2 cannot be zero: {e}") from e
    except TypeError as e:
        raise TypeError(f"Argument is not numeric: {e}") from e
    except OverflowError as e:
        raise OverflowError(f"Numerical overflow: {e}") from e