def water_jug_manual_path():
    steps = []
    a, b = 0, 0
    steps.append((a, b))
    a = 5
    steps.append((a, b))
    transfer = min(a, 4-b)
    a -= transfer
    b += transfer
    steps.append((a, b))
    b = 0
    steps.append((a, b ))
    transfer = min(a, 4-b)
    a -= transfer
    b += transfer
    steps.append((a, b))
    a = 5
    steps.append((a, b ))
    transfer = min(a, 4-b)
    a -= transfer
    b += transfer
    steps.append((a, b))
    b = 0
    steps.append((a, b ))
    print("Steps to reach (2, 0): ")
    for idx, state in enumerate(steps):
        print(f"Step {idx}: Jug1 = {state[0]}L, Jug2 = {state[1]} L")
water_jug_manual_path()
