number=int(input("Enter the number :"))
power=int(input("Enter the power of number :"))
class Power:
    def power(self,num1,num_range):
        if num1==0 and num_range==0:
            return "undefined"
        else:
            ans=1
            for i in range(num_range):
                ans=ans*num1
            return ans
pow=Power()
answer=pow.power(number,power)
print("Power of number is ",answer)

