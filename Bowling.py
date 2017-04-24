#  File: Bowling.py
#  Description:
#  Student's Name: Jairo Portillo
#  Student's UT EID: jep2896
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: 9/5/2016
#  Date Last Modified: 9/7/2016
#
#  Arbitrary variables such as x,y,i,k etc are used as counters/indecices for list
#

def ListSetUp(game): #Sets up the list of text into more usable list for later use
    gamecard = [] # characters for each ball adjusted for strikes. i.e ['X',' ','9','/','-','-']. Every 2 indicies is a frame. Frame 10 is an exception
    points = [] # raw point of each ball                               [ 10, 0 , 9 , 1 , 0 , 0,] for ' ', 0 is instead of Null but does not interfere with sum
    x = 0 #counters
    y = 0
    while x < len(game):
        if game[x] is 'X':
            if len(gamecard) < 18:
                gamecard.append(game[x])
                gamecard.append(" ")
                points.append(10)
                points.append(0)
                y += 2
            else:
                gamecard.append(game[x])
                points.append(10)
                y += 1
        elif game[x] is '/':
            gamecard.append(game[x])
            points.append(10 - points[y-1])
            y += 1
        elif game[x] is '-':
            gamecard.append(game[x])
            points.append(0)
            y += 1
        else:
            gamecard.append(game[x])
            points.append(int(game[x]))
            y +=1
        x += 1
    return {'gc':gamecard,'p':points}
    
def FrameScore(gamecard, points):
    score = [0]*11  # score at each frame length:10
    i = 1        
    k = 1
    while i < len(points):
        if (len(gamecard) == 21 and i >= len(gamecard) - 3):
            score[10] = score[9] + points[len(gamecard)-3] + points[len(gamecard)-2] + points[len(gamecard)-1]
            i = len(points)
        else:
            if gamecard[i-1] is 'X':
                score[k] = score[k-1] + points[i-1]
                if gamecard[i+1] is 'X':
                    score[k] = score[k] + points[i+1]
                    if gamecard[i+2] is not ' ':
                        score[k] = score[k] + points[i+2]
                    else:
                        score[k] = score[k] + points[i+3]   
                else:
                    score[k] = score[k] + points[i+1] + points[i+2]
                k += 1
                i += 2
            elif gamecard[i] is '/':
                score[k] = score[k-1] + points[i-1] + points[i] + points[i+1]
                k += 1
                i += 2
            else:
                score[k] = score[k-1] + points[i-1] + points[i]                     
                k += 1
                i += 2
    return score

def ScoreStr(gamecard,score):
    i = 0
    j = 1
    FrameNum = "" # number of the frame
    RowLine = ""  #lines between rows
    Points = "" #Raw Points
    Score = ""  # Score at each frame
    while i < len(gamecard):
        if i < 18:
            FrameNum = FrameNum + "  " + str(j) + " "
            RowLine = RowLine + "+---"
            Points = Points + "|" + gamecard[i] + " " + gamecard[i+1]
            if score[j] < 10:
                Score = Score + "|  " + str(score[j])
            elif score[j] >= 100:
                Score = Score + "|" + str(score[j])
            else:
                Score = Score + "| " + str(score[j])
            i += 2
            j += 1            
        else:
            FrameNum = FrameNum + "   " + str(j)
            RowLine = RowLine + "+-----+"
            if score[j] < 10:
                Score = Score + "|    " + str(score[j])
            elif score[j] >= 100:
                Score = Score + "|  " + str(score[j])
            else:
                Score = Score + "|   " + str(score[j])
            Score = Score + "|"
            if len(gamecard) == 20:
                Points = Points + "|" + gamecard[18] + " " + gamecard[19] + "  |"
            else:
                Points = Points + "|" + gamecard[18] + " " + gamecard[19] + " " + gamecard[20] +"|"
            i = len(gamecard)        
    
    print(FrameNum)
    print(RowLine)
    print(Points)
    print(Score)
    print(RowLine)
                  
            
            

def main():
    f = open('scores.txt')
    for line in f:
        game = line.split()        
        ListSet = ListSetUp(game)
        gamecard = ListSet['gc'] # characters for each ball adjusted for strikes. i.e ['X',' ']. Every 2 indicies is a frame. Frame 10 is an exception
        points = ListSet['p'] # raw point of each ball
        Scores = FrameScore(gamecard,points)        
        ScoreStr(gamecard,Scores)
main() 
