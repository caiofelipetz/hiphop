from random import randint
import datetime

arr=[]

start_time = datetime.datetime.now()

for x in range(500):
  arr.append(randint(1,1000))


end_time = datetime.datetime.now()

time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds()

print("Tempo para preencher array: ",execution_time,' segundos')



def arvore():
  i = 0
  start_time = datetime.datetime.now()
  heapSize = len(arr)
  while i<len(arr):
    test = False 
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    #print(i,left,right)
    if (left < heapSize and arr[left] > arr[i]):
      largest = left;
      
      #print(arr)
      
    if (right < heapSize and arr[right] > arr[largest]):
      largest = right
      
      #print(arr)
      
    if (largest != i):
      test =True
      temp = arr[i]
      arr[i] = arr[largest]
      arr[largest] = temp;
      #print(arr)
  
      i=0
    if test == False: 
      i = i+1
  
  end_time = datetime.datetime.now()
  
  time_diff = (end_time - start_time)
  execution_time = time_diff.total_seconds()
  print("Tempo para criar arvore: ",execution_time,' segundos')
  print(arr)
arvore()
w = int(input('Digite 1 Para buscar valor, 2 Para adicionar valor, 3 para remover valor,4 para ver a arvore gerada'))
if w == 1:
  value=input("digite o valor que deseja buscar: ")
  arvore()

if w==2:
  value=int(input("digite o valor que deseja adicionar: "))
  arr.append(value)
  arvore()
if w==3: 
  value=int(input("digite o valor que deseja remover: "))
  arr.remove(value)
  arvore()
if w==4:
  print(arr)