# tuple გამოიყენება ელემენტების ჯგუფურად შესანახად.
# ის ჰგავს სიას (list) მაგრამ განსხვავებით სიებისგან
# ტაფლი უცვლადია (immutable) — მასში არსებული ელემენტების შეცვლა შეუძლებელია

# ტაფლის ძირითადი თვისებები
#  უცვლადობა (immutable)
#  წვდომა ინდექსით
#  შესაძლებელია სხვადასხვაგვარი ტიპის ელემენტების შენახვა


vegetables = ("კიტრი", "პამიდორი", "ბროკოლი", "სტაფილო", "ბადრიჯანი")


print(len(vegetables))


sorted_vegetables = sorted(vegetables)
print(sorted_vegetables)


veg1, veg2, veg3, *rest = vegetables

print("პირველი:", veg1)
print("მეორე:", veg2)
print("მესამე:", veg3)
print("დანარჩენი:", rest)
