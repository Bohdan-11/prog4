#Шаблон Адаптер на примере температур

from abc import ABC, abstractmethod

#interface
class Temperature (ABC):
    @abstractmethod
    def get_kelvin(self) -> float:
        pass

#исходная работа кода
class Kelvin(Temperature):
    def __init__(self, kelvin):
        self.kelvin = kelvin
    def get_kelvin(self) -> float:
        return self.kelvin
        

#Инструменты (Adatee)
class Cels:
    def __init__(self, value: float):
        self.value = value
    def get_celsius(self) -> float:
        return self.value

class Far:
    def __init__(self, value: float):
        self.value = value
    def get_faherenheit(self) -> float:
        return self.value
   
#Адаптеры
class CelsAdapter(Temperature):
    def __init__(self, celsius = Cels):
        self._celsius = celsius
    def get_kelvin(self) -> float:
        return self._celsius.get_celsius() + 273.15
    
class FarAdapter(Temperature):
    def __init__(self, fahrenheit = Far):
        self._fahrenheit = fahrenheit
    def get_kelvin(self) -> float:
        return (self._fahrenheit.get_faherenheit()-32)*5/9 + 273.15


p = 101325
V = 50
nu = 2085
R = 8.31
#клиент
class TemperatureProcessor:
    def process(self, temp: Temperature):
        T = temp.get_kelvin()
        print(f"processing at {T}K\n")
        
        #p*V=nu*R*T
        p1 = (nu*R*T)/V
        V1 = (nu*R*T)/p
        nu1 = (p*V)/(R*T)
        print(f"p = {p1}, при V = {V}, nu = {nu}\n")
        print(f"V = {V1}, при p = {p}, nu = {nu}\n")
        print(f"nu = {nu1}, при V = {V}, p = {p}\n------------------------------------\n")
        
        
        
        
        
        
k = 300
c = 22
f = 71.6
processor = TemperatureProcessor()

#вызов стандартного функционала
processor.process(Kelvin(k))

#вызов через цельсия
processor.process(CelsAdapter(Cels(c)))

#вызов через фарингейт
processor.process(FarAdapter(Far(f)))

