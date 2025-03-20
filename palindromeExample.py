class MyMath:
    @staticmethod
    def is_prime(n: int) -> bool:
        return len([i for i in range(1,n+1) if n%i==0])==2
    @staticmethod
    def is_palindrome(n: int) -> bool:
        return str(n) == str(n)[::-1]
print(MyMath.is_prime(10))
print(MyMath.is_prime(17))
print(MyMath.is_palindrome(121))
print(MyMath.is_palindrome(123))
