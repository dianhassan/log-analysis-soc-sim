# Detection Use Cases

These use cases are built from the honeypot log data model.

---

## 1. Brute Force Login Attempts
- **Description:** Detect repeated failed login attempts from the same source host against the honeypot.
- **Fields used:** `sourcehost`, `username`, `timestamp`
- **Logic:** More than 10 failed attempts within 5 minutes.
- **Severity:** Medium

---

## 2. Suspicious Geo Access
- **Description:** Identify login attempts originating from high-risk or unusual countries.
- **Fields used:** `country`, `sourcehost`
- **Logic:** Source country in a predefined "watchlist" (e.g., China, Russia, Iran, DPRK).
- **Severity:** Medium to High

---

## 3. Impossible Travel
- **Description:** Detect the same username logging in from two different countries within 1 hour.
- **Fields used:** `username`, `country`, `timestamp`
- **Logic:** Compare consecutive events per username; trigger if `country` changes within ≤ 1 hour.
- **Severity:** Medium

---

## 4. Admin Account Abuse
- **Description:** Detect login attempts targeting privileged accounts.
- **Fields used:** `username`, `destinationhost`
- **Logic:** Username in list of admin accounts (e.g., `Administrator`, `root`) AND login attempt present.
- **Severity:** High

---

## 5. Distributed Attack (Multiple Sources)
- **Description:** Identify multiple unique source IPs targeting the same honeypot within a short time frame.
- **Fields used:** `destinationhost`, `sourcehost`, `timestamp`
- **Logic:** > 20 distinct `sourcehost` values in 10 minutes against the same `destinationhost`.
- **Severity:** High

---

## 6. Geo Visualization (Situational Awareness)
- **Description:** Plot attacker source IPs on a world map to see where attacks originate.
- **Fields used:** `latitude`, `longitude`, `country`, `sourcehost`
- **Logic:** Map each event using `iplocation` fields; aggregate by country or city.
- **Severity:** Informational (dashboard visualization)
