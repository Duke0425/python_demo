import psutil
while True:
    print(f"CPU: {psutil.cpu_freq()}")