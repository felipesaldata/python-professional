def is_prime(number: int) -> str:
    operations = [x for x in range(2, number) if number % x == 0]
    if len(operations) == 0:
        result = "your number is prime / tu número es primo"
    else:
        result = "your number is not prime / tu número no es primo"
    return print(result)
        
def run():
    try:
        number: int = is_prime(int(input("Insert a integer number / Ingresa un número entero:")))
    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    run()