#Trả lời câu 1 chương 2
import math
try:
    r=float(input("Nhap ban kinh r: "))
    cv=2*math.pi*r
    dt=r**2
    print("Chu vi hinh tron la: ",round(cv))  
    print("Dien tich hinh tron la: ",round(dt))
except:
    print("Ban da nhap sai gia tri")