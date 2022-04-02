#두 개의 가전제품 클래스의 부모 클래스를 만들고 메소드를 override하기 안 해도 상관 X

class ElecProduct: #독립적으로는 의미가 없음 상속받는 자식 클래스가 override해야 의미가 있음
    volume = 0
    
    def volumeCcontrol(self, volume):
        pass

class ElecTv(ElecProduct):
   
    def volumeControl(self, volume): #부모 클래스의 volume을 overriding 안 해도 상관 X 다형성만 못 씀
        self.volume += volume #생성된 객체의 volume에 volume 누적
        print("TV소리 크기 : ", self.volume)

class ElecRadio(ElecProduct):
   
    def volumeControl(self, volume):
        vol = volume
        self.volume += vol #생성된 객체의 volume에 volume 누적
        print("라디오 소리 크기 : ", self.volume)

    def showProduct(self):
        print("라디오 만세")


tv = ElecTv()
tv.volumeControl(5)
tv.volumeControl(-2)
print()
radio = ElecRadio()
radio.volumeControl(7)
radio.showProduct()

print("-----다형성-----") #객체 지향적 언어라서 이렇게 사용 가능 높은 기술력이 생길 때는 반드시 사용됨
product = tv
product.volumeControl(10)
product = radio
product.volumeControl(7)

