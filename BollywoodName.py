#Bollywood Name Generator:
first_name = input("Enter the first name of any bollywood actor")
last_name = input("Enter the last name of any bollywood actor")
print(f'*************************************************************************\n')
print(f'***   Entered Name: "{first_name} {last_name}"')
print(f'***   Hero:         "{first_name[::-1]} {last_name.upper()}"')
print(f'***   Villain:      "THE {first_name.upper()} {last_name.upper()}"')
print(f'***   Comedian:     "{first_name.title()} {last_name.title()} Ji"')
print();
print(f'*************************************************************************\n')
