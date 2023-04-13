#Problem 1
price=float(input("Price: "))
a=input("Are you prime member? " )
def cdp(price, a):
    if (a=="yes" or a=="Yes" or a=="YES"):
        d1 = 0.15*price
        p_a_d1= price-d1
        d2= 0.08*p_a_d1
        p_a_d2=p_a_d1-d2
        return p_a_d2
    else:
        b_f_d=0.08*price
        f_p= price-b_f_d
        return f_p
print("Your final price after calculating all discounts is Rs",cdp(price,a))


#Problem 2
#[A]
a=input()
def chat(a):
    if len(a)<=200:
        return a
    else:
        b=a[:200]
        return b
print(chat(a))

#[B]
a=input()
n=30
word_list=a.split()[:n]
output=" ".join(word_list)
print(output)
