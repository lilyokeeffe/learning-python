temperatures= [12, 18, 7, 24, 31, 15, 9]
for temperature in temperatures:
    if temperature > 28:
        print(f"Stopped at {temperature}-temperature too high")
        break
    print (temperature)
