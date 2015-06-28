import os
while True:
    print("Region:\n1.) Oregon\n2.) N. Virginia\n3.) N. California")
    os.system("aws ec2 describe-instances --output table")
    n = raw_input("Would you like to Exit? Enter 'Y' or 'Yes' to exit:")
    n = n.lower()
    if (n.strip() == 'yes') or (n.strip() == 'y'):
        break
