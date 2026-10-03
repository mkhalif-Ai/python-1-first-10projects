fee = 50
money_have = 320
months = 320/50
print(f"months: {months.__floor__()}")
print(f"remaining:${money_have%fee}")
