import gameInfo
import event
import uiacikarttirma
import uiCommon

	def __ServerCommand_Build(self):
		serverCommandList={

			## New System Plugin ##
			"PythonToLua"			: self.__PythonToLua, # .python to Quest
			"PythonIslem"			: self.__PythonIslem, # .python to Quest
			"LuaToPython"			: self.__LuaToPython, # Quest to .python
			## END - New System Plugin - END ##

		}

	def OpenQuestWindow(self, skin, idx):
		if gameInfo.INPUT == 1:
			return
		self.interface.OpenQuestWindow(skin, idx)

	
	## add the funcs end of line (en alt satýra fonksiyonlarý ekle)##
	def __PythonToLua(self, id):
		gameInfo.PYTHONTOLUA = int(id)

	def __PythonIslem(self, PythonIslem):
		if PythonIslem == "PYTHONISLEM":
			net.SendQuestInputStringPacket(gameInfo.PYTHONISLEM)
		
	def __LuaToPython(self, LuaToPython):
		if LuaToPython.find("#quest_input#") != -1:
			gameInfo.INPUT = 1
		elif LuaToPython.find("#quest_inputbitir#") != -1:
			gameInfo.INPUT = 0

		elif LuaToPython.find("#acikarttirma_para#") != -1:
			bol = LuaToPython.split("#")
			gameInfo.ACIKARTTIRMA_PARA = int(bol[2])
		elif LuaToPython.find("alisveris_item_ekle#") != -1:
			self.ac = uiacikarttirma.EsyaEkleWindow()
			self.ac.Open()
		elif LuaToPython.find("alisveris_itemler") != -1:
			bol = LuaToPython.split("|")
			gameInfo.ACIKARTTIRMA_ITEMLER_LIST.insert(0, str(bol[1]))
		elif LuaToPython.find("alisxveris_itemler_gelen_teklifler") != -1:
			bol = LuaToPython.split("|")
			bol_ = LuaToPython.split("#")
			gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER.insert(0, "#sira_"+str(bol_[26])+str(bol[1]))
		elif LuaToPython.find("alisxveris_itemler_verilen_teklifler") != -1:
			bol = LuaToPython.split("|")
			bol_ = LuaToPython.split("#")
			gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER.insert(0, "#sira_"+str(bol_[26])+str(bol[1]))
		elif LuaToPython.find("alisxveris_itemler_yenile") != -1:
			bol = LuaToPython.split("#")
	
			i = 0
			while i < len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST):
				if gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i].split("#")[26] == bol[1]:
					del gameInfo.ACIKARTTIRMA_ITEMLER_LIST[i]
					break
				else:
					i += 1
	
			gameInfo.ACIKARTTIRMA_SATIN_AL = 1
		elif LuaToPython.find("acikarttirma_para_yok") != -1:
			self.parayok = uiCommon.PopupDialog()
			self.parayok.SetText("You dont have enough to money.")
			self.parayok.Open()

	""" for the open the auctionhaus menu (açýk arttýrma menüsünü açmak için) """
		import uiacikarttirma
		self.ac = uiacikarttirma.AcikArttirmaWindow()
		self.ac.Show()