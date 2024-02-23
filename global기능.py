def print_counter():
    global counter #집안에있는 counter가 아니라 집 밖에 있는 counter가 동일하게 출력된다.
    counter = 200
    print('counter in house =', counter)

counter = 100 # => 200
print_counter()
print('counter on woeld =', counter)
