from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pydoc import *
import webbrowser as wb


#Above this note are the things we will need for my program
#Just some simple packages for Python to make Widgets and GUIs


#This will assign Tkinter as root, It will come in handy later
root = Tk()



################################################################
################################################################
#############Before We dive into the program####################
#####I would like to reccommend you skim through real quick#####
##And Collapse all Functions before going through to view them##
###You will also need to assign the path to the text document###
############And the image, included with the code###############
################################################################
################################################################

















##################################################
##################################################
##################################################
##################################################
##################################################

def DataBut():
    T = Toplevel()
    T.title('Champion Counters and Data')
    T.geometry('400x200')
    
    def AatroxInfo():
        messagebox.showinfo('Aatrox','Aatrox is an AD champion. \nUsually a top laner, he may also be played in the jungle. \n \nHis counters are Jax, Riven, and Teemo. \n \nAdditionally Try to kill him when his resource bar is low, as this will make him revive with much lower health.')
    def AhriInfo():
        messagebox.showinfo('Ahri', 'Ahri is a Mage, thus an AP champion. \nYou will generally only see her in the mid lane, though be mindful of her roaming, as her charm is very strong for early ganks. \n \nHer counter are Leblanc, Swain, and Diana. \n \nYou should try to stay behind minions to prevent yourself from getting Charmed.')
    def AkaliInfo():
        messagebox.showinfo('Akali','Akali is a hybrid champion, Meaning she may play AP or AD. \nKeep a close eye on her buys, as to shut her down \n Her primary lane is mid, but may be seen top \n \n Her counters are Lee Sin, Annie, and Diana \n \nPost level 6, try to prevent her use of Mark of the Assassin, as she can proc it twice using her dashes')
    def AliInfo():
        messagebox.showinfo('Alistar','Ali is a flex Champion, you will usually see him with an AP Support build however. \n \nHis counters are Janna, Vayne, and Tristana. \n \nDont stand too close to enemy tower when pushing so that Alistar wont be able to use Flash pulverize into headbutt combo.' )
    def AmumuInfo():
        messagebox.showinfo('Amumu','Amumu is a Magical Damage Champ \nMost often played in the jungle, he may suprise you with his tanky health. \n \nHis counters are Shyvana, Lee Sin, and Shaco. \n \nBe sure to try to not bunch up in a team fight, as you will be punished by his AOE CC Ultimate.')
    def AniviaInfo():
        messagebox.showinfo('Anivia','Anivia is a Mid lane Mage so AP champion. \n \nHer counters are Fizz, Kassadin, and Diana. \n \nWhen facing her, try to punish her when she misses her stun, and avoid fightning in small paths such as the jungle. \nShe will use her wall + AOE to cheese the fight.')
    def AnnieInfo():
        messagebox.showinfo('Annie','Annie is a AP mage \nYou will see her mostly mid lane, but may also work in the bot lane. \n \nHer counters are Brand, Sion, and Oriana \n \nDo your best to keep distance when her stun is up, and try to keep a close eye on her passive stacks as she can land a suprise stun with her E.')
    def AsheInfo():
        messagebox.showinfo('Ashe','Ashe is an AD archer \nShe is a fighter, and will be seen in the bot lane as an ADC \n \nHer counters are Ezreal, Draven, and Graves \n \nWhen facing her play aggressively in lane against her, because her Volley has a really long cooldown at earlier levels.')
    def SolInfo():
        messagebox.showinfo('Aurelion Sol','Aurelion Sol is an AP Mage. \nHe is a Mid laner. \n \nHis Coutners are Yasuo, Zed, and Zoe. \n \nIf you happen to face an Aurelion Sol Be sure to manage a good distance between his stars, Try to put him under tower and apply pressure, Sol loves to roam, so try to deny that by having him lose waves when he does.')
    def AzirInfo():
        messagebox.showinfo('Azir', 'Azir is an AD assassin \nMost often you will see him mid, but he also sees play top as well. \n \nHis counters are Ziggs, Talon, and Syndra \n \nAzir has to get close for his ultimate to be effective. If hes dashing into a dangerous situation, you can assume hes about to ult.')
    def BardInfo():
        messagebox.showinfo('Bard','Bard is a Magic support character \nHe will only be seen beside his bot laner, as a support. \n \nHis counters are Morgana, Sivir, and Teemo \n \nWhen facing a bard you shouldnt have much trouble, a good tip however is to stay away from groups of minions, so he can not stun you')
    def BlitzInfo():
        messagebox.showinfo('Blitzcrank','Blitz is a AP tanky mage \nBlitz is a support thus he will be seen in the bot lane. \n \nHis counters are Leona, Alistar, and Morgana \n \nBlitz can be a tough bot to crack, positioning is your enemy in this fight. Try to stay behind minions to avoid his hook, and punish him when he misses')
    def BrandInfo():
        messagebox.showinfo('Brand','Brand is a hard hitting AP mage \nThough for a long time seen in the mid lane, his most often played lane today is Support, both are potent. \n \nHis counters are Kassadin, Fizz, and Galio \n \nBrand can be tough to counter, the best thing you can do is run away from the initial target that brand uses his ultimate on. \nIf you are playing support, be sure to stay away from your adc, as you could kill him after brand ults you.')
    def BraumInfo():
        messagebox.showinfo('Braum','Braum is a tank support \nNowadays you will see him support, but he may be seen top as well. \n \nHis counters are Morgana, Zyra, and Leona \n \nBraum must land winters bite or a basic attack to start concussive blows. If you et marked, exit combat range BEFORE getting hit 3 more times to avoid the stun')
    def CaitlynInfo():
        messagebox.showinfo('Caitlyn','Caitlyn is a AD sniper adc \nCaitlyn is a bot laner, AD carry- With a lot of range \n \nHer Counters are Siver, Jinx, and Varus \n \nWhen facing a caitlyn try your best to stay behind minions so her Piltover Peacemaker will do less damage, additionally her Ult can be blocked by a teamate standing in its path.')
    def CamilleInfo():
        messagebox.showinfo('Camille','Camille is an AD swiss army knife assassin \nHer most frequent role is in the top but she sees jungle play as well. \n \nHer counters are Garen, Teemo, and Poppy \n \nCamille doesnt get a power spike at level 6, as soon as you get your ult you should initiate a fight before she can scale up')
    def CassInfo():
        messagebox.showinfo('Cassiopeia','Cassie is an AP mage \nShe is a magic damage mid laner \n \nHer coutners are Galio, Oriana, and Lux \n \nWhile fighting her, try to turn around when you see her ultimate being cast as to avoid the stun.')
    def ChoInfo():
        messagebox.showinfo('ChoGath','Cho is a tanky mage \nCho is a tank, often seen top, however he may be seen in the jungle and mid. \n \nHis counters are KogMaw, Warwick, and Vayne \n \nDodging his rupture by turning back shortly will let you escape him easily, try to kill him early so he wont be able to get his feast stacks as well.')
    def CorkiInfo():
        messagebox.showinfo('Corki','Corki is an AD hybrid bot laner \n \nHis coutner are Caitlyn, LeBlanc, and Draven \n \nTry to avoid extended fights because his gatling gun will rip through armor, additionally try to stop him from backing in lane, as this will immensly help you as his abilities cost a lot of mana')
    def DariusInfo():
        messagebox.showinfo('Darius','Darius is an AD bruiser \n \nHis primary lane is Top but he is often seen in the jungle as well \n \nHis coutners are Yorick, Kayle, and Jayce \n \nOnce his Apprehend is on CD he is incredibly easy to kite, also try to deny his reset on his ult with a sheild or heal, this significantly lowers his damage output in teamfights.')
    def DianaInfo():
        messagebox.showinfo('Diana', 'Diana is an AP mage assassin \nShe is most often seen Mid, but sees play in the jungle and top as well \n \nHer counters are Mordekaiser, ChoGath, and Heimerding \n \nDidging her Crescent Strike will lower her damage output significantly post level 6.')
    def MundoInfo():
        messagebox.showinfo('Dr.Mundo','Mundo is a AD Fighter \nHis most seen lane is Top, but sees nearly as much play in the jungle as well \n \nHis counters are KogMaw, Olaf, and Trundle \n \nIgnite significantly lowers Mundos Health regen from his passive and Ult, If he cant be bursted by your team when he turns on his ult, ignore him until it end.')
    def DravenInfo():
        messagebox.showinfo('Draven','Draven is the classic AD Fighter \nDraven is an all around ADC bot laner \n \nHis counters are Varus, Thresh, and Blitz \n \nTry to Punish draven for moving to catch axes with a skillshot, or CC from a support. If you can stop a catch this will drop his damage output considerably.')
    def Ekko():
        messagebox.showinfo('Ekko','Ekko is an AP fighter class \nHe is primarily a mid/jungler, though you may see tank ekko top. \n \nHis counters are LeBlanc, Diana, and Xin Zhao \n \nWhen Ekko is low on hp and you feel he is about to ultimate, ignite him. This will lower the heal. Also be mindful that Ekkos timewinder, does more damage on the way back.')
    def Elise():
        messagebox.showinfo('Elise','Elise is AP mage. \nThouh she can be played Mid, Top, And even bot, you will likely see her jungling. \n \nHer counters are Kassadin, Wukong, and Yorick \n \nTry to stay behind minions so that she wont be able to stun you. If elise uses Rappel to enter a teamfight, focus her- Rappel is her only escape ability.')
        
    def Evelynn():
        messagebox.showinfo('Evelynn','Evelynn is another hybrid champ, so watch whether she stacks ap or ad \nShe can be played mid lane, though you will more often see her jungle. \n \nHer counters are Ryze, RakSai, and Twisted Fate. \n \nEvelynn is vulnerable to slows after she uses her dark frenzy. Additionally her power spike is at levels 3 and 6, so watch for ganks around these times.')
    def Ezreal():
        messagebox.showinfo('Ezreal','Ezreal can be played both AP and AD \nHe is a very strong Bot lane bully, though he is squishy. \n \nHis counters are Draven, Graves, and Miss Fortune \n \nTtry to focus him if he uses his arcane shift to enter a fight. His wave clear is poor, so harrass to gain a Creep advantage.')
    def Fiddlesticks():
        messagebox.showinfo('Fiddlesticks','Fiddle is an AP mage \nFiddle makes for an oppressive support, but may be played Mid and Jungle as well \n \nHis counters are Janna, Kassadin, and Evelynn \n \nUsing a stun-knockup-displacement- or silence will stop his ultimate if he is channeling. When facing fiddle never stand close to your teamate unless, you are near creeps to prevent damage from his crows')
    def Fiora():
        messagebox.showinfo('Fiora','Fiora is an AD fighter \nShe will often be seen Top, but watch out for her in the jungle as well \n \nHer counters are Jax, Pantheon, and Darius \n \nAttempt to punish her when her Lunge is on cooldown, which is her main mobility skill.')
    def Fizz():
        messagebox.showinfo('Fizz','Fizz is an ApP Fighter \nMost notable for his Mid gameplay, fizz can be seen top as well \n \nHis counters are Ryze, Kayle, and Lissandra \n \nMake sure to focus him after he uses playful/trickster to enter a fight, and avoid staying in lane with low health. His trident will deal greater damage to lower health targets.')
    def Galio():
        messagebox.showinfo('Galio','Galio is an AP tank \nHe sees play in both Mid and Top lane \n \nHis counters are Udyr, Akali, and Braum \n \nDont clump together so Galio wont be able to use flash and his ult combo to CC your team.')
    def Gangplank():
        messagebox.showinfo('Gangplank','Gangplank is an AD fighter \nHis primary lane is Top but may jungle as well \n \nHis counters are Pantheon, Fiora, and Poppy \n \nBuying early armor is very effective against gangplank, as it will lower the damage from his parrrley and auto attacks.')
    def Garen():
        messagebox.showinfo('Garen','Garen is the classic AD fighter \nHe is a Top lane bruiser \n \nHis couters are Teemo, Gnar, and Yorick \n \nAlways avoid staying in lane with low health, Garens Ultimate will dela massive damage to lower heath targets.')
    def Gnar():
        messagebox.showinfo('Gnar','Gnar is another tanky AD fighter \nYou should only expect him top lane \n \nHis counters are Pantheon, Wukong, and Nidalee \n \nALWAYS keep an eye on his rage bar. If you arent careful, he can hop on a minion and transform on you dealing massive burst damage. ')
    def Gragas():
        messagebox.showinfo('Gragas','Gragas, is an AP brute \n He may be seen Top, Jungle, and even mid \n \nHis counters are Yasuo, Ahri, and Leblanc \n \nHis Ult is extremely strong against grouped up champs- so avoid being clumped together.')
    def Graves():
        messagebox.showinfo('Graves','Graves is an AD fighter. \nYou will only see him as an adc bot lane role. \n \nHis counters are Caitlyn, Sivir, and Corki \n \nHis auto attack range is quite low, so picking close range ap carries will pressure graves to not sit in auto range during teamfights. Abuse long range, adc and skillshots for harrass.')
    def Hecarim():
        messagebox.showinfo('Hecarim','Hecarim is a AD Fighter \nThough most destructive in the jungle, Hecarim can be seen top as well \n \nHis counters are Nasus, Aatrox, and Sejuani \n \nAvoid staying bunched up so he wont be able to use his ultimate to fear multiple people.')
    def Heimerdinger():
        messagebox.showinfo('Heimerdinger','Heimer is an AP mage \nYou should only expect him to be in mid lane \n \nHis counters are Syndra, Malzahar, and Xerath \n \nKilling his turrets first when cast will generate lower damage output from the heimerdinger. avoid the center of his grenades as well, as it will stun you instead of a blind.')
    def Illaoi():
        messagebox.showinfo('Illaoi','Illaoi is an Ap fighter/tank \nShe will most often be seen Top \n \nHer counters are Lulu, Tryndamere, and Vayne \n \nAvoid standing close to the tentacle she spawn as she is likely to use this chance to use her W and case them to hit you- VERY HARD -.')
    def Irelia():
        messagebox.showinfo('Irelia','Irelia is an AD assassin \nShe is a deadly force in the top lane. \n \nHer counters are Olaf, Garen, and Udyr \n \nAttach speed reduction is expremely strong against ireleia, which lessens the effectiveness of her Hiten Styles active.')
    def Ivern():
        messagebox.showinfo('Ivern','Ivern is an AP champion \nThough you will often never see an iver, when you do \nHe will be playing either Jungle or Support \n \nHis counters are Illaoi, Graves, KhaZix, and the lack of a fanbase \n \nIf in the instance you do encounter an Ivern, make sure to check his bushes with skillshots, and stay away from them as melee. \nIvern receives a damage increase when inside the bush.')
    def Janna():
        messagebox.showinfo('Janna','Janna is an AP  Support \nYou will only see her playing support in the bot lane \nSome fringe builds allow her to mid as well \n \nHer counters are Sona, Nami, and Zyra \n \nIn lane, if she shields herself, it leaves her carry more open to being killed, or harrassed, capitalize.')
    def JarvanIV():
        messagebox.showinfo('Jarvan IV','Jarvan is an AD Tank \nMost often played jungle he may be played top as well \n \nHis counters are Yorick, Pantheon, and Jax \n \nDisplacement/Dash/Jump abilities will let you leap out of his Ultimate early.')
    def Jax():
        messagebox.showinfo('Jax','Jax is a Hypbrid Fighter, watch his build \nJax may be seen Top, and Jungle \n \nHis counter are Malphite, Pantheon, and Singed \n \nAvoid attacking him when he turns on hsi counterstrike, to negate unnecessary damage.')
    def Jayce():
        messagebox.showinfo('Jayce','Jayce is an Ad fighter \nThough able to play other lanes, you should only see him Top \n \nHis counters are Yorick, Fiora, and Xin Zhao \n \nKepp your distance behind minions to avoid being hit by his long range poke.')
    def Jhin():
        messagebox.showinfo('Jhin','Jayce is an AD assassin \nYou should only see him ADC in the bot lane \n \nHis counters are Lucian, Miss Fortune, and Vayne \n \nKeep in mind every 4th shot he fires WILL crit, which grants him a short burst of speed, after the 4th shot however, he need to reload, take advantage of this and burst him.')
    def Jinx():
        messagebox.showinfo('Jinx','Jinx is an AD fighter \nThough able to play mid, she will likely be seen bot \n \nHer counters are Ezreal, Corki, and Sivir \n \nHer base auto attack range is low in minigun stnace, which makes her easier to harass.')
    def KaiSa():
        messagebox.showinfo('KaiSa','Kaisa is an AP assassin \nShe will often be seen bot lane \n \nHer counters are Caitlyn, Miss Fortune, and Aatrox \n \nWhen in lane, abuse KaiSas short auto attack range by pokeing when she tries to move forward to CS. ')
    def Kalista():
        messagebox.showinfo('Kalista','')
    def Karma():
        messagebox.showinfo('Karma','')
    def Karthus():
        messagebox.showinfo('Karthus','')
    def Kassadin():
        messagebox.showinfo('Kassadin','')
    def Katarina():
        messagebox.showinfo('Katarina','')
    def Kayle():
        messagebox.showinfo('Kayle','')
    def Kayn():
        messagebox.showinfo('Kayne','')
    def Kennen():
        messagebox.showinfo('Kennen','')
    def KhaZix():
        messagebox.showinfo('KhaZix','')
    def Kindred():
        messagebox.showinfo('Kindred','')
    def Kled():
        messagebox.showinfo('Kled','')
    def KogMaw():
        messagebox.showinfo('KogMaw','')
    def LeBlanc():
        messagebox.showinfo('LeBlanc','')
    def LeeSin():
        messagebox.showinfo('LeeSin','')
    def Leona():
        messagebox.showinfo('Leona','')
    def Lissandra():
        messagebox.showinfo('Lissandra','')
    def Lucian():
        messagebox.showinfo('Lucian','')
    def Lulu():
        messagebox.showinfo('Lulu','')
    def Lux():
        messagebox.showinfo('Lux','')
    def Malphite():
        messagebox.showinfo('Malphite','')
    def Malzahar():
        messagebox.showinfo('Malzahar','')
    def Maokai():
        messagebox.showinfo('Maokai','')
    def MasterYi():
        messagebox.showinfo('Master Yi','')
    def MissFortune():
        messagebox.showinfo('Miss Fortune','')
    def Mordekaiser():
        messagebox.showinfo('Mordekaiser','')
    def Morgana():
        messagebox.showinfo('Morgana','')
    def Nami():
        messagebox.showinfo('Nami','')
    def Nasus():
        messagebox.showinfo('Nasus','')
    def Nautilus():
        messagebox.showinfo('Nautilus','')
    def Neeko():
        messagebox.showinfo('Neeko','')
    def Nidalee():
        messagebox.showinfo('Nidalee','')
    def Nocturne():
        messagebox.showinfo('Nocturne','')
    def NunuWillump():
        messagebox.showinfo('Nunu + Willump','')
    def Olaf():
        messagebox.showinfo('Olaf','')
    def Orianna():
        messagebox.showinfo('Oriana','')
    def Ornn():
        messagebox.showinfo('Ornn','')
    def Pantheon():
        messagebox.showinfo('Pantheon','')
    def Poppy():
        messagebox.showinfo('Poppy','')
    def Pyke():
        messagebox.showinfo('Pyke','')
    def Quinn():
        messagebox.showinfo('Quinn','')
    def Rakan():
        messagebox.showinfo('Rakan','')
    def Rammus():
        messagebox.showinfo('Rammus','')
    def RekSai():
        messagebox.showinfo('RekSai','')
    def Renekton():
        messagebox.showinfo('Renekton','')
    def Rengar():
        messagebox.showinfo('Rengar','')
    def Riven():
        messagebox.showinfo('Riven','')
    def Rumble():
        messagebox.showinfo('Rumble','')
    def Ryze():
        messagebox.showinfo('Ryze','')
    def Sejuani():
        messagebox.showinfo('Sejuani','')
    def Shaco():
        messagebox.showinfo('Shaco','')
    def Shen():
        messagebox.showinfo('Shen','')
    def Shyvana():
        messagebox.showinfo('Shyvana','')
    def Singed():
        messagebox.showinfo('Singed','')
    def Sion():
        messagebox.showinfo('Sion','')
    def Sivir():
        messagebox.showinfo('Sivir','')
    def Skarner():
        messagebox.showinfo('Skarner','')
    def Sona():
        messagebox.showinfo('Sona','')
    def Soraka():
        messagebox.showinfo('Soraka','')
    def Swain():
        messagebox.showinfo('Swain','')
    def Syndra():
        messagebox.showinfo('Syndra','')
    def TahmKench():
        messagebox.showinfo('Tahm Kench','')
    def Taliyah():
        messagebox.showinfo('','')
    def Talon():
        messagebox.showinfo('','')
    def Taric():
        messagebox.showinfo('','')
    def Teemo():
        messagebox.showinfo('','')
    def Thresh():
        messagebox.showinfo('','')
    def Tristana():
        messagebox.showinfo('','')
    def Trundle():
        messagebox.showinfo('','')
    def Tryndamere():
        messagebox.showinfo('','')
    def TwistedFate():
        messagebox.showinfo('','')
    def Twitch():
        messagebox.showinfo('','')
    def Udyr():
        messagebox.showinfo('','')
    def Urgot():
        messagebox.showinfo('','')
    def Varus():
        messagebox.showinfo('','')
    def Vayne():
        messagebox.showinfo('','')
    def Veigar():
        messagebox.showinfo('','')
    def VelKoz():
        messagebox.showinfo('','')
    def Vi():
        messagebox.showinfo('','')
    def Viktor():
        messagebox.showinfo('','')
    def Vladimir():
        messagebox.showinfo('','')
    def Volibear():
        messagebox.showinfo('','')
    def Warwick():
        messagebox.showinfo('','')
    def Wukong():
        messagebox.showinfo('','')
    def Xayah():
        messagebox.showinfo('','')
    def Xerath():
        messagebox.showinfo('','')
    def XinZhao():
        messagebox.showinfo('','')
    def Yasuo():
        messagebox.showinfo('','')
    def Yorick():
        messagebox.showinfo('','')
    def Zac():
        messagebox.showinfo('','')
    def Zed():
        messagebox.showinfo('','')
    def Ziggs():
        messagebox.showinfo('','')
    def Zilean():
        messagebox.showinfo('','')
    def Zoe():
        messagebox.showinfo('','')
    def Zyra():
        messagebox.showinfo('','')
    def error():
        messagebox.showerror('Oops','didnt list a real character, or didnt select a champion try again')

    
        



    














































    def ClickInfo():
        selection = ChampComboBox.get()
        if selection == 'Aatrox':
            AatroxInfo()
        elif selection == 'Ahri':
            AhriInfo()
        elif selection == 'Akali':
            AkaliInfo()
        elif selection == 'Alistar':
            AliInfo()
        elif selection == 'Amumu':
            AmumuInfo()
        elif selection == 'Anivia':
            AniviaInfo()
        elif selection == 'Annie':
            AnnieInfo()
        elif selection == 'Ashe':
            AsheInfo()
        elif selection == 'AurelionSol':
            SolInfo()
        elif selection == 'Azir':
            AzirInfo()
        elif selection == 'Bard':
            BardInfo()
        elif selection == 'Blitzcrank':
            BlitzInfo()
        elif selection == 'Brand':
            BrandInfo()
        elif selection == 'Braum':
            BraumInfo()
        elif selection == 'Caitlyn':
            CaitlynInfo()
        elif selection == 'Camille':
            CamilleInfo()
        elif selection == 'Cassiopeia':
            CassInfo()
        elif selection == 'ChoGath':
            ChoInfo()
        elif selection == 'Corki':
            CorkiInfo()
        elif selection == 'Darius':
            DariusInfo()
        elif selection == 'Diana':
            DianaInfo()
        elif selection == 'DrMundo':
            MundoInfo()
        elif selection == 'Draven':
            DravenInfo()
        elif selection == 'Ekko':
            Ekko()
        elif selection == 'Elise':
            Elise()
        elif selection == 'Evelynn':
            Evelynn()
        elif selection == 'Ezreal':
            Ezreal()
        elif selection == 'Fiddlesticks':
            Fiddlesticks()
        elif selection == 'Fiora':
            Fiora()
        elif selection == 'Fizz':
            Fizz()
        elif selection == 'Galio':
            Galio()
        elif selection == 'Gangplank':
            Gangplank()
        elif selection == 'Garen':
            Garen()
        elif selection == 'Gnar':
            Gnar()
        elif selection == 'Gragas':
            Gragas()
        elif selection == 'Graves':
            Graves()
        elif selection == 'Hecarim':
            Hecarim()
        elif selection == 'Heimerdinger':
            Heimerdinger()
        elif selection == 'Illaoi':
            Illaoi()
        elif selection == 'Irelia':
            Irelia()
        elif selection == 'Ivern':
            Ivern()
        elif selection == 'Janna':
            Janna()
        elif selection == 'JarvanIV':
            JarvanIV()
        elif selection == 'Jax':
            Jax()
        elif selection == 'Jayce':
            Jayce()
        elif selection == 'Jhin':
            Jhin()
        elif selection == 'Jinx':
            Jinx()
        elif selection == 'KaiSa':
            KaiSa()
        elif selection == 'Kalista':
            Kalista()
        elif selection == 'Karma':
            Karma()
        elif selection == 'Karthus':
            Karthus()
        elif selection == 'Kassadin':
            Kassadin()
        elif selection == 'Katarina':
            Katarina()
        elif selection == 'Kayle':
            Kayle()
        elif selection == 'Kayn':
            Kayn()
        elif selection == 'Kennen':
            Kennen()
        elif selection == 'KhaZix':
            KhaZix()
        elif selection == 'Kindred':
            Kindred()
        elif selection == 'Kled':
            Kled()
        elif selection == 'KogMaw':
            KogMaw()
        elif selection == 'LeBlanc':
            LeBlanc()
        elif selection == 'LeeSin':
            LeeSin()
        elif selection == 'Leona':
            Leona()
        elif selection == 'Lissandra':
            Lissandra()
        elif selection == 'Lucian':
            Lucian()
        elif selection == 'Lulu':
            Lulu()
        elif selection == 'Lux':
            Lux()
        elif selection == 'Malphite':
            Malphite()
        elif selection == 'Malzahar':
            Malzahar()
        elif selection == 'Maokai':
            Maokai()
        elif selection == 'MasterYi':
            MasterYi()
        elif selection == 'MissFortune':
            MissFortune()
        elif selection == 'Mordekaiser':
            Mordekaiser()
        elif selection == 'Morgana':
            Morgana()
        elif selection == 'Nami':
            Nami()
        elif selection == 'Nasus':
            Nasus()
        elif selection == 'Nautilus':
            Nautilus()
        elif selection == 'Neeko':
            Neeko()
        elif selection == 'Nidalee':
            Nidalee()
        elif selection == 'Nocturne':
            Nocturne()
        elif selection == 'Nunu&Willump':
            NunuWillump()
        elif selection == 'Olaf':
            Olaf()
        elif selection == 'Orianna':
            Orianna()
        elif selection == 'Ornn':
            Ornn()
        elif selection == 'Pantheon':
            Pantheon()
        elif selection == 'Poppy':
            Poppy()
        elif selection == 'Pyke':
            Pyke()
        elif selection == 'Quinn':
            Quinn()
        elif selection == 'Rakan':
            Rakan()
        elif selection == 'Rammus':
            Rammus()
        elif selection == 'RekSai':
            RekSai()
        elif selection == 'Renekton':
            Renekton()
        elif selection == 'Rengar':
            Rengar()
        elif selection == 'Riven':
            Riven()
        elif selection == 'Rumble':
            Rumble()
        elif selection == 'Ryze':
            Ryze()
        elif selection == 'Sejuani':
            Sejuani()
        elif selection == 'Shaco':
            Shaco()
        elif selection == 'Shen':
            Shen()
        elif selection == 'Shyvana':
            Shyvana()
        elif selection == 'Singed':
            Singed()
        elif selection == 'Sion':
            Sion()
        elif selection == 'Sivir':
            Sivir()
        elif selection == 'Skarner':
            Skarner()
        elif selection == 'Sona':
            Sona()
        elif selection == 'Soraka':
            Soraka()
        elif selection == 'Swain':
            Swain()
        elif selection == 'Syndra':
            Syndra()
        elif selection == 'TahmKench':
            TahmKench()
        elif selection == 'Taliyah':
            Taliyah()
        elif selection == 'Talon':
            Talon()
        elif selection == 'Taric':
            Taric()
        elif selection == 'Teemo':
            Teemo()
        elif selection == 'Thresh':
            Thresh()
        elif selection == 'Tristana':
            Tristana()
        elif selection == 'Trundle':
            Trundle()
        elif selection == 'Tryndamere':
            Tryndamere()
        elif selection == 'TwistedFate':
            TwistedFate()
        elif selection == 'Twitch':
            Twitch()
        elif selection == 'Udyr':
            Udyr()
        elif selection == 'Urgot':
            Urgot()
        elif selection == 'Varus':
            Varus()
        elif selection == 'Vayne':
            Vayne()
        elif selection == 'Veigar':
            Veigar()
        elif selection == 'VelKoz':
            VelKoz()
        elif selection == 'Vi':
            Vi()
        elif selection == 'Viktor':
            Viktor()
        elif selection == 'Vladimir':
            Vladimir()
        elif selection == 'Volibear':
            Volibear()
        elif selection == 'Warwick':
            Warwick()
        elif selection == 'Wukong':
            Wukong()
        elif selection == 'Xayah':
            Xayah()
        elif selection == 'Xerath':
            Xerath()
        elif selection == 'XinZhao':
            XinZhao()
        elif selection == 'Yasuo':
            Yasuo()
        elif selection == 'Yorick':
            Yorick()
        elif selection == 'Zac':
            Zac()
        elif selection == 'Zed':
            Zed()
        elif selection == 'Ziggs':
            Ziggs()
        elif selection == 'Zilean':
            Zilean()
        elif selection == 'Zoe':
            Zoe()
        elif selection == 'Zyra':
            Zyra()                
        else:
            error()
        
            


    ChampComboBox = ttk.Combobox(T, values=Champs)
    ChampComboBox.pack()
    T_Button = Button(T, text='Submit', bg='black', fg='white', command=ClickInfo)
    T_Button.pack()



    
    

    
    









#So The first thing i chose to do was to set up a list
#This will be to index every Champion in league


Champs = []

#I decided to use a text file, as this would be faster than
#Putting every champion into the list individually
#This also means i can update the text document
#As champions are added to the game








#Right here we display execution of importing a file, by means of the open function
with open('ChampionsFolder.txt') as f:
    for line in f:
        line = line.split()
        Champs.append(line)
    
















#This chunk of text is just an intoduction for the programs
#Various Functions
print('This is your all in one League of legends helper/Teambuilder \n \n')
print('I can show you the current best pick champions in each roll \n')
print('Im also equiped with a Ban helper, that functions well as a counter picker \n \n')
print('FOR EACH ROLE!!! \n \n \n')
print('Go ahead and see all of my tools for yourself!')










#Now i assigned a print function to the Champion list
#To execute upon users need, as not to flood our terminal
def ShowChampions():
    print('\n \n \nHere are all the champions in leauge\n \n \n',Champs, '\n \n \n')













#Now we dive into tkinter
#This will assign a name to a picture of my choice
Map =  PhotoImage(file='MAP.png')


#And this will convert that image into a label


MAP_label = Label(root, image=Map)
#The extra parameters allow the window to be resized


MAP_label.place(x=0, y=0, relwidth=1, relheight=1)

#This will make our window title name, and how large the window is
root.title('League of Legends Helper')
root.geometry('640x455')


#Before anything i needed lists for each role in league, to help me later
T_lane = []
Jung = []
M_lane = []
B_lane = []
Pansy =  []















#Now to assign a team class
#This will make automating certain functions a breeze
class Team:
    def __init__(self, Top, Mid, Bot, Jungle, Support):
        self.Top = Top
        self.Mid = Mid
        self.Bot = Bot
        self.Jungle = Jungle
        self.Support = Support
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)






















#Okay so next up was to get a solid base of functions
#These functions will be used to assign to buttons
#That only execute upon pressing them
def clickSelect1():
    #Toplevel opens a new window we will make the function T for short
    T = Toplevel()
    #Now for a Title and window size
    T.title('Select your champion')
    T.geometry('300x100')
    #Next a little explanation, Like the picture of the map
    #I made a label, this time instead of root (out main window)
    #I went ahead as to only assign it for our Toplevel
    T_lab = Label(T, text='Choose a champ and press submit')
    T_lab.pack()
    #okay, now i needed another function
    #This function is for a button only native to my Toplevel
    #upon it's press we will append a value
    #from the combo box within the Toplevel

    def click1():
        Top = ChampComboBox.get()
        print('\n \nYour Top Laner is:   ', Top)
        T_lane.append(Top)
        T.destroy()
    #But What is a combo box?
    #The combobox is a neat tool or widget in Tkinter
    #that essentially equates to a dropdown menu
    #Let's see how it works
    ChampComboBox = ttk.Combobox(T, values=Champs)
    #Assign a name to the box
    #assign where it is going to be (TopLevel)
    #And what options are available (Champs or the list we made from the text file)    
    ChampComboBox.pack()
    #Now we get to the cool stuff, My button
    #first we needed a button itself, and where to put it (T)
    #then give it a cool color
    #and finally assign a command to it, or fucntion, (in this case The Click1)
    T_Button = Button(T, text='Submit', bg='black', fg='white', command=click1)
    T_Button.pack()
#The rest of these are all just alterations of clickSelect1
#To Cater for each roll
def clickSelect2():
    T = Toplevel()
    T.title('Select your champion')
    T.geometry('300x100')
    T_lab = Label(T, text='Choose a champ and press submit')
    T_lab.pack()
    def click2():
        JG = ChampComboBox.get()
        print('\n \nYour Jungler is:   ', JG)
        Jung.append(JG)
        T.destroy()
       
    ChampComboBox = ttk.Combobox(T, values=Champs)
    ChampComboBox.pack()
    T_Button = Button(T, text='Submit', bg='black', fg='white', command=click2)
    T_Button.pack()

def clickSelect3():
    T = Toplevel()
    T.title('Select your champion')
    T.geometry('300x100')
    T_lab = Label(T, text='Choose a champ and press submit')
    T_lab.pack()
    def click3():
        Mid = ChampComboBox.get()
        print('\n \nYour Mid Laner is:   ', Mid)
        M_lane.append(Mid)
        T.destroy()
       
    ChampComboBox = ttk.Combobox(T, values=Champs)
    ChampComboBox.pack()
    T_Button = Button(T, text='Submit', bg='black', fg='white', command=click3)
    T_Button.pack()

def clickSelect4():
    T = Toplevel()
    T.title('Select your champion')
    T.geometry('300x100')
    T_lab = Label(T, text='Choose a champ and press submit')
    T_lab.pack()
    def click4():
        Bot = ChampComboBox.get()
        print('\n \nYour Bot Laner is:   ', Bot)
        B_lane.append(Bot)
        T.destroy()
       
    ChampComboBox = ttk.Combobox(T, values=Champs)
    ChampComboBox.pack()
    T_Button = Button(T, text='Submit', bg='black', fg='white', command=click4)
    T_Button.pack()

def clickSelect5():
    T = Toplevel()
    T.title('Select your champion')
    T.geometry('300x100')
    T_lab = Label(T, text='Choose a champ and press submit')
    T_lab.pack()
    def click5():
        Support = ChampComboBox.get()
        print('\n \nYour Support is:   ', Support)
        Pansy.append(Support)
        T.destroy()
        
        
       
    ChampComboBox = ttk.Combobox(T, values=Champs)
    ChampComboBox.pack()
    T_Button = Button(T, text='Submit', bg='black', fg='white', command=click5)
    T_Button.pack()
   

















#Now to give our application a little more beef i needed to flesh it out more
#So i went ahead and made another function
#This time to creat a seperate Toplevel from all of the clickSelects

#Let's check it out
def TierList():
    #Much like the clickSelect
    #I went ahead and made a Toplevel
    T = Toplevel()

    #This time with a new name, and window size

    T.title('League Tier List')
    T.geometry('300x300')

    #Again just a simple label, to describe what to do, and telling it where to be
    Tier_Label = Label(T, text='Select a role')
    #Unlike the other, we packed this widget to the top
    #normally as i've found pack just puts it in the first available space
    #however we can manipulate it in various ways
    #here is just one of them
    Tier_Label.pack(side=TOP)


    #Next I went ahead and made individual functions
    #For each role to display a messagebox
    #Think like an alert window

    def TopTier():
        messagebox.showinfo('Top Tier List', 'The best Top laners are \nViktor \nJax \nRiven \nCamille \nPantheon')
    def JGTier():
        messagebox.showinfo('Jungle Tier List','The best Junglers are \nKhaZix \nShaco \nJax \nKayn \nRammus')
    def MidTier():
        messagebox.showinfo('Mid Tier List','The best Mid laners are \nAhri \nTwisted Fate \nKarthus \nKassadin \nKatarina')
    def BotTier():
        messagebox.showinfo('Bot Tier List','The best Bot laners are \nLucian \nKarthus \nDraven \nMiss Fortune \nHeimerdinger')
    def SuppTier():
       messagebox.showinfo('Support Tier List','The best Supports are \nZyra \nSona \nBrand \nBard \nZilean')
    
    #You will see me use a similar fucntion to this next one
    #In alot of my other TopLevels
    #It Simply closes the window upon activation
    #This way we can make a close window button

    def closeTier():
        T.destroy()

    #Finally I made a bunch of buttons to assign our different functions to
    buttonClose = Button(T, text='Close', bg='black', fg='white', command=closeTier)
    buttonTop = Button(T, text='Top', bg="green", fg='black', command=TopTier)
    buttonJG = Button(T, text='Jungle', bg="blue", fg='black', command=JGTier)
    buttonMid = Button(T, text='Mid', bg="purple", fg='black', command=MidTier)
    buttonBot = Button(T, text='Bot', bg="red", fg='black', command=BotTier)
    buttonSupp = Button(T, text='Support', bg="pink", fg='black', command=SuppTier)
    buttonTop.place(x=0, y=135)
    buttonJG.place(x=60, y=135)
    buttonMid.place(x=140, y=135)
    buttonBot.place(x=200, y=135)
    buttonSupp.place(x=250, y=135)
    buttonClose.place(x=130, y=275)





















    




























#Now for the bread and butter
#First we need a list of champions to ban
#based on each character on our team
BanList = []

#Next we needed a means for Python
#To check each and every one of our Team members Champions
#So let's see how i did it all with 1 function

#Collapse will help navigate, ill skip toward the end though with another brick of #'s to help you search through the function

def LockIn():
    #After our user builds his team via our Toplevel Functions
    #The application will give us a breakdown of the team, Just to ensure it worked properly


    print('\nYour Team is as follows:  \n \n', T_lane,':TOP', Jung,':JUNGLE', M_lane,':MID', B_lane,':BOT', Pansy,':SUPPORT')
    

    #Next we set up a for loop
    #There are a lot of loops you could use for this 
    #However seeing as we only have members on the team
    #We only need to loop through it 5 times

    for i in range(5):


        #Okay I know it is very Daunting, but it's actually simple

        #IF "x" is in (==) list1 or "x" is in (==) list2 ECT
        
        if T_lane[0] == 'Aatrox' or B_lane[0] == 'Aatrox' or M_lane[0] == 'Aatrox' or Jung[0] == 'Aatrox' or Pansy[0] == 'Aatrox':
            #Then Append (a,b,c) To our ban list
            BanList.append('Jax, Teemo, Fiora')

            #Then we made a loop inside of each
            #To replace that champion
            #according to the list he/she was in
            #This is necessary to ensure, when the loop goes again
            #It doesnt continuosly stop at the first
            #Criteria it meets

            if T_lane[0] == 'Aatrox':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Aatrox':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Aatrox':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Aatrox':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Aatrox':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Ahri' or B_lane[0] == 'Ahri' or M_lane[0] == 'Ahri' or Jung[0] == 'Ahri' or Pansy[0] == 'Ahri':
            BanList.append('LeBlanc, Swain, Diana')
            if T_lane[0] == 'Ahri':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Ahri':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Ahri':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Ahri':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Ahri':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Akali' or B_lane[0] == 'Akali' or M_lane[0] == 'Akali' or Jung[0] == 'Akali' or Pansy[0] == 'Akali':
            BanList.append('Lee Sin, Annie, Diana')
            if T_lane[0] == 'Akali':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Akali':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Akali':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Akali':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Akali':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Alistar' or B_lane[0] == 'Alistar' or M_lane[0] == 'Alistar' or Jung[0] == 'Alistar' or Pansy[0] == 'Alistar':
            BanList.append('Janna, Vayne, Tristana')
            if T_lane[0] == 'Alistar':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Alistar':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Alistar':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Alistar':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Alistar':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Amumu' or B_lane[0] == 'Amumu' or M_lane[0] == 'Amumu' or Jung[0] == 'Amumu' or Pansy[0] == 'Amumu':
            BanList.append('Shyvana, Lee Sin, Shaco')
            if T_lane[0] == 'Amumu':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Amumu':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Amumu':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Amumu':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Amumu':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Anivia' or B_lane[0] == 'Anivia' or M_lane[0] == 'Anivia' or Jung[0] == 'Anivia' or Pansy[0] == 'Anivia':
            BanList.append('Fizz, Kassadin, Diana')
            if T_lane[0] == 'Anivia':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Anivia':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Anivia':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Anivia':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Anivia':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Annie' or B_lane[0] == 'Annie' or M_lane[0] == 'Annie' or Jung[0] == 'Annie' or Pansy[0] == 'Annie':
            BanList.append('Brand, Sion, Orianna')
            if T_lane[0] == 'Annie':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Annie':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Annie':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Annie':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Annie':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Ashe' or B_lane[0] == 'Ashe' or M_lane[0] == 'Ashe' or Jung[0] == 'Ashe' or Pansy[0] == 'Ashe':
            BanList.append('Ezreal, Draven, Sivir')
            if T_lane[0] == 'Ashe':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Ashe':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Ashe':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Ashe':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Ashe':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'AurelionSol' or B_lane[0] == 'AurelionSol' or M_lane[0] == 'AurelionSol' or Jung[0] == 'AurelionSol' or Pansy[0] == 'AurelionSol':
            BanList.append('Yasuo, Zed, Zoe')
            if T_lane[0] == 'AurelionSol':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'AurelionSol':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'AurelionSol':
                M_lane.insert(0, '1')
            elif Jung[0] == 'AurelionSol':
                Jung.insert(0, '1')
            elif Pansy[0] == 'AurelionSol':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Azir' or B_lane[0] == 'Azir' or M_lane[0] == 'Azir' or Jung[0] == 'Azir' or Pansy[0] == 'Azir':
            BanList.append('Ziggs, Talon, Syndra')
            if T_lane[0] == 'Azir':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Azir':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Azir':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Azir':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Azir':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Bard' or B_lane[0] == 'Bard' or M_lane[0] == 'Bard' or Jung[0] == 'Bard' or Pansy[0] == 'Bard':
            BanList.append('Morgana, Sivir, Teemo')
            if T_lane[0] == 'Bard':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Bard':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Bard':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Bard':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Bard':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Blitzcrank' or B_lane[0] == 'Blitzcrank' or M_lane[0] == 'Blitzcrank' or Jung[0] == 'Blitzcrank' or Pansy[0] == 'Blitzcrank':
            BanList.append('Leona, Alistar, Morgana')
            if T_lane[0] == 'Blitzcrank':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Blitzcrank':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Blitzcrank':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Blitzcrank':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Blitzcrank':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Brand' or B_lane[0] == 'Brand' or M_lane[0] == 'Brand' or Jung[0] == 'Brand' or Pansy[0] == 'Brand':
            BanList.append('Kassaadin, Fizz, Galio')
            if T_lane[0] == 'Brand':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Brand':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Brand':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Brand':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Brand':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Braum' or B_lane[0] == 'Braum' or M_lane[0] == 'Braum' or Jung[0] == 'Braum' or Pansy[0] == 'Braum':
            BanList.append('Morgana, Zyra, Leona')
            if T_lane[0] == 'Braum':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Braum':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Braum':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Braum':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Braum':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Caitlyn' or B_lane[0] == 'Caitlyn' or M_lane[0] == 'Caitlyn' or Jung[0] == 'Caitlyn' or Pansy[0] == 'Caitlyn':
            BanList[0].append('Sivir, Jinx, Varus')
            if T_lane[0] == 'Caitlyn':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Caitlyn':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Caitlyn':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Caitlyn':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Caitlyn':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Camille' or B_lane[0] == 'Camille' or M_lane[0] == 'Camille' or Jung[0] == 'Camille' or Pansy[0] == 'Camille':
            BanList.append('Garen, Teemo, Fiora')
            if T_lane[0] == 'Camille':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Camille':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Camille':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Camille':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Camille':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Cassiopeia' or B_lane[0] == 'Cassiopeia' or M_lane[0] == 'Cassiopeia' or Jung[0] == 'Cassiopeia' or Pansy[0] == 'Cassiopeia':
            BanList.append('Galio, Orianna, Lux')
            if T_lane[0] == 'Cassiopeia':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Cassiopeia':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Cassiopeia':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Cassiopeia':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Cassiopeia':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'ChoGath' or B_lane[0] == 'ChoGath' or M_lane[0] == 'ChoGath' or Jung[0] == 'ChoGath' or Pansy[0] == 'ChoGath':
            BanList.append('Warwick, KogMaw, Vayne')
            if T_lane[0] == 'ChoGath':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'ChoGath':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'ChoGath':
                M_lane.insert(0, '1')
            elif Jung[0] == 'ChoGath':
                Jung.insert(0, '1')
            elif Pansy[0] == 'ChoGath':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Corki' or B_lane[0] == 'Corki' or M_lane[0] == 'Corki' or Jung[0] == 'Corki' or Pansy[0] == 'Corki':
            BanList.append('Caitlyn, LeBlanc, Draven')
            if T_lane[0] == 'Corki':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Corki':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Corki':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Corki':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Corki':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Darius' or B_lane[0] == 'Darius' or M_lane[0] == 'Darius' or Jung[0] == 'Darius' or Pansy[0] == 'Darius':
            BanList.append('Kayle, Yorick, Jayce')
            if T_lane[0] == 'Darius':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Darius':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Darius':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Darius':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Darius':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Diana' or B_lane[0] == 'Diana' or M_lane[0] == 'Diana' or Jung[0] == 'Diana' or Pansy[0] == 'Diana':
            BanList.append('Mordekaiser, ChoGath, Heimerdinger')
            if T_lane[0] == 'Diana':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Diana':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Diana':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Diana':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Diana':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'DrMundo' or B_lane[0] == 'DrMundo' or M_lane[0] == 'DrMundo' or Jung[0] == 'DrMundo' or Pansy[0] == 'DrMundo':
            BanList.append('Darius, Olaf, Riven')
            if T_lane[0] == 'DrMundo':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'DrMundo':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'DrMundo':
                M_lane.insert(0, '1')
            elif Jung[0] == 'DrMundo':
                Jung.insert(0, '1')
            elif Pansy[0] == 'DrMundo':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Draven' or B_lane[0] == 'Draven' or M_lane[0] == 'Draven' or Jung[0] == 'Draven' or Pansy[0] == 'Draven':
            BanList.append('Varus, Caitlyn, Thresh')
            if T_lane[0] == 'Draven':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Draven':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Draven':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Draven':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Draven':
                Pansy.insert(0, '1')    
        elif T_lane[0] == 'Ekko' or B_lane[0] == 'Ekko' or M_lane[0] == 'Ekko' or Jung[0] == 'Ekko' or Pansy[0] == 'Ekko':
            BanList.append('LeBlanc, Diana, Xin Zhoa')
            if T_lane[0] == 'Ekko':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Ekko':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Ekko':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Ekko':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Ekko':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Elise' or B_lane[0] == 'Elise' or M_lane[0] == 'Elise' or Jung[0] == 'Elise' or Pansy[0] == 'Elise':
            BanList.append('Kassadin, Wukong, Yorick')
            if T_lane[0] == 'Elise':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Elise':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Elise':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Elise':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Elise':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Evelynn' or B_lane[0] == 'Evelynn' or M_lane[0] == 'Evelynn' or Jung[0] == 'Evelynn' or Pansy[0] == 'Evelynn':
            BanList.append('Ryze, RekSai, Twisted Fate')
            if T_lane[0] == 'Evelynn':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Evelynn':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Evelynn':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Evelynn':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Evelynn':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Ezreal' or B_lane[0] == 'Ezreal' or M_lane[0] == 'Ezreal' or Jung[0] == 'Ezreal' or Pansy[0] == 'Ezreal':
            BanList.append('Draven, Graves, Miss Fortune')
            if T_lane[0] == 'Ezreal':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Ezreal':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Ezreal':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Ezreal':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Ezreal':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Fiddlesticks' or B_lane[0] == 'Fiddlesticks' or M_lane[0] == 'Fiddlesticks' or Jung[0] == 'Fiddlesticks' or Pansy[0] == 'Fiddlesticks':
            BanList.append('Janna, Kassadin, Evenlynn')
            if T_lane[0] == 'Fiddlesticks':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Fiddlesticks':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Fiddlesticks':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Fiddlesticks':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Fiddlesticks':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Fiora' or B_lane[0] == 'Fiora' or M_lane[0] == 'Fiora' or Jung[0] == 'Fiora' or Pansy[0] == 'Fiora':
            BanList.append('Jax, Pantheon, Darius')
            if T_lane[0] == 'Fiora':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Fiora':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Fiora':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Fiora':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Fiora':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Fizz' or B_lane[0] == 'Fizz' or M_lane[0] == 'Fizz' or Jung[0] == 'Fizz' or Pansy[0] == 'Fizz':
            BanList.append('Ryze, Kayle, Lissandra')
            if T_lane[0] == 'Fizz':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Fizz':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Fizz':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Fizz':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Fizz':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Galio' or B_lane[0] == 'Galio' or M_lane[0] == 'Galio' or Jung[0] == 'Galio' or Pansy[0] == 'Galio':
            BanList.append('Akali, Udyr, Braum')
            if T_lane[0] == 'Galio':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Galio':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Galio':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Galio':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Galio':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Gangplank' or B_lane[0] == 'Gangplank' or M_lane[0] == 'Gangplank' or Jung[0] == 'Gangplank' or Pansy[0] == 'Gangplank':
            BanList.append('Pantheon, Fiora, Irelia')
            if T_lane[0] == 'Gangplank':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Gangplank':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Gangplank':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Gangplank':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Gangplank':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Garen' or B_lane[0] == 'Garen' or M_lane[0] == 'Garen' or Jung[0] == 'Garen' or Pansy[0] == 'Garen':
            BanList.append('Teemo, Gnar, Elise')
            if T_lane[0] == 'Garen':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Garen':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Garen':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Garen':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Garen':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Gnar' or B_lane[0] == 'Gnar' or M_lane[0] == 'Gnar' or Jung[0] == 'Gnar' or Pansy[0] == 'Gnar':
            BanList.append('Pantheon, Wukong, Irelia')
            if T_lane[0] == 'Gnar':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Gnar':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Gnar':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Gnar':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Gnar':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Gragas' or B_lane[0] == 'Gragas' or M_lane[0] == 'Gragas' or Jung[0] == 'Gragas' or Pansy[0] == 'Gragas':
            BanList.append('Yasuo, Ahri, Evelynn')
            if T_lane[0] == 'Gragas':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Gragas':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Gragas':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Gragas':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Gragas':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Graves' or B_lane[0] == 'Graves' or M_lane[0] == 'Graves' or Jung[0] == 'Graves' or Pansy[0] == 'Graves':
            BanList.append('Caitlyn, Sivir, Corki')
            if T_lane[0] == 'Graves':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Graves':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Graves':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Graves':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Graves':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Hecarim' or B_lane[0] == 'Hecarim' or M_lane[0] == 'Hecarim' or Jung[0] == 'Hecarim' or Pansy[0] == 'Hecarim':
            BanList.append('Nasus, Aatrox, Sejuani')
            if T_lane[0] == 'Hecarim':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Hecarim':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Hecarim':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Hecarim':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Hecarim':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Heimerdinger' or B_lane[0] == 'Heimerdinger' or M_lane[0] == 'Heimerdinger' or Jung[0] == 'Heimerdinger' or Pansy[0] == 'Heimerdinger':
            BanList.append('Syndra, Malzahar, Xerath')
            if T_lane[0] == 'Heimerdinger':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Heimerdinger':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Heimerdinger':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Heimerdinger':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Heimerdinger':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Illaoi' or B_lane[0] == 'Illaoi' or M_lane[0] == 'Illaoi' or Jung[0] == 'Illaoi' or Pansy[0] == 'Illaoi':
            BanList.append('Lulu, Tryndamere, Jarvan IV')
            if T_lane[0] == 'Illaoi':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Illaoi':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Illaoi':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Illaoi':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Illaoi':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Irelia' or B_lane[0] == 'Irelia' or M_lane[0] == 'Irelia' or Jung[0] == 'Irelia' or Pansy[0] == 'Irelia':
            BanList.append('Olaf, Garen, Darius')
            if T_lane[0] == 'Irelia':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Irelia':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Irelia':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Irelia':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Irelia':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Ivern' or B_lane[0] == 'Ivern' or M_lane[0] == 'Ivern' or Jung[0] == 'Ivern' or Pansy[0] == 'Ivern':
            BanList.append('Illaoi, KhaZix, Graves')
            if T_lane[0] == 'Ivern':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Ivern':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Ivern':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Ivern':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Ivern':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Janna' or B_lane[0] == 'Janna' or M_lane[0] == 'Janna' or Jung[0] == 'Janna' or Pansy[0] == 'Janna':
            BanList.append('Sona, Nami, Blitzcrank')
            if T_lane[0] == 'Janna':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Janna':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Janna':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Janna':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Janna':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'JarvanIV' or B_lane[0] == 'JarvanIV' or M_lane[0] == 'JarvanIV' or Jung[0] == 'JarvanIV' or Pansy[0] == 'JarvanIV':
            BanList.append('Yorick, Jax, Shen')
            if T_lane[0] == 'JarvanIV':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'JarvanIV':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'JarvanIV':
                M_lane.insert(0, '1')
            elif Jung[0] == 'JarvanIV':
                Jung.insert(0, '1')
            elif Pansy[0] == 'JarvanIV':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Jax' or B_lane[0] == 'Jax' or M_lane[0] == 'Jax' or Jung[0] == 'Jax' or Pansy[0] == 'Jax':
            BanList.append('Malphite, Renekton, Singed')
            if T_lane[0] == 'Jax':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Jax':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Jax':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Jax':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Jax':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Jayce' or B_lane[0] == 'Jayce' or M_lane[0] == 'Jayce' or Jung[0] == 'Jayce' or Pansy[0] == 'Jayce':
            BanList.append('Yorick, Fiora, Xin Zhao')
            if T_lane[0] == 'Jayce':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Jayce':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Jayce':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Jayce':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Jayce':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Jhin' or B_lane[0] == 'Jhin' or M_lane[0] == 'Jhin' or Jung[0] == 'Jhin' or Pansy[0] == 'Jhin':
            BanList.append('Lucian, Miss Fortune, Vayne')
            if T_lane[0] == 'Jhin':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Jhin':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Jhin':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Jhin':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Jhin':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Jinx' or B_lane[0] == 'Jinx' or M_lane[0] == 'Jinx' or Jung[0] == 'Jinx' or Pansy[0] == 'Jinx':
            BanList.append('Ezreal, Corki, Sivir')
            if T_lane[0] == 'Jinx':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Jinx':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Jinx':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Jinx':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Jinx':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'KaiSa' or B_lane[0] == 'KaiSa' or M_lane[0] == 'KaiSa' or Jung[0] == 'KaiSa' or Pansy[0] == 'KaiSa':
            BanList.append('Caitlyn, Miss Fortune, Aatrox')
            if T_lane[0] == 'KaiSa':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'KaiSa':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'KaiSa':
                M_lane.insert(0, '1')
            elif Jung[0] == 'KaiSa':
                Jung.insert(0, '1')
            elif Pansy[0] == 'KaiSa':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Kalista' or B_lane[0] == 'Kalista' or M_lane[0] == 'Kalista' or Jung[0] == 'Kalista' or Pansy[0] == 'Kalista':
            BanList.append('Ashe, Caitlyn, Vayne')
            if T_lane[0] == 'Kalista':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Kalista':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Kalista':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Kalista':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Kalista':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Karma' or B_lane[0] == 'Karma' or M_lane[0] == 'Karma' or Jung[0] == 'Karma' or Pansy[0] == 'Karma':
            BanList.append('Veigar, Talon, Xerath')
            if T_lane[0] == 'Karma':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Karma':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Karma':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Karma':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Karma':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Karthus' or B_lane[0] == 'Karthus' or M_lane[0] == 'Karthus' or Jung[0] == 'Karthus' or Pansy[0] == 'Karthus':
            BanList.append('Soraka, Kassadin, Fizz')
            if T_lane[0] == 'Karthus':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Karthus':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Karthus':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Karthus':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Karthus':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Kassadin' or B_lane[0] == 'Kassadin' or M_lane[0] == 'Kassadin' or Jung[0] == 'Kassadin' or Pansy[0] == 'Kassadin':
            BanList.append('Talon, Pantheon, Heimerdinger')
            if T_lane[0] == 'Kassadin':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Kassadin':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Kassadin':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Kassadin':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Kassadin':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Katarina' or B_lane[0] == 'Katarina' or M_lane[0] == 'Katarina' or Jung[0] == 'Katarina' or Pansy[0] == 'Katarina':
            BanList.append('Diana, Fiddlesticks, Malzahar')
            if T_lane[0] == 'Katarina':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Katarina':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Katarina':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Katarina':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Katarina':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Kayle' or B_lane[0] == 'Kayle' or M_lane[0] == 'Kayle' or Jung[0] == 'Kayle' or Pansy[0] == 'Kayle':
            BanList.append('Anivia, Pantheon, Orianna')
            if T_lane[0] == 'Kayle':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Kayle':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Kayle':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Kayle':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Kayle':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Kayn' or B_lane[0] == 'Kayn' or M_lane[0] == 'Kayn' or Jung[0] == 'Kayn' or Pansy[0] == 'Kayn':
            BanList.append('Warwick, KhaZix, Xin Zhao')
            if T_lane[0] == 'Kayn':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Kayn':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Kayn':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Kayn':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Kayn':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Kennen' or B_lane[0] == 'Kennen' or M_lane[0] == 'Kennen' or Jung[0] == 'Kennen' or Pansy[0] == 'Kennen':
            BanList.append('Diana, Janna, Swain')
            if T_lane[0] == 'Kennen':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Kennen':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Kennen':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Kennen':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Kennen':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'KhaZix' or B_lane[0] == 'KhaZix' or M_lane[0] == 'KhaZix' or Jung[0] == 'KhaZix' or Pansy[0] == 'KhaZix':
            BanList.append('Lee Sin, Jayce, Pantheon')
            if T_lane[0] == 'KhaZix':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'KhaZix':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'KhaZix':
                M_lane.insert(0, '1')
            elif Jung[0] == 'KhaZix':
                Jung.insert(0, '1')
            elif Pansy[0] == 'KhaZix':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Kindred' or B_lane[0] == 'Kindred' or M_lane[0] == 'Kindred' or Jung[0] == 'Kindred' or Pansy[0] == 'Kindred':
            BanList.append('Lee Sin, Diana, Gragas')
            if T_lane[0] == 'Kindred':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Kindred':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Kindred':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Kindred':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Kindred':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Kled' or B_lane[0] == 'Kled' or M_lane[0] == 'Kled' or Jung[0] == 'Kled' or Pansy[0] == 'Kled':
            BanList.append('Fiora, Shen, Jax')
            if T_lane[0] == 'Kled':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Kled':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Kled':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Kled':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Kled':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'KogMaw' or B_lane[0] == 'KogMaw' or M_lane[0] == 'KogMaw' or Jung[0] == 'KogMaw' or Pansy[0] == 'KogMaw':
            BanList.append('Blitzcrank, Lucian, Jinx')
            if T_lane[0] == 'KogMaw':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'KogMaw':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'KogMaw':
                M_lane.insert(0, '1')
            elif Jung[0] == 'KogMaw':
                Jung.insert(0, '1')
            elif Pansy[0] == 'KogMaw':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'LeBlanc' or B_lane[0] == 'LeBlanc' or M_lane[0] == 'LeBlanc' or Jung[0] == 'LeBlanc' or Pansy[0] == 'LeBlanc':
            BanList.append('Galio, Morgana, Diana')
            if T_lane[0] == 'LeBlanc':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'LeBlanc':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'LeBlanc':
                M_lane.insert(0, '1')
            elif Jung[0] == 'LeBlanc':
                Jung.insert(0, '1')
            elif Pansy[0] == 'LeBlanc':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'LeeSin' or B_lane[0] == 'LeeSin' or M_lane[0] == 'LeeSin' or Jung[0] == 'LeeSin' or Pansy[0] == 'LeeSin':
            BanList.append('Trundle, Udyr, Singed')
            if T_lane[0] == 'LeeSin':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'LeeSin':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'LeeSin':
                M_lane.insert(0, '1')
            elif Jung[0] == 'LeeSin':
                Jung.insert(0, '1')
            elif Pansy[0] == 'LeeSin':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Leona' or B_lane[0] == 'Leona' or M_lane[0] == 'Leona' or Jung[0] == 'Leona' or Pansy[0] == 'Leona':
            BanList.append('Morgana, Alistar, Janna')
            if T_lane[0] == 'Leona':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Leona':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Leona':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Leona':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Leona':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Lissandra' or B_lane[0] == 'Lissandra' or M_lane[0] == 'Lissandra' or Jung[0] == 'Lissandra' or Pansy[0] == 'Lissandra':
            BanList.append('Kassadin, Syndra, Diana')
            if T_lane[0] == 'Lissandra':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Lissandra':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Lissandra':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Lissandra':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Lissandra':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Lucian' or B_lane[0] == 'Lucian' or M_lane[0] == 'Lucian' or Jung[0] == 'Lucian' or Pansy[0] == 'Lucian':
            BanList.append('Vayne, Draven, Tristana')
            if T_lane[0] == 'Lucian':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Lucian':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Lucian':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Lucian':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Lucian':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Lulu' or B_lane[0] == 'Lulu' or M_lane[0] == 'Lulu' or Jung[0] == 'Lulu' or Pansy[0] == 'Lulu':
            BanList.append('Syndra, Soraka, Sona')
            if T_lane[0] == 'Lulu':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Lulu':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Lulu':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Lulu':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Lulu':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Lux' or B_lane[0] == 'Lux' or M_lane[0] == 'Lux' or Jung[0] == 'Lux' or Pansy[0] == 'Lux':
            BanList.append('Talon, Gragas, Fizz')
            if T_lane[0] == 'Lux':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Lux':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Lux':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Lux':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Lux':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Malphite' or B_lane[0] == 'Malphite' or M_lane[0] == 'Malphite' or Jung[0] == 'Malphite' or Pansy[0] == 'Malphite':
            BanList.append('Rumble, Zac, Shen')
            if T_lane[0] == 'Malphite':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Malphite':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Malphite':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Malphite':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Malphite':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Malzahar' or B_lane[0] == 'Malzahar' or M_lane[0] == 'Malzahar' or Jung[0] == 'Malzahar' or Pansy[0] == 'Malzahar':
            BanList.append('Gangplank, Syndra, Galio')
            if T_lane[0] == 'Malzahar':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Malzahar':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Malzahar':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Malzahar':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Malzahar':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Maokai' or B_lane[0] == 'Maokai' or M_lane[0] == 'Maokai' or Jung[0] == 'Maokai' or Pansy[0] == 'Maokai':
            BanList.append('Shyvana, Nasus, Pantheon')
            if T_lane[0] == 'Maokai':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Maokai':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Maokai':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Maokai':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Maokai':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'MasterYi' or B_lane[0] == 'MasterYi' or M_lane[0] == 'MasterYi' or Jung[0] == 'MasterYi' or Pansy[0] == 'MasterYi':
            BanList.append('Jax, Pantheon, Tryndamere')
            if T_lane[0] == 'MasterYi':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'MasterYi':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'MasterYi':
                M_lane.insert(0, '1')
            elif Jung[0] == 'MasterYi':
                Jung.insert(0, '1')
            elif Pansy[0] == 'MasterYi':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'MissFortune' or B_lane[0] == 'MissFortune' or M_lane[0] == 'MissFortune' or Jung[0] == 'MissFortune' or Pansy[0] == 'MissFortune':
            BanList.append('Tristana, Draven, Caitlyn')
            if T_lane[0] == 'MissFortune':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'MissFortune':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'MissFortune':
                M_lane.insert(0, '1')
            elif Jung[0] == 'MissFortune':
                Jung.insert(0, '1')
            elif Pansy[0] == 'MissFortune':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Mordekaiser' or B_lane[0] == 'Mordekaiser' or M_lane[0] == 'Mordekaiser' or Jung[0] == 'Mordekaiser' or Pansy[0] == 'Mordekaiser':
            BanList.append('Zyra, Yorick, Garen')
            if T_lane[0] == 'Mordekaiser':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Mordekaiser':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Mordekaiser':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Mordekaiser':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Mordekaiser':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Morgana' or B_lane[0] == 'Morgana' or M_lane[0] == 'Morgana' or Jung[0] == 'Morgana' or Pansy[0] == 'Morgana':
            BanList.append('Talon, Karma, Zed')
            if T_lane[0] == 'Morgana':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Morgana':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Morgana':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Morgana':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Morgana':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Nami' or B_lane[0] == 'Nami' or M_lane[0] == 'Nami' or Jung[0] == 'Nami' or Pansy[0] == 'Nami':
            BanList.append('Lulu, Ezreal, Fizz')
            if T_lane[0] == 'Nami':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Nami':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Nami':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Nami':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Nami':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Nasus' or B_lane[0] == 'Nasus' or M_lane[0] == 'Nasus' or Jung[0] == 'Nasus' or Pansy[0] == 'Nasus':
            BanList.append('Teemo, Olaf, Rumble')
            if T_lane[0] == 'Nasus':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Nasus':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Nasus':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Nasus':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Nasus':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Nautilus' or B_lane[0] == 'Nautilus' or M_lane[0] == 'Nautilus' or Jung[0] == 'Nautilus' or Pansy[0] == 'Nautilus':
            BanList.append('Garen, Shyvana, Olaf')
            if T_lane[0] == 'Nautilus':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Nautilus':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Nautilus':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Nautilus':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Nautilus':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Nidalee' or B_lane[0] == 'Nidalee' or M_lane[0] == 'Nidalee' or Jung[0] == 'Nidalee' or Pansy[0] == 'Nidalee':
            BanList.append('Yasuo, Pantheon, Zed')
            if T_lane[0] == 'Nidalee':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Nidalee':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Nidalee':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Nidalee':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Nidalee':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Nocturne' or B_lane[0] == 'Nocturne' or M_lane[0] == 'Nocturne' or Jung[0] == 'Nocturne' or Pansy[0] == 'Nocturne':
            BanList.append('Olaf, Alistar, Lee Sin')
            if T_lane[0] == 'Nocturne':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Nocturne':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Nocturne':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Nocturne':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Nocturne':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Nunu&Willump' or B_lane[0] == 'Nunu&Willump' or M_lane[0] == 'Nunu&Willump' or Jung[0] == 'Nunu&Willump' or Pansy[0] == 'Nunu&Willump':
            BanList.append('Cassiopeia, Sona, Soraka')
            if T_lane[0] == 'Nunu&Willump':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Nunu&Willump':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Nunu&Willump':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Nunu&Willump':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Nunu&Willump':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Olaf' or B_lane[0] == 'Olaf' or M_lane[0] == 'Olaf' or Jung[0] == 'Olaf' or Pansy[0] == 'Olaf':
            BanList.append('Kayle, Yorick, Elise')
            if T_lane[0] == 'Olaf':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Olaf':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Olaf':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Olaf':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Olaf':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Orianna' or B_lane[0] == 'Orianna' or M_lane[0] == 'Orianna' or Jung[0] == 'Orianna' or Pansy[0] == 'Orianna':
            BanList.append('Syndra, Ziggs, Diana')
            if T_lane[0] == 'Orianna':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Orianna':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Orianna':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Orianna':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Orianna':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Ornn' or B_lane[0] == 'Ornn' or M_lane[0] == 'Ornn' or Jung[0] == 'Ornn' or Pansy[0] == 'Ornn':
            BanList.append('Jax, Urgot, Fiora')
            if T_lane[0] == 'Ornn':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Ornn':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Ornn':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Ornn':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Ornn':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Pantheon' or B_lane[0] == 'Pantheon' or M_lane[0] == 'Pantheon' or Jung[0] == 'Pantheon' or Pansy[0] == 'Pantheon':
            BanList.append('Olaf, Shen, Elise')
            if T_lane[0] == 'Pantheon':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Pantheon':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Pantheon':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Pantheon':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Pantheon':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Poppy' or B_lane[0] == 'Poppy' or M_lane[0] == 'Poppy' or Jung[0] == 'Poppy' or Pansy[0] == 'Poppy':
            BanList.append('Olaf, Leona, Renekton')
            if T_lane[0] == 'Poppy':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Poppy':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Poppy':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Poppy':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Poppy':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Pyke' or B_lane[0] == 'Pyke' or M_lane[0] == 'Pyke' or Jung[0] == 'Pyke' or Pansy[0] == 'Pyke':
            BanList.append('Nami, Sion, Sona')
            if T_lane[0] == 'Pyke':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Pyke':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Pyke':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Pyke':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Pyke':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Quinn' or B_lane[0] == 'Quinn' or M_lane[0] == 'Quinn' or Jung[0] == 'Quinn' or Pansy[0] == 'Quinn':
            BanList.append('Caitlyn, Varus, Miss Fortune')
            if T_lane[0] == 'Quinn':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Quinn':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Quinn':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Quinn':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Quinn':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Rakan' or B_lane[0] == 'Rakan' or M_lane[0] == 'Rakan' or Jung[0] == 'Rakan' or Pansy[0] == 'Rakan':
            BanList.append('Morgana, Lulu, Leona')
            if T_lane[0] == 'Rakan':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Rakan':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Rakan':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Rakan':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Rakan':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Rammus' or B_lane[0] == 'Rammus' or M_lane[0] == 'Rammus' or Jung[0] == 'Rammus' or Pansy[0] == 'Rammus':
            BanList.append('Trundle, Soraka, RekSai')
            if T_lane[0] == 'Rammus':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Rammus':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Rammus':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Rammus':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Rammus':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'RekSai' or B_lane[0] == 'RekSai' or M_lane[0] == 'RekSai' or Jung[0] == 'RekSai' or Pansy[0] == 'RekSai':
            BanList.append('Fizz, Irelia, Darius')
            if T_lane[0] == 'RekSai':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'RekSai':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'RekSai':
                M_lane.insert(0, '1')
            elif Jung[0] == 'RekSai':
                Jung.insert(0, '1')
            elif Pansy[0] == 'RekSai':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Renekton' or B_lane[0] == 'Renekton' or M_lane[0] == 'Renekton' or Jung[0] == 'Renekton' or Pansy[0] == 'Renekton':
            BanList.append('Trundle, Vayne, Elise')
            if T_lane[0] == 'Renekton':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Renekton':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Renekton':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Renekton':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Renekton':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Rengar' or B_lane[0] == 'Rengar' or M_lane[0] == 'Rengar' or Jung[0] == 'Rengar' or Pansy[0] == 'Rengar':
            BanList.append('Jax, Fiora, Pantheon')
            if T_lane[0] == 'Rengar':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Rengar':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Rengar':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Rengar':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Rengar':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Riven' or B_lane[0] == 'Riven' or M_lane[0] == 'Riven' or Jung[0] == 'Riven' or Pansy[0] == 'Riven':
            BanList.append('Garen, Kennen, Pantheon')
            if T_lane[0] == 'Riven':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Riven':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Riven':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Riven':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Riven':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Rumble' or B_lane[0] == 'Rumble' or M_lane[0] == 'Rumble' or Jung[0] == 'Rumble' or Pansy[0] == 'Rumble':
            BanList.append('Yorick, Elise, Viktor')
            if T_lane[0] == 'Rumble':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Rumble':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Rumble':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Rumble':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Rumble':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Ryze' or B_lane[0] == 'Ryze' or M_lane[0] == 'Ryze' or Jung[0] == 'Ryze' or Pansy[0] == 'Ryze':
            BanList.append('Cassiopeia, Oriana, Xerath')
            if T_lane[0] == 'Ryze':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Ryze':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Ryze':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Ryze':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Ryze':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Sejuani' or B_lane[0] == 'Sejuani' or M_lane[0] == 'Sejuani' or Jung[0] == 'Sejuani' or Pansy[0] == 'Sejuani':
            BanList.append('Xin Zhao, Vi, Elise')
            if T_lane[0] == 'Sejuani':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Sejuani':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Sejuani':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Sejuani':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Sejuani':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Shaco' or B_lane[0] == 'Shaco' or M_lane[0] == 'Shaco' or Jung[0] == 'Shaco' or Pansy[0] == 'Shaco':
            BanList.append('Lee Sin, Udyr, Shyvana')
            if T_lane[0] == 'Shaco':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Shaco':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Shaco':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Shaco':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Shaco':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Shen' or B_lane[0] == 'Shen' or M_lane[0] == 'Shen' or Jung[0] == 'Shen' or Pansy[0] == 'Shen':
            BanList.append('Yorick, Jayce, Warwick')
            if T_lane[0] == 'Shen':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Shen':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Shen':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Shen':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Shen':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Shyvana' or B_lane[0] == 'Shyvana' or M_lane[0] == 'Shyvana' or Jung[0] == 'Shyvana' or Pansy[0] == 'Shyvana':
            BanList.append('Olaf, Elise, Trundle')
            if T_lane[0] == 'Shyvana':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Shyvana':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Shyvana':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Shyvana':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Shyvana':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Singed' or B_lane[0] == 'Singed' or M_lane[0] == 'Singed' or Jung[0] == 'Singed' or Pansy[0] == 'Singed':
            BanList.append('Teemo, Kayle, Elise')
            if T_lane[0] == 'Singed':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Singed':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Singed':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Singed':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Singed':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Sion' or B_lane[0] == 'Sion' or M_lane[0] == 'Sion' or Jung[0] == 'Sion' or Pansy[0] == 'Sion':
            BanList.append('Pantheon, Garen, Riven')
            if T_lane[0] == 'Sion':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Sion':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Sion':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Sion':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Sion':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Sivir' or B_lane[0] == 'Sivir' or M_lane[0] == 'Sivir' or Jung[0] == 'Sivir' or Pansy[0] == 'Sivir':
            BanList.append('Vayne, Draven, Twitch')
            if T_lane[0] == 'Sivir':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Sivir':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Sivir':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Sivir':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Sivir':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Skarner' or B_lane[0] == 'Skarner' or M_lane[0] == 'Skarner' or Jung[0] == 'Skarner' or Pansy[0] == 'Skarner':
            BanList.append('Morgana, Xin Zhao, Lulu')
            if T_lane[0] == 'Skarner':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Skarner':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Skarner':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Skarner':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Skarner':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Sona' or B_lane[0] == 'Sona' or M_lane[0] == 'Sona' or Jung[0] == 'Sona' or Pansy[0] == 'Sona':
            BanList.append('Thresh, Blitzcrank, Leona')
            if T_lane[0] == 'Sona':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Sona':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Sona':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Sona':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Sona':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Soraka' or B_lane[0] == 'Soraka' or M_lane[0] == 'Soraka' or Jung[0] == 'Soraka' or Pansy[0] == 'Soraka':
            BanList.append('Gnar, Miss Fortune, Blitzcrank')
            if T_lane[0] == 'Soraka':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Soraka':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Soraka':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Soraka':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Soraka':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Swain' or B_lane[0] == 'Swain' or M_lane[0] == 'Swain' or Jung[0] == 'Swain' or Pansy[0] == 'Swain':
            BanList.append('Viktor, Syndra, Lux')
            if T_lane[0] == 'Swain':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Swain':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Swain':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Swain':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Swain':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Syndra' or B_lane[0] == 'Syndra' or M_lane[0] == 'Syndra' or Jung[0] == 'Syndra' or Pansy[0] == 'Syndra':
            BanList.append('Fizz, Kayle, Yasuo')
            if T_lane[0] == 'Syndra':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Syndra':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Syndra':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Syndra':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Syndra':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'TahmKench' or B_lane[0] == 'TahmKench' or M_lane[0] == 'TahmKench' or Jung[0] == 'TahmKench' or Pansy[0] == 'TahmKench':
            BanList.append('Janna, Vayne, Singed')
            if T_lane[0] == 'TahmKench':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'TahmKench':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'TahmKench':
                M_lane.insert(0, '1')
            elif Jung[0] == 'TahmKench':
                Jung.insert(0, '1')
            elif Pansy[0] == 'TahmKench':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Taliyah' or B_lane[0] == 'Taliyah' or M_lane[0] == 'Taliyah' or Jung[0] == 'Taliyah' or Pansy[0] == 'Taliyah':
            BanList.append('Ziggs, Zed, Veigar')
            if T_lane[0] == 'Taliyah':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Taliyah':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Taliyah':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Taliyah':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Taliyah':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Talon' or B_lane[0] == 'Talon' or M_lane[0] == 'Talon' or Jung[0] == 'Talon' or Pansy[0] == 'Talon':
            BanList.append('Lee Sin, Yorick, Diana')
            if T_lane[0] == 'Talon':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Talon':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Talon':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Talon':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Talon':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Taric' or B_lane[0] == 'Taric' or M_lane[0] == 'Taric' or Jung[0] == 'Taric' or Pansy[0] == 'Taric':
            BanList.append('Sivir, Lulu, Morgana')
            if T_lane[0] == 'Taric':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Taric':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Taric':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Taric':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Taric':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Teemo' or B_lane[0] == 'Teemo' or M_lane[0] == 'Teemo' or Jung[0] == 'Teemo' or Pansy[0] == 'Teemo':
            BanList.append('Yorick, Pantheon, Rumble')
            if T_lane[0] == 'Teemo':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Teemo':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Teemo':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Teemo':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Teemo':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Thresh' or B_lane[0] == 'Thresh' or M_lane[0] == 'Thresh' or Jung[0] == 'Thresh' or Pansy[0] == 'Thresh':
            BanList.append('Lulu, Morgana, Alistar')
            if T_lane[0] == 'Thresh':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Thresh':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Thresh':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Thresh':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Thresh':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Tristana' or B_lane[0] == 'Tristana' or M_lane[0] == 'Tristana' or Jung[0] == 'Tristana' or Pansy[0] == 'Tristana':
            BanList.append('Corki, Vayne, Diana')
            if T_lane[0] == 'Tristana':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Tristana':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Tristana':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Tristana':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Tristana':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Trundle' or B_lane[0] == 'Trundle' or M_lane[0] == 'Trundle' or Jung[0] == 'Trundle' or Pansy[0] == 'Trundle':
            BanList.append('Sona, Darius, Pantheon')
            if T_lane[0] == 'Trundle':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Trundle':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Trundle':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Trundle':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Trundle':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Tryndamere' or B_lane[0] == 'Tryndamere' or M_lane[0] == 'Tryndamere' or Jung[0] == 'Tryndamere' or Pansy[0] == 'Tryndamere':
            BanList.append('Teemo, Rammus, Pantheon')
            if T_lane[0] == 'Tryndamere':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Tryndamere':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Tryndamere':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Tryndamere':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Tryndamere':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'TwistedFate' or B_lane[0] == 'TwistedFate' or M_lane[0] == 'TwistedFate' or Jung[0] == 'TwistedFate' or Pansy[0] == 'TwistedFate':
            BanList.append('Fizz, Diana, Kassadin')
            if T_lane[0] == 'TwistedFate':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'TwistedFate':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'TwistedFate':
                M_lane.insert(0, '1')
            elif Jung[0] == 'TwistedFate':
                Jung.insert(0, '1')
            elif Pansy[0] == 'TwistedFate':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Twitch' or B_lane[0] == 'Twitch' or M_lane[0] == 'Twitch' or Jung[0] == 'Twitch' or Pansy[0] == 'Twitch':
            BanList.append('Tristanda, Caitlyn, Lee Sin')
            if T_lane[0] == 'Twitch':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Twitch':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Twitch':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Twitch':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Twitch':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Udyr' or B_lane[0] == 'Udyr' or M_lane[0] == 'Udyr' or Jung[0] == 'Udyr' or Pansy[0] == 'Udyr':
            BanList.append('Ashe, Teemo, Jax')
            if T_lane[0] == 'Udyr':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Udyr':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Udyr':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Udyr':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Udyr':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Urgot' or B_lane[0] == 'Urgot' or M_lane[0] == 'Urgot' or Jung[0] == 'Urgot' or Pansy[0] == 'Urgot':
            BanList.append('Graves, Bard, Vayne')
            if T_lane[0] == 'Urgot':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Urgot':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Urgot':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Urgot':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Urgot':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Varus' or B_lane[0] == 'Varus' or M_lane[0] == 'Varus' or Jung[0] == 'Varus' or Pansy[0] == 'Varus':
            BanList.append('Graves, Lucian, Sivir')
            if T_lane[0] == 'Varus':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Varus':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Varus':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Varus':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Varus':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Vayne' or B_lane[0] == 'Vayne' or M_lane[0] == 'Vayne' or Jung[0] == 'Vayne' or Pansy[0] == 'Vayne':
            BanList.append('Caitlyn, Quinn, Draven')
            if T_lane[0] == 'Vayne':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Vayne':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Vayne':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Vayne':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Vayne':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Veigar' or B_lane[0] == 'Veigar' or M_lane[0] == 'Veigar' or Jung[0] == 'Veigar' or Pansy[0] == 'Veigar':
            BanList.append('Fizz, Talon, Zed')
            if T_lane[0] == 'Veigar':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Veigar':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Veigar':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Veigar':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Veigar':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'VelKoz' or B_lane[0] == 'VelKoz' or M_lane[0] == 'VelKoz' or Jung[0] == 'VelKoz' or Pansy[0] == 'VelKoz':
            BanList.append('Yasuo, LeBlanc, Fizz')
            if T_lane[0] == 'VelKoz':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'VelKoz':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'VelKoz':
                M_lane.insert(0, '1')
            elif Jung[0] == 'VelKoz':
                Jung.insert(0, '1')
            elif Pansy[0] == 'VelKoz':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Vi' or B_lane[0] == 'Vi' or M_lane[0] == 'Vi' or Jung[0] == 'Vi' or Pansy[0] == 'Vi':
            BanList.append('Riven, Pantheon, Jax')
            if T_lane[0] == 'Vi':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Vi':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Vi':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Vi':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Vi':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Viktor' or B_lane[0] == 'Viktor' or M_lane[0] == 'Viktor' or Jung[0] == 'Viktor' or Pansy[0] == 'Viktor':
            BanList.append('Brand, Ziggs, Syndra')
            if T_lane[0] == 'Viktor':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Viktor':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Viktor':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Viktor':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Viktor':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Yorick' or B_lane[0] == 'Yorick' or M_lane[0] == 'Yorick' or Jung[0] == 'Yorick' or Pansy[0] == 'Yorick':
            BanList.append('ChoGath, Trundle, Irelia')
            if T_lane[0] == 'Yorick':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Yorick':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Yorick':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Yorick':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Yorick':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Vladimir' or B_lane[0] == 'Vladimir' or M_lane[0] == 'Vladimir' or Jung[0] == 'Vladimir' or Pansy[0] == 'Vladimir':
            BanList.append('Swain, Jarvan IV, Malzahar')
            if T_lane[0] == 'Vladimir':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Vladimir':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Vladimir':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Vladimir':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Vladimir':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Zac' or B_lane[0] == 'Zac' or M_lane[0] == 'Zac' or Jung[0] == 'Zac' or Pansy[0] == 'Zac':
            BanList.append('Vi, Zilean, Yorick')
            if T_lane[0] == 'Zac':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Zac':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Zac':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Zac':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Zac':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Volibear' or B_lane[0] == 'Volibear' or M_lane[0] == 'Volibear' or Jung[0] == 'Volibear' or Pansy[0] == 'Volibear':
            BanList.append('Teemo, Elise, Jayce')
            if T_lane[0] == 'Volibear':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Volibear':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Volibear':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Volibear':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Volibear':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Warwick' or B_lane[0] == 'Warwick' or M_lane[0] == 'Warwick' or Jung[0] == 'Warwick' or Pansy[0] == 'Warwick':
            BanList.append('Yorick, Wukong, Udyr')
            if T_lane[0] == 'Warwick':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Warwick':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Warwick':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Warwick':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Warwick':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Wukong' or B_lane[0] == 'Wukong' or M_lane[0] == 'Wukong' or Jung[0] == 'Wukong' or Pansy[0] == 'Wukong':
            BanList.append('Lee Sin, Darius, Garen')
            if T_lane[0] == 'Wukong':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Wukong':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Wukong':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Wukong':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Wukong':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Xayah' or B_lane[0] == 'Xayah' or M_lane[0] == 'Xayah' or Jung[0] == 'Xayah' or Pansy[0] == 'Xayah':
            BanList.append('Miss Fortune, Caitlyn, Tristana')
            if T_lane[0] == 'Xayah':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Xayah':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Xayah':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Xayah':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Xayah':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Xerath' or B_lane[0] == 'Xerath' or M_lane[0] == 'Xerath' or Jung[0] == 'Xerath' or Pansy[0] == 'Xerath':
            BanList.append('Ahri, Syndra, Zed')
            if T_lane[0] == 'Xerath':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Xerath':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Xerath':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Xerath':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Xerath':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'XinZhao' or B_lane[0] == 'XinZhao' or M_lane[0] == 'XinZhao' or Jung[0] == 'XinZhao' or Pansy[0] == 'XinZhao':
            BanList.append('Jax, Pantheon, Fiora')
            if T_lane[0] == 'XinZhao':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'XinZhao':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'XinZhao':
                M_lane.insert(0, '1')
            elif Jung[0] == 'XinZhao':
                Jung.insert(0, '1')
            elif Pansy[0] == 'XinZhao':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Yasuo' or B_lane[0] == 'Yasuo' or M_lane[0] == 'Yasuo' or Jung[0] == 'Yasuo' or Pansy[0] == 'Yasuo':
            BanList.append('Jax, Malzahar, Fiora')
            if T_lane[0] == 'Yasuo':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Yasuo':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Yasuo':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Yasuo':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Yasuo':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Zed' or B_lane[0] == 'Zed' or M_lane[0] == 'Zed' or Jung[0] == 'Zed' or Pansy[0] == 'Zed':
            BanList.append('Kayle, Jax, Lissaandra')
            if T_lane[0] == 'Zed':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Zed':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Zed':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Zed':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Zed':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Ziggs' or B_lane[0] == 'Ziggs' or M_lane[0] == 'Ziggs' or Jung[0] == 'Ziggs' or Pansy[0] == 'Ziggs':
            BanList.append('LeBlanc, Syndra, Yasuo')
            if T_lane[0] == 'Ziggs':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Ziggs':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Ziggs':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Ziggs':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Ziggs':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Zilean' or B_lane[0] == 'Zilean' or M_lane[0] == 'Zilean' or Jung[0] == 'Zilean' or Pansy[0] == 'Zilean':
            BanList.append('Sivir, Blitzcrank, Lux')
            if T_lane[0] == 'Zilean':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Zilean':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Zilean':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Zilean':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Zilean':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Zoe' or B_lane[0] == 'Zoe' or M_lane[0] == 'Zoe' or Jung[0] == 'Zoe' or Pansy[0] == 'Zoe':
            BanList.append('Zed, Fizz, Diana')
            if T_lane[0] == 'Zoe':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Zoe':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Zoe':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Zoe':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Zoe':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Zyra' or B_lane[0] == 'Zyra' or M_lane[0] == 'Zyra' or Jung[0] == 'Zyra' or Pansy[0] == 'Zyra':
            BanList.append('Fizz, Katarina, Anivia')
            if T_lane[0] == 'Zyra':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Zyra':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Zyra':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Zyra':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Zyra':
                Pansy.insert(0, '1')
        elif T_lane[0] == 'Neeko' or B_lane[0] == 'Neeko' or M_lane[0] == 'Neeko' or Jung[0] == 'Neeko' or Pansy[0] == 'Neeko':
            BanList.append('Ivern, Fiddlesticks, Nunu')
            if T_lane[0] == 'Neeko':
                T_lane.insert(0, '1')
            elif B_lane[0] == 'Neeko':
                B_lane.insert(0, '1')
            elif M_lane[0] == 'Neeko':
                M_lane.insert(0, '1')
            elif Jung[0] == 'Neeko':
                Jung.insert(0, '1')
            elif Pansy[0] == 'Neeko':
                Pansy.insert(0, '1')
        else:
            print('Sorry, error, champion not selected')
            T_lane.clear()
            B_lane.clear()
            M_lane.clear()
            Jung.clear()
            Pansy.clear()
    ################################################
    ################################################
    ################################################
    ################################################
    ################################################
    ################################################
    ################################################
    ################################################
    ################################################
    ################################################










    #Then at the end of the loop, we tell the user who to ban
    #Not too shabby huh?
    #At the end of out loop we even accounted for accidents with an else
    #The else just tells the user that something was wrong
    #And to ensure a clean restart
    #Clears each list appended via TopLevel

    print('Nice team, Ill do my best to find your optimal bannings. The first entry of each line should be your top priority \n')
    print('\nBased on my calculations \nYour bans should look like \n \n', BanList[0],'\n', BanList[1], '\n', BanList[2], '\n', BanList[3], '\n', BanList[4])
    print('\n \nThank you for using league of legends helper, GLHF!')
    BanList.clear()
    
        
        
        

















#Now i know that last functions was a lot to take in
#But believe me, it's nothing compared to not just writing it all out
#But getting the Syntax correct for all of
#In addition to researching every champions counter











#Anyway, Let's see what i did next


#With all the hard stuff out of the way
#It was time to make buttons to put it all into action


#Buttons 1-5 are here to open our Toplevel windows
#Then take the data and append them to the corrilating Lists
button1 = Button(text='Top', bg="green", fg='black', command=clickSelect1)
button2 = Button(text='Jungle', bg="blue", fg='black', command=clickSelect2)
button3 = Button(text='Mid', bg="purple", fg='black', command=clickSelect3)
button4 = Button(text='Bot', bg="red", fg='black', command=clickSelect4)
button5 = Button(text='Support', bg="pink", fg='black', command=clickSelect5)

#Then we have a button with the lockin function bound
#As to execute our lock in function (The 2000 line fucntion....you cant miss it)
button6 = Button(text='Lock In', bg='orange', fg='white', command=LockIn)

#Then I made a Button for our tier list
#To execture our Tier List TopLevel
#With the best champions by role
#Bound to buttons within the TopLevel
button7 = Button(text='Tier List', bg='Black', fg='white', command=TierList)


#Finally our Print Champions level
#This is just a button for one to use to view every champion
#In our Champs List, as to see if it's all appended correcly
button8 = Button(text='Print Champions', bg='Black', fg='white', command=ShowChampions)
button9 = Button(text='Champ Data', bg='black', fg='white', command=DataBut)


#Before we get to the finished product
#I just needed to find the coordinates
#That i saw most aesthetically pleasing on the map
#For each button to be places
button1.place(x=130, y=80)
button2.place(x=160, y=200)
button3.place(x= 305, y=215)
button4.place(x=480, y= 350)
button5.place(x=440, y=380)

button6.place(x=320, y=430)
button7.place(x=130, y=430)
button8.place(x=0, y=430)
button9.place(x=565, y=430)





  


























































def topsecrettunnel():
    T = Toplevel()
    T.title('Top Secret Link')
    T_label = Label(T, text='Click the button for a suprise')
    T_label.pack()
    
    def supersecretfunction():
        wb.open_new_tab('http://rpart.riotgames.com/na/en/gallery.html')
    secrets = Button(T, text='Suprise', bg='black', fg='white', command=supersecretfunction)
    secrets.pack()

unimportant = Button(text='Do Not Click', bg="brown", fg='white', command=topsecrettunnel)
unimportant.place(x=565, y=0)
    


#And after 2xxx Lines of code here we are
#The mainloop function
#It took a lot of hours
#Couple days
#And a lot of research
#But I was able to do it
#My own Finished application
#Well equped with a user friendly GUI
mainloop()
