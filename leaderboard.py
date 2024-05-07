import csv
def read_board()->list:
    '''
    reads file
    :return:
    '''
    try:
        with open('leaderboard.txt','r',newline='') as file:
            reader=csv.reader(file)
            for line in reader:
                scores=line
            return scores
    except:
        with open('leaderboard.txt','w',newline='') as file:
            writer=csv.writer(file)
            writer.writerow('')
            return [' ']
def new_score(score:int)->None:
    '''
    adds score to all scores then sorts and writes
    :param score:
    :return:
    '''
    scores=read_board()
    sorted_scores=sort_board(scores)
    with open('leaderboard.txt','w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(sorted_scores)

def sort_board(scores:list)->list:
    '''
    bubble sort to sort list
    :param scores:
    :return:
    '''

    cscores=scores[:]
    for i in range(len(cscores)):
        for j in range(len(cscores[i:-1])):
            if cscores[j]>cscores[j+1]:
                cscores[j],cscores[j+1]=cscores[j+1],cscores[j]

    return cscores

if __name__=='__main__':
    print(sort_board([3,421,23,5,15,23,2342342424,1]))

