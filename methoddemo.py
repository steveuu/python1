class MethodDemo:
    a=1

    @classmethod
    def classM(cls):
        print('Class Method. cls.a = ', cls.a)

    @staticmethod
    def staticM():
        print('Static method.')

MethodDemo.classM()
MethodDemo.staticM()

md1=MethodDemo()
md1.classM()
