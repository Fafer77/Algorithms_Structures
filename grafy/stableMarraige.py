N = 4

def w_preferance(prefer, w, m, m1):
    for man in range(N):
        if prefer[w][man] == m1:
            return True
        if prefer[w][man] == m:
            return False

def stable_marriage(prefer):
    woman_partner = [-1 for i in range(N)]
    free_man = [False for i in range(N)]
    free_count = N

    while(free_count > 0):
        m = 0
        while(m < N):
            if (free_man[m] == False):
                break
            m += 1
        
        i = 0
        while i < N and free_man[m] == False:
            w = prefer[m][i]
            
            if (woman_partner[w - N] == -1):
                woman_partner[w - N] = m
                free_man[m] = True
                free_count -= 1
            else:
                m1 = woman_partner[w - N]
                if not w_preferance(prefer, w, m, m1):
                    woman_partner[w - N] = m
                    free_man[m1] = False
                    free_man[m] = True
            i += 1

    print("Woman ", " Man")
    for i in range(N):
        print(i + N, "\t", woman_partner[i])


prefer = [[7, 5, 6, 4], [5, 4, 6, 7],
          [4, 5, 6, 7], [4, 5, 6, 7],
          [0, 1, 2, 3], [0, 1, 2, 3],
          [0, 1, 2, 3], [0, 1, 2, 3]]
 
stable_marriage(prefer)
