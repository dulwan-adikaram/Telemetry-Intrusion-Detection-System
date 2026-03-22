import pandas as pd
import matplotlib.pyplot as plt
import time

print("\n====================================")
print("  Telemetry Intrusion Detection System ")
print("====================================\n")

# Load telemetry dataset
data = pd.read_csv("telemetry_data.csv")

# Reset index to avoid index errors
data = data.reset_index(drop=True)

# ---------------------------------
# ATTACK SIMULATION (FINAL 🔥)
# ---------------------------------

print("\n⚠️ Injecting simulated telemetry attacks...\n")

# Use only valid indices (0–13)
data.loc[8, "speed"] = 300
data.loc[9, "rpm"] = 15000
data.loc[10, "brake"] = 100
data.loc[11, "throttle"] = 95
data.loc[11, "brake"] = 90

print("Telemetry Data Preview:\n")
print(data.head())

print("\nTotal telemetry records:", len(data))


# ---------------------------------
# TELEMETRY DASHBOARD VISUALIZATION
# ---------------------------------

plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.plot(data["time"], data["speed"])
plt.title("Speed Telemetry")

plt.subplot(3,1,2)
plt.plot(data["time"], data["throttle"])
plt.title("Throttle Telemetry")

plt.subplot(3,1,3)
plt.plot(data["time"], data["brake"])
plt.title("Brake Telemetry")

plt.tight_layout()
plt.show()


# ---------------------------------
# TELEMETRY SECURITY MONITOR
# ---------------------------------

print("\nStarting Real-Time Telemetry Monitoring...\n")

alerts = 0
log_file = open("security_log.txt", "a")

for index, row in data.iterrows():

    # Skip invalid rows
    if pd.isna(row["speed"]) or pd.isna(row["rpm"]):
        continue

    print(f"Time {row['time']}s | Speed:{row['speed']} | Throttle:{row['throttle']} | Brake:{row['brake']} | RPM:{row['rpm']}")

    # Speed anomaly detection (safe)
    if index > 0:
        try:
            prev_speed = data.loc[index - 1, "speed"]

            if abs(row["speed"] - prev_speed) > 80:
                alert = f"[ALERT] Sudden speed spike detected at time {row['time']}"
                print(alert)
                log_file.write(alert + "\n")
                alerts += 1
        except:
            pass

    # RPM anomaly
    if row["rpm"] > 11000:
        alert = f"[ALERT] RPM anomaly detected at time {row['time']} : {row['rpm']} RPM"
        print(alert)
        log_file.write(alert + "\n")
        alerts += 1

    # Brake anomaly
    if row["brake"] > 95:
        alert = f"[ALERT] Brake anomaly detected at time {row['time']} : {row['brake']}%"
        print(alert)
        log_file.write(alert + "\n")
        alerts += 1

    # Impossible driver input
    if row["throttle"] > 80 and row["brake"] > 50:
        alert = f"[ALERT] Impossible driver input detected at time {row['time']}"
        print(alert)
        log_file.write(alert + "\n")
        alerts += 1

    time.sleep(1)

log_file.close()


# ---------------------------------
# SPEED ANOMALY VISUALIZATION
# ---------------------------------

plt.figure()

plt.plot(data["time"], data["speed"], label="Speed")

anomaly_points = data[abs(data["speed"].diff()) > 80]

plt.scatter(anomaly_points["time"], anomaly_points["speed"])

plt.title("Speed Telemetry Monitoring")
plt.xlabel("Time")
plt.ylabel("Speed")
plt.legend()

plt.show()


# ---------------------------------
# FINAL REPORT
# ---------------------------------

print("\n====================================")
print(" Telemetry Security Report ")
print("====================================")

if alerts == 0:
    print("No telemetry anomalies detected.")
else:
    print(f"Total anomalies detected: {alerts}")

print("\nSecurity events saved to security_log.txt")
print("\nTelemetry monitoring completed.")