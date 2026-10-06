import __name__isequalto__main__45_

__name__isequalto__main__45_.welcome()

#Note: (1)If file imported by you have some executing functions then , as soon as you import it will get executed 
#      thouh you don't want it to happen 

#(2)So you should make use of " if (__name__=='main'):" in the file to be imported

#(3)Precautions: 1)If you think that a file created by you will be required in the future and you may import it in some other 
#                  files , you shold make use of this syntax

#                2)If you are importing a local file (file created by your friend, etc.) you should check for 
#                  functions if any , and then only import the file 