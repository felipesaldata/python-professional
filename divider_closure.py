def make_division_by(n):
    def divider(x):
        assert type(x) == float or int, "Solo puedes utilizar números"
        assert n != 0, "en esta realidad no podemos dividir entre 0 :c"
        return x/n
    return divider

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    division_by_18 = make_division_by(18)
    print(division_by_18(54))


if __name__ == '__main__':
    run() 