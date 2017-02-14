import random
import inventorytracking

def makeCatalog(n):
    """
    """
    styles = ["Cowboy", "Hiking", "Rain", "Riding", "Loafer", "Oxford", "Pump", "Sling-back", "Wing-tip", "Athletic", "Hightop", "Moccasin", "Sandal"]

    sizes = [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14]
    
    catalog = []
    
    fw = inventorytracking.Boot("test", 0, "1212")
    
    #prints for testing
    #print(styles)
    #print(sizes)
    #print(catalog)
    #print(fw)

    for i in range(0, n):
        fwtype = random.choice(styles)
        fwsize = random.choice(sizes)
        sku = "1234-{0}".format(i)
        
        #print(fwtype)
        
        if styles.index(fwtype) < 4:
            fw = inventorytracking.Boot(fwtype, fwsize, sku)
        
        elif styles.index(fwtype) < 9:
            fw = inventorytracking.DressShoe(fwtype, fwsize, sku)
        
        elif styles.index(fwtype) < 13:
            fw = inventorytracking.CasualShoe(fwtype, fwsize, sku)

        else:
            print("you fucked up somewhere")
            fw = inventorytracking.Boot("YOU DUMFUCK", 69, "SHAME")
            print(fw)
            
        catalog.append(fw)
        #for j in range(0, len(catalog)):
        #        print(catalog[j])

    #print("FINAL ", catalog)
    return catalog

cat = makeCatalog(10)
cat2 = makeCatalog(10)

def print_cat(c, lform=False):
    print("CATALOG:")
    if lform == True:
        for k in range(0, len(c)):
            print(c[k], c[k].sku)
    else:
        for k in range(0, len(c)):
            print(c[k])

def print_catL(c): #includes SKU at end
    print("CATALOG - LONG:")
    for k in range(0, len(c)):
        print(c[k], c[k].sku)

print_cat(cat, True)
print_cat(cat2)
