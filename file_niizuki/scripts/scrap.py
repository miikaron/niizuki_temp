import os
from os.path import join, dirname
from bs4 import BeautifulSoup
import requests
import time
import json
import traceback

FIREFOX_AGENT = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"}

lista_navi = []
collab_ships = []

def crea_lista(wiki):
    #----------------------------------------------------------------------------------------------------
    # List of Ships
    ship_list_url = wiki+"/List_of_Ships"
    headers = FIREFOX_AGENT
    shiplist_req = requests.get(ship_list_url, headers=headers)
    #BeautifulSoup object: Collect and Parse
    sl_soup = BeautifulSoup(shiplist_req.text, "html.parser")
    #----------------------------------------------------------------------------------------------------
    standard_list = []
    research_ships = []

    sl_table = sl_soup.find_all("table", {"class": "wikitable sortable jquery-tablesorter"})
    row_tab1 = sl_table[0].find_all("tr")
    for row in row_tab1:
        cols = row.find_all("td")
        for td in cols:
            a = td.find("a")
            if a:
                if a.text.isnumeric():
                    standard_list.append(a["href"])
                    lista_navi.append(a["href"])
    row_tab2 = sl_table[1].find_all("tr")
    for row in row_tab2:
        cols = row.find_all("td")
        for td in cols:
            a = td.find("a")
            if a:
                if a.text.startswith("Plan"):
                    research_ships.append(a["href"])
                    lista_navi.append(a["href"]) 
    row_tab3 = sl_table[2].find_all("tr")
    for row in row_tab3:
        cols = row.find_all("td")
        for td in cols:
            a = td.find("a")
            if a:
                if a.text.startswith(("Collab", "1006")):
                    collab_ships.append(a["href"])
                    lista_navi.append(a["href"])

def aggiorna_database():
    #----------------------------------------------------------------------------------------------------
    wiki = "https://azurlane.koumakan.jp"
    crea_lista(wiki)

    if os.path.exists(join("file_niizuki", "mydatabase.json")):
        try:
            os.remove(join("file_niizuki", "mydatabase.json"))
        except FileNotFoundError:
            print("Scrap.py: creazione file 'mydatabase.json'")
            f = open(join('file_niizuki', 'mydatabase.json'), "w")
            f.close()
        except Exception:
            print(traceback.format_exc())
    #----------------------------------------------------------------------------------------------------
    #print(standard_list, research_ships, collab_ships, lista_navi, sep="---")
    #----------------------------------------------------------------------------------------------------
    #lista_navi = ["/Aurora", "/Akashi", "/Maury", "/Wichita", "/Ayanami"] # (lista_navi2 -- debug)

    for nave in lista_navi:
        nome = nave
        try:
            #Pagina Wiki: Nave
            main_url = wiki+nome
            headers = FIREFOX_AGENT
            req = requests.get(main_url, headers=headers)
            soup = BeautifulSoup(req.text, "html.parser")
            #Body: Nave
            body = soup.body
    #----------------------------------------------------------------------------------------------------
            #Main title = Nome della nave
            h1_ship_name = body.find("h1", {"id": "firstHeading"})
            #print(h1_ship_name)
            
            if h1_ship_name:
                nome_nave = h1_ship_name.get_text()
                nome_nave_lower = nome_nave.lower()
                nome_nave_url = "/"+nome_nave.replace(" ", "_")
    #----------------------------------------------------------------------------------------------------
            #print(nome_nave, nome_nave_lower, nome_nave_url, sep="---")
    #-------------------------------------------------------------------------------------------------s---
            # Tabella parte 1
    #----------------------------------------------------------------------------------------------------
            table_content_p1 = []
            href_title = []

            tables = body.find_all("table", {"style": "border-left:0; height:130px; margin:0; width:100%"})
            a_href = tables[0].find_all("a", href=True)
            for href in a_href:
                #print(href)
                anchor_with_title = href.get("title")
                href_title.append(anchor_with_title)
                for string in href.strings:
                    string = repr(string) if string else print("No string found")
                    table_content_p1.append(string.strip("'"))
            
            #print(href_title, "-", table_content_p1)
            try:
                rarità = href_title[1]
                tempo = table_content_p1[0] if table_content_p1[0] != "Cannot Be Constructed" else "Non può essere costruita"
                classe = table_content_p1[1]
            except IndexError:
                rarità = href_title[0]
                tempo = href_title[0]
                classe = table_content_p1[0]

    #----------------------------------------------------------------------------------------------------        
            #print(tempo, rarità, classe, sep="---")
    #----------------------------------------------------------------------------------------------------
            # Tabella parte 2
    #----------------------------------------------------------------------------------------------------
            table_content_p2 = []

            tab_p2_td = tables[1].find_all("td")
            for td in tab_p2_td:
                raw_info = td.text[:-1]
                info = raw_info.strip("\n  ")

                #Fix info
                if info == "Battleship →  Aviation Battleship":
                    info = "Battleship → Aviation Battleship"
                if info == "Light Cruiser →  Heavy Cruiser":
                    info = "Light Cruiser → Heavy Cruiser"

                table_content_p2.append(info)
            #print(table_content_p2)

            try:
                id_nave = table_content_p2[0]
                nazionalità = table_content_p2[1]
                tipo = table_content_p2[2]
            except IndexError:
                id_nave = table_content_p2[0]
                nazionalità = table_content_p2[1]
                tipo = table_content_p2[2]
            
            if nazionalità == "Universal":
                abbreviazione = "__[UNIV]__"
                img_nazione = "https://azurlane.koumakan.jp/w/images/d/da/Cm_1.png"

            if nazionalità == "Sakura Empire":
                abbreviazione = "__[IJN]__"
                img_nazione = "https://azurlane.koumakan.jp/w/images/9/93/Sakuraempire_orig.png"

            if nazionalità == "Eagle Union":
                abbreviazione = "__[USS]__"
                img_nazione = "https://azurlane.koumakan.jp/w/images/2/21/Eagleunion_orig.png"

            if nazionalità == "Royal Navy":
                abbreviazione = "__[HMS]__"
                img_nazione = "https://azurlane.koumakan.jp/w/images/8/86/Royalnavy_orig.png"

            if nazionalità == "Iron Blood":
                abbreviazione = "__[KMS]__"
                img_nazione = "https://azurlane.koumakan.jp/w/images/f/f5/Ironblood_edited.png"

            if nazionalità == "Dragon Empery":
                abbreviazione = "__[ROC]__"
                img_nazione = "https://azurlane.koumakan.jp/w/images/3/3f/Azurlane-logo-1.png"

            if nazionalità == "Iris Libre":
                abbreviazione = "__[FFNF]__"
                img_nazione = "https://azurlane.koumakan.jp/w/images/5/59/Iris_orig.png"

            if nazionalità == "Vichya Dominion":
                abbreviazione = "__[MNF]__"
                img_nazione = "https://azurlane.koumakan.jp/w/images/a/a1/Vf_1.png"

            if nazionalità == "Northern Parliament":
                abbreviazione = "__[SN]__"
                img_nazione = "https://azurlane.koumakan.jp/w/images/b/b2/Northunion_orig.png"

            if nazionalità == "Sardegna Empire":
                abbreviazione = "__[RN]__"
                img_nazione = "https://azurlane.koumakan.jp/w/images/f/f1/Rn_1.png"

            if nazionalità == "Venus Vacation":
                abbreviazione = " "
                img_nazione = "https://azurlane.koumakan.jp/w/images/0/0d/Um_1.png"

            if nazionalità == "Neptunia":
                abbreviazione = "__[HDN]__"
                img_nazione = "https://azurlane.koumakan.jp/w/images/e/e0/Neptune_nation.png"

            if nazionalità == "KizunaAI":
                abbreviazione = "DOAXVV"
                img_nazione = "https://azurlane.koumakan.jp/w/images/0/0d/Um_1.png"

            if nazionalità == "Hololive":
                abbreviazione = " "
                img_nazione = "https://azurlane.koumakan.jp/w/images/0/0d/Um_1.png"
            
            if nazionalità == "Utawarerumono":
                abbreviazione = " "
                img_nazione = "https://azurlane.koumakan.jp/w/images/0/0d/Um_1.png"

            if nazionalità == "Bilibili":
                abbreviazione = " "
                img_nazione = "https://azurlane.koumakan.jp/w/images/5/5c/Bi_1.png"

    #----------------------------------------------------------------------------------------------------
            # colore_tipo: dd, cl, ca, cb, bb, bc, bm, bbv, cv, cvl, ar, ae, ss, ssv
    #----------------------------------------------------------------------------------------------------

            colore_embed = 0x778899
            colore_tipo = [0x87cefa, 0xfff3ad, 0xffdead, 0xff9980, 0xff3c3c, 0xf4676b, 0xffcccc, 0xdc143c, 0xb654f4, 0xc77cf6, 0x21cd8f, 0x7fffd4, 0x4dff4d, 0x66ff66]

            if tipo == "Destroyer":
                colore_embed = colore_tipo[0] 
            if tipo == "Light Cruiser":
                colore_embed = colore_tipo[1]
            if tipo == "Heavy Cruiser":
                colore_embed = colore_tipo[2]
            if tipo == "Large Cruiser":
                colore_embed = colore_tipo[3]
            if tipo == "Battleship":
                colore_embed = colore_tipo[4]
            if tipo == "Battlecruiser":
                colore_embed = colore_tipo[5]
            if tipo == "Monitor":
                colore_embed = colore_tipo[6]
            if tipo == "Battleship → Aviation Battleship":
                colore_embed = colore_tipo[7]
            if tipo == "Aircraft Carrier":
                colore_embed = colore_tipo[8]
            if tipo == "Light Aircraft Carrier":
                colore_embed = colore_tipo[9]
            if tipo == "Repair Ship":
                colore_embed = colore_tipo[10]
            if tipo == "Munition Ship":
                colore_embed = colore_tipo[11]
            if tipo == "Submarine":
                colore_embed = colore_tipo[12]
            if tipo == "Submarine Carrier":
                colore_embed = colore_tipo[13]
            if tipo == "Light Cruiser → Heavy Cruiser":
                colore_embed = colore_tipo[2]

            #print(id_nave, tipo, colore_embed, nazionalità, abbreviazione, img_nazione, sep="---")

    #----------------------------------------------------------------------------------------------------
            # Check if ship has retrofit
            div_content_list = []

            divs = body.find("div", {"id": "mw-normal-catlinks"})
            div_links = divs.find_all("a", href=True)
            #print(div_links)

            for dv_link in div_links:
                content = dv_link.get("title")
                div_content_list.append(content)
                with_retrofit = "Category:Ships with retrofit"

            retrofit = "disponibile" if with_retrofit in div_content_list else "non disponibile"
            #print(retrofit)

    #----------------------------------------------------------------------------------------------------
            # Icona.png
            ship_icon = body.find("img")
            icona_nave = wiki+ship_icon["src"]
            # Immagine.png

            try:
                div = body.find("div", {"class": "adaptiveratioimg"})
                ship_img = div.find("img")
                img_nave = wiki+ship_img["src"]
            except TypeError:
                img_nave = "https://azurlane.koumakan.jp/w/images/3/36/UnknownT1BP.png"
            
            #print(icona_nave, img_nave, sep="\n")

    #----------------------------------------------------------------------------------------------------
            # Tabella: Miscellaneous Info
    #----------------------------------------------------------------------------------------------------
            info = []
            info_link_list = []

            info_table = body.find("table", {"class": "wikitable", "style": "margin:0; width:100%"})
            for a in info_table.find_all("a", href=True):
                info_link = a["href"]
                info_link_list.append(info_link)

            cell = info_table.find_all("td")
            for td in cell:
                raw_info = td.text.split("\n")
                for raw_x in raw_info[:-1]:
                    info.append(raw_x)
            #Remove "Play" from <Play (Name)>
            no_play = info[9].split(" ")
            #print(no_play)

            if "Play" in no_play:
                info[9] = " ".join(no_play[1:])
            #print(info, info_link_list)

    #----------------------------------------------------------------------------------------------------        
            try:
                artista = info[1]
            except IndexError:
                artista = " "
            try:
                doppiatrice = info[9].strip()
            except IndexError:
                doppiatrice = " "
            """
            try:
                web = info_link_list[1]
            except IndexError:
                web = " "
            try:
                pixiv = info_link_list[2]
            except IndexError:
                pixiv = " "
            try:
                twitter = info_link_list[3]
            except IndexError:
                twitter = " "
            """
            try:
                link_doppiatrice = info_link_list[4]
            except IndexError:
                link_doppiatrice = " "

            #print(artista, doppiatrice, web, pixiv, twitter, link_doppiatrice, sep="\n")

    #----------------------------------------------------------------------------------------------------
            # Tabella: Equipment
    #----------------------------------------------------------------------------------------------------
            equip_info = []

            equip_table = body.find("table", {"class": "wikitable", "style": "text-align:center; width:100%"})
            for td in equip_table.find_all("td"): 
                span_info = td.text[:-1] if td.text[:-1] != " → " else "##"
                equip_info.append(span_info)
                #print(span_info)

            leading_text = ": __" if "##" not in equip_info else " "
            trailing_text = "__" if "##" not in equip_info else " "

            try:
                efficienza1 = equip_info[1] + leading_text+equip_info[2] + trailing_text
            except IndexError:
                efficienza1 = " "
            try:
                efficienza2 = equip_info[5] + leading_text+equip_info[6] + trailing_text
            except IndexError:
                efficienza2 = " "
            try:
                efficienza3 = equip_info[9] + leading_text+equip_info[10] + trailing_text
            except IndexError:
                efficienza3 = " "

            #print(efficienza1, efficienza2, efficienza3, sep="\n")

    #----------------------------------------------------------------------------------------------------
            # Tabella: | Strengthen Level (Limit Break Ranks) | Skills |
    #----------------------------------------------------------------------------------------------------
            lbs_table = body.find("table", {"class": "mw-collapsible wikitable"})
            rows = lbs_table.find_all("tr")
            #print(rows)

            skill_name = []
            skill_color = []
            skill_text = []
            lb_text = []
            lb_part_temp = []
            lb_text_temp = []
            
            for row in rows:
                lb_td = row.td
                if lb_td:
                    td_img = lb_td.find_all("img")          #Icona stat (navi PR)
                    if td_img:
                        #style1 = row.find("th")
                        #level = style1.text
                        for img in td_img:
                            anchor_with_title = img.get("title")
                            lb_part_raw = anchor_with_title+" "+img.next_sibling.strip()
                            lb_part_temp.append(lb_part_raw)
                        lb_part = " ".join(lb_part_temp)    #Unisci testo icone
                        lb_part_temp.clear()
                        lb_text_temp.append(lb_part)        #Testo (riga + icone)    
                        #Testo sotto alle icone stat:
                        li = lb_td.find_all("li")
                        li_text = ", "+li[-1].text
                        #print(li_text)
                        lb_text_temp.append(li_text)
                        lb_content = "• "+"".join(lb_text_temp)
                        #print(lb_content)
                        #Testo completo (casella con riga + icone) 
                        lb_text.append(lb_content)
                        #print(lb_content)
                        lb_text_temp.clear()
                    else:
                        #Testo caselle "riga senza icone"
                        raw_lb_content = "• "+lb_td.text.replace("Gains", ", Gains").replace("Upgrades", ", Upgrades").replace("IM", "I, M").replace("%S", "%, S").strip()
                        lb_content = raw_lb_content.replace("• , ", "• ")
                        if lb_content != "• ":
                            lb_text.append(lb_content)
    #----------------------------------------------------------------------------------------------------
                    td_skill = lb_td.find_next_sibling("td")
                    skill = td_skill.text
                    if skill and skill != "\n":
                        skill_name.append(skill.split("CN", 1)[0].strip())
                        style = lb_td.find_next("td").get("style")
                        #skill_color.append(style.split(";", 1)[0])
                        skill_color.append(style)
                        raw_text = td_skill.find_next_sibling("td").text
    #----------------------------------------------------------------------------------------------------
                        # Fix Nowaki's skill
                        target = "0% -"
                        res = [i for i in range(len(raw_text)) if raw_text.startswith(target, i)]
                        if res:
                            try:
                                t1 = raw_text.replace(raw_text, raw_text[:res[0]-1]+"\n• ")
                                t2 = raw_text.replace(raw_text, raw_text[res[0]-1:res[1]-1]+"\n• ")
                                t3 = raw_text.replace(raw_text, raw_text[res[1]-1:res[2]-1]+"\n• ")
                                t4 = raw_text.replace(raw_text, raw_text[res[2]-1:])

                                new_text = t1+t2+t3+t4
                                skill_text.append(new_text)
                            except Exception:
                                text = raw_text.strip().replace("Barrage preview (gif)", "")
                                skill_text.append(text)
    #----------------------------------------------------------------------------------------------------
                        else:
                            text = raw_text.strip().replace("Barrage preview (gif)", "")
                            skill_text.append(text) 

            #print(lb_text, skill_name. skill_color. skill_text, sep="\n")    
    #----------------------------------------------------------------------------------------------------
            try:
                lb1 = lb_text[0] if lb_text[0] else "Non disponibile"
            except IndexError:
                lb1 = "Non disponibile"
            try:
                lb2 = lb_text[1] if lb_text[1] else "Non disponibile"
            except IndexError:
                lb2 = " "
            try:
                lb3 = lb_text[2] if lb_text[2] else "Non disponibile"
            except IndexError:
                lb3 = " "
            try:
                lb4 = lb_text[3] if lb_text[2] else "Non disponibile"
            except IndexError:
                lb4 = " "
            try:
                lb5 = lb_text[4] if lb_text[2] else "Non disponibile"
            except IndexError:
                lb5 = " "
            try:
                lb6 = lb_text[5] if lb_text[2] else "Non disponibile"
            except IndexError:
                lb6 = " "
    #----------------------------------------------------------------------------------------------------
            try:
                nome_skill1 = skill_name[0] if skill_name[0] and len(skill_name[0])>2 else "Non disponibile"
            except IndexError:
                nome_skill1 = "Non disponibile"
            try:
                nome_skill2 = skill_name[1] if skill_name[1] and len(skill_name[1])>2 else " "
            except IndexError:
                nome_skill2 = " "
            try:
                nome_skill3 = skill_name[2] if skill_name[2] and len(skill_name[2])>2 else " "
            except IndexError:
                nome_skill3 = " "
            try:
                nome_skill4 = skill_name[3] if skill_name[3] and len(skill_name[3])>2 else " "
            except IndexError:
                nome_skill4 = " "
            try:
                nome_skill5 = skill_name[4] if skill_name[4] and len(skill_name[4])>2 else " "
            except IndexError:
                nome_skill5 = " "
    #----------------------------------------------------------------------------------------------------
            # colori_skill: background-color: DeepSkyBlue, Gold, Pink
    #----------------------------------------------------------------------------------------------------
            blu = "📘"
            giallo = "📒"
            rosso = "📕"
    #----------------------------------------------------------------------------------------------------
            skill_blu = "background-color:DeepSkyBlue"
            skill_gialla = "background-color:Gold"
            skill_rossa = "background-color:Pink"
            try:
                if skill_blu in skill_color[0]:
                    colore1 = blu
                elif skill_gialla in skill_color[0]:
                    colore1 = giallo
                elif skill_rossa in skill_color[0]:
                    colore1 = rosso
                else:
                    colore1 = " "
            except IndexError:
                colore1 = " "
            try:
                if skill_blu in skill_color[1]:
                    colore2 = blu
                elif skill_gialla in skill_color[1]:
                    colore2 = giallo
                elif skill_rossa in skill_color[1]:
                    colore2 = rosso
                else:
                    colore2 = " "
            except IndexError:
                colore2 = " "
            try:
                if skill_blu in skill_color[2]:
                    colore3 = blu
                elif skill_gialla in skill_color[2]:
                    colore3 = giallo
                elif skill_rossa in skill_color[2]:
                    colore3 = rosso
                else:
                    colore3 = " "
            except IndexError:
                colore3 = " "
            try:
                if skill_blu in skill_color[3]:
                    colore4 = blu
                elif skill_gialla in skill_color[3]:
                    colore4 = giallo
                elif skill_rossa in skill_color[3]:
                    colore4 = rosso
                else:
                    colore4 = " "
            except IndexError:
                colore4 = " "
            try:
                if skill_blu in skill_color[4]:
                    colore5 = blu
                elif skill_gialla in skill_color[4]:
                    colore5 = giallo
                elif skill_rossa in skill_color[4]:
                    colore5 = rosso
                else:
                    colore5 = " "
            except IndexError:
                colore5 = " "
    #----------------------------------------------------------------------------------------------------
            try:
                skill1 = "\n"+skill_text[0] if skill_name[0] else " "
            except IndexError:
                skill1 = " "
            try:
                skill2 = "\n"+skill_text[1] if skill_name[1] else " "    
            except IndexError:
                skill2 = " "
            try:
                # Fix Yuubari's skill
                if len(skill_text[2]) > 900:
                    skill3 = "\nUse a random piece of prototype equipment with various effects every 12 seconds:" + \
                        "\n• 17% - Prototype Type-0 Main Gun: Fires an HE ammo barrage." + \
                        "\n• 17% - Prototype Torpedo Tube: Fires a torpedo barrage." + \
                        "\n• 14% - Special Pyrotechnics Bomb: Fires a shrapnel bomb." + \
                        "\n• 14% - Repulsion Shield: Spawns a stationary shield that can block 60 hits and lasts for 18 seconds." + \
                        "\n• 14% - Projection Barrier: Spawns a stationary shield that can block 99 hits and lasts for 6 seconds." + \
                        "\n• 14% - Portable Repair Kit: Heals all ships in the fleet for 0.4% (2.4%) of Yuubari's maximum HP." + \
                        "\n• 10% - Value Bandages: Heals all ships in the fleet for 9 HP."
                else:
                    skill3 = "\n"+skill_text[2] if skill_name[2] else " "
            except IndexError:
                skill3 = " "
            try:
                skill4 = "\n"+skill_text[3] if skill_name[3] else " "
            except IndexError:
                skill4 = " "
            try:
                skill5 = "\n"+skill_text[4] if skill_name[4] else " "
            except IndexError:
                skill5 = " "

    #----------------------------------------------------------------------------------------------------
            # print(lb1, lb2, lb3, sep="\n")
            # print(nome_skill1, nome_skill2, nome_skill3, nome_skill4, sep="\n")
            # print(colore1, colore2, colore3, colore4, sep="\n")
            # print(skill1, skill2, skill3, skill4, sep="\n")
    #----------------------------------------------------------------------------------------------------
            time.sleep(0.5)
            # Wiki (Gallery)
            gallery = "/Gallery"
    #----------------------------------------------------------------------------------------------------
            s_url = wiki+nome+gallery
            headers = FIREFOX_AGENT
            skin_req = requests.get(s_url, headers=headers)
            skin_soup = BeautifulSoup(skin_req.text, "html.parser")
            #Body (gallery)
            body2 = skin_soup.body
    #----------------------------------------------------------------------------------------------------
            nome_skin = []
            img_list = []
            removed_title = ["Normal", "CN", "Censored", "Without Background"]
            divs = body2.find_all("div", {"class": "tabbertab"}, title = True)
            for div in divs:
                #print(div)
                title = div.get("title")

                # Remove [ Normal], [CN (or CENSORED)], [Without Background] buttons
                if title not in removed_title:
                    nome_skin.append(title)
                    a = div.find("a", {"class": "image"})
                    if a:
                        for img in a.find_all("img"):
                            img_list.append(img.get("src"))
                    #print(img_list)
            url_skin = []
            for img in img_list:
                url = wiki+img
                url_skin.append(url)
            
            skin_list = [i for x in zip(nome_skin, url_skin) for i in x]
    #----------------------------------------------------------------------------------------------------
            #print(skin_list)
    #----------------------------------------------------------------------------------------------------
            td_style = []
            td_style_build = []
            map1 = []
            map2 = []
            map3 = []
            map4 = []
            divs = body.find("div", {"id": "Construction"})
            count = 0
            text_check = ["⚪JP/KR only", "⚪CN only"]
            for td in divs.find_all("td", style=lambda stile: stile and stile.startswith("background-color:")):
                style = td.get("style")
                rspan = td.get("rowspan")
                if rspan == "2":
                    td_style_build.append(style)
                else:
                    count += 1
                    td_style.append(style)
                    if count < 14:
                        map1.append(style) if td.text.strip() not in text_check else map1.append("None")
                    if count < 27 and count > 13:
                        map2.append(style) if td.text.strip() not in text_check else map2.append("None")
                    if count < 40 and count > 26:
                        map3.append(style) if td.text.strip() not in text_check else map3.append("None")
                    if count < 53 and count > 39:
                        map4.append(style) if td.text.strip() not in text_check else map4.append("None")
            #print(map1, map2, map3, map4, sep="\n")

            map_row1 = []
            for idx, cap1 in enumerate(map1):
                if cap1 == "background-color:LightGreen" or cap1 == "background-color:PaleGreen":
                    cap_number = idx+1
                    row1 = " • "+str(cap_number)+"-1"
                    map_row1.append(row1)
                elif cap1 == "background-color:LemonChiffon" or cap1 == "background-color:LightYellow":
                    cap_number = idx+1
                    row1_boss = " • "+str(cap_number)+"-1 (Boss node)"
                    map_row1.append(row1_boss)
                else:
                    map_row1.append("")
            map_row2 = []
            for idx, cap2 in enumerate(map2):
                if cap2 == "background-color:LightGreen" or cap2 == "background-color:PaleGreen":
                    cap_number = idx+1
                    row2 = " • "+str(cap_number)+"-2"
                    map_row2.append(row2)
                elif cap2 == "background-color:LemonChiffon" or cap2 == "background-color:LightYellow":
                    cap_number = idx+1
                    row2_boss = " • "+str(cap_number)+"-2 (Boss node)"
                    map_row2.append(row2_boss)
                else:
                    map_row2.append("")
            map_row3 = []
            for idx, cap3 in enumerate(map3):
                if cap3 == "background-color:LightGreen" or cap3 == "background-color:PaleGreen":
                    cap_number = idx+1
                    row3 = " • "+str(cap_number)+"-3"
                    map_row3.append(row3)
                elif cap3 == "background-color:LemonChiffon" or cap3 == "background-color:LightYellow":
                    cap_number = idx+1
                    row3_boss = " • "+str(cap_number)+"-3 (Boss node)"
                    map_row3.append(row3_boss)
                else:
                    map_row3.append("")
            map_row4 = []
            for idx, cap4 in enumerate(map4):
                if cap4 == "background-color:LightGreen" or cap4 == "background-color:PaleGreen":
                    cap_number = idx+1
                    row4 = " • "+str(cap_number)+"-4"
                    map_row4.append(row4)
                elif cap4 == "background-color:LemonChiffon" or cap4 == "background-color:LightYellow":
                    cap_number = idx+1
                    row4_boss = " • "+str(cap_number)+"-4 (Boss node)"
                    map_row4.append(row4_boss)
                else:
                    map_row4.append("")
            mp_list = [map_row1, map_row2, map_row3, map_row4]
            #print(mp_list)

            try:
                map_cap1 = [idx[0] for idx in mp_list]
                map_cap2 = [idx[1] for idx in mp_list]
                map_cap3 = [idx[2] for idx in mp_list]
                map_cap4 = [idx[3] for idx in mp_list]
                map_cap5 = [idx[4] for idx in mp_list]
                map_cap6 = [idx[5] for idx in mp_list]
                map_cap7 = [idx[6] for idx in mp_list]
                map_cap8 = [idx[7] for idx in mp_list]
                map_cap9 = [idx[8] for idx in mp_list]
                map_cap10 = [idx[9] for idx in mp_list]
                map_cap11 = [idx[10] for idx in mp_list]
                map_cap12 = [idx[11] for idx in mp_list]
                map_cap13 = [idx[12] for idx in mp_list]
                all_cap1 = " • Cap 1" if "" not in map_cap1 else ""
                all_cap2 = " • Cap 2" if "" not in map_cap2 else ""
                all_cap3 = " • Cap 3" if "" not in map_cap3 else ""
                all_cap4 = " • Cap 4" if "" not in map_cap4 else ""
                all_cap5 = " • Cap 5" if "" not in map_cap5 else ""
                all_cap6 = " • Cap 6" if "" not in map_cap6 else ""
                all_cap7 = " • Cap 7" if "" not in map_cap7 else ""
                all_cap8 = " • Cap 8" if "" not in map_cap8 else ""
                all_cap9 = " • Cap 9" if "" not in map_cap9 else ""
                all_cap10 = " • Cap 10" if "" not in map_cap10 else ""
                all_cap11 = " • Cap 11" if "" not in map_cap11 else ""
                all_cap12 = " • Cap 12" if "" not in map_cap12 else ""
                all_cap13 = " • Cap 13" if "" not in map_cap13 else ""

                cap1 = "".join(map(str, map_cap1)) if all_cap1 == "" else all_cap1
                cap2 = "".join(map(str, map_cap2)) if all_cap2 == "" else all_cap2
                cap3 = "".join(map(str, map_cap3)) if all_cap3 == "" else all_cap3
                cap4 = "".join(map(str, map_cap4)) if all_cap4 == "" else all_cap4
                cap5 = "".join(map(str, map_cap5)) if all_cap5 == "" else all_cap5
                cap6 = "".join(map(str, map_cap6)) if all_cap6 == "" else all_cap6
                cap7 = "".join(map(str, map_cap7)) if all_cap7 == "" else all_cap7
                cap8 = "".join(map(str, map_cap8)) if all_cap8 == "" else all_cap8
                cap9 = "".join(map(str, map_cap9)) if all_cap9 == "" else all_cap9
                cap10 = "".join(map(str, map_cap10)) if all_cap10 == "" else all_cap10
                cap11 = "".join(map(str, map_cap11)) if all_cap11 == "" else all_cap11
                cap12 = "".join(map(str, map_cap12)) if all_cap12 == "" else all_cap12
                cap13 = "".join(map(str, map_cap13)) if all_cap13 == "" else all_cap13

                cap_list = cap1+cap2+cap3+cap4+cap5+cap6+cap7+cap8+cap9+cap10+cap11+cap12+cap13
            except IndexError:
                cap_list = " "

            #print(cap_list)
            #----------------------------------------------------------------------------------------------------
            add_info = []
            for td in divs.find_all("td", {"style": "text-align:left"}):
                text_td = td.text
                if text_td:
                    text_td = text_td.replace("  "," ")
                    add_info.append(text_td.replace("\n", ""))
                a_td = td.find_all("a")
                for a in a_td:
                    a_string = a.string
                    if a_string:
                        add_info.append(a_string.strip())

            #print(add_info)
            #----------------------------------------------------------------------------------------------------
            # Check if ship is limited
            limited = "no"

            light = ""
            heavy = ""
            special =""
            exchange = ""
            collection = ""
            limited_build = ""

            if td_style_build:
                if td_style_build[3] == "background-color:LemonChiffon":
                    limited = "sì"
            #----------------------------------------------------------------------------------------------------
                # Build: Light | Heavy | Special
                if td_style_build[0] in ("background-color:lightgreen", "background-color:LemonChiffon"):
                    light = "Build: Light | "
                if td_style_build[1] in ("background-color:lightgreen", "background-color:LemonChiffon"):
                    heavy = "Build: Heavy | " if light == "" else "Heavy | "
                if td_style_build[2] in ("background-color:lightgreen", "background-color:LemonChiffon"):
                    if light == "" and heavy == "":
                        special ="Build: Special | "
                    else:
                        special ="Special | "
                # Exchange
                if td_style_build[4] == "background-color:lightgreen":
                    exchange = " Exchange |"

            build_info = light + heavy + special
            
            if nome != "/Akashi":
                raw_collection = add_info[0].replace("Awarded and unlocked in construction when", "Ricompensa per aver raggiunto l'obiettivo in Colletion:\n") \
                                if [s for s in add_info if "Collection" in s] else None

                if raw_collection:
                    if raw_collection.startswith("Ricompensa"):
                        # Remove 'Collections...' or 'Collection...'
                        collection_text = raw_collection.replace(" Collections goal is met by getting ", "").replace(" Collection goal is met by getting ", "")+"\nIn seguito sarà disponibile in " # + build_info
                    else:
                        collection_text = raw_collection.replace(" Collection goal is met using the following ships: ", "max limit-break di ")+".\nIn seguito sarà disponibile in " # + build_info
                
                    # Clean 'collection_text'
                    collection = collection_text.replace("CN/EN: ", "") if collection_text.startswith("CN/EN") else collection_text.replace(" star rating in ", " ottenute facendo il limit-break alle ")
            else:
                collection = "Ricompensa per aver completato la Questline di Akashi.\nIn seguito sarà disponibile in " # + build_info



            # Monthly Login Reward
            login_mensile = "Ricompensa login mensile | " if [s for s in add_info if "Monthly login reward" in s] else ""
            
            # Check if ship 'Faction' is 'Universal'
            bulin = "Ricompensa login | Missioni settimanali | Eventi | Shop | Exchange" if nazionalità == "Universal" else ""
            
            # Check if ship 'Construction Time' is 'Research'
            research_text = "Research" if tempo == "Research" else ""

            # Check if ship is 'Unreleased'
            unreleased_text = "Non disponibile" if tempo == "Unreleased" else ""

            if research_text:
                limited_build = research_text
            if unreleased_text:
                limited_build = unreleased_text
            if limited == "sì" and add_info:
                limited_build = f"Event Build: {add_info[0]} "

            # Obtainment text
            acquisizione = bulin + login_mensile + collection + limited_build + build_info + exchange
            acquisizione__drop = acquisizione + "\nDrop:"+cap_list

            # Check if ship drop is available
            acquisizione = acquisizione__drop if len(cap_list) > 2 else acquisizione

            if acquisizione:
                # Fetch more info
                if len(acquisizione) == len(build_info + exchange):
                    acquisizione = build_info + add_info[0] if add_info else build_info
            else:
                try:
                    acquisizione = add_info[0]
                except Exception:
                    acquisizione = "Nulla di particolare"

            #print(acquisizione)
    #----------------------------------------------------------------------------------------------------
            collab = "no"
            if nome in collab_ships:
                collab = "sì"
    #----------------------------------------------------------------------------------------------------
            # Creazione database
    #----------------------------------------------------------------------------------------------------
            ship = {
                nome_nave_lower: {
                    "artista": artista,
                    "doppiatrice": doppiatrice,
                    "link_doppiatrice": link_doppiatrice,
                    "nome_nave": nome_nave,
                    "rarità": rarità,
                    "tempo": tempo,
                    "retrofit": retrofit,
                    "nazionalità": nazionalità,
                    "abbreviazione": abbreviazione,
                    "classe": classe,
                    "tipo": "__[%s]__"%tipo,
                    "id": id_nave,
                    "colore_embed": colore_embed,
                    "acquisizione": acquisizione,
                    "limited": limited,
                    "collab": collab,
                    "wiki_nave": [
                        wiki + nome_nave_url, #wiki
                        icona_nave, #icona
                        img_nazione, #nazione
                        img_nave, #immagine
                    ],
                    "efficienza": [
                        efficienza1,
                        efficienza2,
                        efficienza3,
                    ],
                    "rank": [
                        lb1,
                        lb2,
                        lb3,
                        lb4,
                        lb5,
                        lb6,
                    ],
                    "skill": [
                        #1
                        nome_skill1 + " " + colore1 + skill1,
                        #2
                        nome_skill2 + " " + colore2 + skill2,
                        #3
                        nome_skill3 + " " + colore3 + skill3,
                        #4
                        nome_skill4 + " " + colore4 + skill4,
                        #5
                        nome_skill5 + " " + colore5 + skill5,
                    ],
                    "skin": skin_list,
                },
            }

    #----------------------------------------------------------------------------------------------------
            json_object = json.dumps(ship, indent=4)
            
            with open((join("file_niizuki", "mydatabase.json")), "a+") as outfile:
                outfile.write(json_object)
    #----------------------------------------------------------------------------------------------------
        except Exception:
            print(traceback.format_exc(), main_url, sep="\n")

    # Fix data format
    lines = []
    replacements = {"    }": "    },", "}{":     ""}
    with open((join("file_niizuki", "mydatabase.json"))) as infile:
        for line in infile:
            for x, y in replacements.items():
                line = line.replace(x, y)
            if not line.isspace():
                lines.append(line)
    with open((join("file_niizuki", "mydatabase.json")), "w") as f:
        lines[-2] = lines[-2].rstrip().replace(",", "")
        for line in lines:
            f.write(line)

if __name__ == '__main__':
    from pathlib import Path
    path = Path(__file__)
    os.chdir(path.parents[2])

    aggiorna_database()