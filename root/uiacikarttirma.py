import os
import ui
import app
import grp
import net
import snd
import chat
import player
import locale
import gameInfo
import uiScriptLocale
import uiCommon
import event
import item
import uiToolTip
import mouseModule
import uiPickMoney
import wndMgr

YENILE = 0
islem = 0

class AcikArttirmaWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()

		self.TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
		#gameInfo.MONEY_INPUT = 1
		self.dlgPickMoney = uiPickMoney.PickMoneyDialog()
		self.dlgPickMoney.LoadDialog()
		self.dlgPickMoney.Hide()
	
		self.tek = 0
		self.adet = 0
		self.sayfa = 1
		self.toplam_slot = 100

		self.gosterilenItemler = []

		self.loading = 0
		self.full = 0
		self.zaman = app.GetTime()
		self.menu = ""
		self.menu_alt = ""

		self.itemsayfasi = 0
		self.yenile = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.zaman = app.GetTime()
		self.__LoadWindow()
		self.SetCenterPosition()
		ui.ScriptWindow.Show(self)

		self.GameInfoTemizle()

		gameInfo.PYTHONISLEM = "#acikarttirma_para_ve_itemler#"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)

	def Close(self):
		snd.PlaySound("sound/ui/click.wav")
		self.Hide()

	def GameInfoTemizle(self):
		global YENILE
		gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER = []
		gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER = []
		gameInfo.ACIKARTTIRMA_ITEMLER_LIST = []
		gameInfo.ACIKARTTIRMA_SATIN_AL = 0
		gameInfo.ACIKARTTIRMA_PARA = 0
		YENILE = 0
		self.menu = ""
		self.menu_alt = ""

	def __LoadWindow(self):
		try:			
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/acikarttirmadialog.py")
		except:
			import exception
			exception.Abort("AlisverisWindow.LoadWindow.LoadObject")

		self.ListBox = ui.ListBox_Scroll_Alisveris()
		self.ListBox.SetParent(self.GetChild("board"))
		self.ListBox.SetSize(566 + 75 + 5, 492-25)
		self.ListBox.SetPosition(136, 109)
		self.ListBox.Show()

		self.TitleBar = self.GetChild("TitleBar")
		self.Money_Yatir = self.GetChild("Money_Yatir")
		self.Money_Cek = self.GetChild("Money_Cek")
		self.AnaSayfa = self.GetChild("AnaSayfa")
		self.Itemlerim = self.GetChild("Itemlerim")
		self.Siparisler = self.GetChild("Siparisler")
		self.Teklifler = self.GetChild("Teklifler")
		self.Yenile = self.GetChild("Yenile")

		self.hepsi = self.GetChild("hepsi")
		self.silahlar = self.GetChild("silahlar")
		self.zirhlar = self.GetChild("zirhlar")
		self.kalkanlar = self.GetChild("kalkanlar")
		self.kasklar = self.GetChild("kasklar")
		self.kupeler = self.GetChild("kupeler")
		self.ayakkabilar = self.GetChild("ayakkabilar")
		self.bilezikler = self.GetChild("bilezikler")
		self.diger = self.GetChild("diger")
		self.siparis_ekle = self.GetChild("Siparis_Ekle")
		self.siparis_benim = self.GetChild("Siparis_Benim")
		self.siparis_liste = self.GetChild("Siparis_Liste")
		
		self.AraValue = self.GetChild("FindValue")
		self.Ara = self.GetChild("AraButton")

		self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.Money_Yatir.SetEvent(ui.__mem_func__(self.__MoneyYatir))
		self.Money_Cek.SetEvent(ui.__mem_func__(self.__MoneyCek))
		self.AnaSayfa.SetEvent(ui.__mem_func__(self.__AnaSayfa))
		self.Itemlerim.SetEvent(ui.__mem_func__(self.__Itemlerim))
		self.Teklifler.SetEvent(ui.__mem_func__(self.__Teklifler))
		self.Siparisler.SetEvent(ui.__mem_func__(self.__Siparisler))
		self.Yenile.SetEvent(ui.__mem_func__(self.__Yenile))
		self.Ara.SetEvent(lambda : self.__Ara(self.AraValue.GetText()))
		self.hepsi.SetEvent(ui.__mem_func__(self.__AnaSayfa))
		self.silahlar.SetEvent(ui.__mem_func__(self.__ShowSilahlar))
		self.zirhlar.SetEvent(ui.__mem_func__(self.__ShowZirhlar))
		self.kalkanlar.SetEvent(ui.__mem_func__(self.__ShowKalkanlar))
		self.kasklar.SetEvent(ui.__mem_func__(self.__ShowKasklar))
		self.kupeler.SetEvent(ui.__mem_func__(self.__ShowKupeler))
		self.ayakkabilar.SetEvent(ui.__mem_func__(self.__ShowAyakkabilar))
		self.bilezikler.SetEvent(ui.__mem_func__(self.__ShowBilezikler))
		self.diger.SetEvent(ui.__mem_func__(self.__ShowDiger))
		self.siparis_ekle.SetEvent(ui.__mem_func__(self.__SiparisEkle))
		self.siparis_benim.SetEvent(ui.__mem_func__(self.__SiparisBenim))
		self.siparis_liste.SetEvent(ui.__mem_func__(self.__SiparisListe))

		self.siparis_benim.Hide()
		self.siparis_liste.Hide()
		self.GetChild("yukleniyor").Show()

	def __SiparisEkle(self):
		pass

	def __SiparisBenim(self):
		self.ListBox.ClearItem()
		self.ListBox.Hide()
		self.menu_alt = "benim"
		self.siparis_liste.SetUp()
		#self.siparis_benim.SetUp()
		toplam = 0
			
		yol = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_SIPARIS
		if len(yol) != 0:
			for i in xrange(0, len(yol)):
				bol = yol[i].split("#")
				if bol[24] == player.GetName():
					self.ListBox.Show() #liste'ye eklenecek...
					toplam += 1

		self.GetChild("listelenenitem").Show()
		self.GetChild("listelenenitem_sayi").Show()
		if toplam != 0:
			self.GetChild("listelenenitem_sayi").SetText("|cFFFFFF00|H|h("+str(toplam)+")")
		else:
			self.GetChild("listelenenitem_sayi").SetText("|cFFFF0000|H|h("+str(toplam)+")")

	def __SiparisListe(self):
		self.ListBox.ClearItem()
		self.ListBox.Hide()
		self.menu_alt = "liste"
		self.siparis_benim.SetUp()
		#self.siparis_liste.SetUp()
		toplam = 0

		yol = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_SIPARIS
		if len(yol) != 0:
			for i in xrange(0, len(yol)):
				bol = yol[i].split("#")
				if bol[24] != player.GetName():
					self.ListBox.Show() #liste'ye eklenecek...
					toplam += 1

		self.GetChild("listelenenitem").Show()
		self.GetChild("listelenenitem_sayi").Show()
		if toplam != 0:
			self.GetChild("listelenenitem_sayi").SetText("|cFFFFFF00|H|h("+str(toplam)+")")
		else:
			self.GetChild("listelenenitem_sayi").SetText("|cFFFF0000|H|h("+str(toplam)+")")

	def __Siparisler(self):
		self.menu = "siparis"
		self.menu_alt = "benim"
		self.__SiparisBenim()

	def __ShowSilahlar(self):
		self.GelismisSecenekler(5)
	def __ShowZirhlar(self):
		self.GelismisSecenekler(1)
	def __ShowKalkanlar(self):
		self.GelismisSecenekler(8)
	def __ShowKasklar(self):
		self.GelismisSecenekler(2)
	def __ShowKupeler(self):
		self.GelismisSecenekler(7)
	def __ShowAyakkabilar(self):
		self.GelismisSecenekler(3)
	def __ShowBilezikler(self):
		self.GelismisSecenekler(4)
	def __ShowDiger(self):
		self.GelismisSecenekler(9)

	def GelismisSecenekler(self, gelen):
		self.ListBox.ClearItem()
		self.ListBox.Hide()
		self.gosterilenItemler = []
		toplam = 0
		kontrol = 0
		self.menu = "gelismis_secenekler"
		self.menu_alt = str(gelen)
		if self.menu != "siparis" and len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST) != 0:
			for i in xrange(0, len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST)):
				if not gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i] in self.gosterilenItemler:
					bol = gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")
					if int(bol[27]) == int(gelen):
						items = gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")
						metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
						slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]
						#if bol[24] == player.GetName():
						#	self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
						#else:
						#	self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar", metinAttr, slotAttr)
						if bol[24] == player.GetName():
					#if "sira_"+str(bol[26]) in gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER.keys():
							if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER) != 0:
								for x in xrange(0, len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER)):
									bol2 = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER[x].split("#")
									if "sira_"+str(bol[26]) == bol2[1]:
										kontrol = 1
									else:
										kontrol = 0
								if kontrol == 1:
									self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim_teklifli", metinAttr, slotAttr)
								else:
									self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
							else:
								self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
						else:
							#if "sira_"+str(bol[26]) in gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER.keys():
							if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER) != 0:
								for x2 in xrange(len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER)):
									bol2 = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER[x2].split("#")
									if "sira_"+str(bol[26]) == bol2[1]:
										kontrol = 1
									else:
										pass
										
								if kontrol == 1:
									self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar_teklifli", metinAttr, slotAttr)
								else:
									self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar", metinAttr, slotAttr)
							else:
								self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar", metinAttr, slotAttr)
						self.gosterilenItemler.append(gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i])
						toplam += 1
						self.ListBox.Show()
			self.GetChild("listelenenitem").Show()
			self.GetChild("listelenenitem_sayi").Show()
			if toplam != 0:
				self.GetChild("listelenenitem_sayi").SetText("|cFFFFFF00|H|h("+str(toplam)+")")
			else:
				self.GetChild("listelenenitem_sayi").SetText("|cFFFF0000|H|h("+str(toplam)+")")

	def __AnaSayfa(self):
		self.menu = ""
		self.menu_alt = ""
		self.ListBox.ClearItem()
		self.ListBox.Show()
		self.gosterilenItemler = [] 
		toplam = 0
		if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST) != 0:
			self.ItemEkle()

	def __Itemlerim(self):
		self.menu = "itemlerim"
		self.menu_alt = ""
		self.ListBox.ClearItem_Yenile()
		self.ListBox.Hide()
		self.gosterilenItemler = []
		toplam = 0
		if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST) != 0:
			for i in xrange(0, len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST)):
				kontrol = 0
				if not gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i] in self.gosterilenItemler:
					bol = gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")
					items = gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")
					metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
					slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]
					#if bol[24] == player.GetName():
					#	self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
					#	self.ListBox.Show()
					if bol[24] == player.GetName():
					#if "sira_"+str(bol[26]) in gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER.keys():
						if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER) != 0:
							for x in xrange(0, len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER)):
								bol2 = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER[x].split("#")
								if "sira_"+str(bol[26]) == bol2[1]:
									kontrol = 1
								else:
									pass
							if kontrol == 1:
								self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim_teklifli", metinAttr, slotAttr)
							else:
								self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
						else:
							self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
						toplam += 1
					else:
						pass
					self.ListBox.Show()
					self.gosterilenItemler.append(gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i])
			self.GetChild("listelenenitem").Show()
			self.GetChild("listelenenitem_sayi").Show()
			if toplam != 0:
				self.GetChild("listelenenitem_sayi").SetText("|cFFFFFF00|H|h("+str(toplam)+")")
			else:
				self.GetChild("listelenenitem_sayi").SetText("|cFFFF0000|H|h("+str(toplam)+")")

	def __Teklifler(self):
		self.menu = "tekliflerim"
		self.menu_alt = ""
		self.ListBox.ClearItem_Yenile()
		self.ListBox.Hide()
		self.gosterilenItemler = []
		toplam = 0
		if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST) != 0:
			for i in xrange(0, len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST)):
				kontrol = 0
				if not gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i] in self.gosterilenItemler:
					bol = gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")
					items = gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")
					metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
					slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]
					if bol[24] != player.GetName():
						if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER) != 0:
							for x in xrange(0, len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER)):
								bol2 = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER[x].split("#")
								if "sira_"+str(bol[26]) == bol2[1]:
									kontrol = 1
								else:
									pass
							if kontrol == 1:
								self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar_teklifli", metinAttr, slotAttr)
								self.ListBox.Show()
								toplam += 1
							else:
								pass
								#self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
						#else:
						#	self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
					self.gosterilenItemler.append(gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i])
			self.GetChild("listelenenitem").Show()
			self.GetChild("listelenenitem_sayi").Show()
			if toplam != 0:
				self.GetChild("listelenenitem_sayi").SetText("|cFFFFFF00|H|h("+str(toplam)+")")
			else:
				self.GetChild("listelenenitem_sayi").SetText("|cFFFF0000|H|h("+str(toplam)+")")

	def __Yenile(self):
		self.menu = ""
		self.menu_alt = ""
		self.ListBox.ClearItem()
		self.gosterilenItemler = []
		gameInfo.ACIKARTTIRMA_ITEMLER_LIST = []

		self.GameInfoTemizle()

		gameInfo.PYTHONISLEM = "#acikarttirma_para_ve_itemler#"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)

		self.GetChild("yukleniyor").Show()
		self.tek = 0
		self.loading = 0
		self.full = 0
		self.zaman = app.GetTime()

	def __Ara(self, isim):
		self.menu = ""
		self.menu_alt = ""
		self.gosterilenItemler = []
		self.ListBox.ClearItem_Yenile()
		self.ListBox.Hide()
		#isim = self.AraValue.GetText()
		isim = isim
		toplam = 0
		if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST) != 0:
			for i in xrange(0, len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST)):
				kontrol = 0
				bol = gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")
				items = gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")
				#metinAttr = [items[3],items[4],items[5],items[6],items[7],items[8]]
				#slotAttr =  [(items[9],items[10]),(items[11],items[12]),(items[13],items[14]),(items[15],items[16]),(items[17],items[18]),(items[19],items[20]),(items[21],items[22])]
				metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
				slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]
				item.SelectItem(int(bol[1]))
				ad = item.GetItemName()
				if str(ad).find(isim) != -1:
					self.menu = "aramalar"
					self.menu_alt = isim
					if bol[24] == player.GetName():
						if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER) != 0:
							for x in xrange(0, len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER)):
								bol2 = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER[x].split("#")
								if "sira_"+str(bol[26]) == bol2[1]:
									kontrol = 1
								else:
									kontrol = 0
							if kontrol == 1:
								self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim_teklifli", metinAttr, slotAttr)
							else:
								self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
						else:
							self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
					else:
						if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER) != 0:
							for x2 in xrange(len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER)):
								bol2 = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER[x2].split("#")
								if "sira_"+str(bol[26]) == bol2[1]:
									kontrol = 1
								else:
									pass
									
							if kontrol == 1:
								self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar_teklifli", metinAttr, slotAttr)
							else:
								self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar", metinAttr, slotAttr)
						else:
							self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar", metinAttr, slotAttr)
					#if bol[24] == player.GetName():
					#	self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
					#else:
					#	self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar", metinAttr, slotAttr)
					######self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar", metinAttr, slotAttr)
					self.ListBox.Show()
					toplam += 1
			self.GetChild("listelenenitem").Show()
			self.GetChild("listelenenitem_sayi").Show()
			if toplam != 0:
				self.GetChild("listelenenitem_sayi").SetText("|cFFFFFF00|H|h("+str(toplam)+")")
			else:
				self.GetChild("listelenenitem_sayi").SetText("|cFFFF0000|H|h("+str(toplam)+")")

	def __MoneyYatir(self):
		gameInfo.MONEY_DIALOG = 1
		ParaManager().Open(1, 0, 0, 0, 0) #islem, item sira, item kodu, item satici, fiyat
	
	def __MoneyCek(self):
		gameInfo.MONEY_DIALOG = 2
		ParaManager().Open(2, 0, 0, 0, 0) #islem, item sira, item kodu, item satici, fiyat

	def SendChat(self, gelen):
		chat.AppendChat(chat.CHAT_TYPE_INFO, str(gelen))

	def OnUpdate(self):
		global YENILE
		self.GetChild("Money").SetText(str(locale.NumberToMoneyString(gameInfo.ACIKARTTIRMA_PARA)))

		if gameInfo.ACIKARTTIRMA_SATIN_AL == 1 and YENILE == 0:
			self.ListBox.ClearItem_Yenile()
			self.gosterilenItemler = []
			self.GetChild("listelenenitem").Hide()
			self.GetChild("listelenenitem_sayi").Hide()
			if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST) != 0:
				if self.menu == "gelismis_secenekler":
					self.GelismisSecenekler(int(self.menu_alt))
				elif self.menu == "itemlerim":
					self.__Itemlerim()
				elif self.menu == "tekliflerim":
					self.__Teklifler()
				elif self.menu == "aramalar":
					self.__Ara(self.menu_alt)
				else:
					self.ItemEkle()
			
			if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST) == 0:
				self.GetChild("listelenenitem").Show()
				self.GetChild("listelenenitem_sayi").Show()
				self.GetChild("listelenenitem_sayi").SetText("|cFFFF0000|H|h(0)")

			gameInfo.ACIKARTTIRMA_SATIN_AL = 0
			YENILE = 1

		if self.menu == "siparis":
			self.GetChild("findtext").Hide()
			self.GetChild("FindSlot").Hide()
			self.GetChild("FindValue").Hide()
			self.GetChild("AraButton").Hide()
			self.GetChild("item_satici").SetText("Alýcý")
			if self.menu_alt == "benim":
				self.siparis_benim.Down()
				#self.siparis_liste.SetUp()
			elif self.menu_alt == "liste":
				self.siparis_liste.Down()
				#self.siparis_benim.SetUp()
			self.siparis_ekle.Show()
			self.siparis_benim.Show()
			self.siparis_liste.Show()
		else:
			self.GetChild("findtext").Show()
			self.GetChild("FindSlot").Show()
			self.GetChild("FindValue").Show()
			self.GetChild("AraButton").Show()
			self.GetChild("item_satici").SetText("Satýcý")
			self.siparis_ekle.Hide()
			self.siparis_benim.Hide()
			self.siparis_liste.Hide()

		if self.full < 102:
			self.GetChild("yukleniyor").SetFontName("Tahoma:60")
			self.GetChild("yukleniyor").SetText("%"+str(self.full))
			self.full += 1

		if self.full == 101 and self.loading == 0:
			self.GetChild("yukleniyor").Hide()
			self.loading = 1

		if app.GetTime() < self.zaman + 2:
			self.ListBox.Hide()
			self.GetChild("listelenenitem").Hide()
			self.GetChild("listelenenitem_sayi").Hide()
		else:
			if self.tek == 0 and len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST) != 0:
				self.ItemEkle()
				self.tek = 1
			
			if self.tek == 0 and len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST) == 0:
				self.GetChild("listelenenitem").Show()
				self.GetChild("listelenenitem_sayi").Show()
				self.GetChild("listelenenitem_sayi").SetText("|cFFFF0000|H|h(0)")

		self.GetChild("renk_rakip").SetText("|c000000|H|hNormally item")
		self.GetChild("renk_senin").SetText("|cFFFF0000|H|hYour")
		self.GetChild("renk_teklif").SetText("|cFFFFFF00|H|hYours (with bids)")
		self.GetChild("renk_teklif_verdigin").SetText("|cFF32CD32|H|hYour offer")

	def ItemEkle(self):
		for i in xrange(0, len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST)):
			kontrol = 0
			if not gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i] in self.gosterilenItemler:
				bol = gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")
				items = gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")
				metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
				slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]
				if bol[24] == player.GetName():
					#if "sira_"+str(bol[26]) in gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER.keys():
					if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER) != 0:
						for x in xrange(0, len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER)):
							bol2 = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER[x].split("#")
							if "sira_"+str(bol[26]) == bol2[1]:
								kontrol = 1
							else:
								pass
						if kontrol == 1:
							self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim_teklifli", metinAttr, slotAttr)
						else:
							self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
					else:
						self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "benim", metinAttr, slotAttr)
				else:
					#if "sira_"+str(bol[26]) in gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER.keys():
					if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER) != 0:
						for x2 in xrange(len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER)):
							bol2 = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER[x2].split("#")
							if "sira_"+str(bol[26]) == bol2[1]:
								kontrol = 1
							else:
								pass
								
						if kontrol == 1:
							self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar_teklifli", metinAttr, slotAttr)
						else:
							self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar", metinAttr, slotAttr)
					else:
						self.ListBox.InsertItem(i, bol[1], bol[2], bol[25], bol[24], bol[26], "esyalar", metinAttr, slotAttr)
					self.gosterilenItemler.append(gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i])
		self.GetChild("listelenenitem").Show()
		self.GetChild("listelenenitem_sayi").Show()
		if len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST) != 0:
			self.GetChild("listelenenitem_sayi").SetText("|cFFFFFF00|H|h("+str(len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST))+")")
		else:
			self.GetChild("listelenenitem_sayi").SetText("|cFFFF0000|H|h("+str(len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST))+")")
		self.ListBox.Show()

class ParaManager(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		self.type = None
		self.yatirButton = None
		self.cekButton = None
		self.Money = None

		self.islemler = 0
		self.item_sira = 0
		self.item_kodu = 0
		self.item_satici = ""
		self.item_fiyat = 0
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/moneydialog.py")
		except:
			import exception
			exception.Abort("test.__LoadScript.LoadObject")

		try: 
			self.board = self.GetChild("Board")
			self.titleBar = self.GetChild("TitleBar")
			self.yatirButton = self.GetChild("yatirButton")
			self.cekButton = self.GetChild("cekButton")
			self.girilenInput = self.GetChild("Input")
			
			self.yang_text = self.GetChild("yang_girilen")
			self.yang_slot = self.GetChild("yang_resim")
			self.yang_input = self.GetChild("Input")
			
			## Aliþveriþe uygun yerler ##
			"""
			self.board.SetSize(210, 70)
			self.SetPosition(210, 70)
			self.cekButton.Hide()
			self.titleBar.SetWidth(210-15) """
			self.board.SetSize(210, 90)
			self.SetPosition(210, 90)
			self.cekButton.Hide()
			self.titleBar.SetWidth(210-15)

			self.GirdiginPara = ui.TextLine_Alisveris()
			self.GirdiginPara.SetParent(self.board)
			self.GirdiginPara.SetPosition(0, 35)
			if self.girilenInput.GetText() == "" or self.girilenInput.GetText() == 0:
				self.GirdiginPara.SetText("0 Yang")
			else:
				self.GirdiginPara.SetText(str(locale.NumberToMoneyString(self.girilenInput.GetText())))
			self.GirdiginPara.SetWindowHorizontalAlignCenter()
			self.GirdiginPara.SetHorizontalAlignCenter()
			self.GirdiginPara.Show()

			## Aliþveriþ TitleName ##
			self.GetChild("TitleName").SetText("Enter the Price")

			## Aliþveriþ Butonlarýn SetText ve ToolTipText'leri ##
			self.yatirButton.SetText("Add")
			self.yatirButton.SetToolTipText("Add to Auction!")

		except:
			import exception
			exception.Abort("test.__LoadScript.BindObject")
			
		self.girilenInput.SetMax(10)
		self.girilenInput.SetNumberMode()
			
		self.yatirButton.SetEvent(self.__OnClickYatirButton)
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.isLoaded = TRUE

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Destroy(self):
		self.Hide()
		
	def Open(self, islem, sira, kod, satici, fiyat):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		self.girilenInput.SetText("")
		self.SetTop()
		self.SetCenterPosition()
		self.Show()

		self.Islem(islem, sira, kod, satici, fiyat)
		
	def GetType(self):
		return self.type
	
	def __OnClickYatirButton(self):
		global YENILE
		money = self.girilenInput.GetText()
		if money == "" or int(money) == 0:
			self.girilenInput.SetText("")
			return

		if self.islemler == 1:
			if player.GetElk() < int(money):
				chat.AppendChat(chat.CHAT_TYPE_INFO, "<Auction House> : You dont have enough to money.")
				return

			if int(gameInfo.ACIKARTTIRMA_PARA)+int(money) > 1999999999:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "<Auction House> : You cant carry more money 2T")
				return

			gameInfo.ACIKARTTIRMA_PARA += int(money)
			gameInfo.PYTHONISLEM = "acikarttirma_para_ekle#"+str(money)+"#"
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)
			
		elif self.islemler == 2:
			if int(money) > int(gameInfo.ACIKARTTIRMA_PARA):
				chat.AppendChat(chat.CHAT_TYPE_INFO, "<Auction House> : You dont have enough to money for withdraw.")
				return

			gameInfo.ACIKARTTIRMA_PARA -= int(money)
			gameInfo.PYTHONISLEM = "acikarttirma_para_cek#"+str(money)+"#"
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)

		elif self.islemler == 3:  #islem, item sira, item kodu, item satici, fiyat
			if int(money) > int(self.item_fiyat):
				chat.AppendChat(chat.CHAT_TYPE_INFO, "<Auction House> : You can not give a higher bid price than the normal price.")
				return
	
			gameInfo.PYTHONISLEM = "acikarttirma_teklifver#"+str(money)+"#"+str(self.item_sira)+"#"+str(self.item_kod)+"#"+str(self.item_satici)+"#"
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)

			i = 0
			while i < len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST):
				if gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")[26] == str(self.item_sira):
					del gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i]
					break
				else:
					i += 1
	
			if gameInfo.ACIKARTTIRMA_SATIN_AL == 0:
				gameInfo.ACIKARTTIRMA_SATIN_AL = 1

			YENILE = 0
	
		self.Close()
	
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def Islem(self, islem, sira, kod, satici, fiyat): #islem, item sira, item kodu, item satici, fiyat
		if islem == 1:
			self.GetChild("TitleName").SetText("Deposit money")
			self.yatirButton.SetText("deposit")
			self.islemler = 1
		elif islem == 2:
			self.GetChild("TitleName").SetText("Withdraw Money")
			self.yatirButton.SetText("Withdraw")
			self.islemler = 2
		elif islem == 3:
			item.SelectItem(int(kod))
			self.GetChild("TitleName").SetText(str(item.GetItemName()))
			self.yatirButton.SetText("Bid")
			self.islemler = 3
			self.item_sira = int(sira)
			self.item_kod = int(kod)
			self.item_satici = satici
			self.item_fiyat = int(fiyat)

			#self.yang_text.SetPosition(15, 40+30)
			#self.yang_slot.SetPosition(48, 40+30)
			#self.yang_input.SetPosition(90, 18+30)

			#self.yatirButton.SetPosition(140, 40+30)
			#self.cekButton.SetPosition(140+65, 40+30)

	def OnUpdate(self):
		if self.girilenInput.GetText() == "" or self.girilenInput.GetText() == 0:	
			self.GirdiginPara.SetText("0 Yang")
		else:
			if int(self.girilenInput.GetText()) >= 1999999999:
				#self.yatirButton.Down()
				self.GirdiginPara.SetText("|cFFFF0000|H|h"+str(locale.NumberToMoneyString(self.girilenInput.GetText())))
			else:
				#self.yatirButton.SetUp()
				#self.yatirButton.Enable()
				#self.yatirButton.SetUp()
				self.GirdiginPara.SetText(str(locale.NumberToMoneyString(self.girilenInput.GetText())))

	def OnPressExitKey(self):
		self.Close()
		return TRUE

class EsyaEkleWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		self.type = None
		self.yatirButton = None
		self.cekButton = None
		self.Money = None
		self.islemler = 0
		self.ItemSlot = 0
		self.ItemVnum = 0
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/acikarttirmadialog_esyaekle.py")
		except:
			import exception
			exception.Abort("test.__LoadScript.LoadObject")

		try: 
			self.board = self.GetChild("board")
			self.titleBar = self.GetChild("TitleBar")
			self.wndSlot = self.GetChild("Item_Slot")
			self.toolTip = uiToolTip.ItemToolTip()
			self.para = self.GetChild("ParaValue")
			
			self.koyButton = self.GetChild("TamamButton")
			self.iptalButton = self.GetChild("IptalButton")
	
		except:
			import exception
			exception.Abort("test.__LoadScript.BindObject")
			
		#self.girilenInput.SetMax(10)
		#self.girilenInput.SetNumberMode()
			
		self.koyButton.SetEvent(self.__OnClickEsyaKoy)
		self.iptalButton.SetEvent(self.Close)
		#self.yatirButton.SetEvent(self.__OnClickYatirButton)

		self.wndSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.wndSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.wndSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		self.wndSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		self.wndSlot.SetUnselectItemSlotEvent(ui.__mem_func__(self.UnselectItemSlot))
		self.wndSlot.SetUsableItem(TRUE)
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.isLoaded = TRUE

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Destroy(self):
		self.Hide()
		
	def Open(self):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		#self.girilenInput.SetText("")
		self.SetTop()
		self.SetCenterPosition()
		self.Show()
	
	def OverInItem(self, index):
		self.toolTip.ClearToolTip()
		slotIndex = self.ItemSlot

		itemVnum = player.GetItemIndex(slotIndex)
		itemCount = player.GetItemCount(slotIndex)
		
		metinSlot = [player.GetItemMetinSocket(slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		attrSlot = [player.GetItemAttribute(slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
		
		self.toolTip.AddRefineItemData(itemVnum, metinSlot, attrSlot)
			
	def OverOutItem(self):
		self.toolTip.Hide()

	def SelectEmptySlot(self, selectedSlotPos):
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			itemVnum = player.GetItemIndex(attachedSlotPos)
			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				self.wndSlot.SetItemSlot(0, itemVnum , player.GetItemCount(attachedSlotPos))
				self.ItemSlot = attachedSlotPos
				self.ItemVnum = itemVnum
		mouseModule.mouseController.DeattachObject()

	def UnselectItemSlot(self, selectedSlotPos):
		self.ClearSlot()

	def SelectItemSlot(self, selectedSlotPos):
		slotIndex = self.ItemSlot
		curCursorNum = app.GetCursor()
		selectedSlotPos = selectedSlotPos
		selectedItemID = player.GetItemIndex(slotIndex)
		itemCount = player.GetItemCount(slotIndex)
		type = player.SLOT_TYPE_PRIVATE_SHOP
		mouseModule.mouseController.AttachObject(self, type, selectedSlotPos, selectedItemID, itemCount)
		mouseModule.mouseController.SetCallBack("INVENTORY", ui.__mem_func__(self.DropToInventory))
		snd.PlaySound("sound/ui/pick.wav")
		self.ClearSlot()
		
	def DropToInventory(self):
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		self.ClearSlot()
		
	def ClearSlot(self):
		self.ItemSlot = -1
		self.ItemVnum = -1
		
		self.wndSlot.ClearSlot(0)
		self.wndSlot.RefreshSlot()

	def GetType(self):
		return self.type
	
	def __OnClickEsyaKoy(self):
		money = self.para.GetText()
		if money == "" or int(money) == 0:
			self.para.SetText("")
			return

		types = ""
		item.SelectItem(int(self.ItemVnum))
		if item.IsWearableFlag(item.WEARABLE_BODY):
			types = "1"
		elif item.IsWearableFlag(item.WEARABLE_HEAD):
			types = "2"
		elif item.IsWearableFlag(item.WEARABLE_FOOTS):
			types = "3"
		elif item.IsWearableFlag(item.WEARABLE_WRIST):
			types = "4"
		elif item.IsWearableFlag(item.WEARABLE_WEAPON):
			types = "5"
		elif item.IsWearableFlag(item.WEARABLE_NECK):
			types = "6"
		elif item.IsWearableFlag(item.WEARABLE_EAR):
			types = "7"
		elif item.IsWearableFlag(item.WEARABLE_SHIELD):
			types = "8"
		else:
			types = "9"
		
		gameInfo.PYTHONISLEM = "acikarttirma_itemkoy#"+str(self.ItemSlot)+"#"+str(self.ItemVnum)+"#"+str(money)+"#"+str(types)+"#"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		
		self.Close()
		#AlisverisWindow().Yenile()
	
	def SendSystemChat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "<Auction House: "+str(text))
	
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnUpdate(self):
		if self.para.GetText() == "" or self.para.GetText() == 0:
			self.GetChild("findtext").SetText("Price : 0 Yang")
		else:
			self.GetChild("findtext").SetText("Price : " + str(locale.NumberToMoneyString(self.para.GetText())))
		
	def OnPressExitKey(self):
		self.Close()
		return TRUE
