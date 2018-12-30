def f1(n):
    print("A")
    return 2
print("B")
def f2():
    return 1
    print("c")
print(f1(f2()))



a = [42,39,123]
b = sorted(a,reverse=True)
a[0] = b
b[0] = 7
b.sort()
print(a)


class A:
    def f(self):
    return self.g()

    def g(self):
        return "A"
class B:
    def g(self):
        return "B"

a = A()
b = B()
print(a.f(),b.f())
print(a.g(),b.g())
