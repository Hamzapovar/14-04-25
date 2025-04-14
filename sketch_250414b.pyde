def setup():
    size(600,400)
    
def draw():
    for razmer in 5,15,20,50,80:
        translate(100,0)
        fill(250,0,0)
        rect(0,200,razmer,razmer)
