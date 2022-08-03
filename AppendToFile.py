f = open("demo.txt", "a")

f.write("\nhello")
text = "\nhope you are doing well"

for i in range (0,5):
    f.write(text)

f.close()