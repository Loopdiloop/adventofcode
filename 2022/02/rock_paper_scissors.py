import numpy

strategy = numpy.loadtxt("strategy.txt", dtype=(str,str))

## Star 1
#winning_condition 
win = dict(A="Y", #rock - paper 
    B="Z", #paper - scissors
    C="X", #scissors - rock
)

#draw
draw= dict(A="X", #rock
    B="Y", #paper
    C="Z", #scissors
)

#points_for_choice, both star 1 and star 2
rpc_points = dict(X=1, A=1,  #rock - 1p
    Y=2, B=2,  #paper - 2p
    Z=3, C=3, #scissors - 3p
)

points = 0
for i in strategy:
    points += rpc_points[i[1]]
    if win[i[0]] == i[1]:
        points += 6
    elif draw[i[0]] == i[1]:
        points += 3
    else:
        continue
print("Star 1: ", points)


## Star 2
# use dict rpc_points from star 1

what_to_do = dict(X=dict(A="C", B="A", C="B", p=0),  # losing conditions
    Y=dict(A="A", B="B", C="C", p=3),  # draw
    Z=dict(A="B", B="C", C="A", p=6),  # win
    )

points = 0
for i in strategy:
    my_choice = what_to_do[i[1]][i[0]]
    points += rpc_points[my_choice]
    points += what_to_do[i[1]]["p"]
    
print("Star 2: ", points)







## ----------------------------------------
## Older/initial solution:
## ----------------------------------------
"""
strategy = numpy.loadtxt("strategy.txt", dtype=(str,str))

## Star 1
#winning_condition 
win = dict(A="Y", #rock - paper 
    B="Z", #paper - scissors
    C="X", #scissors - rock
)

#draw
draw= dict(A="X", #rock
    B="Y", #paper
    C="Z", #scissors
)

#points_for_choice
rpc_points = dict(X=1, #rock - 1p
    Y=2, #paper - 2p
    Z=3, #scissors - 3p
)

points = 0
for i in strategy:
    points += rpc_points[i[1]]
    if win[i[0]] == i[1]:
        points += 6
    elif draw[i[0]] == i[1]:
        points += 3
    else:
        continue
print("Star 1: ", points)


## Star 2


#winning_condition 
win = dict(A="B", #rock - paper 
    B="C", #paper - scissors
    C="A", #scissors - rock
)

#draw
draw= dict(A="A", #rock
    B="B", #paper
    C="C", #scissors
)

#lose
lose= dict(A="C", #rock - scissors
    B="A", #paper - rock
    C="B", #scissors - paper
)

#points_for_choice
rpc_points = dict(A=1, #rock - 1p
    B=2, #paper - 2p
    C=3, #scissors - 3p
)

#win-lose-draw
condition_points= dict(X=0, #lose
    Y=3, #draw
    Z=6, #win
)

what_to_do = dict(X=lose, Y=draw, Z=win)

print(rpc_points)

points = 0
for i in strategy:
    my_choice = what_to_do[i[1]][i[0]]
    points += rpc_points[my_choice]
    points += condition_points[i[1]]
    
    
print("Star 2: ", points)
"""