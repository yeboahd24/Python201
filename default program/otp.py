 #Python Program for simple OTP genertaor

import random as r
# function for otp generation
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    print ("Your One Time Password is: ")
    print (otp)
otpgen()