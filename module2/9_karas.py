def calculate_polynomial(coefficients, x):
    n = len(coefficients) - 1
    result = 0
    for i in range(n + 1):
        term = coefficients[i] * (x ** (n - i))

        if abs(term) > 2000000000 or abs(result + term) > 2000000000:
            return "Переповнення: значення перевищує 2 000 000 000"

        result += term
    return result


def main():
    coefficients = [-2, 2, 0, -1, 1, 2, 7]

    print("Коефіцієнти полінома:", end=" ")
    for coef in coefficients:
        print(coef, end=" ")
    print()

    try:
        x = float(input("Введіть дійсне число x: ").replace(',', '.'))
    except ValueError:
        print("Помилка: введіть коректне число")
        return

    result = calculate_polynomial(coefficients, x)

    if isinstance(result, str):
        print(result)
    else:
        print(f"P({x}) = {result:.2f}")


if __name__ == "__main__":
    main()
