'''
Input: non-zero natural number n
Output:
  1. The number of bases of the vector space Zn2 over Z2
  2. The vector of each such basis(n<=4)
'''
import colorama
from colorama import Fore, Style
import random
import numpy as np
import math
import sympy
import itertools
import copy

basis_corrent = []

def valid(option_chosen:str):
    if option_chosen.isnumeric() and int(option_chosen) in [1,2,3]:
        return True
    return False
  
def add_number_in_base_2(number:int):
  #This functio only add 1 in number and return that number
  number_list = []
  while number > 0:
    number_list.append(number%10)
    number //= 10
  carry = 0
  if number_list[0] + 1 == 2:
    carry = 1
    number_list[0] = 0
  else:
    number_list[0] += 1
  counter = 1
  while carry != 0 and counter < len(number_list):
    if number_list[counter] + carry == 2:
      number_list[counter] = 0
      carry = 1
    else:
      number_list[counter] += carry
      carry = 0
    counter += 1
  if carry == 1:
    number_list.append(carry)
  multiplyer = 1
  for i in range(len(number_list)):
    number = number + number_list[i] * multiplyer
    multiplyer *= 10
  return number
      

def generate_posible_vector(length:int):
  #We need an initial number for stop
  #I use a integer number bigger than the biggest vector because the vector can be (0,0,1) and i can't type an integer number who start with 0. But when i write the vectors i deleted 1 from in front
  number_initial = 10 ** length * 2
  last_num = 10 ** length
  list_of_vectors = []
  while last_num < number_initial :
    #Here i generate all vector by adding 1 in base 2, because 1+1 = 10 in base 2
    last_num = add_number_in_base_2(last_num)
    list_of_vectors.append(str(last_num)[1::])
  #I delete the last element because isn't valid
  list_of_vectors.pop()
  return list_of_vectors

def choose_option():
    option = input("Choose option: ")
    if not valid(option):
        raise ValueError("You need to write a valid option!")
    try:
        option_proceed(int(option))
    except ValueError as e:
        print(Fore.RED + "ERROR: " + str(e) + Style.RESET_ALL)

def generate_list(length:int):
  #This function generate the output!
  #Posible vector generates all posibile vectors in base Z2
  posible_vector = generate_posible_vector(length)
  #Generate all basis
  counter = generate_basis(posible_vector, 0,[],length,0)
  file_write(f"The number of bases of the vector space Z2{length}  over Z2 is {counter} \n")
  print_all_basis()
      
def is_in_list(posible_list:list, elem:str):
  # This function verify if the elem is in basis list, and return True if is in list, else return False
  for i in posible_list:
    if i == elem:
      return False
  return True

def print_list(list_print:list,counter:int):
  string = '('
  for i in list_print:
    string += '('
    for j in i:
      string = string + j +','
    string = string[:-1] + '),'
  string = string[:-1]+')'
  file_write(f"{counter}. {string} \n")
  

def transform_in_array(basis_list:list):
  new_list = []
  for i in basis_list:
    new_list.append([])
    for j in i:
      new_list[-1].append(int(j))
  return new_list

def add_in_basis(basis_list:list):
  #Adding in a list all correct basis
  global basis_corrent
  basis_corrent.append(copy.deepcopy(basis_list))

def print_all_basis():
  global basis_corrent
  for i in range(len(basis_corrent)):
    print_list(basis_corrent[i],i+1)

def generate_basis(posible_vector:list, i:int,basis_list:list,length:int,counter:int):
  #This is a recursive function, he stop when basis_list is valid, length of basis list = length of n
  if len(basis_list) == length:
    new_list = transform_in_array(basis_list)
    if length >= 2:
      if np.linalg.det(new_list) != 0:
        counter += 1
        add_in_basis(basis_list)
        #print_list(basis_list,counter)
    else:
      counter += 1
      add_in_basis(basis_list)
    return counter
  elif len(basis_list) < length:
    # If isn't valid basis we are going further and put the next valid vector in basis.
    # Here are generated all basis in recusrive way
    for j in range(len(posible_vector)):
      if not is_in_list(basis_list,posible_vector[j]):
        continue
      basis_list.append(posible_vector[j])
      counter = generate_basis(posible_vector, j,basis_list,length,counter)
      basis_list.pop()
  return counter

def file_write(text:str):
  file = open("inpout.txt","a")
  file.write(text)
  file.close

def input_list():
  natural_number = input("Type a natural number: ").strip()
  if not natural_number.isnumeric():
    raise ValueError("You doesen't write a natural number!")
  natural_number = int(natural_number)
  if natural_number <= 0:
    raise ValueError("You doesen't write a natural number!")
  file_write(f"Input: n = {natural_number} \n")
  file_write(f"Output: ")
  generate_list(natural_number)

def tests():
  #We generate all list for number 0,1,2,3,4
  generate_list(int(0))
  generate_list(int(1))
  generate_list(int(2))
  generate_list(int(3))
  generate_list(int(4))

def option_proceed(option_choosen:int):
  #In this function we proeed the option for quit, tests and for input!
  if option_choosen == 3:
    quit()
  if option_choosen == 2:
    tests()
  elif option_choosen == 1:
    try:
      input_list()
    except ValueError as e:
      print(Fore.RED + "ERROR: " + str(e) + Style.RESET_ALL)
  
def print_menu():
  print("Project 2 - Algebra [Voda Ioan]")
  print("1. Input natural number n.")
  print("2. Tests (0,1,2,3,4)")
  print("3. Exit")
def start():
  while True:
    print_menu()
    try:
      choose_option()
    except ValueError as e:
      print(Fore.RED + "ERROR: " + str(e) + Style.RESET_ALL)

if __name__ == "__main__":
  start()
  pass