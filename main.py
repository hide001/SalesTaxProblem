# Basic sales tax is applicable at a rate of 10% on all goods, except books, food,
# and medical products that are exempt. Import duty is an additional sales tax
# applicable on all imported goods at a rate of 5%, with no exemptions.

# When I purchase items I receive a receipt which lists the name of all the items
# and their price (including tax), finishing with the total cost of the items,
# and the total amounts of sales taxes paid.  The rounding rules for sales tax are
# that for a tax rate of n%, a shelf price of p contains (np/100 rounded up to
# the nearest 0.05) amount of sales tax.

import os
from math import ceil

salesTaxExemptCat = ["book","books","Book","Books","food","medical","chocolate","Chocolate","chocolates","Chocolates","pill","pills","Pill","Pills"]
salesTaxRate = 0.1
importDutyRate = 0.05
itemBought = []
reciptArray = []





class main:

    def engine(self):
        value = ''
        while(value != "n"):
            value = input("Item (give 'n' to quit entering): \t")
        
            if(value != "n"):
                rate = float(input("Price / unit: \t"))
                quantity = float(input("Quantity: \t"))
                isImport = input("Is imported? (y/n): \t")
                itemBought.append(value)
                isTruethatExempt = product().isExempt(salesTaxExemptCat,value)
                grossPrice = rate*quantity
                if(isTruethatExempt == 1 and isImport == "y"): 
                    #not sales tax but import duty
                    netPrice = grossPrice*importDutyRate + grossPrice 
                    print(netPrice)
                    salesTax = 0
                    mathLogic().makeRecipt(value,netPrice,salesTax)
                elif(isTruethatExempt == 1 and isImport == "n"):
                    #no sales tax and no import duty, So
                    netPrice = grossPrice
                    print(netPrice)
                    salesTax = 0
                    mathLogic().makeRecipt(value,netPrice,salesTax)
                elif(isTruethatExempt == -1 and isImport == "y"):
                    #sales tax + not import duty
                    salesTax = grossPrice*salesTaxRate
                    salesTax = round(salesTax)
                    netPrice = (grossPrice*importDutyRate) + grossPrice
                    print(netPrice)
                    mathLogic().makeRecipt(value,netPrice,salesTax)
                elif(isTruethatExempt == -1 and isImport == "n"):
                    #sales tax + import duty
                    salesTax = grossPrice*salesTaxRate
                    salesTax = round(salesTax)
                    netPrice = salesTax + grossPrice
                    print(netPrice)
                    mathLogic().makeRecipt(value,netPrice,salesTax)
        return -1


class mathLogic:
    def round(self,number):
        number = ceil(number*20)/20
        return number

    def printRecipt(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("#"*60 + " " + "Your Bill of Sales" + " " + "#"*60)
        serialNo = 1
        totalSalesTax = 0
        totalAmount = 0
        for i in range(len(reciptArray)): 
            print(str(serialNo) + ". " + reciptArray[i][0] + ": "+ str(reciptArray[i][1]))
            serialNo = serialNo + 1
            totalSalesTax = totalSalesTax + reciptArray[i][2]
            totalAmount = totalAmount + reciptArray[i][1]
        print("Total Sales Tax: \t" + str(totalSalesTax) + "\nTotal Amount: \t" + str(totalAmount))

    def makeRecipt(self,value,netPrice,salesTax):
        recipttuple = (value,netPrice,salesTax)
        reciptArray.append(recipttuple)


class product:
    def isExempt(self,arr,val):
        for i in range(len(arr)):
            if arr[i] == val:
                return 1
        return -1



##################Calling Methods###########
main().engine()
mathLogic().printRecipt()


