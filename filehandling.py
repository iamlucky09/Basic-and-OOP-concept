# yo vaneko chai file handling like create,read,write,append type ko kura haru hunchan
# file create garna ra tesma massage write lekhna,
#open('file name','permission')
# write garna 
a="kundan chapagain" # yesle euta string liyo
file=open('file.txt','w') # file create garyo name file.txt vanera ani tesma write garne vanera permission diyo
file.write(a) # file ma write garne
print('Your file is created') 
file.close()

# vako file lai read garna 
file=open('file.txt','r')
# filecontent=file.read()
print(file.read())

# write a list into file
lis=['car','jeep','van']
file=open('file1.txt','w')
file.writelines(lis)
print('file creaated')
file.close()

# read list from file
file=open('file1.txt','r')
filecontent=file.readlines()
print(filecontent)
file.close()

#appending a value into file
b="I'm a student"
file=open('file.txt','a')
file.write(b)
print("file is updated")
file.close()

# reading file that is appended
file=open('file.txt','r')
print(file.read())