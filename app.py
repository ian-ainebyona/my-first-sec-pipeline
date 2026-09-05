def calculate_total(price: float, tax_rate: float) -> float:
    return price + (price * tax_rate)

def main():
    print("---Sales Tax Calculator---")
    try:
        #capture input and convert text to decimal numbers(float)
        
        price = float(input("Enter item price ($)"))
        tax_rate= float(input("Enter tax rate (e.g., 0.05 for 5%)"))

        if price <0 or tax_rate < 0:
            print("Error: Price and tax rate must be positive numbers.")
        else:
            total = calculate_total(price, tax_rate)
            #:.2f formats the number to 2 decimal places
            print(f"Total price including tax: ${total:.2f}")
    except ValueError:
        print("Error: Invalid input. Please enter valid numeric values only.")

if __name__ == "__main__":
    main()
    