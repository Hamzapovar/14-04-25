x=0
def setup():
    size(600,600)
def draw():
    global x
    for y in 100,200,300,400,500:
        fill(random(1,255),random(1,255),random(1,255))
        rect(x,y,50,50)
        x=x+1    
