def verify_card_number(card_number):
    # Entferne Leerzeichen und Bindestriche
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Prüfe, ob die Eingabe nur aus Ziffern besteht
    if not card_number.isdigit():
        return "INVALID!"
    
    total = 0
    num_digits = len(card_number)
    
    # Beginne von rechts, jede zweite Ziffer (außer die Prüfziffer) verdoppeln
    for i in range(num_digits):
        digit = int(card_number[num_digits - 1 - i])
        # Jede zweite Ziffer verdoppeln (Index i wird von rechts gezählt)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9  # Das ist dasselbe wie die beiden Ziffern zu summieren
        total += digit
    
    # Prüfen, ob die Summe ein Vielfaches von 10 ist
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"

# Beispielaufrufe:
print(verify_card_number('453914889'))            # VALID!
print(verify_card_number('4111-1111-1111-1111')) # VALID!
print(verify_card_number('453914881'))           # INVALID!
print(verify_card_number('1234 5678 9012 3456')) # INVALID!
