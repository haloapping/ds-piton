def print_fizzbuzz(n: int) -> str:
    if n <= 0:
        return "n must be greater than 0"

    words = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            words.append("fizzbuzz")
        elif i % 5 == 0:
            words.append("buzz")
        elif i % 3 == 0:
            words.append("fizz")
        else:
            words.append(str(i))

    return " ".join(words)


print(print_fizzbuzz(50))
