#다중 상속

class Animal:
    def move(self):
        pass

class Dog(Animal): #Animal을 상속받는 단일 상속
    name = "개"
    
    def move(self):
        print("개는 낮에 돌아다님")

class Cat(Animal):
    name = "냥이"

    def move(self):
        print("고양이는 밤에 움직임")
        print("눈빛이 빛남")

class Wolf(Dog, Cat): #Dog과 Cat을 상속받는 다중 상속
    pass

class Fox(Cat, Dog):

    def move(self):
        print("나는 여우야")

    def foxMethod(self):
        print("Fox 고유 메소드")

dog = Dog()
print(dog.name)
dog.move()
print("-----------------")
cat = Cat()
print(Cat.name)
cat.move()
print("-----------------")
wolf = Wolf()
wolf.move()
print(wolf.name)
print("-----------------")
print(Wolf.__mro__) #Wolf 클래스의 탐색 순서 Dog을 먼저 상속해서 Dog을 먼저 찾음
print("-----------------")
fox=Fox()










