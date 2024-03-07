
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
                                  intoi = db.index(table);
                                  while db[intoi] != "endtab;":
                                        intoi += 1
                                  db.insert(intoi, value)
                                except ValueError:
                                    print("GDB INSERTVTT ERROR")
                      
def gaft(table):
    try:
      returnar = []
      cycler = 0
      iot = db.index(table)
      returnar.append(db[iot])
      cycler += 1
      while db[iot + cycler] != "endtab;":
        returnar.append(db[iot + cycler])
        cycler += 1
      return(returnar)
        
    except:
      print("GDB ERROR GAFT")
      
    
      
      
      
      
    
    
    
    