from ops.percent import percent

def cal_tip(price, tip_rate, num_people: int):
    """
    인당 팁 금액을 계산합니다.
    
    Args:
        price: 총 금액
        tip_rate: 팁 비율
        num_people: 인원 수
    """
    try:
        tip_amount = percent(price, tip_rate)
        return tip_amount / num_people
    except ZeroDivisionError as e:
        raise ZeroDivisionError("num_people cannot be zero") from e