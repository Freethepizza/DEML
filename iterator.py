global_position = 0
list = ["li","h1","h2","h3","h4","h5","h6","p","b","i"]

def Next_element(list,times):
    position=0
    for i in range(0, times):
        position+=times
        if position is times:
            return str(list[position-1])



for x in range(1, 11):
    if Next_element(list,x) is "h2":
        print(x)
