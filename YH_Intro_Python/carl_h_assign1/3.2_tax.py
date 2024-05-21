#ask the users for there monthly income
income_user = int(input("Enter you income for this month:"))

#test if the users income is lower then 38k a month, then we calculat the tax by 30%
if income_user < 38000:
    
    taxincome = income_user * 0.30

    print("Your incometaxes are:", round(taxincome))
#if the users income is higher then 38k but lower then 50k, we calculat using 35%
elif income_user >= 38000 and income_user <= 50000:

    taxincome = 38000 * 0.30 + (income_user -38000) * 0.35
    
    print("Your incometaxes are:", round(taxincome))
#else if the users income is higher then 50k(brooklyn 99: noice) a month, then we calculat the tax by 40%
else:
    
    taxincome = 38000 * 0.30 + 12000 * 0.35 + (income_user - 50000) * 0.40
    
    print("Your incometaxes are:", round(taxincome))
##### THE END #####