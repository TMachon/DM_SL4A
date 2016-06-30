import sl4a
import time

droid = sl4a.Android()

liste = ["Savigny RER","Château","Lucien Sampaix"]
droid.dialogCreateInput("Où veux-tu un bus ?")
droid.dialogSetItems(liste)
droid.dialogShow()
reponse = droid.dialogGetResponse().result['item']

retour = time.asctime()
time = int(retour[11:13])*100 + int(retour[14:16])

if reponse == 0 :
    code = ["3143","3145"]
elif reponse == 1 :
    if time <= 1240 :
        code = ["2821","2821"]
    else :
        code = ["1704","1705"]
else :
    if time <= 1240 :
        code = ["2874"]
    else :
        code = ["2873"]

for i in range(len(code)) :
    droid.smsSend("0632438362",code[i])

droid.makeToast("SMS envoyé(s)")