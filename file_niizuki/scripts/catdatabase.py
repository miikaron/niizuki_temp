#-------------------------------------------------------------------------------
#formattazione skill e altro
tre_ast = "***"
punti_ast_spazio = ":*** "

bold = "**"
#-------------------------------------------------------------------------------
#Esteso
universal_est = "*Universal*"
ijn_est = "*Sakura Empire*"
uss_est = "*Eagle Union*"
hms_est = "*Royal Navy*"
kms_est = "*Ironblood*"
roc_est = "*Dragon Empery*"
ffnf_est = "*Iris Libre*"
mnf_est = "*Vichya Dominion*"
sn_est = "*North Union*"
hdn_est = "*Neptunia*"
#Abbreviazioni
universal = "__[UNIV]__"
ijn = "__[IJN]__"
uss = "__[USS]__"
hms = "__[HMS]__"
kms = "__[KMS]__"
roc = "__[ROC]__"
ffnf = "__[FFNF]__"
mnf = "__[MNF]__"
sn = "__[SN]__"
hdn = "__[HDN]__"
#-------------------------------------------------------------------------------
#Tipo
dd = "DD"
cl = "CL"
ca = "CA"
cb = "CB"
bb = "BB"
bc = "BC"
bm = "BM"
bbv = "BBV"
cv = "CV"
cvl = "CVL"
ar = "AR"
ss = "SS"
ssv = "SSV"
#-------------------------------------------------------------------------------
#Rarità
N = "(Normal)"
R = "(Rare)"
E = "(Elite)"
SR = "(Super Rare)"
UR = "(Ultra Rare)"
PR = "(Priority)"
U = "(Unreleased)"
#-------------------------------------------------------------------------------
#Skill
rosso = "📕"
blu = "📘"
giallo = "📒"
boh = " "
#-------------------------------------------------------------------------------
#Info
none = "Non può essere costruita"
meowfficer = "https://azurlane.koumakan.jp/Meowfficer"
icona_rare = "https://azurlane.koumakan.jp/w/images/thumb/e/ea/CommonMeowficerIcon.png/90px-CommonMeowficerIcon.png"
img_rare = "https://azurlane.koumakan.jp/w/images/thumb/6/61/CommonMeowficer.png/384px-CommonMeowficer.png"
box = "Cat Boxes"

gold = 0xF4FF6C
purple = 0xDDA0DD
blue = 0xb0e0e6
#-------------------------------------------------------------------------------
                            #Immagine fazione
#-------------------------------------------------------------------------------
img_universal = "https://azurlane.koumakan.jp/w/images/d/da/Cm_1.png"
img_eagle = "https://azurlane.koumakan.jp/w/images/2/21/Eagleunion_orig.png"
img_royal = "https://azurlane.koumakan.jp/w/images/8/86/Royalnavy_orig.png"
img_iron = "https://azurlane.koumakan.jp/w/images/f/f5/Ironblood_edited.png"
img_sakura = "https://azurlane.koumakan.jp/w/images/9/93/Sakuraempire_orig.png"
#-------------------------------------------------------------------------------
catdatabase = {
"antenna": {
        "nome_gatta": "Antenna",
        "rarità_gatta": SR,
        "tempo_gatta": "10:45:00",
        "esteso_gatta": uss_est,
        "nazionalità_gatta": uss,
        "colore_gatta": gold,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Antenna", #wiki
            "https://azurlane.koumakan.jp/w/images/e/ef/AntennaIcon.png", #icona
            img_eagle, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/1/13/Antenna.png/384px-Antenna.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "43 → 141",
            "64 → 210",
            "55 → 180",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Ace Shooter" + punti_ast_spazio + blu,
        ],
        "condition": [
            "In battle with enemy Main Fleet or Recon Fleet",
            "BB, BC, or BBV as Flagship",
            "None",
        ],
        "effect": [
            "Increase Accuracy for BB, BC, BBV in fleet significantly based on Tactics stat",
            "Increase damage dealt by flagship based on Command stat",
            "Increase Evasion and AA for BB, BC, BBV based on Command stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"bishamaru": {
        "nome_gatta": "Bishamaru",
        "rarità_gatta": SR,
        "tempo_gatta": "09:58:00",
        "esteso_gatta": ijn_est,
        "nazionalità_gatta": ijn,
        "colore_gatta": gold,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Bishamaru", #wiki
            "https://azurlane.koumakan.jp/w/images/b/b6/BishamaruIcon.png", #icona
            img_sakura, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/3/3f/Bishamaru.png/384px-Bishamaru.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "38 → 125",
            "49 → 161",
            "68 → 223",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Fist of Counterattack" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Staff Cat",
            "None",
            "Fleet contains only 1 CV/L at start of battle.",
        ],
        "effect": [
            "Increase Airpower and Reload (minor effect) of all light carriers and carriers in the equipped fleet based on Command stat",
            "Decrease rate of ambush based on Support stat for the equipped fleet.",
            "First airstrike reload speed is increased by 8% and will contain extra torpedo bombers.",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"beer": {
        "nome_gatta": "Beer",
        "rarità_gatta": R,
        "tempo_gatta": "02:32:00",
        "esteso_gatta": kms_est,
        "nazionalità_gatta": kms,
        "colore_gatta": blue,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Beer", #wiki
            icona_rare, #icona
            img_iron, #nazione
            img_rare, #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "28 → 92",
            "41 → 134",
            "49 → 161",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Destroyer Command" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Staff Cat",
            "Staff Cat",
            "Staff Cat",
        ],
        "effect": [
            "Increase Evasion for DD, based on Command stat",
            "Increase Accuracy for DD, based on Tactics stat",
            "Increase Torpedo for DD, based on Support stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"sg": {
        "nome_gatta": "SG",
        "rarità_gatta": R,
        "tempo_gatta": "02:25:00",
        "esteso_gatta": uss_est,
        "nazionalità_gatta": uss,
        "colore_gatta": blue,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/SG", #wiki
            icona_rare, #icona
            img_eagle, #nazione
            img_rare, #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "41 → 134",
            "51 → 167",
            "26 → 85",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Reconnaissance" + punti_ast_spazio + blu,
        ],
        "condition": [
            "None",
            "Staff Cat",
            "Staff Cat",
        ],
        "effect": [
            "Decrease chance of ambush based on Support stat",
            "Increase Accuracy for CL, CA, based on Tactics stat",
            "Increase Firepower for CL, CA, based on Command stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"rose": {
        "nome_gatta": "Rose",
        "rarità_gatta": R,
        "tempo_gatta": "02:17:00",
        "esteso_gatta": hms_est,
        "nazionalità_gatta": hms,
        "colore_gatta": blue,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Rose", #wiki
            icona_rare, #icona
            img_royal, #nazione
            img_rare, #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "64 → 210",
            "29 → 95",
            "23 → 75",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Battleship Support" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Staff Cat",
            "Staff Cat",
            "Staff Cat",
        ],
        "effect": [
            "Increase Reload for BB, BC, BBV, based on Support stat",
            "Increase Accuracy for BB, BC, BBV, based on Support stat",
            "Increase Firepower for BB, BC, BBV, based on Support stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"asamaru": {
        "nome_gatta": "Asamaru",
        "rarità_gatta": R,
        "tempo_gatta": "02:06:00",
        "esteso_gatta": ijn_est,
        "nazionalità_gatta": ijn,
        "colore_gatta": blue,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Asamaru", #wiki
            icona_rare, #icona
            img_sakura, #nazione
            img_rare, #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "24 → 78",
            "48 → 157",
            "40 → 131",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Cruiser Command" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Staff Cat",
            "Staff Cat",
            "Staff Cat",
        ],
        "effect": [
            "Increase Accuracy for CV, CVL, based on Tactics stat",
            "Increase Torpedo for CL, CA, based on Support stat",
            "Increase Torpedo for CL, CA, based on Command stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"lady": {
        "nome_gatta": "Lady",
        "rarità_gatta": R,
        "tempo_gatta": "02:03:00",
        "esteso_gatta": uss_est,
        "nazionalità_gatta": uss,
        "colore_gatta": blue,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Lady", #wiki
            icona_rare, #icona
            img_eagle, #nazione
            img_rare, #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "28 → 92",
            "40 → 131",
            "52 → 171",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Carrier Support" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Staff Cat",
            "Staff Cat",
            "Staff Cat",
        ],
        "effect": [
            "Increase Reload for CV, CVL, based on Support stat",
            "Increase Airpower for CV, CVL, based on Command stat",
            "Increase Accuracy for CV, CVL, based on Tactics stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"katsumaru": {
        "nome_gatta": "Katsumaru",
        "rarità_gatta": R,
        "tempo_gatta": "01:55:00",
        "esteso_gatta": ijn_est,
        "nazionalità_gatta": ijn,
        "colore_gatta": blue,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Katsumaru", #wiki
            icona_rare, #icona
            img_sakura, #nazione
            img_rare, #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "36 → 118",
            "47 → 154",
            "32 → 105",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Battleship Support" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Staff Cat",
            "Staff Cat",
            "Staff Cat",
        ],
        "effect": [
            "Increase Accuracy for BB, BC, BBV, based on Support stat",
            "Increase AA for BB, BC, BBV, based on Command stat",
            "Increase Firepower for BB, BC, BBV, based on Tactics stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"tofu": {
        "nome_gatta": "Tofu",
        "rarità_gatta": R,
        "tempo_gatta": "01:54:00",
        "esteso_gatta": kms_est,
        "nazionalità_gatta": kms,
        "colore_gatta": blue,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Tofu", #wiki
            icona_rare, #icona
            img_iron, #nazione
            img_rare, #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "37 → 121",
            "46 → 151",
            "36 → 118",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Cruiser Support" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Staff Cat",
            "Staff Cat",
            "Staff Cat",
        ],
        "effect": [
            "Increase Evasion for CL, CA, based on Support stat",
            "Increase Firepower for CL, CA, based on Support stat",
            "Increase Firepower for CL, CA, based on Command stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"bugles": {
        "nome_gatta": "bugles",
        "rarità_gatta": R,
        "tempo_gatta": "01:39:00",
        "esteso_gatta": hms_est,
        "nazionalità_gatta": hms,
        "colore_gatta": blue,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Bugles", #wiki
            icona_rare, #icona
            img_royal, #nazione
            img_rare, #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "29 → 95",
            "38 → 125",
            "52 → 171",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Cruiser Tactics" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Staff Cat",
            "Staff Cat",
            "Staff Cat",
        ],
        "effect": [
            "Increase Firepower for CL, CA, CB, based on Tactics stat",
            "Increase Accuracy for CL, CA, CB, based on Tactics stat",
            "Increase Evasion for CL, CA, based on Tactics stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"bunny": {
        "nome_gatta": "Bunny",
        "rarità_gatta": E,
        "tempo_gatta": "06:09:00",
        "esteso_gatta": uss_est,
        "nazionalità_gatta": uss,
        "colore_gatta": purple,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Bunny", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/f/f5/EagleUnionMeowficerIcon.png/90px-EagleUnionMeowficerIcon.png", #icona
            img_eagle, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/e/e7/EagleUnionMeowficer.png/384px-EagleUnionMeowficer.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "43 → 141",
            "55 → 180",
            "36 → 118",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Self Limiter" + punti_ast_spazio + blu,
        ],
        "condition": [
            "While equipped as Commander Cat, when fleet contacts non-flagship enemy units and the fleet contains a destroyer",
            "While the lead ship is a destroyer and its HP not 0, at the beginning of battle, when the lead destroyer gets close to the enemy",
            "None*",
        ],
        "effect": [
            "15% chance of launching preemptive torpedo strike.",
            "Fire Meowficer Barrage I. Limited to once per battle.",
            "Meowficer Barrage I improves to Meowficer Barrage II.",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"eagle": {
        "nome_gatta": "Eagle",
        "rarità_gatta": E,
        "tempo_gatta": "05:36:00",
        "esteso_gatta": uss_est,
        "nazionalità_gatta": uss,
        "colore_gatta": purple,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Eagle", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/f/f5/EagleUnionMeowficerIcon.png/90px-EagleUnionMeowficerIcon.png", #icona
            img_eagle, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/e/e7/EagleUnionMeowficer.png/384px-EagleUnionMeowficer.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "33 → 108",
            "52 → 171",
            "49 → 161",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Wings of Fortune" + punti_ast_spazio + blu,
        ],
        "condition": [
            "While equipped as Staff Cat",
            "None*",
            "While equipped as Staff Cat",
        ],
        "effect": [
            "Increase Reload (minor effect) of all light carriers and carriers in the equipped fleet based on Tactics stat",
            "Decrease the chance of enemy airstrikes based on Tactics stat for the equipped fleet.",
            "Increase Airpower (medium effect) of all light carriers and carriers in the equipped fleet based on Command stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"potato": {
        "nome_gatta": "Potato",
        "rarità_gatta": E,
        "tempo_gatta": "06:45:00",
        "esteso_gatta": kms_est,
        "nazionalità_gatta": kms,
        "colore_gatta": purple,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Potato", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/a/ab/IronbloodMeowficerIcon.png/90px-IronbloodMeowficerIcon.png", #icona
            img_iron, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/b/ba/IronbloodMeowficer.png/384px-IronbloodMeowficer.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "35 → 115",
            "56 → 184",
            "43 → 141",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Iron Knight of the Sea" + punti_ast_spazio + blu,
        ],
        "condition": [
            "While equipped as Staff Cat",
            "While equipped as Staff Cat",
            "When battling a main fleet (battleship node)",
        ],
        "effect": [
            "Increase Evasion (minor effect) of all battleships, battlecruisers, and aviation battleships in the equipped fleet based on Command stat",
            "Increase Accuracy (medium effect) of all battleships, battlecruisers, and aviation battleships in the equipped fleet based on Tactics stat",
            "Decrease damage received by flagship based on Tactics stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"edelweiss": {
        "nome_gatta": "Edelweiss",
        "rarità_gatta": E,
        "tempo_gatta": "05:57:00",
        "esteso_gatta": kms_est,
        "nazionalità_gatta": kms,
        "colore_gatta": purple,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Edelweiss", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/a/ab/IronbloodMeowficerIcon.png/90px-IronbloodMeowficerIcon.png", #icona
            img_iron, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/b/ba/IronbloodMeowficer.png/384px-IronbloodMeowficer.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "34 → 111",
            "59 → 194",
            "41 → 134",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Brave of the Sea" + punti_ast_spazio + blu,
        ],
        "condition": [
            "While equipped as Staff Cat",
            "While equipped as Staff Cat",
            "None",
        ],
        "effect": [
            "Increase Torpedo (minor effect) of all submarines in the equipped fleet based on Command stat",
            "Increase Accuracy (medium effect) of all submarines in the equipped fleet based on Command stat",
            "Increase submarine hunting range level by 1",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"gral": {
        "nome_gatta": "Gral",
        "rarità_gatta": E,
        "tempo_gatta": "05:57:00",
        "esteso_gatta": kms_est,
        "nazionalità_gatta": kms,
        "colore_gatta": purple,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Gral", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/a/ab/IronbloodMeowficerIcon.png/90px-IronbloodMeowficerIcon.png", #icona
            img_iron, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/b/ba/IronbloodMeowficer.png/384px-IronbloodMeowficer.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "32 → 105",
            "51 → 167",
            "48 → 157",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Sentinel of the Sea" + punti_ast_spazio + blu,
        ],
        "condition": [
            "While equipped as Staff Cat",
            "While equipped as Staff Cat",
            "While equipped as Staff Cat",
        ],
        "effect": [
            "Increase Torpedo (minor effect) of all submarines in the equipped fleet based on Command stat",
            "Increase Evasion (medium effect) of all submarines in the equipped fleet based on Command stat",
            "Increase Accuracy (medium effect) of all submarines in the equipped fleet based on Command stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"justice": {
        "nome_gatta": "Justice",
        "rarità_gatta": SR,
        "tempo_gatta": "10:24:00",
        "esteso_gatta": uss_est,
        "nazionalità_gatta": uss,
        "colore_gatta": gold,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Justice", #wiki
            "https://azurlane.koumakan.jp/w/images/b/b9/JusticeIcon.png", #icona
            img_eagle, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/0/03/Justice.png/384px-Justice.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "44 → 144",
            "52 → 171",
            "52 → 171",
        ],
        "skill_gatta": [
            #1
            tre_ast + "31 Knots of Justice" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Fleet contains 3 DDs",
            "Commander Cat, engaged with non-boss enemy destroyer",
            "Commander Cat with DD in fleet, engaged with allied fleet also engaged in adjacent square",
        ],
        "effect": [
            "Increase map movement range by 1",
            "15% chance of preemptive torpedo strike to reduce %HP",
            "Ability to swap positions with allied fleet on the map and take over the allied fleet's battle",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"lime": {
        "nome_gatta": "Lime",
        "rarità_gatta": SR,
        "tempo_gatta": "10:05:00",
        "esteso_gatta": hms_est,
        "nazionalità_gatta": hms,
        "colore_gatta": gold,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Lime", #wiki
            "https://azurlane.koumakan.jp/w/images/d/d7/LimeIcon.png", #icona
            img_royal, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/3/34/Lime.png/384px-Lime.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "55 → 180",
            "52 → 171",
            "58 → 190",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Faithful to Duty" + punti_ast_spazio + boh,
        ],
        "condition": [
            "Staff Cat",
            "Staff Cat, fleet engages in battle adjacent to inaccessible terrain",
            "None",
        ],
        "effect": [
            "Increase Firepower and AA for BB, BC, BBV based on Command stat",
            "Increase Firepower for entire fleet based on Tactics stat",
            "Increase damage dealt to enemy BB, BC, BBV based on Tactics stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"oscar": {
        "nome_gatta": "Oscar",
        "rarità_gatta": SR,
        "tempo_gatta": "10:03:00",
        "esteso_gatta": kms_est,
        "nazionalità_gatta": kms,
        "colore_gatta": gold,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Oscar", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/5/5a/OscarIcon.png/90px-OscarIcon.png", #icona
            img_iron, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/6/68/Oscar.png/384px-Oscar.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "37 → 101",
            "66 → 217",
            "54 → 177",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Unsinkable Fortune" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Staff Cat",
            "Staff Cat, fleet contains BB, BC, BBV, and encounters non-boss enemy fleet",
            "Staff Cat, in battle with Main Fleet",
        ],
        "effect": [
            "Increase Firepower and Accuracy for BB, BC, BBV based on Command stat",
            "15% chance preemptive shelling to reduce %HP based on Command stat, fleet level, and fleet power",
            "Decrease damage taken by BB, BC, BBV based on support stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"pound": {
        "nome_gatta": "Pound",
        "rarità_gatta": SR,
        "tempo_gatta": "10:27:00",
        "esteso_gatta": hms_est,
        "nazionalità_gatta": hms,
        "colore_gatta": gold,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Pound", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/1/11/PoundIcon.png/90px-PoundIcon.png", #icona
            img_royal, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/9/9a/Pound.png/384px-Pound.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "67 → 220",
            "59 → 194",
            "36 → 118",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Sweet Deception" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Commander Cat",
            "Commander Cat, 4 or more Royal Navy ships in fleet at start of battle",
            "Commander Cat",
        ],
        "effect": [
            "Increase Firepower and AA for BB, BC, BBV, based on Command stat",
            "Decrease damage taken by vanguard based on Support stat",
            "Increase Evasion of friendly Royal Navy ships significantly based on Support stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"ark": {
        "nome_gatta": "Ark",
        "rarità_gatta": E,
        "tempo_gatta": "07:26:00",
        "esteso_gatta": hms_est,
        "nazionalità_gatta": hms,
        "colore_gatta": purple,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Ark", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/b/ba/RoyalNavyMeowficerIcon.png/90px-RoyalNavyMeowficerIcon.png", #icona
            img_royal, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/4/4d/RoyalNavyMeowficer.png/384px-RoyalNavyMeowficer.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "39 → 128",
            "48 → 157",
            "44 → 144",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Tiddles' Legacy" + punti_ast_spazio + blu,
        ],
        "condition": [
            "While equipped as Staff Cat",
            "When a patrol fleet (destroyer node) is within 2 squares",
            "While equipped as Staff Cat",
        ],
        "effect": [
            "Increase Accuracy for CV, CVL (minor) based on Tactical stat",
            "Increase map movement range by 1",
            "Increase Aviation for CV, CVL (medium) based on Command stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"marble": {
        "nome_gatta": "Marble",
        "rarità_gatta": E,
        "tempo_gatta": "06:43:00",
        "esteso_gatta": hms_est,
        "nazionalità_gatta": hms,
        "colore_gatta": purple,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Marble", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/b/ba/RoyalNavyMeowficerIcon.png/90px-RoyalNavyMeowficerIcon.png", #icona
            img_royal, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/4/4d/RoyalNavyMeowficer.png/384px-RoyalNavyMeowficer.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "23 → 75",
            "64 → 210",
            "44 → 144",
        ],
        "skill_gatta": [
            #1
            tre_ast + "SKILL" + punti_ast_spazio + blu,
        ],
        "condition": [
            "None",
            "While equipped as Staff cat",
            "While equipped as Staff cat",
        ],
        "effect": [
            "Decrease ambush chance based on Support stat",
            "Increase reload for BB, BC, BBV (minor) based on Command stat",
            "Increase Firepower for Royal Navy ships (minor) based on Command stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"pepper": {
        "nome_gatta": "Pepper",
        "rarità_gatta": E,
        "tempo_gatta": "06:16:00",
        "esteso_gatta": hms_est,
        "nazionalità_gatta": hms,
        "colore_gatta": purple,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Pepper", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/b/ba/RoyalNavyMeowficerIcon.png/90px-RoyalNavyMeowficerIcon.png", #icona
            img_royal, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/4/4d/RoyalNavyMeowficer.png/384px-RoyalNavyMeowficer.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "44 → 144",
            "50 → 164",
            "45 → 148",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Resource Interceptor" + punti_ast_spazio + blu,
        ],
        "condition": [
            "While equipped as Staff Cat",
            "While equipped as Staff Cat, when battling transport fleet (gold ship node)",
            "While equipped as Staff Cat",
        ],
        "effect": [
            "Increase Evasion (minor effect) of all light cruisers and heavy cruisers in the equipped fleet based on Support stat",
            "Increase Firepower (large effect) of all light cruisers and heavy cruisers in the equipped fleet based on Tactics stat",
            "Increase Torpedo (medium effect) of all light cruisers and heavy cruisers in the equipped fleet based on Command stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"soup": {
        "nome_gatta": "Soup",
        "rarità_gatta": E,
        "tempo_gatta": "05:30:00",
        "esteso_gatta": hms_est,
        "nazionalità_gatta": hms,
        "colore_gatta": purple,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Soup", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/b/ba/RoyalNavyMeowficerIcon.png/90px-RoyalNavyMeowficerIcon.png", #icona
            img_royal, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/4/4d/RoyalNavyMeowficer.png/384px-RoyalNavyMeowficer.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "39 → 128",
            "55 → 180",
            "33 → 108",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Patrol Hunter" + punti_ast_spazio + blu,
        ],
        "condition": [
            "While equipped as Staff Cat and battling against a patrol fleet (destroyer node)",
            "While equipped as Staff Cat and battling against a patrol fleet (destroyer node)",
            "When a patrol fleet (destroyer node) is within 3 squares of the equipped fleet",
        ],
        "effect": [
            "Increase Accuracy (medium effect) of all destroyers in the equipped fleet based on Tactics stat",
            "Increase Evasion (minor effect) of all destroyers in the equipped fleet based on Support stat",
            "Equipped fleet's map movement is increased by 1.",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"yoshimaru": {
        "nome_gatta": "Yoshimaru",
        "rarità_gatta": E,
        "tempo_gatta": "06:23:00",
        "esteso_gatta": ijn_est,
        "nazionalità_gatta": ijn,
        "colore_gatta": purple,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Yoshimaru", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/e/e0/SakuraEmpireMeowficerIcon.png/90px-SakuraEmpireMeowficerIcon.png", #icona
            img_sakura, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/3/34/SakuraEmpireMeowficer.png/384px-SakuraEmpireMeowficer.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "36 → 118",
            "62 → 203",
            "36 → 118",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Wild Intuition" + punti_ast_spazio + blu,
        ],
        "condition": [
            "While equipped as Staff Cat",
            "While equipped as Staff Cat",
            "While equipped as Staff Cat, when escort fleet (frontline) contains only one ship and is a destroyer",
        ],
        "effect": [
            "Increase Evasion (minor effect) of all destroyers in the equipped fleet based on Command stat",
            "Increase Torpedo (medium effect) of all destroyers in the equipped fleet based on Support stat",
            "Increase Torpedo (large effect) of that destroyer in the equipped fleet based on Command stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"jiromaru": {
        "nome_gatta": "Jiromaru",
        "rarità_gatta": E,
        "tempo_gatta": "05:17:00",
        "esteso_gatta": ijn_est,
        "nazionalità_gatta": ijn,
        "colore_gatta": purple,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Jiromaru", #wiki
            "https://azurlane.koumakan.jp/w/images/e/e0/SakuraEmpireMeowficerIcon.png", #icona
            img_sakura, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/3/34/SakuraEmpireMeowficer.png/384px-SakuraEmpireMeowficer.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "33 → 108",
            "61 → 200",
            "41 → 134",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Ultimate move: Three-Layered Strike" + punti_ast_spazio + blu,
        ],
        "condition": [
            "While equipped as Staff Cat",
            "While equipped as Staff Cat",
            "When equipped fleet contains a light carrier or carrier and contacts non-flagship enemy units",
        ],
        "effect": [
            "Increase Accuracy (minor effect) of all light carriers and carriers in the equipped fleet based on Tactics stat",
            "Increase Airpower (medium effect) of all light carriers and carriers in the equipped fleet based on Command stat",
            "15% chance of launching an airstrike. Damage is based on Tactics stat, as well as levels and fleet powers of both fleets.",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"steel": {
        "nome_gatta": "Steel",
        "rarità_gatta": SR,
        "tempo_gatta": "09:35:00",
        "esteso_gatta": kms_est,
        "nazionalità_gatta": kms,
        "colore_gatta": gold,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Steel", #wiki
            "https://azurlane.koumakan.jp/w/images/thumb/3/37/SteelIcon.png/90px-SteelIcon.png", #icona
            img_iron, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/c/c9/Steel.png/384px-Steel.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "40 → 131",
            "66 → 217",
            "52 → 171",
        ],
        "skill_gatta": [
            #1
            tre_ast + "Silent Hunter" + punti_ast_spazio + blu,
        ],
        "condition": [
            "None",
            "None",
            "None",
        ],
        "effect": [
            "Increase Torpedo for SS, SSV based on Command and Support stat",
            "Increase submarine hunting range by 1",
            "Increase %HP reduction by submarine hunt based on Tactics stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
"takemaru": {
        "nome_gatta": "Takemaru",
        "rarità_gatta": SR,
        "tempo_gatta": "09:40:00",
        "esteso_gatta": ijn_est,
        "nazionalità_gatta": ijn,
        "colore_gatta": gold,
        "acquisizione_gatta": box,
        "wiki_gatta": [
            "https://azurlane.koumakan.jp/Takemaru", #wiki
            "https://azurlane.koumakan.jp/w/images/1/16/TakemaruIcon.png", #icona
            img_sakura, #nazione
            "https://azurlane.koumakan.jp/w/images/thumb/b/be/Takemaru.png/384px-Takemaru.png", #immagine
            meowfficer, #wiki meowfficer
        ],
        "stat_gatta": [
            "30 → 98",
            "62 → 203",
            "66 → 217",
        ],
        "skill_gatta": [
            #1
            tre_ast + "engeful Tail Whip" + punti_ast_spazio + blu,
        ],
        "condition": [
            "Commander Cat",
            "Commander Cat, enemy Main Fleet within 2 squares",
            "Commander Cat, 30 seconds passed into battle with Main Fleet",
        ],
        "effect": [
            "Increase Firepower and Torpedo for CL, CA, CB based on Tactics stat",
            "Decrease damage taken by flagship based on Command stat",
            "Increase Accuracy and Evasion for CL, CA, CB, significantly based on Tactics stat",
        ],
        "incoming": "no",
        "incoming_x": "no",
    },
}
