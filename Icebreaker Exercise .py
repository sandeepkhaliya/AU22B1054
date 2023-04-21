
a=int(input("Enter wavelength of visible light in nm "))
if 380<=a<=750:
    if 380<=a<450:
        print("Violet")
    elif 450<=a<495:
        print("Blue")
    elif 495<=a<570:
        print("Green")
    elif 570<=a<590:
        print("Yellow")
    elif 590<=a<620:
        print("Orange")
    elif 620<=a<=750:
        print("Red")
else:
    print("Entered wavelength is outside of visible spectrum")


# In[ ]:


a=int(input("Enter Frequency "))
if a<3*(10**9):
    print("Radio Waves")
elif 3*10*9<=a<3*10*12:
    print("Microwaves")
elif 3*10*12<=a<4.3*10*14:
    print("Infrared Light")
elif 4.3*10*9<=a<7.5*10*14:
    print("Visible Light")
elif 7.5*10*14<=a<3*10*17:
    print("Ultravoilet Light")
elif 3*10*19<=a<3*10*19:
    print("X-rays")
else:
    print("Gamma rays")
