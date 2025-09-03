# Data Model

This data model defines the normalized fields parsed from honeypot logs.

| Field          | Description                               | Example                  |
|----------------|-------------------------------------------|--------------------------|
| timestamp      | Event time                                | 2024-01-24 01:05:00      |
| sourcehost     | Source IP address (attacker)              | 61.178.82.2              |
| destinationhost| Target system                             | honeypot-vm              |
| username       | Account name used in login attempt        | Administrator            |
| country        | Geo-located country of source IP          | China                    |
| state          | Geo-located region/state (if available)   | null                     |
| latitude       | Latitude of source IP                     | 51.061544                |
| longitude      | Longitude of source IP                    | 30.295947                |
| label          | Combined identifier (country + IP)        | China - 61.178.82.2      |
