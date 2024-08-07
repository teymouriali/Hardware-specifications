try:
    import psutil
except Exception:
    print("Please install the program dependencies first")
    exit(0)
import csv
import time
import os
from datetime import datetime

# Function definition to get hardware information from the system


def coll():

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    net = psutil.net_io_counters()

    data = {
        "date-time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")],
        "cpu uses(%)": [cpu],
        "ram total(GB)": [round(ram.total/1024)],
        "ram availble(GB)": [round(ram.available/1024.0)],
        "ram used(GB)": [round(ram.used/1024.0)],
        "disk total(B)": [round(disk.total.real/1024.0)],
        "disk availble(B)": [round(disk.free.real/1024.0)],
        "disk use(%)": [disk.percent],
        "networksend(B)": [round(net.bytes_sent)],
        "networkrecive(B)": [round(net.bytes_recv)]


    }

    filen = ["date-time", "cpu uses(%)", "ram total(GB)", "ram availble(GB)", "ram used(GB)", "disk total(B)",
             "disk availble(B)", "disk use(%)", "networksend(B)", "networkrecive(B)"]
    # Create a directory named the current month and year of the system
    directory = time.strftime("%Y-%m")
    # Creating the directory path along with the file created in the current path with the name of the current day, month and year of the system
    directoryp = os.path.join(directory, time.strftime("%Y-%m-%d.csv"))
    # Checking whether or not there is a directory to create it
    if not os.path.exists(directoryp):
        os.makedirs(directory, exist_ok=True)
    # Checking whether or not the file is to be created in the same directory path
    with open(directoryp, "a", newline="") as csvv:
        write = csv.DictWriter(csvv, fieldnames=filen)

        if csvv.tell() == 0:
            write.writeheader()

        write.writerow(data)


def main():
    try:
        print("__the program is running (check current directory)__")
        while True:
            coll()
            time.sleep(1)
    except KeyboardInterrupt:
        # stopped by current user
        print(f" *** stopped by {os.getlogin()} *** ")


if __name__ == "__main__":
    main()
