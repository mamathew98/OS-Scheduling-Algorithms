import sys


def main():
    process_queue = {}
    total_wtime = 0
    remburs = {}

    n = int(input('Enter the total no of processes: '))
    for i in range(n):
        # append a list object to the list
        nameinput = input('Enter p_name: ')
        process_queue.setdefault(nameinput, [])

        arrtime = int(input('Enter p_arrival: '))
        process_queue[nameinput].append(arrtime)
        total_wtime += process_queue[nameinput][0]

        btime = int(input('Enter p_bust: '))
        process_queue[nameinput].append(btime)
        remburs.setdefault(nameinput, btime)

        print('')

    # process_queue.sort(key=lambda process_queue: process_queue[1])
    tperiod = []
    t = 0
    # wt = {}
    # burst=remburs
    while any(remburs.values()):
        for i in list(process_queue.items()):
            try:
                if i[1][0] <= t and 0 < remburs[i[0]] < remburs[tperiod[t]]:
                    tperiod[t] = i[0]
            except:
                if i[1][0] <= t:
                    tperiod.append(i[0])
                continue
        if len(tperiod) == t:
            tperiod.append(-1)
        if tperiod[t] != -1:
            remburs[tperiod[t]] -= 1
            # if burst[tperiod[t]] - remburs[tperiod[t]] == 1:
            # wt.setdefault(tperiod[t],arrival[tperiod[t]]-t)
            if remburs[tperiod[t]] == 0:
                process_queue[tperiod[t]].append(t + 1)

        t += 1
    sys.stdout.write(str(tperiod))
    sys.stdout.write("\n")
    wt = 0
    tat = 0
    sys.stdout.write("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time\n")
    for i in list(process_queue.items()):
        sys.stdout.write(
            i[0] + "\t\t" + str(i[1][1]) + "\t\t" + str(i[1][2] - i[1][0] - i[1][1]) + "\t\t" + str(i[1][2] - i[1][0]))
        tat += i[1][2] - i[1][0]
        wt += i[1][2] - i[1][0] - i[1][1]
        sys.stdout.write("\n")

    sys.stdout.write("Average Waiting time is: " + str(wt / n) + "\n")
    sys.stdout.write("Average Turn Arount Time is: " + str(tat / n))


if __name__ == "__main__":
    main()
    input()
