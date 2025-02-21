a = float(input())
x = float(input())
b = float(input())
y = float(input())
s_re=a+b
s_im=x+y
print(f"Sum: {s_re}+{s_im}i")
pr_re = (a*b)-(x*y)
pr_im = (a*y)+(x*b)
print(f"Product: {pr_re}+{pr_im}i")
