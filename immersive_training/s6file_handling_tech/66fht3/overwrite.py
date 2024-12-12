""""""
f = open("demo.txt", "w")
f.write("------------A new content!!!--------")
f.close()

#open and read
f = open("demo.txt","r")
print(f.read())
print("----------finished writing then read the file--------")

