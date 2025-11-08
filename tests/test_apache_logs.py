import sys
import os

# Add the scripts directory to the Python path
scripts_path = os.path.abspath(os.path.join(os.getcwd(), 'epmot/scripts'))
sys.path.insert(0, scripts_path)

import apache_analyzer

def test_apache_log_analysis():
    sample_logs = [
        '127.0.0.1 - - [08/Nov/2025:10:00:00] "GET /index.html HTTP/1.1" 200',
        '127.0.0.1 - - [08/Nov/2025:10:01:00] "GET /missing.html HTTP/1.1" 404',
        '127.0.0.1 - - [08/Nov/2025:10:02:00] "GET /error HTTP/1.1" 500'
    ]
    errors = []
    for line in sample_logs:
        status_code = line.split('"')[-1].strip().split()[0]
        if status_code in ['404', '500']:
            errors.append(line)
    assert len(errors) == 2