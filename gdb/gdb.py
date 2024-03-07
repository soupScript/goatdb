db = []

def addt(tname):
    if str(tname) == tname:
        db.append("newtab;")
        db.append(tname)
        db.append("endtab;")
    else:
        print("GDB ERROR TNAME IS NOT A STRING")

def insertvtt(value, table, fronted):
    if fronted or fronted == "":
        index = db.index(table)
        db.insert(index + 1, value)
    elif fronted == False:
        try:
            intoi = db.index(table)
            while db[intoi] != "endtab;":
                intoi += 1
            db.insert(intoi, value)
        except ValueError:
            print("GDB INSERTVTT ERROR")

def gaft(table, etn):
    try:
        returnar = []
        cycler = 0
        iot = db.index(table)
        if etn == False:
            returnar.append(db[iot])
        cycler += 1
        while db[iot + cycler] != "endtab;":
            returnar.append(db[iot + cycler])
            cycler += 1
        return returnar

    except:
        print("GDB ERROR GAFT")

def gvn(value, table):
    try:
        intoi = db.index(table)
        while db[intoi] != 'endtab;':
            intoi += 1
            if db[intoi] == value:
                return db.index(value) - db.index(table)
                break
                

        db.insert(intoi, value)

    except:
        print('GDB ERROR GVN')
      
      
      
