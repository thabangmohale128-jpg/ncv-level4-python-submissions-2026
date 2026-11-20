#THABANG DAVID MOHALE                      20 NOVEMBER 2026
# ============================================================
# COMMUNITY WATER CONSUMPTION AND BILLING MANAGEMENT SYSTEM
# Input: water_readings.txt (220 records)
# Output: billing_report.txt, errors.log
# Tariff: First 6 kL Free | Next 14 kL @ R8.50 | Above 20 kL @ R12.00
# Categories: LOW 0-20 kL | MODERATE 21-50 kL | HIGH above 50 kL
# Rules: No sorted(), max(), min(), sum() - loops only
# ============================================================

# ---------- User-defined functions ----------
# Q5: Progressive tariff - NOT flat rate
# Example: 25 kL = (14 x 8.50) + (5 x 12.00) = R179.00
def calculate_charge(consumption):
        if consumption <= 6:
        return 0.0
    elif consumption <= 20:
        return (consumption - 6) * 8.50
    else:
        return (14 * 8.50) + ((consumption - 20) * 12.00)
# Q6: Classification
def get_label(consumption):
      if consumption <= 20:
        return "LOW"
    elif consumption <= 50:
        return "MODERATE"
    else:
        return "HIGH"
# Q7: Manually rank top 5 - NO sorted(), max(), min()
# Build list of [meter, consumption] from dictionary
def rank_top_five(households):
      ranking = []
    for meter in households:
        ranking.append([meter, households[meter]["consumption"]])
# Bubble Sort - largest first
    n = len(ranking)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ranking[j][1] < ranking[j + 1][1]:
                temp = ranking[j]
                ranking[j] = ranking[j + 1]
                ranking[j + 1] = temp
# Return top 5
    top5 = []
    count = 0
    for item in ranking:
        if count < 5:
            top5.append(item)
            count = count + 1
    return top5

# Q1: Read file, handle missing file
print("=== WATER BILLING SYSTEM ===")
try:
    f = open("water_readings.txt", "r")
    lines = f.readlines()
    f.close()
    print(f"File loaded: {len(lines)} lines read")
except FileNotFoundError:
    print("ERROR: water_readings.txt not found!")
    lines = []

# Q2 + Q3: Split, clean, validate, store in dictionary 
households = {}
errors_log = []
rejected = 0

for line in lines:
    original = line.strip()
    if original == "":
        continue
    parts = original.split(",")
# Q3a: Missing fields - must have 5 fields
    if len(parts) != 5:
        errors_log.append(original + " | REASON: Missing fields - expected 5 fields")
        rejected = rejected + 1
        continue
# Q2: Clean fields
    meter = parts[0].strip()
    name = parts[1].strip()
    prev_str = parts[2].strip()
    curr_str = parts[3].strip()
    area = parts[4].strip()
# Q3b: Missing fields - empty field
    if meter == "" or name == "" or prev_str == "" or curr_str == "" or area == "":
        errors_log.append(original + " | REASON: Missing fields - empty field")
        rejected = rejected + 1
        continue
# Q3c: Duplicate meter number
    if meter in households:
        errors_log.append(original + " | REASON: Duplicate meter number")
        rejected = rejected + 1
        continue
# Q3d: Non-numeric readings
    try:
        prev = int(prev_str)
        curr = int(curr_str)
    except:
        errors_log.append(original + " | REASON: Non-numeric reading")
        rejected = rejected + 1
        continue
# Q3e: Negative readings
    if prev < 0 or curr < 0:
        errors_log.append(original + " | REASON: Negative reading")
        rejected = rejected + 1
        continue
# Q3f: Current below previous
    if curr < prev:
        errors_log.append(original + " | REASON: Current reading below previous reading")
        rejected = rejected + 1
        continue
# Q4: Consumption
    consumption = curr - prev
# Q5: Bill
    charge = calculate_charge(consumption)
# Q6: Classification
    label = get_label(consumption)
# Q2: Store valid record in dictionary
    households[meter] = {
        "name": name,
        "prev": prev,
        "curr": curr,
        "area": area,
        "consumption": consumption,
        "charge": charge,
        "label": label
    }

# Q7: Rank top 5 
top5 = rank_top_five(households)

# Totals with loops - no sum()
accepted = len(households)
total_consumption = 0
total_charge = 0.0
low_count = 0
moderate_count = 0
high_count = 0
for meter in households:
    total_consumption = total_consumption + households[meter]["consumption"]
    total_charge = total_charge + households[meter]["charge"]
    if households[meter]["label"] == "LOW":
        low_count = low_count + 1
    elif households[meter]["label"] == "MODERATE":
        moderate_count = moderate_count + 1
    else:
        high_count = high_count + 1

# Q8: Write billing_report.txt 
# Must show: billing info + categories + top 5 + summary
out = open("billing_report.txt", "w")
out.write("=== COMMUNITY WATER BILLING REPORT ===\n\n")
out.write("--- VALID HOUSEHOLD BILLING INFORMATION ---\n")
out.write("MeterNumber,HouseholdName,Area,Previous,Current,Consumption(kL),Charge(R),Category\n")
for meter in households:
    h = households[meter]
    out.write(f"{meter},{h['name']},{h['area']},{h['prev']},{h['curr']},{h['consumption']},{h['charge']:.2f},{h['label']}\n")
out.write("\n--- TOP 5 HIGHEST CONSUMING HOUSEHOLDS ---\n")
for i in range(len(top5)):
    meter = top5[i][0]
    h = households[meter]
    out.write(f"{i+1}. {meter} - {h['name']} ({h['area']}) - {h['consumption']} kL - R{h['charge']:.2f} - {h['label']}\n")
out.write("\n--- SUMMARY ---\n")
out.write(f"Accepted (valid): {accepted}\n")
out.write(f"Rejected (invalid): {rejected}\n")
out.write(f"Total consumption: {total_consumption} kL\n")
out.write(f"Total billed: R{total_charge:.2f}\n")
out.write(f"LOW: {low_count} | MODERATE: {moderate_count} | HIGH: {high_count}\n")
out.close()

# Q8: Write errors.log 
err_file = open("errors.log", "w")
for e in errors_log:
    err_file.write(e + "\n")
err_file.close()

# Q8: Display accepted and rejected totals
print("\n--- SUMMARY ---")
print(f"Accepted (valid): {accepted}")
print(f"Rejected (invalid): {rejected}")
print(f"Total consumption: {total_consumption} kL")
print(f"Total billed: R{total_charge:.2f}")
print(f"LOW: {low_count} | MODERATE: {moderate_count} | HIGH: {high_count}")
print("\n--- TOP 5 HIGHEST CONSUMING HOUSEHOLDS ---")
for i in range(len(top5)):
    meter = top5[i][0]
    h = households[meter]
    print(f"{i+1}. {meter} - {h['name']} ({h['area']}) - {h['consumption']} kL - R{h['charge']:.2f} - {h['label']}")
print("\nFiles created: billing_report.txt, errors.log")