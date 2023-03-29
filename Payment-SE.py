#!/usr/bin/env python
# coding: utf-8

# In[24]:


def Payment():
    global i
    id=input("Your Assigned ID: ")
    print(" Payment")
    print(" --------------------------------")
    print("   HAVAN HEIGHTS PAYMENT ")
    print(" --------------------------------")
    print("  MODE OF PAYMENT")

    print("  1- Credit/Debit Card")
    print("  2- Jazcash")
    print("  3- Cash")
    x=int(input("-> "))
    if (x==1):
        card=input("    Enter your Card No:")
    elif(x==2):
        jazzid=input("  Enter your Jazz ID.")
    else:
        print("         Proceed to Payment")
    print("\n PAYMENT OF HAVAN HEIGHTS")
    print("  (YES/NO)")
    inp=str(input("->"))
    if inp=='YES' or inp=='NO':
        print(" --------------------------------")
        print("            Total  Bill")
        print(" --------------------------------")
        print("\n Amount: ",50000,"\t")
        print("\n Room Type: ",'Standard',"\t")
        print(" --------------------------------")
        print(" --------------------------------")
        print("")
        print(" lOOKING FORWARD TO HOST YOU AGAIN :) ")
    else:
        print("  Invalid ")


# In[25]:


Payment()


# In[ ]:




