signal = input("Enter traffic signal (red/yellow/green): ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")