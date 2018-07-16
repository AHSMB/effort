# File name: loops.py
# Author: AHSMB
# Date created: 7/16/2018
# Date last modified: 7/16/2018
# Python Version: 3.7.0

def main():
  # Try to use range with a floating point number
  num = 29
  try:
    for count in range(num/2):
      print(count, end=" ")
  except:
    print("Using range with a floating number doesn't work.")
    for count in range(int(num/2)):
      print(count, end=" ")
    print("Converting the float to an int works with range, though.")

if __name__ == "__main__":
  main()