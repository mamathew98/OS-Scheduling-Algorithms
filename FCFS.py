# implementation of FirstComeFirstServed Scheduling algorithm
import sys

def main():
    process_queue = []  # containing a list = [process name, process arrival time, process burst time] for each process
    total_btime = 0  # total burst time

    n = int(input('Enter the total number of process: '))  # taking process quantity
    for i in range(n):
        process_queue.append([])  # append a empty list object to the list
        nameinput = input('Enter p_name: ')  # taking name of the process from user
        for j in range(i):
            if process_queue[j][0] == nameinput:
                nameinput = input(
                    'This name is taken please enter another: ')  # if the given name was taken it asks for another name
        process_queue[i].append(nameinput)

        process_queue[i].append(int(input('Enter p_arrival: ')))  # taking arrival time of the process from user

        process_queue[i].append(int(input('Enter p_bust: ')))  # taking burst time of the process from user
        total_btime += process_queue[i][2]
        print('')
    process_queue.sort(key=lambda process_queue: process_queue[1])  # sort the list ascending by arrival time

    sys.stdout.write("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time\n")
    s = "Process order : "
    wt = 0
    total_wtime = 0
    for i in range(0, n):
        sys.stdout.write(str(process_queue[i][0]) + "\t\t" + str(process_queue[i][2]) + "\t\t" + str(wt) + "\t\t" + str(
            wt + process_queue[i][2]))
        sys.stdout.write("\n")
        s += str(process_queue[i][1] + wt) + "[" + process_queue[i][0] + "]" + str(
            process_queue[i][1] + wt + process_queue[i][2]) + " ---> "
        total_wtime += wt
        try:
            wt = process_queue[i][1] + wt + process_queue[i][2] - process_queue[i + 1][1]
            if wt < 0:
                wt = 0
        except:
            break

    sys.stdout.write(s[:-5]+"\n")

    sys.stdout.write("Average Waiting time is: " + str(total_wtime / n)+"\n")
    sys.stdout.write("Average Turn Arount Time is: " + str((total_wtime + total_btime) / n))



if __name__ == "__main__":
    main()
    input()
