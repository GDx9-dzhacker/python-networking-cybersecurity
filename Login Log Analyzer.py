failed_attemps = {}


with open("C:/Users/User/Documents/fichier important/login.log", "r") as f :
     for line in f :
            ip,status = line.split()
            if status == "LOGIN_FAILED" :
                 if ip in failed_attemps :
                       failed_attemps[ip] += 1
                 else :
                  failed_attemps[ip] = 1

for ip, attemps in failed_attemps.items() :
     if attemps >= 3 :
          print("ALERTE :\n" \
          f"suspicious IP :{ip} \n " \
          f"failed attemps : {attemps}")