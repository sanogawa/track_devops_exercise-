def add(a, b, c=0):
  
    # a, b, c が数値型（int もしくは float）かどうかを確認
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        return -1
    
    # a, b, c が 0 ≤ x ≤ 10 の範囲内にあるか確認
    if not all(0 <= i <= 10 for i in [a, b, c]):
        return -2
    
    try:
        # a, b, c を合計して整数型に変換して返す
        return int(a + b + c)
    except:
        # 万が一の例外処理
        return "error"

  
#  try:
#    return int(a + b) + int(c)
#  except:
#    return "error"
