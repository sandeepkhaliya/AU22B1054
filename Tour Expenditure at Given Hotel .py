Room_type=input("Type of room booked- ")
if Room_type== "Deluxe room" or Room_type=="Deluxe Room" or Room_type=="DELUXE ROOM" or Room_type=="deluxe room" or Room_type=="deluxe" or Room_type=="Deluxe":
    days=int(input("Total number of days- "))
    food_amount=float(input("Total Amount of food- "))
    Room_Tariff= 7500*days
    tax_on_food=0.18*food_amount
    tip= 0.1*food_amount
    cgst=tax_on_food/2
    sgst=tax_on_food/2
    Total=Room_Tariff+tax_on_food+tip+food_amount
    print("Room Tariff: INR",Room_Tariff)
    print("Gst- CGST= INR",cgst,"SGST= INR",sgst)
    print("Tip: INR",tip)
    print("Grand Total: INR",Total)
elif Room_type== "NON AC ROOM" or Room_type=="non-ac room" or Room_type=="Non-ac room" or Room_type=="Non AC Room" or Room_type=="non ac room" or Room_type=="non ac":
    days=int(input("Total number of days- "))
    food_amount=float(input("Total Amount of food- "))
    Room_Tariff= 4500*days
    tax_on_food=0.05*food_amount
    tip= 0.1*food_amount
    cgst=tax_on_food/2
    sgst=tax_on_food/2
    Total=Room_Tariff+tax_on_food+tip+food_amount
    print("Room Tariff: INR",Room_Tariff)
    print("Gst- CGST= INR",cgst,"SGST= INR",sgst)
    print("Tip: INR",tip)
    print("Grand Total: INR",Total)
else:
    print("Invalid Room Type")