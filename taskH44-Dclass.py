#Задание на выбор или дополнительное про классы (тема 10ого семинара)|
#Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы:
#рост, огнеопасность, цвет.

#Класс обеспечивает выполнение методов (dr — экземпляр класса)
#экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту
#экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:

#цвет меньший по алфавиту;
#рост - среднее арифметическое из двух округлённое до целого вниз,
#огнеопасность - большее из двух;

#из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая честь от деления роста на число, к
#огнеопасности прибавляется остаток от деления огнеопасности на число;

#Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное
#значению атрибута огнеопасность;

#change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет

#str- возвращает строку:
#Dragon with height «рост», danger <огнеопасность> and color «цвет».

repr- возвращaет строку:
Dragon(‹рост>, <огнеопасность>, <цвет>)

Пример

dr = Dragon(69, 5, “brown™)
dr1 = Dragon(69, 5, “gray")
print (dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n")
print()

dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr+dr1
print(dr, dr1, dr2, sep="\n")

print(dr("Welcome")

Вывод

False True True
Dragon with height 69, danger 5 and color brown.
Dragon with height 69, danger 5 and color gray.

Dragon with height 66, danger 10 and color white.
Dragon with height 35, danger 6 and color gray.
Dragon with height 50, danger 10 and color brown.
WelcomeWelcomeWelcomeWelcomeWelcome


"""класс Dragon """
# 1 > инициализации переменных аргументов
   def __init__(self, height, danger, color):   
      self.name = name
      self.height = height
      self.danger = danger
      self.color = color

# 2 > сравнение объектов
   """ Возвращает True, если текущий объект больше, чем объект other"""     
   def __gt__(self, other):
      return self.height > other.height and self.danger > other.danger and self.color > other.color  

   """ Возвращает True, если текущий объект больше или равен объекту other"""
   def __ge__(self, other):
      return self.height >= other.height and self.danger >= other.danger and self.color >= other.color

   """ Возвращает True, если текущий объект равен объекту other"""
   def __eq__(self, other):                 
      return self.height==other.height and self.danger==other.danger and self.color==other.color
     
   """ Возвращает True, если текущий объект не равен объекту other"""
   def __ne__(self, other):
      return self.height!=other.height and self.danger!=other.danger and self.color!=other.color    

   """Возвращает True, если текущий объект меньше, чем объект other"""
   def __lt__(self, other):
      return self.height < other.height and self.danger < other.danger and self.color < other.color 

   """Возвращает True, если текущий объект меньше или равен объекту other"""
   def __le__(self, other):
      return self.height <= other.height and self.danger <= other.danger and self.color <= other.color   

# 3 > результат суммирования двух объектов
   def __add__(self, other):              
      import math
      if type(other) == Dragon:
         height_new = int((self.height + other.height)/2)
         height_new = math.floor((self.height + other.height)/2)
         danger_new = max(self.danger, other.danger)
         color_new = min(self.color, other.color)
         dr2 = Dragon(height_new, danger_new, color_new)
         return dr2
            
   """Возвращает результат вычитания двух объектов"""   
#4 > Возвращает результат вычитания числа из объекта 
    def __sub__(self, number):          
       if type(number) == int or type(number) == float: 
          height_new =self.height - int((self.height)/number)
          danger_new = self.danger + self.danger % number
       return f"результат вычитания >>> Dragon with height {height_new}, danger {danger_new} and color {self.color}"  
       else:
          print('Введено не число!')

   """метод __call__вызывается при вызове объекта как функции"""
    
#5 > повторение аргумента-строки <danger>-раз
   def __call__(self, string):          
      if self.danger !=0:
         return string * self.danger
      else:
         print(f'нет возврата строки: т.к. атрибут <danger> ={self.danger}')

# 6 > замена текущего цвета
   def change_color(self, color):       
      self.color = color
      return print(f'цвет успешно заменен > {self.__str__()}')

# 7 >  str- возвращает строку:
   def __str__(self):                   
      return f'Dragon with height {self.height}, danger {self.danger} and color {self. color} ' 

# 8 > rept- возвращает строку
   def __repr__(self):                
      return f'Dragon({self.height}, {self.danger}, {self. color})'  
