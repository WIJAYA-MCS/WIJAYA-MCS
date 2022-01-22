# fruits = ["Mangga", "Apple", "Durian"]
# for buah in fruits: # jumlah pengulangannya sudah diketahui ==> for loop
#     print(buah)

# nomor = [1, 2, 3, 4, 5]
# for num in nomor:
#     print(num) 

# # range function yg mengurutkan angka ke asalnya

# x = range(6) # dimulai dari nol, maka pengulangannya 0,1,2,3,4,5
# for i in x:
#     print(i)

# x = range(20)
# for i in x:
#     print(i)

# x = range(1, 20, 3)
# for i in x:
#     print(i)

# while loop pengulangan untuk eksekusi statement sepanjang True
# while True:
#     print("Hello, World")

# while 3 == 3:
#     print("Hello, World!")

# i = 1
# while i < 6:
#     # i +=1 artinya i+1
#     print(i) 
#     i +=1

# while True:
#     pass

# for i in range (5):
#     if i ==3:
#         continue
#     print(i)

# for i in range (5):
#     if i ==3:
#         break
#     print(i)

adj_list = ["Murah", "Enak", "Bagus"]
fruit_list = ["Apel", "Mangga", "Durian"]

for i in fruit_list:
    for j in adj_list:
        print(i+ " " + j)