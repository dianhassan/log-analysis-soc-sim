# 🛡️ RDP Brute Force Detection – Analysis Report

## 📌 Introduction
This report analyzes honeypot logs capturing Remote Desktop Protocol (RDP) brute-force attempts.  
RDP brute-force is a common method attackers use to gain unauthorized access by repeatedly trying different usernames and passwords.

---

## 📂 Dataset Summary
- **Total Events:** 11,512  
- **Time Range:** 2021-10-26 → 2024-01-24  
- **Unique Source IPs:** 40  
- **Unique Usernames Attempted:** 831  
- **Countries Seen:** 19  

---

## 🔍 Key Findings
- Attackers heavily targeted **Administrator** accounts in different variations (`administrator`, `Administrator`, `ADMINISTRATOR`, `Administrador`, `Administrateur`).  
- Activity was global, but **Russia, Philippines, China, Taiwan, and Egypt** were the top sources.  
- Brute-force attempts were sustained over more than **two years**, proving constant probing activity.  
- Several IP addresses generated thousands of login attempts:
  - `119.93.221.41` – 2,915 attempts  
  - `94.232.41.158` – 2,055 attempts  
  - `87.251.67.98` – 1,107 attempts  
  - `45.141.84.54` – 1,089 attempts  
  - `61.223.113.218` – 836 attempts
 
    <img width="2000" height="1000" alt="rdp_top_ips" src="https://github.com/user-attachments/assets/d8d3b044-6fc7-4f06-a362-01c523ece7ff" />


---

## 🚨 Detection Use Cases
1. **Brute Force Login Attempts** – Detect >10 failed logins from the same IP within 5 minutes.  
2. **Suspicious Geo Access** – Detect attempts from watchlist countries (e.g., Russia, China, Iran).  
3. **Impossible Travel** – Same username seen from different countries within 1 hour.  
4. **Admin Account Abuse** – Any login attempts against `Administrator` or variants.  
5. **Distributed Attack** – >20 unique IPs targeting the honeypot in 10 minutes.  

---

## 📊 Visualizations
- **Timeline Chart:** Shows spikes in brute-force attempts over time.  
- **Geo Map:** Displays attacker source locations globally.  
- **Top 10 Attackers Table:** Highlights IPs with the highest number of attempts.  
- **Username Distribution:** Shows variations of admin usernames targeted.  


<img width="2000" height="1000" alt="rdp_top_ips" src="https://github.com/user-attachments/assets/13eea67b-3642-452b-9433-a0abda0ef834" />
<img width="2000" height="1000" alt="rdp_timeline" src="https://github.com/user-attachments/assets/d928cb80-ce88-4a1f-a741-6c463f8ddfe2" />
<img width="2000" height="1000" alt="rdp_top_users" src="https://github.com/user-attachments/assets/a884b2df-d394-4fe8-b4bb-4b1a8a36b0ad" />
<img width="2000" height="1000" alt="rdp_top_countries" src="https://github.com/user-attachments/assets/efff8607-e53a-4598-a58c-ce58fa380b81" />


---

## ✅ Lessons Learned
- Attackers focus overwhelmingly on default/admin accounts.  
- Normalizing logs into a SIEM data model allows flexible detections and dashboards.  
- Even small honeypots capture valuable real-world attack data.  
- Geo-mapping provides strong situational awareness for SOC teams.  

---

## 🔮 Next Steps
- Add Windows Event Logs to correlate successful logins.  
- Create Sigma rules for cross-SIEM portability.  
- Map detections to **MITRE ATT&CK T1110 (Brute Force)**.  
- Set thresholds to reduce false positives in production SOC environments.  
