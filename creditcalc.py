import argparse
import math


parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

error_msg = "Incorrect parameters."

parameters = [args.type, args.payment, args.principal, args.periods, args.interest]

num_of_none_input_params = 0
for par in parameters:
    if not par:
        num_of_none_input_params += 1

is_zero_values = False
for ind in range(1, len(parameters)):
    if parameters[ind]:
        if float(parameters[ind]) < 0:
            is_zero_values = True

if num_of_none_input_params > 1:
    print(error_msg)
elif not args.interest:
    print(error_msg)
elif args.type != "annuity" and args.type != "diff":
    print(error_msg)
elif args.type == "diff" and args.payment:
    print(error_msg)
elif is_zero_values:
    print(error_msg)

elif args.type == "diff":
    loan_principal = float(args.principal)
    number_of_periods = int(args.periods)
    loan_interest = float(args.interest)
    nominal_interest = loan_interest / 100 / 12
    full_sum = 0
    for n in range(1, number_of_periods + 1):
        diff_payment = math.ceil(loan_principal / number_of_periods + nominal_interest * (loan_principal - loan_principal * (n - 1) / number_of_periods))
        full_sum += diff_payment
        print("Month " + str(n) + ": payment is " + str(diff_payment))

    print("")
    print("Overpayment = ", str(math.ceil(full_sum - loan_principal)))

elif args.type == "annuity":
    if not args.periods:
        loan_principal = float(args.principal)
        monthly_payment = float(args.payment)
        loan_interest = float(args.interest)
        nominal_interest = loan_interest / 100 / 12
        n = math.ceil(math.log(monthly_payment / (monthly_payment - nominal_interest * loan_principal), nominal_interest + 1))
        full_sum = monthly_payment * n

        years = n // 12
        months = n % 12

        if years == 0:
            str_and = ''
            str_years = ''
            if months == 1:
                str_months = str(months) + " month"
            else:
                str_months = str(months) + " months"
        else:
            if years == 1:
                if months == 0:
                    str_and = ''
                    str_months = ''
                    str_years = str(years) + " year"
                elif months == 1:
                    str_and = " and "
                    str_months = str(months) + " month"
                    str_years = str(years) + " year"
                else:
                    str_and = " and "
                    str_months = str(months) + " months"
                    str_years = str(years) + " year"
            else:
                if months == 0:
                    str_and = ''
                    str_months = ''
                    str_years = str(years) + " years"
                elif months == 1:
                    str_and = " and "
                    str_months = str(months) + " month"
                    str_years = str(years) + " years"
                else:
                    str_and = " and "
                    str_months = str(months) + " months"
                    str_years = str(years) + " years"

        print('It will take {str_years}{str_and}{str_months} to repay this loan!'.format(str_years=str_years,
                                                                                         str_months=str_months,
                                                                                         str_and=str_and))
        print("Overpayment = ", str(math.ceil(full_sum - loan_principal)))

    elif not args.payment:
            loan_principal = float(args.principal)
            number_of_periods = int(args.periods)
            loan_interest = float(args.interest)
            nominal_interest = loan_interest / 100 / 12

            monthly_payment = math.ceil(loan_principal * nominal_interest * math.pow(1 + nominal_interest, number_of_periods) / (math.pow(1 + nominal_interest, number_of_periods) - 1))
            full_sum = monthly_payment * number_of_periods

            print('Your annuity payment = {monthly_payment}!'.format(monthly_payment=monthly_payment))
            print("Overpayment = ", str(math.ceil(full_sum - loan_principal)))

    elif not args.principal:
            monthly_payment = float(args.payment)
            number_of_periods = int(args.periods)
            loan_interest = float(args.interest)
            nominal_interest = loan_interest / 100 / 12

            loan_principal = math.floor(monthly_payment * (math.pow(nominal_interest + 1, number_of_periods) - 1) / nominal_interest / math.pow(nominal_interest + 1, number_of_periods))
            full_sum = monthly_payment * number_of_periods

            print('Your loan principal = {loan_principal}!'.format(loan_principal=loan_principal))
            print("Overpayment = ", str(math.ceil(full_sum - loan_principal)))
