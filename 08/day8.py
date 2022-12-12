
import numpy

forest=[]
forest_list=[]
with open("input.txt") as f:
    for line in f:
        line = list(line)
        if "\n" in line:
            line.remove("\n")
        forest.append(numpy.array(line, dtype=int))
    forest = numpy.array(forest)

#STAR 1
visible_trees=0
#add outside trees
visible_trees += 2*len(forest[0,:]) 
visible_trees += 2*len(forest[:,0]) 
visible_trees -= 4
print("edge: ", visible_trees)
print("dims: ", len(forest[:,0]), len(forest[0,:]))


for i in range(1, len(forest[0,:])-1):
    for j in range(1, len(forest[:,0])-1):
        tree = forest[i,j]
        this_tree_visible=False

        if all(tree > forest[:i,j]):
            this_tree_visible=True
        if all(tree > forest[i+1:,j]):
            this_tree_visible=True

        if all(tree > forest[i,:j]):
            this_tree_visible=True
        if all(tree > forest[i,j+1:]):
            this_tree_visible=True
        
        if this_tree_visible:
            visible_trees += 1
print(visible_trees)

def view_in_one_dir(v):
    dist = 1
    if all(v<0):
        dist = len(v)
        return dist
    
    for i in v:
        if i < 0:
            dist +=1
        else:
            return dist

#STAR 2
best_score=0
best_score_prod=[]
index_best=[]
for i in range(len(forest[0,:])-1):
    for j in range(len(forest[:,0])-1):
        score = 0
        tree = forest[i,j]
        #print(tree)
        view = forest-forest[i,j]
        #i:
        x = view_in_one_dir(view[i+1:,j])
        xx = view_in_one_dir(numpy.flip(view[0:i,j]))
        y = view_in_one_dir(view[i, j+1:])
        yy = view_in_one_dir(numpy.flip(view[i, 0:j]))
        if x*xx*y*yy > best_score:
            best_score = x*xx*y*yy
            best_score_prod = [x,xx,y,yy]
            index_best = [i,j]
print(best_score, best_score_prod, index_best)

