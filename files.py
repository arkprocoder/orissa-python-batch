# f=open("guvi.txt")
# print(f.read())
# f.close()
# f=open("guvi.txt")
# print(f.readline())
# print(f.readline())
# f.close()

# f=open("guvi.txt")
# listdata=f.readlines()
# print(listdata[3:5])
# f.close()

# f=open("employee.txt","w")
# f.write("my name is rohan\ni am a fsd")

# f=open("employee.txt","a")
# f.write("\ni am located at Bangalore")
# f.write("\ni am full stack dev")
# f.close()


f=open("test.txt","x")
f.writelines(['anees\n','guvi\n','mvt\n'])