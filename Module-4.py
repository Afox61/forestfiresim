import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
def read_weather(choice):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and high temperatures from this file.
        dates, highs = [], []
        
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                high = int(row[5])
                highs.append(high)
                if choice == 'high':
                    temp + int(row[5])
                elif choice == 'low':
                    temp = int(row[6])   
            except ValueError:
                continue
            else:
                dates.append(current_date)
                temps.append(temp)

    return dates, highs

# Plot the high temperatures.
#plt.style.use('seaborn')

def plot_weather(dates, temps, label, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    plt.title(f"Daily {label} Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def main():
    while True:
        print("\nMenu:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            dates, temps = read_weather('highs')
            plot_weather(dates, temps, "High", "red")
        elif choice == '2':
            dates, temps = read_weather('lows')
            plot_weather(dates, temps, "Low", "blue")
        elif choice == '3':
            print("Thanks for using the weather viewer. Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

