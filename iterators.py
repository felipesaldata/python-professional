import time

class FiboIter():
    def __init__(self, max_numb:int):
        self.max_numb = max_numb


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):        
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            if self.aux >= self.max_numb:
                print(f"this program is limited to iterate until number {self.max_numb}")
                raise StopIteration                 
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
    
if __name__ == '__main__':
    fibonacci = FiboIter(47)
    for element in fibonacci:
        print(element)
        time.sleep(0.05) #each print wait 0.05 secs for a better understanding of the iteration