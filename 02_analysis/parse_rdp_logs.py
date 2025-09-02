#!/usr/bin/env python3
"""
parse_rdp_honeypot_logs.py

Parses 'rdp_fail.logs' in key=value format into a structured CSV
and generates summary stats + charts.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def parse_logs(log_file):
    rows = []
    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            entry = {}
            parts = line.strip().split(",")
            for part in parts:
                if ":" in part:
                    k, v = part.split(":", 1)
                    entry[k.strip()] = v.strip()
            if entry:
                rows.append(entry)

    df = pd.DataFrame(rows)

    # Normalize timestamp column
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    return df.dropna(subset=["timestamp"])


def analyze(df, outdir="results"):
    os.makedirs(outdir, exist_ok=True)

    # Save parsed logs
    parsed_path = os.path.join(outdir, "parsed_logs.csv")
    df.to_csv(parsed_path, index=False)
    print(f"[+] Parsed logs saved to {parsed_path}")

    # Top source IPs
    top_ips = df["sourcehost"].value_counts().head(10)
    print("\n[Top Failed Source IPs]")
    print(top_ips)

    # Top targeted usernames
    top_users = df["username"].value_counts().head(10)
    print("\n[Top Targeted Usernames]")
    print(top_users)

    # Top countries
    if "country" in df.columns:
        top_countries = df["country"].value_counts().head(10)
        print("\n[Top Source Countries]")
        print(top_countries)

    # Time series chart
    chart_path = os.path.join(outdir, "failed_over_time.png")
    df.set_index("timestamp").resample("5min").size().plot()
    plt.title("Failed RDP logons over time")
    plt.ylabel("Attempts")
    plt.xlabel("Time")
    plt.tight_layout()
    plt.savefig(chart_path)
    print(f"[+] Chart saved to {chart_path}")


def main():
    log_file = "rdp_fail.logs"  # Your log file

    if not os.path.exists(log_file):
        print(f"[-] Could not find {log_file}. Make sure it's in the same folder as this script.")
        return

    df = parse_logs(log_file)
    if df.empty:
        print("[-] No valid log entries parsed. Check log format.")
        return

    analyze(df, outdir="results")


if __name__ == "__main__":
    main()
