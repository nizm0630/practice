# list[시작값 : 끝값 : step]

list1 = list(range(20))

# new_list가 5, 8, 11, 14의 값을 가지도록 list1을 slice
new_list = list1[5:15:3]
print(new_list)

# reverse_list가 17, 13, 9, 5의 값을 가지도록 list1을 slice
reverse_list = list1[17:4:-4]
print(reverse_list)
