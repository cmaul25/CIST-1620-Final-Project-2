from random import *
def random_direction(self, topen=False, lopen=False, bopen=False, ropen=False) -> str:
    # one area open
    # top
    if topen == True and lopen == False and bopen == False and ropen == False:
        return 't'
    # left
    elif topen == False and lopen == True and bopen == False and ropen == False:
        return 'l'
    # bottom
    elif topen == False and lopen == False and bopen == True and ropen == False:
        return 'b'
    # right
    elif topen == False and lopen == False and bopen == False and ropen == True:
        return 'r'
    # two areas
    # one and top
    elif topen == True and lopen == True and bopen == False and ropen == False:
        if random() > .5:
            return 't'
        else:
            return 'l'
    elif topen == True and lopen == False and bopen == True and ropen == False:
        if random() > .5:
            return 't'
        else:
            return 'b'
    elif topen == True and lopen == False and bopen == False and ropen == True:
        if random() > .5:
            return 't'
        else:
            return 'r'
    # one and left
    elif topen == False and lopen == True and bopen == True and ropen == False:
        if random() > .5:
            return 'l'
        else:
            return 'b'
    elif topen == False and lopen == True and bopen == False and ropen == True:
        if random() > .5:
            return 'l'
        else:
            return 'r'
    #one and bottom
    elif topen == False and lopen == False and bopen == True and ropen == True:
        if random() > .5:
            return 'b'
        else:
            return 'r'
    #three areas open
    # 2 and top
    elif topen == True and lopen == True and bopen == True and ropen == False:
        if random() > .33:
            return 't'
        elif random()>.33:
            return 'l'
        else:
            return 'b'
    elif topen == True and lopen == True and bopen == False and ropen == True:
        if random() > .33:
            return 't'
        elif random() > .33:
            return 'l'
        else:
            return 'r'
    elif topen == True and lopen == False and bopen == True and ropen == True:
        if random() > .33:
            return 't'
        elif random() > .33:
            return 'b'
        else:
            return 'r'
    #2 and left
    elif topen == False and lopen == True and bopen == True and ropen == True:
        if random() > .33:
            return 'l'
        elif random() > .33:
            return 'b'
        else:
            return 'r'
    #all
    elif topen == True and lopen == True and bopen == True and ropen == True:
        if random() > .25:
            return 't'
        elif random() > .25:
            return 'l'
        elif random()>.25:
            return 'b'
        else:
            return 'r'
    else:
        print(topen,lopen,bopen,ropen)
        return('error')


