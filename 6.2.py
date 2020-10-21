class Vector3:
    # 构造方法，初始化，定义向量坐标
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    # 两个向量相加，对应分量相加，返回新向量
    def add(self, anotherPoint):
        x = self.__x + anotherPoint.__x
        y = self.__y + anotherPoint.__y
        z = self.__z + anotherPoint.__z
        return Vector3(x, y, z)

    # 减去另一个向量，对应分量相减，返回新向量
    def sub(self, anotherPoint):
        x = self.__x - anotherPoint.__x
        y = self.__y - anotherPoint.__y
        z = self.__z - anotherPoint.__z
        return Vector3(x, y, z)

    # 向量与一个数字相乘，各分量乘以同一个数字，返回新向量
    def mul(self, n):
        x, y, z, = self.__x * n, self.__y * n, self.__z * n
        return Vector3(x, y, z)

    # 向量与一个数字相乘，各分量乘以同一个数字，返回新向量
    def div(self, n):
        x, y, z, = self.__x / n, self.__y / n, self.__z / n
        return Vector3(x, y, z)

    # 查看各分量的值
    def neiji(self,anotherPoint):
        x = self.__x * anotherPoint.__x
        y = self.__y * anotherPoint.__y
        z = self.__z * anotherPoint.__z
        return x + y + z

    #计算向量的内积
    def show(self):
        print('X:{0}, Y:{1}, Z:{2}'.format(self.__x, self.__y, self.__z))

    # 查看向量长度，所有分量平方和的平方根
    @property
    def length(self):
        return (self.__x ** 2 + self.__y ** 2 + self.__z ** 2) ** 0.5


v = Vector3(3, 4, 5)
v1 = v.mul(3)
v1.show()
v2 = v1.add(v)
v2.show()
print(v2.length)
print(v2.neiji(v1))