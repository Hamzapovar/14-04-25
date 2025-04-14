w=0
def setup():
    size(600,600)
def draw():
    global w
    for x in 100,200,300,400,500:
        ellipse(x,w, 50,50)
        w=w+1
    
