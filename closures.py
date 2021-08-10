#Hola 3 -> HolaHolaHola
#Felipe 4 -> FelipeFelipeFelipe

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas" #afirmamos que nos llega una string
        return string*n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_5("Felipe"))

if __name__ == '__main__':
    run() 