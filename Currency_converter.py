def get_amount():
    while True:
        try: 
            amount = float(input("Enter the amount: "))
            if amount<=0:
                raise ValueError()
            return amount
        except ValueError:
            print("Invalid Amount")

def get_currency(label):
    currency=('USD','EUR','CAD')
    while True:
        currencies= input(f"{label} (USD/EUR/CAD): ").upper()
        if currencies not in currency:
            print("invalid currency")
        else:
            return currencies

def converter(amount, source_curreny, target_currency):
    exchange_rates = {
        'USD': { 'EUR': 0.85, 'CAD': 1.25 },
        'EUR': { 'USD': 1.18, 'CAD': 1.47 },
        'CAD': { 'USD': 0.80, 'EUR': 0.68 },
    }
    if source_curreny == target_currency:
        return amount
    else:
        amount= amount*exchange_rates[source_curreny][target_currency]
        return amount

def main():
    amount= get_amount()
    source_curreny= get_currency("source_curreny")
    target_currency= get_currency("target_currency")
    converted_amount= converter(amount, source_curreny, target_currency)
    print(f"{amount} {source_curreny} is equal to {converted_amount} {target_currency}")




if __name__ == "__main__":
  main()








