from solider.solider import Solider


def create_solider(soliderCsv):
    soliders=[]
    for i in list(soliderCsv):
        soilder=Solider(i['מספר אישי'], i['שם פרטי'], i['שם משפחה'], i['מין'], i['עיר מגורים'], int(i['מרחק מהבסיס']))
        soliders.append(soilder)
    return soliders