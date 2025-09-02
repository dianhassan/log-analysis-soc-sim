#!/usr/bin/env python3
"""
parse_rdp_logs_fixed.py

Parses your 'rdp_fail.logs' file into a structured CSV and generates summary stats + chart.
"""

import re
import os
import pandas as pd
import matplotlib.pyplot as plt


def parse_logs(log_file):
    # Regex pattern for typical RDP failed logon lines
    pattern = re.compile(
        r'(?P<timestamp>\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}).*?'
        r'LogonType=(?P<logontype>\d+).*?'
        r'User=(?P<user>\S+).*?'
        r'SourceIP=(?P<ip>\S+).*?'
        r'Status=(?P<status>\S+)'
    )

    rows = []
    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                rows.append(match.groupdict())

    df = pd.DataFrame(rows)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df.dropna(subset=["timestamp"])


def analyze(df, outdir="results"):
    os.makedirs(outdir, exist_ok=True)

    # Save parsed logs
    parsed_path = os.path.join(outdir, "parsed_logs.csv")
    df.to_csv(parsed_path, index=False)
    print(f"[+] Parsed logs saved to {parsed_path}")

    # Top IPs
    top_ips = df["ip"].value_counts().head(10)
    print("\n[Top Failed Source IPs]")
    print(top_ips)

    # Top users
    top_users = df["user"].value_counts().head(10)
    print("\n[Top Targeted Users]")
    print(top_users)

    # Status codes
    statuses = df["status"].value_counts()
    print("\n[Failure Status Codes]")
    print(statuses)

    # Time series chart
    chart_path = os.path.join(outdir, "failed_over_time.png")
    df.set_index("timestamp").resample("5min").size().plot()
    plt.title("Failed RDP logons over time")
    plt.ylabel("Attempts")
    plt.tight_layout()
    plt.savefig(chart_path)
    print(f"[+] Chart saved to {chart_path}")


def main():
    # Use your specific log file here
    log_file = "rdp_fail.logs"

    if not os.path.exists(log_file):
        print(f"[-] Could not find {log_file}. Make sure it's in the same folder as this script.")
        return

    df = parse_logs(log_file)
    if df.empty:
        print("[-] No valid log entries parsed. Check regex pattern or log format.")
        return

    analyze(df, outdir="results")


if __name__ == "__main__":
    main()
