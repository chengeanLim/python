def print_counter():
    global counter
    counter = 200
    print('counter in house=', counter)

def calculate_area(radius):
    global area
    area = 2.14*radius**2

area =0
r= float(input("원의 반지름 :"))
calculate_area(r)
print(area)

