blocks = int(input("Enter the number of blocks: "))
height = 0
#
# Write your code here.
#	
while blocks - height > 0 :
    blocks -= (height+1)
    height += 1
print("The height of the pyramid:", height)