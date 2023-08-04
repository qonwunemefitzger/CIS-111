def compute_monthly_payment(PV, r, n):
    r = r / 100  # Convert APR to decimal
    r_monthly = r / 12  # Monthly interest rate
    Pmt = r_monthly * PV / (1 - (1 + r_monthly) ** (-n))
    return Pmt

if __name__ == "__main__":
    PV = 12000
    r = 7.45
    n = 48

    monthly_payment = compute_monthly_payment(PV, r, n)
    print(f"The monthly payment amount is: ${monthly_payment:.2f}")
