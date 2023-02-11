import os 
def search(filename):
    with open(filename , 'r') as f:
          file_read=f.read()
    if 'binod' in file_read.lower():
        return True
    else:
        return False



if __name__ == "__main__":
    content = os.listdir()
    nbinod=0
    flag=0
    for item in content:
        if item.endswith('txt'):
            print('Detecting Binod:{}'.format(item))
            flag=search(item)
            if(flag==1):
                print('We found Binod in this textfile:{}'.format(item))
                nbinod+=1
            else:
                print('Sorry binod is not available today')
    print("****************Summary of Coding***************************************")
    print("Pushpa I hate u yar")
    print("Hey Love I miss you buddy so much")
    print(nbinod)
    print("Hawa hawa")
    print("love")
    print("Hello world")
    print("All test passed")
    print("Life is fun")
