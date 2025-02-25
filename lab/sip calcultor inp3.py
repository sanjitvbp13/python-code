

def calculate_sip_future_value(monthly_investment, annual_return, years):
    monthly_return_rate = (annual_return / 100) / 12
    
   
    total_months = years * 12
    
    
    future_value = monthly_investment * (((1 + monthly_return_rate) ** total_months - 1) / monthly_return_rate) * (1 + monthly_return_rate)
    
    return future_value

def main():
    print("SIP Mutual Fund Calculator")
    
   
    try:
        monthly_investment = float(input("monthly investment amount: "))
        annual_return = float(input("expected annual return (in %): "))
        years = float(input("years for investment: "))
        
        # Calculate future value
        future_value = calculate_sip_future_value(monthly_investment, annual_return, years)
        
        # Calculate invested amount and estimated return
        invested_amount = monthly_investment * years * 12
        estimated_return = future_value - invested_amount
              
        print(f"Total amount invested: ₹{invested_amount:,.2f}")
        print(f"Estimated return: ₹{estimated_return:,.2f}")
        print(f"\ntotal value: ₹{future_value:,.2f}")
    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    main()
