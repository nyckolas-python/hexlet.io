class Counter:
    value = int(0)
# Именно через аргумент self метод получает доступ к атрибутам связанного объекта 
# (и его класса, конечно же).
    def inc(self, delta=1):
        if self.value + delta >= 0:
            self.value += delta 
        else: self.value = 0
        return self.value
    
    def dec(self, delta=1):
        if self.value - delta >= 0:
            self.value -= delta 
        else: self.value = 0
        return self.value

c = Counter()
c.inc()
c.inc()
c.inc(40)
print(c.value) # 42
c.dec()
c.dec(30)
print(c.value) # 11
c.dec(delta=100)
print(c.value) # 0