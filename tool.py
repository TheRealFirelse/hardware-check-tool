import psutil
import os

def script():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent

        os.system("cls" if os.name == "nt" else "clear")

        if cpu >= 90:
            print("Critical CPU usage, stop the process that uses the most CPU resources? (Y, N)")
            inp = input()
            inp = inp.lower()

            if inp == "y":
                for proc in psutil.process_iter():
                    try:
                        proc.cpu_percent(None)
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass
                    
                max_proc = None
                max_cpu = 0

                for proc in psutil.process_iter(['pid', 'name']):
                    try:
                        cpu_use = proc.cpu_percent(None)

                        if cpu_use >= max_cpu:
                            max_cpu = cpu_use
                            max_proc = proc
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass
                    
                if max_proc:
                    print(f"stop {max_proc.name()} ({max_proc.pid})? (Y, N)")

                    while True:
                        ans = input()
                        ans = ans.lower()

                        if ans == "y":
                            max_proc.kill()
                            break
                    
                        elif ans == "n":
                            break

                        else:
                            print("Incorrect input (Y, N)")
        
        elif cpu >= 75:
            print("Dangerous CPU usage")

        if ram > 85:
            print("Dangerous RAM usage")

        print(f"CPU: {cpu:.1f} | RAM: {ram:.1f}", end="\r", flush=True)

if __name__ == "__main__":
    script()
