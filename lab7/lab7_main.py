#!/usr/bin/python3

import bank_account

def main():
    # Create some BankAccount objects
    checking = bank_account.BankAccount(123, 'John', 1000)
    checking2 = bank_account.BankAccount(7879, 'Sally', 2500)
    savings = bank_account.BankAccount(5641, 'Marty', 9500)
    savings2 = bank_account.BankAccount(8987, 'Erin', 150)

    # Print each of them
    print('======================= INITIAL ACCOUNT STATE ===================\n')
    print(checking)
    print(checking2)
    print(savings)
    print(savings2)

    # Put each of them into a list, then loop through them and deposit $100
    # in each
    print('\n======================= DEPOSIT $100 =====================\n')
    accounts = [checking, checking2, savings, savings2]
    for a in accounts:
        a.deposit(100)
        print(a, a.get_transactions())

    # John and Sally have gotten married, so change their accounts to joint
    # ownership
    print('\n======================= SET JOINT OWNERSHIP ===================\n')
    print(checking.get_account_number(), checking.get_owner())
    print(checking2.get_account_number(), checking2.get_owner())
    checking.set_owner('John and Sally')
    checking2.set_owner('John and Sally')
    print(checking.get_account_number(), checking.get_owner())
    print(checking2.get_account_number(), checking2.get_owner())

    # It's bill time, let's take some withdrawals
    print('\n======================= WITHDRAWAL $500 ===================\n')
    for a in accounts:
        try:
            a.withdrawal(500)
            print(a, a.get_transactions())
        except ValueError as e:
            # Notice you can pass exceptions and objects to format strings
            # just like regular values. That's because each defines a __str__
            # method!
            print('{}! {}'.format(e, a))

    ##Uncomment these lines when you have the transfer method working.
    #print('\n======================= TRANSFERS ===================\n')
    # This one should work.
    #try:
    #    savings.transfer(savings2, 4500)
    #    print(savings, savings.get_transactions())
    #    print(savings2, savings2.get_transactions())
    #except ValueError as e:
    #    print('{}! {}'.format(e, savings))
    ## This should value due to insufficient funds
    #try:
    #    checking.transfer(checking2, 2500)
    #    print(checking, checking.get_transactions())
    #    print(checking2, checking2.get_transactions())
    #except ValueError as e:
    #    print('{}! {}'.format(e, checking))


main()
