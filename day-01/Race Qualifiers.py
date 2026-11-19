qualified = 0
winner_name = ""
winner_seconds = 99999
winner_time = ""
total_runners = 0

name = input("Enter athlete name: ")

while name != "x":

    time = input("Enter time (mm:ss): ")

    if ":" in time:

        parts = time.split(":")

        if len(parts) == 2:

            if parts[0].isdigit() and parts[1].isdigit():

                minutes = int(parts[0])
                seconds = int(parts[1])

                if 0 <= seconds < 60:

                    total_seconds = minutes * 60 + seconds

                    total_runners += 1

                    if total_seconds <= 1500:
                        qualified += 1

                    if total_seconds < winner_seconds:
                        winner_seconds = total_seconds
                        winner_name = name
                        winner_time = time

    name = input("Enter athlete name: ")

if total_runners > 0:
    print("Winner:", winner_name, "(" + winner_time + ")")
    print("Qualified:", qualified, "of", total_runners)
else:
    print("No athletes entered")