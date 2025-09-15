"""
Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
● Fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False
● Trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
● Eat(meal, value) – может принимать в meal только ”nectar” или
“grass”. Если съедает нектар, то value вычитается из части
слона, пчеле добавляется. Иначе – наоборот. Не может
увеличиваться больше 100 и уменьшаться меньше 0.
"""

from dataclasses import dataclass

@dataclass
class BeeElephant:
    __bee: int
    __elephant: int

    def fly(self):
        return self.__bee >= self.__elephant

    def trumpet(self):
        if self.__elephant >= self.__bee:
            return "tu-tu-doo-doo"
        return "wzzzz"

    def eat(self, meal, value):
        match meal:
            case "nectar":
                self.__bee += value
                self.__elephant -= value
                if self.__elephant < 0:
                    self.__elephant = 0
                if self.__bee > 100:
                    self.__bee = 100
            case "grass":
                self.__bee -= value
                self.__elephant += value
                if self.__elephant > 100:
                    self.__elephant = 100
                if self.__bee < 0:
                    self.__bee = 0

a = BeeElephant(100, 0)
print(a.fly())
print(a.trumpet())
a.eat("grass", 10)
