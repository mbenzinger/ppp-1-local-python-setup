def hello():
    print(hello)
hello()

def pack(one, two, three):
    return(one, two, three)
print(pack("first", "second", "third"))

def eat_lunch(lunch_list):
  if len(lunch_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(lunch_list)):
      if i == 0:
        print(f"First I eat {lunch_list[0]}")
      else:
        print(f"Next I eat {lunch_list[i]}")

eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])
