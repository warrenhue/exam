def reverser(s: str, k: int):
    result = []
    for i in range(0, len(s), 2 * k):
        chunk = s[i : i + 2 * k]
        first_k = chunk[:k]
        rest   = chunk[k:]
        result.append(first_k[::-1] + rest)
    return "".join(result)

print(reverser(input(), int(input())))