Define the exchange rate
inr_to_usd_exchange_rate = 84.50

Input the amount in INR
inr_amount = float(input("Enter the amount in INR: "))

Perform the conversion
usd_amount = inr_amount / inr_to_usd_exchange_rate

Display the result
print(f"{inr_amount} INR is equal to {usd_amount} USD")