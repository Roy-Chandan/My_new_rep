#!/usr/bin/python

# generate manual delta file (.csv) to eliminate tedious editing - first pass at it
# mjk - 03/31/2023

import time, sys, re
from datetime import datetime

colHeader = "action,companynumber,datadate,compositeid,fstassetid,assettype,orderstatus,documenttype,documentnumber," + \
            "hubtype,hubid,soldbybranch,soldbyname,soldbyaddr1,soldbyaddr2,soldbycity,soldbystate,soldbycountry,soldbyzip," + \
            "soldby_lat,soldby_long,soldbyemail,soldbyphone,soldtoname,soldtoaddr1,soldtoaddr2,soldtocity,soldtostate," + \
            "soldtocountry,soldtozip,soldto_lat,soldto_long,shiptoname,shiptoaddr1,shiptoaddr2,shiptocity,shiptocountry," + \
            "shiptostate,shiptozip,shipto_lat,shipto_long,shiptocontact,shiptoemail,shiptomobile,shiptophone,soldtoaccount," + \
            "customerpo,soldtocontact,soldtoemail,soldtomobile,soldtophone,rentalsaledate,salespersonnumber,salespersonname," + \
            "compositeitemcode,compositedescription,imei_number,fstorder,fstspad,fstspbp,fstsprc,fstspsc,fstspsp,fstspta," + \
            "fstdescription,pumpendserialnumber,pumpendmodel,enginemodel,mountingtype"

# fill in the default data
action            = "A"
companynumber     = "1"
datadate          = ""        # prompt for this, sample = 2023/03/23 15:35:00.000
compositeid       = ""        # prompt for this, sample = S096231-01
fstassetid        = ""        # prompt for this, sample = S096231-01 CD100S Perkins 403 U552371H 300234031110290
assettype         = "Rental"
orderstatus       = "ReadyToRent"
documenttype      = ""
documentnumber    = ""
hubtype           = "Distributor"
hubid             = "201"
soldbybranch      = "090"
soldbyname        = "Distribution Center / Distributors"
soldbyaddr1       = "22 Floodgate Road"
soldbyaddr2       = ""
soldbycity        = "Bridgeport"
soldbystate       = "NJ"
soldbycountry     = "USA"
soldbyzip         = "8014"
soldby_lat        = "39.8079"
soldby_long       = "-75.3562"
soldbyemail       = "Jesse.WatsonIII@xyleminc.com"
soldbyphone       = "8566254257"
soldtoname        = ""
soldtoaddr1       = ""
soldtoaddr2       = ""
soldtocity        = ""
soldtostate       = ""
soldtocountry     = ""
soldtozip         = ""
soldto_lat        = ""
soldto_long       = ""
shiptoname        = ""
shiptoaddr1       = ""
shiptoaddr2       = ""
shiptocity        = ""
shiptocountry     = ""
shiptostate       = ""
shiptozip         = ""
shipto_lat        = ""
shipto_long       = ""
shiptocontact     = ""
shiptoemail       = ""
shiptomobile      = ""
shiptophone       = ""
soldtoaccount     = ""
customerpo        = ""
soldtocontact     = ""
soldtoemail       = ""
soldtomobile      = ""
soldtophone       = ""
rentalsaledate    = ""
salespersonnumber = ""
salespersonname   = ""
compositeitemcode    = ""     # prompt for this, sample = S096231-01 CD100S Perkins 403 U552371H 300234031110290
compositedescription = ""     # prompt for this, sample = S096231-01 CD100S Perkins 403 U552371H 300234031110290
imei_number       = ""        # prompt for this, sample = 300234031110290
fstorder          = ""
fstspad           = "0"
fstspbp           = "0"
fstsprc           = "0"
fstspsc           = "0"
fstspsp           = "0"
fstspta           = "0"
fstdescription    = "Xylem 4G FST Module"
pumpendserialnumber  = ""     # prompt for this, sample = S096231-01
pumpendmodel      = ""        # prompt for this, sample = CD100S
enginemodel       = ""        # prompt for this, sample = Perkins 403 U552371H
mountingtype      = ""        # prompt for this, sample = Open, sample = CS

# ask for the data we need to fill in

imei_number         = input("IMEI: ")

engineMake          = input("Engine Make: ")
engineModel         = input("Engine Model: ")
engineSerialNo      = input("Engine Serial Number: ")
tempStr = engineMake + " " + engineModel + " " + engineSerialNo
tempStr = re.sub(' +', ' ', tempStr)
enginemodel = tempStr.rstrip()

pumpendmodel        = input("Pump End Model: ")
pumpendserialnumber = input('Pump End Serial Number [use "-" instead of "/"]: ')
mountingtype        = input("Pump Mounting Type [Open or CS]: ")
pumpfleetnumber     = input("Pump Fleet Number: ")

compositeid = pumpendserialnumber
tempStr = pumpendserialnumber + " " + pumpendmodel + " " + enginemodel + " " + imei_number
tempStr = re.sub(' +', ' ', tempStr)
fstassetid = tempStr.rstrip()

compositeitemcode = fstassetid
compositedescription = fstassetid

if pumpfleetnumber == "":
    pumpendserialnumber2 = pumpendserialnumber
else:
    pumpendserialnumber2 = pumpfleetnumber

runDate             = input("Run on date [yyyy/mm/dd]: ")
runTime             = input("Run at time [hh:mm]: ")
fileDate = runDate.replace("/", "") + runTime.replace(":", "") + "00"
runTime = runTime + ":00.000"
datadate = runDate + " " + runTime

print(runDate + " " + runTime)
print(compositeid)
print(fstassetid)
print(compositeitemcode)
print(compositedescription)
print(imei_number)
print(pumpendserialnumber)
print(pumpendmodel)
print(enginemodel)
print(mountingtype)

#IMEI: 300234031110290
#Engine Make:  Perkins
#Engine Model:  403
#Engine Serial Number:  U552371H
#Pump End Model:  CD100S
#Pump End Serial Number:  S096231-01
#Pump Mounting Type:  Critically Silenced - CS
#Device Alias:  CD100S S096231-01

print(colHeader)

print(action + "," + companynumber + "," + datadate + "," + compositeid + "," + fstassetid + "," + assettype + "," + \
      orderstatus + "," + documenttype + "," + documentnumber + "," + hubtype + "," + hubid + "," + \
      soldbybranch + "," + soldbyname + "," + soldbyaddr1 + "," + soldbyaddr2 + "," + soldbycity + "," + \
      soldbystate + "," + soldbycountry  + "," + soldbyzip + "," + soldby_lat + "," + soldby_long + "," + \
      soldbyemail + "," + soldbyphone + "," + soldtoname + "," + soldtoaddr1 + "," + soldtoaddr2 + "," + \
      soldtocity + "," + soldtostate + "," + soldtocountry + "," + soldtozip + "," + soldto_lat + "," + soldto_long + "," + \
      shiptoname + "," + shiptoaddr1 + "," + shiptoaddr2 + "," + shiptocity + "," + shiptocountry + "," + \
      shiptostate + "," + shiptozip + "," + shipto_lat + "," + shipto_long + "," + shiptocontact + "," + shiptoemail + "," + \
      shiptomobile + "," + shiptophone + "," + soldtoaccount + "," + customerpo + "," + soldtocontact + "," + \
      soldtoemail + "," + soldtomobile + "," + soldtophone + "," + rentalsaledate + "," + salespersonnumber + "," + \
      salespersonname + "," + compositeitemcode + "," + compositedescription + "," + imei_number + "," + fstorder + "," + \
      fstspad + "," + fstspbp + "," + fstsprc + "," + fstspsc + "," + fstspsp + "," + fstspta + "," + fstdescription + "," + \
      pumpendserialnumber2 + "," + pumpendmodel + "," + enginemodel + "," + mountingtype)

print('\n' + "Manual_Delta_" + fileDate + ".csv")

