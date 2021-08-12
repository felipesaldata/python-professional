import time

def fibo_gen(max_num: int):
    n1, n2 = 0 , 1
    while n1 <= max_num:
        yield n1
        n1, n2 = n2, n1 + n2
    else:
        print(f"this program is limited to iterate until number {max_num}")    

if __name__ == '__main__':
    fibonacci = fibo_gen(47)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)
