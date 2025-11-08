import re

def analyze_log(file_path):
    with open(file_path, 'r') as f:
        logs = f.readlines()
    errors_404 = sum(1 for line in logs if ' 404 ' in line)
    errors_500 = sum(1 for line in logs if ' 500 ' in line)
    print(f"404 Errors: {errors_404}, 500 Errors: {errors_500}")

if __name__ == "__main__":
    analyze_log("/var/log/apache2/access.log")
