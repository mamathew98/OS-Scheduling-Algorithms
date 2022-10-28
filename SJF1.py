def SJF():
    print ("Enter Processes =>{ Process ID - Process Burst Time - Process Arrival Time }: ")
    print ("Enter '0' When Finished!")
    processes = []
    while(True):
        print(">")
        p = [int(x) for x in input().split(" ")]
        if (p[0] == 0 ):
            break
        processes.append(p)
    processes.sort(key=lambda x: x[2])
##    print (processes)
    p2 = []
    p_info = []
    start = 0
    while (len(processes)>0):
        i = 0
        while (i>=0 and i<len(processes)) :
##            print(i)
##            print(processes)
            if (processes[i][2] <= start) :

                p2.append(processes[i])
                del processes[i]
                if(len(processes) == 0):
                   break
                continue
            i += 1
        if (len(p2)==0):
            start += 1
            continue
        p2.sort(key=lambda x:x[1])
        while True :
            p_info.append([p2[0][0],p2[0][1],start,start - p2[0][2]])
            start += p2[0][1]
            del p2[0]
            if (len(p2)==0):
                break
    
    print( "Processes | Burst time |" + " Start time |"
               " Waiting time |" + 
             " Turn around time")
    for i in range (len(p_info)):
        print(" "+ str(p_info[i][0]) + "\t\t" +
                   str(p_info[i][1]) + "\t\t" +
                   str(p_info[i][2]) + "\t\t" +
                   str(p_info[i][3]) + "\t\t" +
                   str(p_info[i][3]+p_info[i][1]))
    
   
   
            
   
    
SJF()
