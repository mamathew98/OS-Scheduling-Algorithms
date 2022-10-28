def FCFS():
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
    #print (processes)
    p_info = []
    start = 1
    for i in range(len(processes)):
        if (processes[i][2] <= start ):
            p_info.append([processes[i][1] ,  start - processes[i][2] , start ])
            start += processes[i][1]
            #print(p_info)
            continue
        while (processes[i][2] > start) :
            start += 1
        p_info.append([processes[i][1] ,  start - processes[i][2]  , start ])
        start += processes[i][1]
    print( "Processes | Burst time |" + " Start time |"
               " Waiting time |" + 
             " Turn around time")
    for i in range (len(p_info)):
        print(" "+ str(processes[i][0]) + "\t\t" +
                   str(p_info[i][0]) + "\t\t" +
                   str(p_info[i][2]) + "\t\t" +
                   str(p_info[i][1]) + "\t\t" +
                   str(p_info[i][0]+p_info[i][1]))
   
    
FCFS()
