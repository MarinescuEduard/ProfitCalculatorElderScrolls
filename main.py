import pandas as pd


xl = pd.ExcelFile("PotStonks.xlsx")
df = xl.parse("Prices")


def transactionTax(initialPrice):
    taxValue = float(initialPrice) * 8 / 100
    return round(taxValue, 2)


def addPercentage(percentageValue, sumAmount):
    s = float(sumAmount) + float(sumAmount) * float(percentageValue) / 100
    return round(s, 2)


def fiftyPieces(pricePerPiece):
    s = 50*float(pricePerPiece)
    return round(s, 2)


def profitPerTransaction(sumWithProfitAdded, initialPrice):
    s = float(sumWithProfitAdded) - float(initialPrice)
    return round(s, 2)


def resultPercentage(percentageAmount, totalPrice, sellingPrice):
    p1 = addPercentage(percentageAmount, totalPrice)
    if p1 < sellingPrice:
        print("Price" + str(percentageAmount) + "%/1 = " + str(p1) + ". Price+" + str(percentageAmount) + "%/200 = " + str(fiftyPieces(p1)) + ". Tax/50 = " + str(transactionTax(fiftyPieces(p1))))
        s1 = fiftyPieces(p1) - transactionTax(fiftyPieces(p1))
        if profitPerTransaction(s1, fiftyPieces(totalPrice)) > 0:
            print("Profit on 50 pieces of " + str(percentageAmount) + "% would be " + str(profitPerTransaction(s1, fiftyPieces(totalPrice))))
        elif profitPerTransaction(s1, fiftyPieces(totalPrice)) < 0:
            print("Loss on 50 pieces of " + str(percentageAmount) + "% would be " + str(profitPerTransaction(s1, fiftyPieces(totalPrice))))
        else:
            print("Breakeven.")


def finalResult(currentPrice, sellingPrice):
    resultPercentage(5, currentPrice, sellingPrice)
    resultPercentage(10, currentPrice, sellingPrice)
    resultPercentage(20, currentPrice, sellingPrice)
    resultPercentage(30, currentPrice, sellingPrice)
    resultPercentage(40, currentPrice, sellingPrice)
    resultPercentage(50, currentPrice, sellingPrice)
    resultPercentage(60, currentPrice, sellingPrice)
    resultPercentage(70, currentPrice, sellingPrice)
    resultPercentage(80, currentPrice, sellingPrice)
    resultPercentage(90, currentPrice, sellingPrice)
    resultPercentage(100, currentPrice, sellingPrice)
    resultPercentage(110, currentPrice, sellingPrice)
    resultPercentage(120, currentPrice, sellingPrice)


def artaeumPickledFishBowl():
    print()
    print("Artaeum Pickled Fish Bowl")
    print()
    currentPrice = (df['Food Price'][0]*5+df['Food Price'][14]*3+df['Food Price'][18]*3+df['Food Price'][19]*3)/4
    print("Selling price is " + str(df['Selling Price'][0]))
    sellingPrice = df['Selling Price'][0]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def artaeumTakeawayBroth():
    print()
    print("Artaeum Takeaway Broth")
    print()
    currentPrice = (df['Food Price'][0]*20+df['Food Price'][1]*5+df['Food Price'][2]*5+df['Food Price'][3]*5)/4
    print("Selling price is " + str(df['Selling Price'][1]))
    sellingPrice = df['Selling Price'][1]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def braisedRabbit():
    print()
    print("Braised Rabbit with Spring Vegetables")
    print()
    foodPrice = (df['Food Price'][15] + df['Food Price'][16] + df['Food Price'][17]) / 4
    print("Selling price is " + str(df['Selling Price'][2]))
    sellingPrice = df['Selling Price'][2]
    print("Cost/1 = " + str(round(foodPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(foodPrice)))
    finalResult(foodPrice, sellingPrice)
    print()


def longfinpasty():
    print()
    print("Longfin Pasty with Melon")
    print()
    currentPrice = (df['Food Price'][0] + df['Food Price'][1] + df['Food Price'][16] + df['Food Price'][10]) / 4
    print("Selling price is " + str(df['Selling Price'][3]))
    sellingPrice = df['Selling Price'][3]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def witchMothersPotentBrew():
    print()
    print("Witchmother's Potent Brew")
    print()
    currentPrice = (df['Food Price'][12] + df['Food Price'][13] + df['Food Price'][14] + df['Food Price'][15]) / 4
    print("Selling price is " + str(df['Selling Price'][4]))
    sellingPrice = df['Selling Price'][4]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def clockworkCitrus():
    print()
    print("Clockwork Citrus Filet")
    print()
    currentPrice = (df['Food Price'][8] + df['Food Price'][9] + df['Food Price'][10] + df['Food Price'][11]) / 4
    print("Selling price is " + str(df['Selling Price'][5]))
    sellingPrice = df['Selling Price'][5]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def dubiousCamoranThrone():
    print()
    print("Dubious Camoran Throne")
    print()
    currentPrice = (df['Food Price'][4] + df['Food Price'][5] * 3 + df['Food Price'][6] + df['Food Price'][7]) / 4
    print("Selling price is " + str(df['Selling Price'][6]))
    sellingPrice = df['Selling Price'][6]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def bloodyMara():
    print()
    print("Purifying Bloody Mara")
    print()
    currentPrice = (df['Price/Ingredient'][7] + df['Food Price'][20] + df['Food Price'][21] + df['Food Price'][10]) / 4
    print("Selling price is " + str(df['Selling Price'][7]))
    sellingPrice = df['Selling Price'][7]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def bewitchedSugarSkull():
    print()
    print("Bewitched Sugar Skull")
    print()
    currentPrice = (df['Food Price'][22] * 2 + df['Food Price'][23] * 5 + df['Price/Ingredient'][9] * 2 + df['Food Price'][13] * 2 + df['Food Price'][19] * 5) / 4
    print("Selling price is " + str(df['Selling Price'][8]))
    sellingPrice = df['Selling Price'][8]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def weaponPower():
    print()
    print("Essence of Weapon power")
    print()
    currentPrice = (df['Price/Ingredient'][11] + df['Price/Ingredient'][10] + df['Price/Ingredient'][12] + df['Price/Ingredient'][13]) / 4
    print("Selling price is " + str(df['Selling Price'][9]))
    sellingPrice = df['Selling Price'][9]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def spellPower():
    print()
    print("Essence of Spell Power")
    print()
    currentPrice = (df['Price/Ingredient'][0] + df['Price/Ingredient'][1] + df['Price/Ingredient'][2] + df['Price/Ingredient'][13]) / 4
    print("Selling price is " + str(df['Selling Price'][10]))
    sellingPrice = df['Selling Price'][10]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def health():
    print()
    print("Essence of Health")
    print()
    currentPrice = (df['Price/Ingredient'][8] + df['Price/Ingredient'][9] + df['Price/Ingredient'][5] + df['Price/Ingredient'][13]) / 4
    print("Selling price is " + str(df['Selling Price'][11]))
    sellingPrice = df['Selling Price'][11]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def immovMagicka():
    print()
    print("Essence of Immovability (Magicka)")
    print()
    currentPrice = (df['Price/Ingredient'][8] + df['Price/Ingredient'][9] + df['Price/Ingredient'][12] + df['Price/Ingredient'][13]) / 4
    print("Selling price is " + str(df['Selling Price'][12]))
    sellingPrice = df['Selling Price'][12]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def immovStamina():
    print()
    print("Essence of Immovability (Stamina)")
    print()
    currentPrice = (df['Price/Ingredient'][9] + df['Price/Ingredient'][5] + df['Price/Ingredient'][12] + df['Price/Ingredient'][13]) / 4
    print("Selling price is " + str(df['Selling Price'][13]))
    sellingPrice = df['Selling Price'][13]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofhealth():
    print()
    print("Truly Superb Glyph of Health")
    print()
    currentPrice = df['Glyph Price'][0] + df['Glyph Price'][1] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][0]))
    sellingPrice = df['Enchantments Price'][0]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofmagicka():
    print()
    print("Truly Superb Glyph of Magicka")
    print()
    currentPrice = df['Glyph Price'][0] + df['Glyph Price'][2] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][1]))
    sellingPrice = df['Enchantments Price'][1]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofstamina():
    print()
    print("Truly Superb Glyph of Stamina")
    print()
    currentPrice = df['Glyph Price'][0] + df['Glyph Price'][3] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][2]))
    sellingPrice = df['Enchantments Price'][2]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofprismatic():
    print()
    print("Truly Superb Glyph of Prismatic Defense")
    print()
    currentPrice = df['Glyph Price'][0] + df['Glyph Price'][4] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][3]))
    sellingPrice = df['Enchantments Price'][3]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofflame():
    print()
    print("Truly Superb Glyph of Flame")
    print()
    currentPrice = df['Glyph Price'][0] + df['Glyph Price'][5] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][4]))
    sellingPrice = df['Enchantments Price'][4]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofshock():
    print()
    print("Truly Superb Glyph of Shock")
    print()
    currentPrice = df['Glyph Price'][0] + df['Glyph Price'][6] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][5]))
    sellingPrice = df['Enchantments Price'][5]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofweapon():
    print()
    print("Truly Superb Glyph of Weapon Damage")
    print()
    currentPrice = df['Glyph Price'][0] + df['Glyph Price'][7] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][6]))
    sellingPrice = df['Enchantments Price'][6]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofcrushing():
    print()
    print("Truly Superb Glyph of Crushing")
    print()
    currentPrice = df['Glyph Price'][8] + df['Glyph Price'][9] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][7]))
    sellingPrice = df['Enchantments Price'][7]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofphysical():
    print()
    print("Truly Superb Glyph of Increased Physical Harm")
    print()
    currentPrice = df['Glyph Price'][0] + df['Glyph Price'][10] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][8]))
    sellingPrice = df['Enchantments Price'][8]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofmagical():
    print()
    print("Truly Superb Glyph of Increased Magical Harm")
    print()
    currentPrice = df['Glyph Price'][0] + df['Glyph Price'][11] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][9]))
    sellingPrice = df['Enchantments Price'][9]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofmagickarecovery():
    print()
    print("Truly Superb Glyph of Magicka Recovery")
    print()
    currentPrice = df['Glyph Price'][0] + df['Glyph Price'][12] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][10]))
    sellingPrice = df['Enchantments Price'][10]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def gofstaminarecovery():
    print()
    print("Truly Superb Glyph of Stamina Recovery")
    print()
    currentPrice = df['Glyph Price'][0] + df['Glyph Price'][13] + df['Glyph Price'][14]
    print("Selling price is " + str(df['Enchantments Price'][11]))
    sellingPrice = df['Enchantments Price'][11]
    print("Cost/1 = " + str(round(currentPrice, 2)) + ". Cost/50 = " + str(fiftyPieces(currentPrice)))
    finalResult(currentPrice, sellingPrice)
    print()


def intro():
    print("What prices would you like to check?")
    print("1. Food prices")
    print("2. Potions prices")
    print("3. Enchantment prices")
    chosenOption = int(input())
    while chosenOption not in range(1, 4):
        print("Please insert a number between 1 and 3")
        chosenOption = input()
    return int(chosenOption)


def foodprices():
    print("What would you like to check?")
    print("1. Artaeum Pickled Fish Bowl")
    print("2. Artaeum Takeaway Broth")
    print("3. Braised Rabbit with Spring Vegetables")
    print("4. Longfin Pasty with Melon")
    print("5. Witchmother's Potent Brew")
    print("6. Clockwork Citrus Filet")
    print("7. Dubious Camoran Throne")
    print("8. Purifying Bloody Mara")
    print("9. Bewitched Sugar Skull")
    print("10. All of the above")
    chosenOption = int(input())
    while chosenOption not in range(1, 11):
        print("Please insert a number from 1 to 10")
        chosenOption = int(input())
    return chosenOption


def potionsprices():
    print("What would you like to check?")
    print("1. Essence of Weapon Power")
    print("2. Essence of Spell Power")
    print("3. Essence of Health")
    print("4. Essence of Immovability (Magicka)")
    print("5. Essence of Immovability (Stamina)")
    print("6. All of the above")
    chosenOption = int(input())
    while chosenOption not in range(1, 7):
        print("Please insert a number from 1 to 6")
        chosenOption = int(input())
    return chosenOption


def enchantprices():
    print("What would you like to check?")
    print("1. Truly superb glyph of health.")
    print("2. Truly superb glyph of magicka.")
    print("3. Truly superb glyph of stamina.")
    print("4. Truly superb glyph of prismatic defense.")
    print("5. Truly superb glyph of flame.")
    print("6. Truly superb glyph of shock.")
    print("7. Truly superb glyph of weapon damage.")
    print("8. Truly superb glyph of crushing.")
    print("9. Truly superb glyph of increase physical harm.")
    print("10. Truly superb glyph of increase magical harm.")
    print("11. Truly superb glyph of magicka recovery.")
    print("12. Truly superb glyph of stamina recovery.")
    print("13. All of the above")
    chosenOption = int(input())
    while chosenOption not in range(1, 14):
        print("Please insert a number from 1 to 6")
        chosenOption = int(input())
    return chosenOption


def morefood():
    print("Would you like to check another food? Y/N")
    chosenOption = str(input())
    while chosenOption != "Y" or chosenOption != "N":
        if chosenOption == "Y":
            return 0
        elif chosenOption == "N":
            print("Okay, thank you!")
            return 1
        else:
            print("Please enter Y or N")
            chosenOption = input()


def morepotions():
    print("Would you like to check another potion? Y/N")
    chosenOption = str(input())
    while chosenOption != "Y" or chosenOption != "N":
        if chosenOption == "Y":
            return 0
        elif chosenOption == "N":
            print("Okay, thank you!")
            return 1
        else:
            print("Please enter Y or N")
            chosenOption = input()


def moreenchants():
    print("Would you like to check another enchant? Y/N")
    chosenOption = str(input())
    while chosenOption != "Y" or chosenOption != "N":
        if chosenOption == "Y":
            return 0
        elif chosenOption == "N":
            print("Okay, thank you!")
            return 1
        else:
            print("Please enter Y or N")
            chosenOption = input()


m1 = intro()
if m1 == 1:
    c = 0
    while c != 1:
        m2 = foodprices()
        if m2 == 1:
            artaeumPickledFishBowl()
            c = morefood()
        elif m2 == 2:
            artaeumTakeawayBroth()
            c = morefood()
        elif m2 == 3:
            braisedRabbit()
            c = morefood()
        elif m2 == 4:
            longfinpasty()
            c = morefood()
        elif m2 == 5:
            witchMothersPotentBrew()
            c = morefood()
        elif m2 == 6:
            clockworkCitrus()
            c = morefood()
        elif m2 == 7:
            dubiousCamoranThrone()
            c = morefood()
        elif m2 == 8:
            bloodyMara()
            c = morefood()
        elif m2 == 9:
            bewitchedSugarSkull()
            c = morefood()
        elif m2 == 10:
            artaeumPickledFishBowl()
            artaeumTakeawayBroth()
            braisedRabbit()
            longfinpasty()
            witchMothersPotentBrew()
            clockworkCitrus()
            dubiousCamoranThrone()
            bloodyMara()
            bewitchedSugarSkull()
            c = morefood()
elif m1 == 2:
    c = 0
    while c != 1:
        m2 = potionsprices()
        if m2 == 1:
            weaponPower()
            c = morepotions()
        elif m2 == 2:
            spellPower()
            c = morepotions()
        elif m2 == 3:
            health()
            c = morepotions()
        elif m2 == 4:
            immovMagicka()
            c = morepotions()
        elif m2 == 5:
            immovStamina()
            c = morepotions()
        elif m2 == 6:
            weaponPower()
            spellPower()
            health()
            immovMagicka()
            immovStamina()
            c = morepotions()
elif m1 == 3:
    c = 0
    while c != 1:
        m2 = enchantprices()
        if m2 == 1:
            gofhealth()
            c = moreenchants()
        elif m2 == 2:
            gofmagicka()
            c = moreenchants()
        elif m2 == 3:
            gofstamina()
            c = moreenchants()
        elif m2 == 4:
            gofprismatic()
            c = moreenchants()
        elif m2 == 5:
            gofflame()
            c = moreenchants()
        elif m2 == 6:
            gofshock()
            c = moreenchants()
        elif m2 == 7:
            gofweapon()
            c = moreenchants()
        elif m2 == 8:
            gofcrushing()
            c = moreenchants()
        elif m2 == 9:
            gofphysical()
            c = moreenchants()
        elif m2 == 10:
            gofmagical()
            c = moreenchants()
        elif m2 == 11:
            gofmagickarecovery()
            c = moreenchants()
        elif m2 == 12:
            gofstaminarecovery()
            c = moreenchants()
        elif m2 == 13:
            gofhealth()
            gofmagicka()
            gofstamina()
            gofprismatic()
            gofflame()
            gofshock()
            gofweapon()
            gofcrushing()
            gofphysical()
            gofmagical()
            gofmagickarecovery()
            gofstaminarecovery()
            c = moreenchants()
