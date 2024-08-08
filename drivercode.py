import subprocess
import os

def main():
    print("Enter the city to fetch weather report")
    options = int(input("1 Bengaluru\n2 Mumbai\n3 Delhi\n")) 
    if(options == 1):
       # subprocess.call("/home/venkatesha/Desktop/project/bengaluru_node.py", shell=True)
        os.system("python3 bengaluru_node.py")
    elif(options == 2):
        #subprocess.call("./mumbai_node.py", shell=True)
        os.system("python3 mumbai_node.py")
    elif(options == 3):
        #subprocess.call("./delhi_node.py", shell=True)
        os.system("python3 delhi_node.py")
    else:
        print("Data not found")

if __name__ == "__main__":
   main()
