mijn_dict = { 'vis':10, 'vlees':25,'overig':15}
totaal = 50

def presenteer(dic ={}, totaal =0):
    for k,v in dic.items():
        print(f"{k} : {v} euro")
    print("==========================")
    print(f"totaal : {totaal} euro")
