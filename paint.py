# Test
from point import Point

def bound_class_method():
    # 직접 인스턴스 명시 -> 멤버에 접근
    p = Point()
    p.setX(10)
    p.setY(20)
    print(p.getX(), p.getY(), sep=",")

def unbound_class_method():
    # 클래스에 인ㅅ턴스를 전달해서 인스터스 내부에 메서드 호출
    p = Point()
    Point.setX(p, 10)
    Point.setY(p, 20)
    print(Point.getX(p), Point.getY(p))
    print(Point.getX, Point.getY)
    # Point class 내의 함수

def class_member_test():
    p1 = Point()
    p1.setX(10)
    p1.setY(20)

    print("p1: {}, {}".format(p1.getX(), p1.getY()))
    print("instance_count:",
          p1.instance_coount, # 인스턴스에서 접근 가능
          Point.instance_coount) # 인스턴스 없이도 접근 가능
if __name__ == "__main__":
    # bound_class_method()
    # unbound_class_method()
    class_member_test()