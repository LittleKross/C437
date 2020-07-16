from Crypto.PublicKey import RSA
import math
import fractions
publicKeys = {}
vunerableKeys = {}
for i in range(1,101):
    pem1 = open(str(i) + ".pem").read()
    publicKeys[i-1] = RSA.importKey(pem1)
    #print(publicKeys[i-1].n)

#print(len(publicKeys))
for key in publicKeys:
    #print(key)
    for i in range(len(publicKeys)):
        keypublic = publicKeys[key].n
        ipublic = publicKeys[i].n
        if keypublic != ipublic and ((key and i) not in vunerableKeys.keys()):
            gcf = fractions.gcd(keypublic,ipublic)
            if gcf > 1:
                print("==============================================================\nFound vunerable keys:\nKey " + str(key) + ":" + str(publicKeys[key].n) + "\nKey " + str(i) + ": " + str(publicKeys[i].n) + "\nCommon Factor: " + str(gcf) + "\n==============================================================\n\n")
                vunerableKeys[key] = [keypublic,gcf,int((keypublic / gcf))]
                vunerableKeys[i] = [ipublic,gcf,int((ipublic / gcf))]
                
print("==============================================================")
for i in vunerableKeys.items():
    print("<Item: " + str(i[0]) + " P: " + str(i[1][1]) + " Q: " + str(i[1][2]))
print("==============================================================\n")