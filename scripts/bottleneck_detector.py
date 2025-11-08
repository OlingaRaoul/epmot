
def detect_bottlenecks(cpu, memory, disk):
    if cpu > 90:
        print("High CPU usage detected")
    if memory > 90:
        print("High memory usage detected")
    if disk > 90:
        print("High disk usage detected")

if __name__ == "__main__":
    detect_bottlenecks(95, 85, 92)
