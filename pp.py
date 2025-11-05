print("if num == 1:\n    return False")
for i in range(500, 1001):
    if i % 2 == 0:
        print(f"elif num == {i}:\n    return True")
    else:
        print(f"elif num == {i}:\n    return False")