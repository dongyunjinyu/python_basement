import sympy as sym

# 常数
I = sym.I  # 虚数单位
print(sym.sqrt(-1) ** 2)  # -1
E = sym.E  # 自然对数的底
print(sym.ln(E))  # 1
oo = sym.oo  # 正无穷大
print(1 / oo)  # 0
pi = sym.pi  # 圆周率
print(sym.sin(pi / 2))  # 1

# 初等基本函数   能算则算，否则返回自身
print(sym.sqrt(-4))  # 2*I
print(sym.root(8, 3))  # 2     幂在右
print(sym.exp(0))  # 1
print(sym.ln(E))  # 1
print(sym.log(8, 2))  # 3    底数在右
print(sym.atan(6))  # atan(6)
print(sym.factorial(6))  # 720

# 一元函数
x = sym.Symbol('x')  # 定义自变量
f1 = 2 * x + 1  # 声明数学函数（表达式）
print(f1)  # 2*x + 1
print(f1.evalf(subs={x: 2}))  # 5.00000000000000

# 分段函数
x = sym.Symbol('x')
f2 = sym.Piecewise((-x, x < 0), (x, x >= 0))

# 多元函数
x, y = sym.symbols('x y')  # 注意和一元函数声明方法不一样
f3 = sym.exp(x + 3) - sym.ln(y - 1)
print(f3.evalf(subs={x: sym.ln(3) - 3, y: E + 1}))  # 2.00000000000000

# 解方程
x = sym.Symbol('x')
print(sym.solve(x ** 3 - 1, x))  # [1,-1/2-sqrt(3)*I/2,-1/2+sqrt(3)*I/2]
print(sym.solve(sym.exp(x) - 3, x))  # [log(3)]
print(sym.solve(f3, x))  # [log(log(y - 1)) - 3]   使用了上面定义的f2

# 解方程组
x1, x2, x3, x4, x5 = sym.symbols('x1:6')  # 序列定义
ff1 = x1 + 3 * x2 + 5 * x3 - 4 * x4 - 1
ff2 = x1 + 3 * x2 + 2 * x3 - 2 * x4 + x5 + 1
ff3 = x1 - 2 * x2 + x3 - x4 - x5 - 3
ff4 = x1 - 4 * x2 + x3 + x4 - x5 - 3
ff5 = x1 + 2 * x2 + x3 - x4 + x5 + 1
print(sym.solve([ff1, ff2, ff3, ff4, ff5], [x1, x2, x3, x4, x5]))
# {x1: -x5/2, x2: -x5/2 - 1, x3: 0, x4: -x5/2 - 1}  这个线性方程组不满秩

# 求和
i = sym.Symbol('i', integer=True)
print(sym.summation(sym.factorial(i), (i, 1, 10)))
# 4037913   第一个参数是要求和的表达式，第二个是上下标，前闭后闭

# 求单侧极限
x = sym.Symbol('x')
print(sym.limit((1+x)**(1/x), x, 0, dir='+'))  # E
print(sym.limit(sym.atan(x), x, oo))  # pi/2
f4 = sym.Piecewise((-x, x < 0), (x+2, x >= 0))
print(sym.limit(f4, x, 0))  # 2    默认求右极限
print(sym.limit(f4, x, 0, dir='-'))  # 2  特性，函数右连续则用右极限代替左极限
f5 = sym.Piecewise((1/x, x != 0), (0, x == 0))
print(sym.limit(f5, x, 0, dir='+-'))  # zoo  表示正负无穷







""" 解一阶常微分方程 """
# f = sym.symbols('f', cls=sym.Function)  # 定义函数标识符
# x = sym.symbols('x')  # 定义变量
# eq = sym.Eq(sym.diff(f(x), x, 1), x)  # 构造等式，即dy/dx=y
# # diff(函数,自变量,求导次数)
# print(sym.dsolve(eq, f(x)))
# print('#######################')
# sym.pprint(sym.dsolve(eq, f(x)))  # 以"pretty"形式打印方程的解
