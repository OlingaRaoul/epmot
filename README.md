
# EPMOT: Enterprise Performance Monitoring & Optimization Toolkit

## 📦 Overview
EPMOT is a modular toolkit designed to monitor, analyze, and optimize the performance of enterprise systems including Linux servers, databases, and applications like Apache, WebSphere, and Filenet.

## 🛠️ Features
- Linux system resource monitoring
- Apache log analysis for error detection
- SQLite database health checks
- Bottleneck detection based on system metrics
- Flask-based dashboard for visualization
- YAML-based configuration
- Unit testing with pytest

## 📁 Project Structure
```
epmot/
├── README.md
├── docs/
│   └── architecture.md
├── scripts/
│   ├── linux_monitor.sh
│   ├── apache_analyzer.py
│   ├── db_checker.py
│   └── bottleneck_detector.py
├── config/
│   └── sample_config.yaml
├── tests/
│   └── test_apache_logs.py
├── dashboard/
│   └── app.py
└── requirements.txt
```

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/OlingaRaoul/epmot.git
cd epmot
```

### 2. Set Up Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Linux Monitor (macOS-compatible)
```bash
bash scripts/linux_monitor.sh
```

### 4. Run Apache Log Analyzer
```bash
python scripts/apache_analyzer.py
```
Make sure to update the log path in the script or use a sample log file.

### 5. Run Database Checker
```bash
python scripts/db_checker.py
```
Ensure `sample.db` exists or create one using SQLite.

### 6. Run Bottleneck Detector
```bash
python scripts/bottleneck_detector.py
```

### 7. Launch Dashboard
```bash
python dashboard/app.py
```
Visit `http://127.0.0.1:5000` in your browser.

### 8. Run Tests
```bash
pytest tests/test_apache_logs.py
```

## ⚙️ Configuration
Edit `config/sample_config.yaml` to customize paths and intervals.

## 📚 Documentation
See `docs/architecture.md` for module architecture and integration.

## 📄 License
MIT License

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.

## 📧 Contact
For questions or support, contact [olingatoh3.com]
