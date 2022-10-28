#FCFS Implementation

def FCFS():
    processes = [] 
    bt = [] #burstTimes
    print("Plz Enter Processes (Enter '#' When u Finished) :")
    while (True):
        p = input(" PLz Enter Process ID : ")
        if (p=="#"):
            break
        processes.append(int(p))
        b = int(input(" Plz Enter Burst Time : "))
        bt.append(b)
    
    n = len(processes)
    wt = [0] * n #waitin time array
    tat = [0] * n #turnaround time array
    total_wt = 0 #sum of waiting times
    total_tat = 0 #sum of turnaround times
    findAvgTime(processes,n,bt,wt,tat,total_wt,total_tat)
    print( "Processes | Burst time |" + 
                  " Waiting time |" + 
                " Turn around time") 
  
    # Calculate total waiting time  
    # and total turn around time 
    for i in range(n): 

        print(" " + str(i + 1) + "\t\t" + 
                    str(bt[i]) + "\t " + 
                    str(wt[i]) + "\t\t " + 
                    str(tat[i]))  

#========================================================
    
def findWaitingTime(processes,n,bt,wt):
    #Function to find waiting time of all processes
    wt[0]=0     #waiting time p0 = 0
    for i in range(1,n):    #Calculate waiting times
        wt[i] = bt[i - 1] + wt[i - 1]

#=========================================================
def findTurnAroundTime(processes,n,bt,wt,tat):
    #Function to find turnaround time
    for i in range(n):      #calculate turnaround time
        tat[i] = bt[i] + wt[i]

#=========================================================
        
def findAvgTime(processes,n,bt,wt,tat,total_wt,total_tat):
    #Fucntion to find average time
    findWaitingTime(processes,n,bt,wt)
    findTurnAroundTime(processes,n,bt,wt,tat)
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
    print( "Average waiting time = "+str(total_wt / n)) 
    print("Average turn around time = "+str(total_tat / n))

#==========================================================

FCFS()
