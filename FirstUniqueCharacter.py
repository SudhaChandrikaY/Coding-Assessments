def GetUniChar(string):
  Dict = {}
  for i in range(len(string)):
    if string[i] not in Dict:
      Dict[string[i]] = True
    else:
      Dict[string[i]] = False      
  for i in range(len(string)):
    if Dict[string[i]]:
      return i+1
  return -1

if __name__ == '__main__':
  string = input()
  print(GetUniChar(string))
