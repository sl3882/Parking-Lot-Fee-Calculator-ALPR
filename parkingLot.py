
import os
from datetime import datetime, timedelta

import obtainPlateNumber

parking_log = {}
backup_folder = 'C:/Users/lsy84/PycharmProjects/ocrProject/temp'
ob = obtainPlateNumber
def entry(plateNum):
    if plateNum not in parking_log:
        entry_time = datetime.now()
        parking_log[plateNum] = entry_time
        print(f"Vehicle {plateNum} entered at {entry_time}")
    else:
        print(f"Vehicle {plateNum} is already in the parking lot.")

def exit(plateNum, base_rate=10.0, additional_rate=5.0):

    if plateNum in parking_log:
        entry_time = parking_log[plateNum]
        exit_time = datetime.now() + timedelta(minutes=75)

        # Calculate the time spent in hours
        time_spent = exit_time - entry_time
        minutes_spent = time_spent.total_seconds() / 60  # Convert time spent to minutes
        parking_fee = base_rate
        if minutes_spent > 30:
            additional_periods = (minutes_spent - 30) // 30  # Each additional 30 minutes
            parking_fee += additional_periods * additional_rate

        # Calculate parking fee
        print(f"Vehicle {plateNum} exited at {exit_time}.")
        print(f"Total time spent: {minutes_spent:.2f} minutes, Parking fee: ${parking_fee:.2f}")

        # Remove vehicle from parking log
        del parking_log[plateNum]
        image_path = os.path.join(backup_folder, f"{plateNum}.jpg")
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Backup image {plateNum}.jpg has been deleted.")
        else:
            print(f"No backup image found for {plateNum}.")
    else:
        print(f"Vehicle {plateNum} not found in parking log.")

if __name__ == '__main__':
    car1 = ob.getPlate("data/1.jpg")
    car2 = ob.getPlate("data/2.jpg")
    entry(car1)
    entry(car2)

    exit(car1)
