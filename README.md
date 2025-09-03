# 🛡️ RDP Brute Force Detection – SOC Log Analysis Project

## 📌 Project Overview
This project demonstrates how to analyze honeypot logs and build a mini SOC pipeline to detect **Remote Desktop Protocol (RDP) brute-force attacks**.  
RDP brute force is a common attack technique where adversaries repeatedly attempt to log in to a system with different passwords until they succeed. By setting up a honeypot to capture these attempts, we can simulate real-world SOC workflows: parsing logs, detecting attacks, and visualizing activity.

---

## 🎯 Objectives
- Collect and parse honeypot logs containing failed and successful RDP login attempts  
- Create detection rules for brute-force and suspicious activity  
- Build Splunk dashboards (including a geo map) to visualize attacker locations  
- Document findings and map them to SIEM use cases and ATT&CK techniques  

---

## 🔍 Key Features
- **Sample Logs:** Honeypot events showing RDP login attempts (source IP, username, country, timestamp)  
- **Analysis Scripts:** Python code for parsing and normalizing logs  
- **Detection Rules:** Splunk SPL queries for brute-force, impossible travel, admin abuse, and distributed attacks  
- **Dashboards:** Splunk geo map to show global attacker distribution  
- **SIEM Model:** Data model + detection use cases, showing how this project would live inside a SIEM  

---

## 📊 Why RDP Brute Force?
- RDP is one of the **most targeted services** on the internet  
- Brute-force attacks are often the **first step in ransomware campaigns**  
- Detecting and visualizing these attempts shows how SOC teams can **proactively defend critical infrastructure**  

---

## ✅ What This Project Shows
This project highlights:
- How raw honeypot logs can be transformed into meaningful security events  
- How SOC analysts design **detection logic** for brute force and related attack patterns  
- How to **visualize attacker activity geographically** to improve situational awareness  
- How to document detections as **SIEM use cases** for blue team operations  
