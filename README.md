# README.md

# Cybersecurity and Adversarial Robustness of Digital Twin Controlled Grid-Scale Battery Energy Storage System (BESS)

## Overview

This project presents a Digital Twin-based cybersecurity framework for a Grid-Scale Battery Energy Storage System (BESS). The simulator models battery operation under normal conditions and evaluates the impact of cyberattacks on system monitoring and control. It also implements both basic and advanced attack detection mechanisms to identify malicious sensor data manipulation.

The project was developed as part of a Master's research on improving the cyber resilience of Digital Twin-controlled energy storage systems.

---

# Features

* Battery Energy Storage System (BESS) simulation
* Digital Twin synchronization with the physical battery
* Sensor measurement model with configurable noise
* Communication delay simulation
* Sensor spoofing attack simulation
* Replay attack simulation
* Basic attack detector
* Advanced attack detector
* Synchronization error monitoring
* Detector performance evaluation
* Automatic visualization of simulation results
* Validation report generation
* CSV export of simulation results

---

# Project Structure

```text
Project_1/
│
├── main.py
├── simulation.py
├── battery.py
├── digital_twin.py
├── sensor.py
├── attack.py
├── replay_attack.py
├── detector.py
├── advanced_detector.py
├── evaluation.py
├── delay.py
├── plots.py
├── logger.py
├── utils.py
├── config.py
│
├── Bess_data.csv
│
├── results/
│   ├── simulation_results.csv
│   ├── validation_report.txt
│   ├── *.png
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# System Workflow

1. Load BESS operating data.
2. Simulate battery charging and discharging.
3. Measure battery State of Charge (SOC) using the sensor model.
4. Inject cyberattacks (sensor spoofing and replay attack).
5. Apply communication delay.
6. Update the Digital Twin.
7. Calculate synchronization error.
8. Detect attacks using:

   * Basic Detector
   * Advanced Detector
9. Evaluate detector performance.
10. Save results and generate visualizations.

---

# Cyberattack Models

## Sensor Spoofing Attack

The spoofing attack modifies the measured State of Charge (SOC) before it reaches the Digital Twin.

Parameters include:

* Attack probability
* Spoof amount

---

## Replay Attack

The replay attack replaces the current measurement with previously recorded sensor values.

Parameters include:

* Replay probability
* Replay buffer length

---

# Detection Methods

## Basic Detector

The basic detector monitors sudden changes in SOC measurements.

It identifies:

* Large unexpected SOC variations

---

## Advanced Detector

The advanced detector combines multiple indicators including:

* Sensor spoofing detection
* Replay attack detection
* Synchronization error monitoring
* Communication delay awareness

---

# Evaluation Metrics

The simulator evaluates detector performance using:

* True Positives (TP)
* True Negatives (TN)
* False Positives (FP)
* False Negatives (FN)
* Accuracy
* Precision
* Recall
* F1-Score
* Detection Rate
* False Alarm Rate

---

# Output Files

After each simulation, the following files are generated inside the `results/` directory:

* `simulation_results.csv`
* `validation_report.txt`
* SOC plot
* Battery Energy plot
* Solar vs Demand plot
* Battery Power plot
* Synchronization Error plot
* Attack Detection plot
* Detector Performance plot

---

# How to Run

1. Clone the repository.

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the simulation:

```bash
python main.py
```

---

# Example Output

The simulator reports:

* Battery statistics
* Detector statistics
* Attack summary
* Evaluation metrics
* Detection rate
* False alarms

It also generates graphs and exports all simulation results.

---

# Configuration

Simulation parameters can be modified in `config.py`, including:

* Battery capacity
* Initial SOC
* Charge/discharge efficiency
* Delay steps
* Sensor noise
* Spoofing attack probability
* Replay attack probability
* Detection thresholds

---

# Applications

This framework can be used for:

* Digital Twin cybersecurity research
* Smart grid security studies
* Battery Energy Storage System validation
* Attack detection algorithm evaluation
* Academic research and teaching
* Cyber-physical system security experimentation

---

# Future Work

Possible extensions include:

* False Data Injection (FDI) attacks
* Denial-of-Service (DoS) attacks
* Machine learning-based intrusion detection
* Adaptive attack detection
* Multiple distributed batteries
* Real-time communication protocols
* Hardware-in-the-loop testing

---

# Author

**Tabassum Roaidah Ahona**

 B.Sc. Engineering Research Project

**Title:**
*Cybersecurity and Adversarial Robustness of Digital Twin Controlled Grid-Scale Battery Energy Storage System (BESS)*

---

# License

This project is intended for academic and research purposes. Please cite the repository appropriately if it is used in publications or derivative work.
