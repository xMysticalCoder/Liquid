print("Liquid Version 1.01")
variables = dict()
def readcode():
  if code.startswith("p(\"") and code.endswith("\")"):
    print(code[3:-2])
  elif code.startswith("v "):
    code.split()
    
    
  else:
    print("Syntax not understood.")

while True:
  code = input(">> ")
  readcode()