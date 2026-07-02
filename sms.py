#SMS
sms = input("Enter the message: ")

print(f"Per SMS charges is Rs 0.50")
print(f"Only 160 characters are allowed in one SMS for standard price")
print(f"If SMS exceeds more than 160 characters then per character it wll charge RS 0.01")
print(f"Number of characters entered by you is: {len(sms)}")

exceed_characters = sms[160:]
exceed_char_count = len(exceed_characters)
extra_charge = 0.01 * exceed_char_count

print(f"""Exceeded characters are '{exceed_characters}' 

Count of extra characters is {exceed_char_count}""")

print(f"Extra charges for the extra characters at the rate of 0.01 per character is {extra_charge}")
print(f"Total SMS charge is: Rs {extra_charge + 0.50}/-")

print(f"Does SMS contains Spam words related to membership?: {'Free membership' in sms}")
print(f"Does SMS contains Spam words related to urgency?: {'Take action' in sms}")
