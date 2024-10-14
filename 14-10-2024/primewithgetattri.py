class Primenumber:
    def prime(self,num):
        if num<2:
            return False
        for i in range(2,num):
            if num%i==0:
                return False
        return True

    def prime_in_range(self,start, end): 
        for num in range(start, end + 1): #iterate through start and end
            if getattr(self,'prime')(num):
                print(num,end=" ")

# Input
start = int(input("Enter the start of the range:"))
end = int(input("Enter the end of the range: "))

prime_obj=Primenumber()

# Finding and printing prime numbers in the range
print(f"Prime numbers between {start} and {end} are:")
prime_obj.prime_in_range(start, end)
