#IPv4 address generation program
def sepearateur_octet (adresse):# check if the network part of the IPv4 is valid
    try: 
        octet1,octet2,octet3 = adresse.split(".")
        print(f"octet1 : {octet1}")
        print(f"octet2 : {octet2}")
        print(f"octet3 : {octet3}")
        verifier_nombre (octet1, octet2,octet3) 
    except ValueError : 
        print("ERROR : please check THAT your IPv4 network address contains exactly 3 octets")



def verifier_nombre (octet1,octet2,octet3) : # check if bytes are between 0 and 255
    erreur = False
    octets = [octet1, octet2, octet3 ]

    try : 
        for i in octets : 
            if int(i) > 255   : 
                print ("the IP address must not contain a number greater than 255 ")
                erreur = True
            elif int(i) < 0 :
                print ("the IP address must not contain a number less than 0")
                erreur = True
    except ValueError : 
        print("the octets must be numbers")
        erreur = True

    if erreur == True : 
        print("Invalid IP")
    else : 
        print("Valid IP")
        generateur_ipv4(octet1, octet2,octet3 )

def generateur_ipv4(octet1, octet2, octet3 ) : # generate the last byte and create an IPv4 address
    for i in range(0, 255):
        print(f"IPv4 : {octet1}.{octet2}.{octet3}.{i}")

# ---------------------------------------- MAIN PROGRAMME ------------------------------------------------------------------------
ipv4_adresse = input("enter the network part of the IPv4 address : ")
print(f"IPv4 network address: {ipv4_adresse} ")
sepearateur_octet(ipv4_adresse)