import signal
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

timer = 0  # arrival_time == timer

# Class Proses FCFS
class ProcessFCFS:
    def __init__(self, pid: str = "", arrival_time=timer, burst_time: int = 0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.end_time = 0
        self.state = "New"

# Class Proses SJF
class ProcessSJF:
    def __init__(self, pid: str = "", arrival_time=timer, burst_time: int = 0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.end_time = 0
        self.state = "New"

# Class Proses SRTF
class Process:
    def __init__(self, pid: str = "", arrival_time=0, burst_time: int = 0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.completed = False
        self.waiting_time = 0

# Class Proses Prio
class ProcessPrio:
    def __init__(self, pid: str = "", prio: int = 0, arrival_time=timer, burst_time: int = 0, start_time: int = 0, end_time: int = 0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.prio = prio
        self.burst_time = burst_time
        self.current_bt = burst_time
        self.start_time = start_time
        self.end_time = end_time
        self.state = "New"


# Program Utama FCFS
newFCFS = ProcessFCFS()  # state newFCFS
readyFCFS = []  # state readyFCFS
runningFCFS = ProcessFCFS()  # state runningFCFS
list_terminateFCFS = []  # state terminate
list_runningFCFS2 = []  # list history runningFCFS

# Program Utama SJF
newSJF = ProcessSJF()  # state newSJF
readySJF = []  # state readySJF
runningSJF = ProcessSJF()  # state runningSJF
list_terminateSJF = []  # state terminate
list_runningSJF2 = []  # list history runningSJF

# Program utama Priority
newPrio = ProcessPrio()  # state newPrio
readyPrio = []  # state readyPrio
runningPrio = ProcessPrio()  # state runningPrio
waiting = ProcessPrio()  # state waiting
list_terminatePrio = []  # state terminate
list_runningPrio = []
list_runningPrio2 = []

# Gantt Chart FCFS
def Gantt_chartFCFS():
    for item in list_runningFCFS2:
        print("+", end="")
        for j in range(len(item.pid)):
            print("-", end="")
        for j in range(item.end_time-item.start_time):
            print("-", end="")
    print("+")
    for item in list_runningFCFS2:
        print("|" + item.pid, end="")
        for j in range(item.end_time-item.start_time):
            print(" ", end="")
    print("|")
    for item in list_runningFCFS2:
        print("+", end="")
        for j in range(len(item.pid)):
            print("-", end="")
        for j in range(item.end_time-item.start_time):
            print("-", end="")
    print("+")
    for item in list_runningFCFS2:
        print("|", end="")
        for j in range(len(item.pid)):
            print(" ", end="")
        for j in range(item.end_time-item.start_time):
            print(" ", end="")
    print("|")
    print(str(list_runningFCFS2[0].start_time), end="")
    for item in list_runningFCFS2:
        for j in range(len(item.pid)):
            print(" ", end="")
        for j in range(item.end_time-item.start_time):
            print(" ", end="")
        print(str(item.end_time), end="")

# Gantt Chart SJF
def gantt_chartSJF():
    for item in list_runningSJF2:
        print("+", end="")
        for j in range(len(item.pid)):
            print("-", end="")
        for j in range(item.end_time-item.start_time):
            print("-", end="")
    print("+")
    for item in list_runningSJF2:
        print("|" + item.pid, end="")
        for j in range(item.end_time-item.start_time):
            print(" ", end="")
    print("|")
    for item in list_runningSJF2:
        print("+", end="")
        for j in range(len(item.pid)):
            print("-", end="")
        for j in range(item.end_time-item.start_time):
            print("-", end="")
    print("+")
    for item in list_runningSJF2:
        print("|", end="")
        for j in range(len(item.pid)):
            print(" ", end="")
        for j in range(item.end_time-item.start_time):
            print(" ", end="")
    print("|")
    print(str(list_runningSJF2[0].start_time), end="")
    for item in list_runningSJF2:
        for j in range(len(item.pid)):
            print(" ", end="")
        for j in range(item.end_time-item.start_time):
            print(" ", end="")
        print(str(item.end_time), end="")

# Gantt Chart Priority
def Gantt_chartPrio():
    for item in list_runningPrio2:
        print("+", end="")
        for j in range(len(item.pid)):
            print("-", end="")
        for j in range(item.end_time-item.start_time):
            print("-", end="")
    print("+")
    for item in list_runningPrio2:
        print("|" + item.pid, end="")
        for j in range(item.end_time-item.start_time):
            print(" ", end="")
    print("|")
    for item in list_runningPrio2:
        print("+", end="")
        for j in range(len(item.pid)):
            print("-", end="")
        for j in range(item.end_time-item.start_time):
            print("-", end="")
    print("+")
    for item in list_runningPrio2:
        print("|", end="")
        for j in range(len(item.pid)):
            print(" ", end="")
        for j in range(item.end_time-item.start_time):
            print(" ", end="")
    print("|")
    print(str(list_runningPrio2[0].start_time), end="")
    for item in list_runningPrio2:
        for j in range(len(item.pid)):
            print(" ", end="")
        for j in range(item.end_time-item.start_time):
            print(" ", end="")
        print(str(item.end_time), end="")

# Fungsi untuk menangani sinyal Ctrl+C pada FCFS
def signal_handlerFCFS(sig, frame):
    print("\n\nGantt chart:")
    Gantt_chartFCFS()
    print("")
    print("\nTabel Proses Eksekusi:")
    print("Process ID\tArrival Time\tBurst Time\tStart Time\tEnd Time\tTurn Around Time\tWaiting Time")
    total_waiting_time = 0
    for temp in list_terminateFCFS:
        print(f"{temp.pid}\t\t{temp.arrival_time}\t\t{temp.burst_time}\t\t{temp.start_time}\t\t{temp.end_time}\t\t{temp.end_time-temp.arrival_time}\t\t\t{(temp.end_time-temp.arrival_time)-temp.burst_time}")
        total_waiting_time += ((temp.end_time -
                               temp.arrival_time)-temp.burst_time)

    print("Average waiting time = " +
          str(total_waiting_time/len(list_terminateFCFS)))
    exit(0)

# Fungsi untuk menangani sinyal Ctrl+C pada SJF
def signal_handlerSJF(sig, frame):
    print("\n\nGantt chart:")
    gantt_chartSJF()
    print("")
    print("\nTabel Proses Eksekusi:")
    print("Process ID\tArrival Time\tBurst Time\tStart Time\tEnd Time\tTurn Around Time\tWaiting Time")
    total_waiting_time = 0
    for temp in list_terminateSJF:
        print(f"{temp.pid}\t\t{temp.arrival_time}\t\t{temp.burst_time}\t\t{temp.start_time}\t\t{temp.end_time}\t\t{temp.end_time-temp.arrival_time}\t\t\t{(temp.end_time-temp.arrival_time)-temp.burst_time}")
        total_waiting_time += ((temp.end_time -
                               temp.arrival_time)-temp.burst_time)

    print("Average waiting time = " +
          str(total_waiting_time/len(list_terminateSJF)))
    exit(0)

# Fungsi untuk menangani sinyal Ctrl+C pada Priority
def signal_handlerPrio(sig, frame):
    print("\n\nGantt chart:")
    Gantt_chartPrio()
    print("")
    print("\nTabel Proses Eksekusi:")
    print("Process ID\tArrival Time\tBurst Time\tStart Time\tEnd Time\tTurn Around Time\tWaiting Time")
    total_waiting_time = 0
    for temp in list_terminatePrio:
        print(f"{temp.pid}\t\t{temp.arrival_time}\t\t{temp.burst_time}\t\t{temp.start_time}\t\t{temp.end_time}\t\t{temp.end_time-temp.arrival_time}\t\t\t{(temp.end_time-temp.arrival_time)-temp.burst_time}")
        total_waiting_time += ((temp.end_time -
                               temp.arrival_time)-temp.burst_time)

    print("Average waiting time = " +
          str(total_waiting_time/len(list_terminatePrio)))
    exit(0)

# Fitur mengurangi proses pada FCFS
def kurang_ProcessFCFS(pid: str):
    for a in readyFCFS:
        if (a.pid == pid):
            list_terminateFCFS.append(a)
            readyFCFS.remove(a)
            break

# Fitur mengurangi proses pada SJF
def kurang_ProcessSJF(pid: str):
    for a in readySJF:
        if (a.pid == pid):
            list_terminateSJF.append(a)
            readySJF.remove(a)
            break

# Fitur mengurangi proses pada Priority
def kurang_ProcessPrio(pid: str):
    for a in readyPrio:
        if (a.pid == pid):
            list_terminatePrio.append(a)
            readyPrio.remove(a)
            break

# Mencari waktu sisa terpendek pada SRTF
def find_shortest_remaining_time_process(processes, current_time):
    min_remaining_time = float('inf')
    selected_process = None

    for process in processes:
        if process.arrival_time <= current_time and process.remaining_time < min_remaining_time and not process.completed:
            min_remaining_time = process.remaining_time
            selected_process = process

    return selected_process

# Penjadwalan SRTF
def srtf_scheduling(processes):
    n = len(processes)
    completed_processes = 0
    current_time = 0
    gantt_chart = []

    for process in processes:
        process.remaining_time = process.burst_time
        process.completed = False

    while completed_processes < n:
        selected_process = find_shortest_remaining_time_process(
            processes, current_time)

        if selected_process:
            selected_process.remaining_time -= 1
            current_time += 1

            if selected_process.remaining_time == 0:
                selected_process.completed = True
                selected_process.completion_time = current_time
                completed_processes += 1

            gantt_chart.append(selected_process.pid)
        else:
            current_time += 1

    return gantt_chart, current_time

# Menghitung waktu tunggu dan waktu putar pada SRTF
def calculate_waiting_and_turnaround_times(processes):
    for process in processes:
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

# Menampilkan Tabel Eksekusi dan Gantt Chart pada SRTF
def print_results(processes, gantt_chart, total_time):
    print("Gantt Chart:", gantt_chart)
    print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")

    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

# Visualisasi Gantt Chart pada SRTF
def visualize_gantt_chart(gantt_chart, processes):
    process_colors = {}
    for process in processes:
        process_colors[process.pid] = (
            np.random.rand(), np.random.rand(), np.random.rand())

    fig, ax = plt.subplots()
    for idx, process_id in enumerate(gantt_chart):
        ax.broken_barh([(idx, 1)], (0, 1), facecolors=(
            process_colors[process_id],))

    ax.set_ylim(0, 1)
    ax.set_xlim(0, len(gantt_chart))
    ax.set_xlabel('Time')
    ax.set_yticks([])
    ax.set_xticks(list(range(0, len(gantt_chart)+1)))

    # Legend
    legend_elements = [plt.Line2D([0], [0], color=process_colors[process.pid],
                                  label=f"Process {process.pid}") for process in processes]
    ax.legend(handles=legend_elements, loc='upper right')

    plt.show()

# Fitur untuk menambah proses pada SRTF
def add_process(processes, timer):
    while True:
        process_id = str(input("Enter process ID: "))
        burst_time = int(
            input("Burst time of process {}: ".format(process_id)))
        process = Process(process_id, timer, burst_time)
        processes.append(process)
        print(f"Process {process_id} added to the process list.")

        add_another = input(
            "Add another process at the same timer value? (y/n): ")
        if add_another.lower() == "n":
            return False
        else:
            print()
            continue

# Fitur untuk mengurangi proses pada SRTF
def remove_process(processes):
    process_id = input("Enter the process ID you want to remove: ")

    for process in processes:
        if process.pid == process_id:
            processes.remove(process)
            print(f"Process {process_id} removed from the process list.")
            return True

    print(f"Process {process_id} not found in the process list.")
    return False


# Dashboard
print("==================================================================")
print("|Selamat Datang di Simulasi Penjadwalan Proses pada Sistem Operasi|")
print("==================================================================")
print()
print("Terdapat 2 jenis penjadwalan pada simulasi kami : ")
print("1. Non-Preemptive")
print("2. Preemptive")
type = int(input("Masukan jenis penjadwalan yang diinginkan : "))
if (type == 1):
    print("Terdapat 2 algoritma pada penjadwalan Non-Preemptive")
    print("1. First Come First Serve")
    print("2. Shortest Job First")

    choose = int(input("Pilih algoritma yang akan digunakan : "))
    if (choose == 1):
        # ALGORITMA FIRST COME FIRST SERVE

        # Mengatur signal handler
        signal.signal(signal.SIGINT, signal_handlerFCFS)

        while True:
            print("----- TIMER " + str(timer) + " -----")
            # MENAMPILKAN STATE newFCFS
            print("State new : ", newFCFS.pid)
            print("State ready : ", end='')
            for a in readyFCFS:
                print(a.pid + " ", end='')
            print("")
            print("State running : " + runningFCFS.pid)
            print("State Terminate : ", end='')
            for a in list_terminateFCFS:
                print(a.pid + " ", end='')
            print("")
            # END
            print("=================================")
            print("Menu : ")
            print(" 1. Tambah Proses")
            print(" 2. Kurang Proses")
            opsi = str(input("Masukkan menu : "))
            if (opsi == "1"):
                proses = str(input("Masukkan proses "))
                if (proses != ""):  # kalau masukan "" maka dianggapnya bukan suatu proses
                    # jika proses bukan "" maka akan algoritma akan menganggapnya sebagai
                    # suatu proses dan akan meminta burst time dari proses tersebut
                    burst_time = int(
                        input("Burst time proses {} =  ".format(proses)))
                    pid = proses
                    # masuk state newFCFS
                    newFCFS = ProcessFCFS(pid, timer, burst_time)
                    print("Signal : ", end=' ')
                    print(pid + " masuk ke state new")
                    print("Signal : ", end=' ')
                    print(newFCFS.pid + " masuk state ready")
                    readyFCFS.append(newFCFS)  # masuk ke state readyFCFS
                    readyFCFS[0].state = "ready"
                    newFCFS = ProcessFCFS()  # instansiasi objek kosong

                    while (proses != ""):
                        proses = str(input("Masukkan proses "))
                        if (proses != ""):
                            burst_time = int(
                                input("Burst time proses {} =  ".format(proses)))
                            pid = proses
                            # masuk state newFCFS
                            # masuk state newFCFS
                            newFCFS = ProcessFCFS(pid, timer, burst_time)
                            print("Signal : ", end=' ')
                            print(pid + " masuk ke state new")
                            print("Signal : ", end=' ')
                            print(newFCFS.pid + " masuk state ready")
                            # masuk ke state readyFCFS
                            readyFCFS.append(newFCFS)
                            readyFCFS[0].state = "ready"
                            newFCFS = ProcessFCFS()  # instansiasi objek kosong
                        else:
                            break

                    # jika state running kosong
                    if (runningFCFS.pid == ""):
                        # masuk ke state runningFCFS
                        runningFCFS = readyFCFS.pop(0)
                        print("Signal : ", end=' ')
                        print(runningFCFS.pid + " masuk ke state running")
                        runningFCFS.state = "running"
                        runningFCFS.start_time = timer
                        runningFCFS.end_time = runningFCFS.start_time + runningFCFS.burst_time
                        list_runningFCFS2.append(runningFCFS)
            elif (opsi == "2"):
                hapus = str(input("Masukkan proses yang mau dihapus : "))
                pid_hapus = hapus
                kurang_ProcessFCFS(pid_hapus)
            else:
                ...

            if (timer == runningFCFS.end_time):  # end of proses
                runningFCFS.state = "Terminate"
                print("Signal : ", end=' ')
                print(runningFCFS.pid + " " + runningFCFS.state)
                # masukin ke list terminate
                list_terminateFCFS.append(runningFCFS)
                runningFCFS = ProcessFCFS()
                if (len(readyFCFS) > 0):
                    print("Signal : ", end=' ')
                    print(readyFCFS[0].pid + " masuk state running")
                    # masuk ke state runningFCFS
                    runningFCFS = readyFCFS.pop(0)
                    runningFCFS.state = "running"
                    runningFCFS.start_time = timer
                    runningFCFS.end_time = runningFCFS.start_time + runningFCFS.burst_time
                    list_runningFCFS2.append(runningFCFS)

            print("\n=================================")
            print("> Gantt Chart Timer " + str(timer))
            # Baris 1 "Batas atas"
            num = 0
            for item in list_runningFCFS2:
                print("+", end="")
                for j in range(len(item.pid)):
                    print("-", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print("-", end="")
                if (i == (item.end_time - item.start_time)):
                    print("+", end="")
            # Baris 2 (pID)
            print("")
            num = 0
            for item in list_runningFCFS2:
                print("|" + item.pid, end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print(" ", end="")
                if (i == (item.end_time - item.start_time)):
                    print("|", end="")
            # Baris 3 "Batas tengah"
            print("")
            num = 0
            for item in list_runningFCFS2:
                print("+", end="")
                for j in range(len(item.pid)):
                    print("-", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print("-", end="")
                if (i == (item.end_time - item.start_time)):
                    print("+", end="")
            # Baris 4 (spasi kosong buat timer)
            print("")
            num = 0
            for item in list_runningFCFS2:
                print("|", end="")
                for j in range(len(item.pid)):
                    print(" ", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print(" ", end="")
                if (i == (item.end_time - item.start_time)):
                    print("|", end="")
            # Baris 5 (start time)
            print("")
            print(str(list_runningFCFS2[0].start_time), end="")
            num = 0
            for item in list_runningFCFS2:
                for j in range(len(item.pid)):
                    print(" ", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print(" ", end="")
                if (i == (item.end_time - item.start_time)):
                    print(str(item.end_time), end="")
            print("\n=================================")
            timer += 1
    else:
        # ALGORITMA SHORTEST JOB FIRST

        # Mengatur signal handler
        signal.signal(signal.SIGINT, signal_handlerSJF)

        while True:
            print("--- TIMER " + str(timer) + " ---")
            # MENAMPILKAN STATE newSJF
            print("State new : ", newSJF.pid)
            print("State ready : ", end='')
            for a in readySJF:
                print(a.pid + " ", end='')
            print("")
            print("State running : " + runningSJF.pid)
            print("State Terminate : ", end='')
            for a in list_terminateSJF:
                print(a.pid + " ", end='')
            print("")
            # END
            print("=================================")
            print("Menu : ")
            print(" 1. Tambah Proses")
            print(" 2. Kurang Proses")
            opsi = str(input("Masukkan menu : "))
            if (opsi == "1"):
                proses = str(input(""))
                if (proses != ""):  # kalau masukan "" maka dianggapnya bukan suatu proses
                    # jika proses bukan "" maka akan algoritma akan menganggapnya sebagai
                    # suatu proses dan akan meminta burst time dari proses tersebut
                    burst_time = int(
                        input("Burst time proses {} =  ".format(proses)))
                    pid = "P" + proses
                    # masuk state newSJF
                    newSJF = ProcessSJF(pid, timer, burst_time)
                    print("Signal : ", end=' ')
                    print(pid + " masuk ke state new")
                    print("Signal : ", end=' ')
                    print(newSJF.pid + " masuk state ready")
                    readySJF.append(newSJF)  # masuk ke state readySJF
                    readySJF[0].state = "ready"
                    newSJF = ProcessSJF()  # instansiasi objek kosong

                    while (proses != ""):
                        proses = str(input(""))
                        if (proses != ""):
                            burst_time = int(
                                input("Burst time proses {} =  ".format(proses)))
                            pid = "P" + proses
                            # masuk state newSJF
                            # masuk state newSJF
                            newSJF = ProcessSJF(pid, timer, burst_time)
                            print("Signal : ", end=' ')
                            print(pid + " masuk ke state new")
                            print("Signal : ", end=' ')
                            print(newSJF.pid + " masuk state ready")
                            readySJF.append(newSJF)  # masuk ke state readySJF
                            readySJF[0].state = "ready"
                            newSJF = ProcessSJF()  # instansiasi objek kosong
                        else:
                            break

                    readySJF.sort(key=lambda x: (x.burst_time))
                    # jika state runningSJF kosong
                    if (runningSJF.pid == ""):
                        # masuk ke state runningSJF
                        runningSJF = readySJF.pop(0)
                        print("Signal : ", end=' ')
                        print(runningSJF.pid + " masuk ke state running")
                        runningSJF.state = "running"
                        runningSJF.start_time = timer
                        runningSJF.end_time = runningSJF.start_time + runningSJF.burst_time
                        list_runningSJF2.append(runningSJF)

            elif (opsi == "2"):
                hapus = str(input("Masukkan proses yang akan dihapus : "))
                pid_hapus = "P"+hapus
                kurang_ProcessSJF(pid_hapus)

            if (timer == runningSJF.end_time):  # end of proses
                runningSJF.state = "Terminate"
                print("Signal : ", end=' ')
                print(runningSJF.pid + " " + runningSJF.state)
                # masukin ke list terminate
                list_terminateSJF.append(runningSJF)
                runningSJF = ProcessSJF()
                if (len(readySJF) > 0):
                    print("Signal : ", end=' ')
                    print(readySJF[0].pid + " masuk state running")
                    runningSJF = readySJF.pop(0)  # masuk ke state runningSJF
                    runningSJF.state = "running"
                    runningSJF.start_time = timer
                    runningSJF.end_time = runningSJF.start_time + runningSJF.burst_time
                    list_runningSJF2.append(runningSJF)
                #

            print("\n=================================")
            print("> Gantt Chart Timer " + str(timer))
            # Baris 1 "Batas atas"
            num = 0
            for item in list_runningSJF2:
                print("+", end="")
                for j in range(len(item.pid)):
                    print("-", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print("-", end="")
                if (i == (item.end_time - item.start_time)):
                    print("+", end="")
            # Baris 2 (pID)
            print("")
            num = 0
            for item in list_runningSJF2:
                print("|" + item.pid, end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print(" ", end="")
                if (i == (item.end_time - item.start_time)):
                    print("|", end="")
            # Baris 3 "Batas tengah"
            print("")
            num = 0
            for item in list_runningSJF2:
                print("+", end="")
                for j in range(len(item.pid)):
                    print("-", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print("-", end="")
                if (i == (item.end_time - item.start_time)):
                    print("+", end="")
            # Baris 4 (spasi kosong buat timer)
            print("")
            num = 0
            for item in list_runningSJF2:
                print("|", end="")
                for j in range(len(item.pid)):
                    print(" ", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print(" ", end="")
                if (i == (item.end_time - item.start_time)):
                    print("|", end="")
            # Baris 5 (start time)
            print("")
            print(str(list_runningSJF2[0].start_time), end="")
            num = 0
            for item in list_runningSJF2:
                for j in range(len(item.pid)):
                    print(" ", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print(" ", end="")
                if (i == (item.end_time - item.start_time)):
                    print(str(item.end_time), end="")
            print("\n=================================")
            timer += 1
else:
    print("Terdapat 3 algoritma pada penjadwalan Preemptive")
    print("1. Shortest Remaining Time First")
    print("2. Round Robin")
    print("3. Priority")
    choose = int(input("Pilih algoritma yang akan digunakan : "))
    if (choose == 1):
        # ALGORITMA SHORTEST REMAINING TIME FIRST
        processes = []
        timer = 0
        while True:
            print("\nCurrent timer value: {}".format(timer))
            print("Menu:")
            print("1. Add process")
            print("2. Remove process")
            print("3. Gantt Chart")
            print("4. Continue to the next timer value")
            print("5. Exit")
            user_input = input("Select an option (1-5): ")

            if user_input == "1":
                while add_process(processes, timer):
                    pass
            elif user_input == "2":
                remove_process(processes)
                timer -= 1
            elif user_input == "3":
                gantt_chart, total_time = srtf_scheduling(processes)
                calculate_waiting_and_turnaround_times(processes)
                print_results(processes, gantt_chart, total_time)
                visualize_gantt_chart(gantt_chart, processes)
            elif user_input == "4" or not user_input:
                timer += 1
                continue
            elif user_input == "5":
                break
            else:
                print("Invalid input. Please try again.")

            input("Press Enter to continue...")  # Pause for user input

            timer += 1  # Increment timer if user presses Enter without entering other input
    elif (choose == 2):
        # ALGORITMA ROUND ROBIN
        # """
        # 1. Masukkan nilai kuantum
        # 2. masukkan burst time pertama
        # 3. masukkan nilai pada burst time ke list burstTime dan list sisaBurstTime
        # 4. lakukan pengecekan nilai sisaBurstTime
        #     * kalau 0 maka beres
        #     * kalau lebih dari 0 cek lagi apakah nilai sisaBurstTime kurang dari kuantum atau tidak
        #         ** kalau lebih dari kuantum, maka variabel waktuProses ditambah nilai kuantum
        #         ** sisaBurstTime dikurangi quantumnya
        # 5. q = {p1, p3}
        # loop1 = p1 - kuantum
        # loop2 = p2 - kuantum
        # """

        # Inputan banyaknya quantum oleh user
        quantum = int(input("Masukkan quantum: "))

        # varibal- variabel yang diperlukan
        burstTime = []
        sisaBurstTime = []
        turnaroundTime = []
        waktuTunggu = []
        path = []
        tampungLamaProses = []
        tampungLamaProses.append(0)
        lamaProses = 0
        avgWaktuTunggu = 0
        avg_turnaround_time = 0
        namaProses = []

        # variabel untuk menghitung jumlah data
        x = 1
        # Masukkan user
        while True:
            data2 = str(input(f"Masukkan nama proses ke-{x} : "))
            # jika masukkan kosong, maka proses berhenti
            if ((data2 == "")):
                break
            data = str(input(f"Masukkan burst time proses ke-{x} : "))
            # jika nama proses diisi tapi tidak mengisi burst time nya, maka proses tersebut dianggap tidak ada
            if ((data == "")):
                break

            # semua data diappend ke tiap variabel
            namaProses.append(data2)
            burstTime.append(int(data))
            sisaBurstTime.append(int(data))
            # append 0 untuk membuat list yang isinya sebanyak inputan user
            waktuTunggu.append(0)
            turnaroundTime.append(0)
            # loop
            for j in range(x):
                if (sisaBurstTime[j] == -1):
                    print(f"{namaProses[j]} TERMINATED")

                # Jika nilai dari sisaBurstTIme masih lebih besar dari quantum
                if (sisaBurstTime[j] >= quantum):
                    path.append(namaProses[j])
                    lamaProses += quantum
                    tampungLamaProses.append(lamaProses)
                    sisaBurstTime[j] -= quantum
                    print(
                        f"Sisa burst time {namaProses[j]} : {sisaBurstTime[j]}")
                    if (sisaBurstTime[j] <= 0):
                        waktuTunggu[j] = lamaProses - burstTime[j]
                        print(f"{namaProses[j]} TERMINATED")
                        # jika sudah -1 artinya proses tersebut sudah selesai
                        sisaBurstTime[j] = -1  # terminated

                # Jika nilai dari sisaBurstTIme masih lebih kecil dari quantum
                elif ((sisaBurstTime[j] < quantum) & (sisaBurstTime[j] > 0)):
                    path.append(namaProses[j])
                    lamaProses += sisaBurstTime[j]
                    tampungLamaProses.append(lamaProses)
                    waktuTunggu[j] = lamaProses - burstTime[j]
                    # jika sudah -1 artinya proses tersebut sudah selesai
                    sisaBurstTime[j] = -1  # terminated
                    if (sisaBurstTime[j] == -1):
                        print(f"{namaProses[j]} TERMINATED")
            x += 1
            print("=====================")

        while True:
            done = 0
            for j in range(x-1):
                if (sisaBurstTime[j] == -1):
                    print(f"{namaProses[j]} TERMINATED")
                # Jika nilai dari sisaBurstTIme masih lebih besar dari quantum
                if (sisaBurstTime[j] >= quantum):
                    path.append(namaProses[j])
                    lamaProses += quantum
                    tampungLamaProses.append(lamaProses)
                    sisaBurstTime[j] -= quantum
                    print(
                        f"Sisa burst time {namaProses[j]} : {sisaBurstTime[j]}")
                    if (sisaBurstTime[j] <= 0):
                        waktuTunggu[j] = lamaProses - burstTime[j]
                        print(f"{namaProses[j]} TERMINATED")
                        # jika sudah -1 artinya proses tersebut sudah selesai
                        sisaBurstTime[j] = -1  # terminated
                # Jika nilai dari sisaBurstTIme masih lebih kecil dari quantum
                elif ((sisaBurstTime[j] < quantum) & (sisaBurstTime[j] > 0)):
                    path.append(namaProses[j])
                    lamaProses += sisaBurstTime[j]
                    tampungLamaProses.append(lamaProses)
                    waktuTunggu[j] = lamaProses - burstTime[j]
                    sisaBurstTime[j] = -1  # terminated
                    # jika sudah -1 artinya proses tersebut sudah selesai
                    if (sisaBurstTime[j] == -1):
                        print(f"{namaProses[j]} TERMINATED")

                if (sisaBurstTime[j] == -1):
                    done += 1
            print("=====================")
            if (done == x-1):
                break

        for i in range(x-1):
            turnaroundTime[i] = waktuTunggu[i] + burstTime[i]
            avg_turnaround_time += turnaroundTime[i]
            avgWaktuTunggu += waktuTunggu[i]

        avg_turnaround_time /= x-1
        avgWaktuTunggu /= x-1

        print("TABEL OUTPUT")
        print("+--------+------------+--------------+------------+")
        print("| Proses | Burst Time | Waktu Tunggu | Waktu Putar|")
        print("+--------+------------+--------------+------------+")
        for i in range(x-1):
            if ((burstTime[i] < 10) and (waktuTunggu[i] < 10) and (turnaroundTime[i] < 10)):
                print("| ", end="")
                print(
                    f"  {namaProses[i]}   |      {burstTime[i]}     |      {waktuTunggu[i]}       |      {turnaroundTime[i]}   ", end='')
                print("  |")
            elif ((burstTime[i] < 10) and (waktuTunggu[i] < 10) and (turnaroundTime[i] >= 10)):
                print("| ", end="")
                print(
                    f"  {namaProses[i]}   |      {burstTime[i]}     |      {waktuTunggu[i]}       |     {turnaroundTime[i]}   ", end='')
                print("  |")
            elif ((burstTime[i] < 10) and (waktuTunggu[i] >= 10) and (turnaroundTime[i] < 10)):
                print("| ", end="")
                print(
                    f"  {namaProses[i]}   |     {burstTime[i]}     |      {waktuTunggu[i]}       |      {turnaroundTime[i]}   ", end='')
                print("  |")
            elif ((burstTime[i] < 10) and (waktuTunggu[i] >= 10) and (turnaroundTime[i] >= 10)):
                print("| ", end="")
                print(
                    f"  {namaProses[i]}   |      {burstTime[i]}     |     {waktuTunggu[i]}       |     {turnaroundTime[i]}   ", end='')
                print("  |")
            elif ((burstTime[i] >= 10) and (waktuTunggu[i] >= 10) and (turnaroundTime[i] >= 10)):
                print("| ", end="")
                print(
                    f"  {namaProses[i]}   |     {burstTime[i]}     |     {waktuTunggu[i]}       |     {turnaroundTime[i]}   ", end='')
                print("  |")
            elif ((burstTime[i] >= 10) and (waktuTunggu[i] < 10) and (turnaroundTime[i] >= 10)):
                print("| ", end="")
                print(
                    f"  {namaProses[i]}   |     {burstTime[i]}     |      {waktuTunggu[i]}       |     {turnaroundTime[i]}   ", end='')
                print("  |")
        print("---------------------------------------------------")

        print("\nGANTT CHART : ")
        for i in range(len(path)):
            for i in range(5):
                print('=', end='')
        print('=')

        for i in range(len(path)):
            if ((i >= 0) and (i < len(path) - 1)):
                print(f'| {path[i]} ', end='')
            else:
                print(f'| {path[i]} |', end='')
        print("")
        for i in range(len(path)):
            for i in range(5):
                print('=', end='')
        print('=')

        a = 0
        for i in range(len(tampungLamaProses)*5):
            if tampungLamaProses[a] < 10:
                if i % 5 == 0:
                    print(tampungLamaProses[a], end="")
                    if (a <= len(tampungLamaProses)):
                        a += 1
                else:
                    print(" ", end="")
            elif tampungLamaProses[a] >= 10:
                if i % 4 == 0:
                    print(tampungLamaProses[a], end="")
                    if (a <= len(tampungLamaProses)):
                        a += 1
                else:
                    print(" ", end="")
            if (a == len(tampungLamaProses)):
                break
        print("")
        print("\nRata-rata waktu tunggu : ", round(avgWaktuTunggu, 2))
        print("Rata-rata waktu putar  : ", round(avg_turnaround_time, 2))

    else:
        # ALGORITMA PRIORITY

        # Mengatur signal handler
        signal.signal(signal.SIGINT, signal_handlerPrio)

        while True:
            print("----- TIMER " + str(timer) + " -----")
            # MENAMPILKAN STATE newPrio
            print("State new : ", newPrio.pid)
            print("State ready : ", end='')
            for a in readyPrio:
                print(a.pid + " ", end='')
            print("")
            print("State running : " + runningPrio.pid)
            print("State Waiting : " + waiting.pid)
            print("State Terminate : ", end='')
            for a in list_terminatePrio:
                print(a.pid + " ", end='')
            print("")
            # END
            print("=================================")
            print("Menu : ")
            print(" 1. Tambah Proses")
            print(" 2. Kurang Proses")
            opsi = str(input("Masukkan menu : "))
            if (opsi == "1"):
                proses = str(input("Masukkan proses "))
                if (proses != ""):  # kalau masukan "" maka dianggapnya bukan suatu proses
                    # jika proses bukan "" maka akan algoritma akan menganggapnya sebagai
                    # suatu proses dan akan meminta burst time dari proses tersebut
                    burst_time = int(
                        input("Burst time proses {} =  ".format(proses)))
                    prio = int(input("Priority Process {} = ".format(proses)))
                    pid = proses
                    # masuk state newPrio
                    newPrio = ProcessPrio(pid, prio, timer, burst_time)
                    print("Signal : ", end=' ')
                    print(pid + " masuk ke state new")
                    print("Signal : ", end=' ')
                    print(newPrio.pid + " masuk state ready")
                    readyPrio.append(newPrio)  # masuk ke state readyPrio
                    readyPrio[0].state = "ready"
                    newPrio = ProcessPrio()  # instansiasi objek kosong

                    while (proses != ""):
                        proses = str(input("Masukkan proses "))
                        if (proses != ""):
                            burst_time = int(
                                input("Burst time proses {} =  ".format(proses)))
                            prio = int(
                                input("Priority Process {} = ".format(proses)))
                            pid = proses
                            # masuk state newPrio
                            # masuk state newPrio
                            newPrio = ProcessPrio(pid, prio, timer, burst_time)
                            print("Signal : ", end=' ')
                            print(pid + " masuk ke state new")
                            print("Signal : ", end=' ')
                            print(newPrio.pid + " masuk state ready")
                            # masuk ke state readyPrio
                            readyPrio.append(newPrio)
                            readyPrio[0].state = "ready"
                            newPrio = ProcessPrio()  # instansiasi objek kosong
                        else:
                            break

                    # Sorting
                    readyPrio = sorted(readyPrio, key=lambda x: x.prio)

                    if ((readyPrio[0].prio < runningPrio.prio or readyPrio[0].prio == runningPrio.prio and readyPrio[0].current_bt < runningPrio.current_bt) and waiting.pid == ""):
                        print("Signal : ", end=' ')
                        print(runningPrio.pid + " masuk ke state Waiting")
                        waiting.state = "Waiting"
                        # update timer kalau ada interupt
                        list_runningPrio2[len(
                            list_runningPrio2)-1].end_time = timer
                        waiting = runningPrio
                        runningPrio = ProcessPrio()
                        print("Signal : ", end=' ')
                        print(waiting.pid + " masuk ke state ready")
                        waiting.state = "ready"
                        readyPrio.append(waiting)
                        waiting = ProcessPrio()

                    # jika state runningPrio kosong
                    if (runningPrio.pid == ""):
                        # masuk ke state runningPrio
                        runningPrio = readyPrio.pop(0)
                        print("Signal : ", end=' ')
                        print(runningPrio.pid + " masuk ke state running")
                        runningPrio.state = "running"
                        runningPrio.start_time = timer
                        runningPrio.end_time = runningPrio.start_time + runningPrio.current_bt
                        temp = ProcessPrio(runningPrio.pid, runningPrio.prio, runningPrio.arrival_time,
                                           runningPrio.burst_time, runningPrio.start_time, runningPrio.end_time)
                        list_runningPrio2.append(temp)
            elif (opsi == "2"):
                hapus = str(input("Masukkan proses yang mau dihapus : "))
                pid_hapus = hapus
                kurang_ProcessPrio(pid_hapus)
            else:
                ...

            readyPrio = sorted(readyPrio, key=lambda x: x.prio)
            #
            if (timer == runningPrio.end_time):  # end of proses
                runningPrio.state = "Terminate"
                print("Signal : ", end=' ')
                print(runningPrio.pid + " " + runningPrio.state)
                # masukin ke list terminate
                list_terminatePrio.append(runningPrio)
                runningPrio = ProcessPrio()
                if (len(readyPrio) > 0):
                    print("Signal : ", end=' ')
                    print(readyPrio[0].pid + " masuk state running")
                    # masuk ke state runningPrio
                    runningPrio = readyPrio.pop(0)
                    runningPrio.state = "running"
                    runningPrio.start_time = timer
                    runningPrio.end_time = runningPrio.start_time + runningPrio.current_bt
                    temp = ProcessPrio(runningPrio.pid, runningPrio.prio, runningPrio.arrival_time,
                                       runningPrio.burst_time, runningPrio.start_time, runningPrio.end_time)
                    list_runningPrio2.append(temp)
                #
            # updata current burst time ProcessPrio
            runningPrio.current_bt -= 1

            print("\n=================================")
            print("> Gantt Chart Timer " + str(timer))
            # Gantt_chartPrio(list_runningPrio2)
            # gantt chart
            # Baris 1 "Batas atas"
            num = 0
            for item in list_runningPrio2:
                print("+", end="")
                for j in range(len(item.pid)):
                    print("-", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print("-", end="")

            # Baris 2 (pID)
            print("+")
            num = 0
            for item in list_runningPrio2:
                print("|" + item.pid, end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print(" ", end="")
            # Baris 3 "Batas tengah"
            print("|")
            num = 0
            for item in list_runningPrio2:
                print("+", end="")
                for j in range(len(item.pid)):
                    print("-", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print("-", end="")
            # Baris 4 (spasi kosong buat timer)
            print("+")
            num = 0
            for item in list_runningPrio2:
                print("|", end="")
                for j in range(len(item.pid)):
                    print(" ", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print(" ", end="")
            # Baris 5 (start time)
            print("|")
            print(str(list_runningPrio2[0].start_time), end="")
            num = 0
            for item in list_runningPrio2:
                for j in range(len(item.pid)):
                    print(" ", end="")
                i = 0
                while (i < (item.end_time - item.start_time) and num < timer):
                    num += 1
                    i += 1
                    print(" ", end="")
                if (i == (item.end_time - item.start_time)):
                    print(str(item.end_time), end="")

            print("\n=================================")
            timer += 1
