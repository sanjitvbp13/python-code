'''    The activity selection probleam is an optimization probleam which deals with the selection of non conflictiong 
activities the need to be executed by a single persong or machine in a given time frame.  




'''



def ActivitySelection(s, f):
    n = len(f)
  

    i = 0
    print(i, end=' ')

   
    for j in range(1, n):

       
            print(j, end=', ')
            i = j



if __name__ == '__main__':
    s = [5,1,3,0,5,8]
    f = [9,2,4,6,7,9]

    
    ActivitySelection(s, f)


