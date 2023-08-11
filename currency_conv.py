# Real-time Currency Converter with Python
        
# Install forex_python package
from forex_python.converter import CurrencyRates

def main():
  c = CurrencyRates()
  amount = int(input("Enter the amount: "))
  from_currency = input("From Currency: ").upper()
  to_currency = input("To Currency: ").upper()
  
  result = c.convert(from_currency, to_currency, amount)
  print(famount {from_currency} is equal to {result:.2f} {to_currency}")
