m = int(input("Enter marks obtained in Mathematics : "))
p = int(input("Enter marks obtained in Physics : "))
c = int(input("Enter marks obtained in Chemistry : "))
average =(m+p+c)/3
if m<35 or p<35 or c<35:
    print("Failed")
elif average <= 59:
    print("Grade C")
elif average <= 69:
    print("Grade B")
elif average >69:
    print("Grade A")