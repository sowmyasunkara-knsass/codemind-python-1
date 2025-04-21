r1 = float(input("Enter the real part of the first complex number: "))
c1 = float(input("Enter the imaginary part of the first complex numuber: "))
r2 = float(input("Enter the real part of the second complex number: "))
c2 = float(input("Enter the imaginary part of the second complex number: "))
sum_real = r1+r2
sum_imag = c1+c2
print(f"Sum: {sum_real} + {sum_imag}i")
pro_real = (r1*r2)-(c1*c2)
pro_imag = (r1*c2)+(c1*r2)
print(f"Product: {pro_real} + {pro_imag}i")
