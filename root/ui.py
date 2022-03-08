import gameInfo
import localegame
import event
import chat
import net

class TextLine_Alisveris(Window):
	def __init__(self):
		Window.__init__(self)
		self.max = 0
		self.SetFontName(locale.UI_DEF_FONT_LARGE)

	def __del__(self):
		Window.__del__(self)

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterTextLine(self, layer)

	def SetMax(self, max):
		wndMgr.SetMax(self.hWnd, max)

	def SetLimitWidth(self, width):
		wndMgr.SetLimitWidth(self.hWnd, width)

	def SetMultiLine(self):
		wndMgr.SetMultiLine(self.hWnd, TRUE)

	def SetHorizontalAlignArabic(self):
		wndMgr.SetHorizontalAlign(self.hWnd, wndMgr.TEXT_HORIZONTAL_ALIGN_ARABIC)

	def SetHorizontalAlignLeft(self):
		wndMgr.SetHorizontalAlign(self.hWnd, wndMgr.TEXT_HORIZONTAL_ALIGN_LEFT)

	def SetHorizontalAlignRight(self):
		wndMgr.SetHorizontalAlign(self.hWnd, wndMgr.TEXT_HORIZONTAL_ALIGN_RIGHT)

	def SetHorizontalAlignCenter(self):
		wndMgr.SetHorizontalAlign(self.hWnd, wndMgr.TEXT_HORIZONTAL_ALIGN_CENTER)

	def SetVerticalAlignTop(self):
		wndMgr.SetVerticalAlign(self.hWnd, wndMgr.TEXT_VERTICAL_ALIGN_TOP)

	def SetVerticalAlignBottom(self):
		wndMgr.SetVerticalAlign(self.hWnd, wndMgr.TEXT_VERTICAL_ALIGN_BOTTOM)

	def SetVerticalAlignCenter(self):
		wndMgr.SetVerticalAlign(self.hWnd, wndMgr.TEXT_VERTICAL_ALIGN_CENTER)

	def SetSecret(self, Value=TRUE):
		wndMgr.SetSecret(self.hWnd, Value)

	def SetOutline(self, Value=TRUE):
		wndMgr.SetOutline(self.hWnd, Value)

	def SetFeather(self, value=TRUE):
		wndMgr.SetFeather(self.hWnd, value)

	def SetFontName(self, fontName):
		wndMgr.SetFontName(self.hWnd, fontName)

	def SetDefaultFontName(self):
		wndMgr.SetFontName(self.hWnd, locale.UI_DEF_FONT)

	def SetFontColor(self, red, green, blue):
		wndMgr.SetFontColor(self.hWnd, red, green, blue)

	def SetPackedFontColor(self, color):
		wndMgr.SetFontColor(self.hWnd, color)

	def SetText(self, text):
		wndMgr.SetText(self.hWnd, text)

	def GetText(self):
		return wndMgr.GetText(self.hWnd)

	def GetTextSize(self):
		return wndMgr.GetTextSize(self.hWnd)

class Button_Alisveris(Window):
	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

		self.eventFunc = None
		self.eventArgs = None

		self.ButtonText = None
		self.ToolTipText = None

		self.kod = 0

		import uiToolTip
		self.toolTipAlignment = uiToolTip.ToolTip(130)
		self.imageToolTip = uiToolTip.ItemToolTip()
		self.imageToolTip.HideToolTip()

	def __del__(self):
		Window.__del__(self)

		self.eventFunc = None
		self.eventArgs = None

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterButton(self, layer)

	def SetUpVisual(self, filename):
		wndMgr.SetUpVisual(self.hWnd, filename)

	def SetOverVisual(self, filename):
		wndMgr.SetOverVisual(self.hWnd, filename)

	def SetDownVisual(self, filename):
		wndMgr.SetDownVisual(self.hWnd, filename)

	def SetDisableVisual(self, filename):
		wndMgr.SetDisableVisual(self.hWnd, filename)

	def GetUpVisualFileName(self):
		return wndMgr.GetUpVisualFileName(self.hWnd)

	def GetOverVisualFileName(self):
		return wndMgr.GetOverVisualFileName(self.hWnd)

	def GetDownVisualFileName(self):
		return wndMgr.GetDownVisualFileName(self.hWnd)

	def GetText(self):
		if not self.ButtonText:
			return
		return self.ButtonText.GetText()

	def Flash(self):
		wndMgr.Flash(self.hWnd)

	def Enable(self):
		wndMgr.Enable(self.hWnd)

	def Disable(self):
		wndMgr.Disable(self.hWnd)

	def Down(self):
		wndMgr.Down(self.hWnd)

	def SetUp(self):
		wndMgr.SetUp(self.hWnd)

	def SAFE_SetEvent(self, func, *args):
		self.eventFunc = __mem_func__(func)
		self.eventArgs = args
		
	def SetEvent(self, func, *args):
		self.eventFunc = func
		self.eventArgs = args

	def SetTextColor(self, color):
		if not self.ButtonText:
			return
		self.ButtonText.SetPackedFontColor(color)

	def SetText(self, text, height = 4):

		if not self.ButtonText:
			textLine = TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(self.GetWidth()/2, self.GetHeight()/2)
			textLine.SetVerticalAlignCenter()
			textLine.SetHorizontalAlignCenter()
			textLine.Show()
			self.ButtonText = textLine

		self.ButtonText.SetText(text)

	def SetRotation(self, rotation):
		wndMgr.SetRotation(self.hWnd, rotation)

	def SetFormToolTipText(self, type, itemKodu, metinAttr, slotAttr, x, y):
		import player
	
		self.imageToolTip.ClearToolTip()
		self.imageToolTip.AddRefineItemData(int(itemKodu), metinAttr, slotAttr)
		self.imageToolTip.HideToolTip()

	def SetFormToolTipTextGame(self, type, text, x, y):
		self.toolTipAlignment.ClearToolTip()
		self.toolTipAlignment.AutoAppendTextLine(text)
		self.toolTipAlignment.AlignHorizonalCenter()
		self.toolTipAlignment.SetPosition(x + self.GetWidth()/2, y)

	def SetToolTipWindow(self, toolTip):		
		self.ToolTipText=toolTip		
		self.ToolTipText.SetParentProxy(self)

	def SetToolTipImage(self, itemKodu, metinAttr, slotAttr, x=0, y = -19):
		self.SetFormToolTipText("TEXT", itemKodu, metinAttr, slotAttr, x, y)

	def SetToolTipTextGame(self, text, x=0-29, y = -29):
		self.SetFormToolTipTextGame("TEXT", text, x, y)

	def CallEvent(self):
		snd.PlaySound("sound/ui/click.wav")

		if self.eventFunc:
			apply(self.eventFunc, self.eventArgs)

	def ShowToolTip(self):

		self.imageToolTip.ShowToolTip()

	def HideToolTip(self):

		self.imageToolTip.HideToolTip()
			
	def IsDown(self):
		return wndMgr.IsDown(self.hWnd)

## class Listbox'un altýna
class ListBox_Scroll(ListBox):
	def __init__(self):
		ListBox.__init__(self)
		
		self.scrollBar = ScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar.Show()

	def SetSize(self, width, height):
		ListBox.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
		Window.SetSize(self, width, height)
		
		self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH, 0)
		#if gameInfo.MESSAGE_ACIK == 1:
		#	self.scrollBar.SetScrollBarSize(height+23)
		#else:
		self.scrollBar.SetScrollBarSize(height)

	def ClearItem(self):
		ListBox.ClearItem(self)
		self.scrollBar.SetPos(0)

	def _LocateItem(self):
		ListBox._LocateItem(self)
		
		if self.showLineCount < len(self.itemList):
			#self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			self.scrollBar.Show()
		else:
			#self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			self.scrollBar.Hide()

	def GetViewItemCount(self):
		return self.showLineCount

	def GetItemCount(self):
		return len(self.itemList)

	def GetSelectedItemAdi(self):
		secilen = self.textDict.get(self.selectedLine, 0)
		return secilen

	def __OnScroll(self):
		scrollLen = self.GetItemCount()-self.GetViewItemCount()
		if scrollLen < 0:
			scrollLen = 0
		self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))


class Listbox_Alisveris(Window):

	IMAGE_HEIGHT = 32
	TEMPORARY_PLACE = 3
	INFO_IMG_WIDTH = 12
	INFO_IMG_HEIGHT = 12

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.overLine = -1
		self.selectedLine = -1
		self.width = 0
		self.height = 0
		self.stepSize = 17
		self.basePos = 0
		self.showLineCount = 0
		self.itemWidth = 0
		self.itemCenterAlign = TRUE
		import uiToolTip
		self.toolTip = uiToolTip.ItemToolTip()
		self.imageToolTip = uiToolTip.ItemToolTip()
		self.imageToolTip.HideToolTip()

		self.item = []

		self.arkaPlanList = []
		self.itemList = []
		self.itemNameList = []
		self.itemIconList = []
		self.itemAdetList = []
		self.itemFiyatList = []
		self.itemSaticiList = []
		self.SatinAlButtonList = []
		self.TeklifVerButtonList = []

		self.keyDict = {}
		self.textDict = {}
		self.nameDict = {}
		self.levelDict = {}
		self.bayrakDict = {}

		self.event = lambda *arg: None
		
	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.height)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetTextCenterAlign(self, flag):
		self.itemCenterAlign = flag

	def SetBasePos(self, pos):
		self.basePos = pos
		self._LocateItem()

	def ClearItem(self):
		self.keyDict = {}
		self.textDict = {}
		self.nameDict = {}
		self.levelDict = {}
		self.bayrakDict = {}

		self.item = []

		self.arkaPlanList = []
		self.itemList = []
		self.itemNameList = []
		self.itemIconList = []
		self.itemAdetList = []
		self.itemFiyatList = []
		self.itemSaticiList = []
		self.SatinAlButtonList = []
		self.TeklifVerButtonList = []

		self.overLine = -1
		self.selectedLine = -1
	
	def InsertItem(self, number, itemKodu, itemAdet, itemFiyat, itemSatici, itemSiraNo, itemKimin, metinAttr, slotAttr):
		self.keyDict[len(self.itemList)] = number

		arkaplan = ThinBoard()
		arkaplan.SetParent(self)
		arkaplan.SetSize(534+75, 58)
		arkaplan.Hide()

		item.SelectItem(int(itemKodu))

		#self.itemIcon = ImageBox()
		#self.itemIcon.SetParent(self)
		#self.itemIcon.LoadImage(str(item.GetIconImageFileName()))
		#self.itemIcon.Show()

		(itemWidth, itemHeight) = item.GetItemSize()

		self.itemIcon = Button_Alisveris()
		self.itemIcon.SetParent(self)
		self.itemIcon.SetPosition(352, 10)
		self.itemIcon.SetUpVisual(str(item.GetIconImageFileName()))
		self.itemIcon.SetOverVisual(str(item.GetIconImageFileName()))
		self.itemIcon.SetDownVisual(str(item.GetIconImageFileName()))
		self.itemIcon.SetToolTipImage(int(itemKodu), metinAttr, slotAttr)
		self.itemIcon.w = itemWidth
		self.itemIcon.h = itemHeight
		self.itemIcon.Show()

		adi = TextLine_Alisveris()
		adi.SetParent(self)
		if itemKimin == "esyalar":
			adi.SetText(str(item.GetItemName()))
		elif itemKimin == "esyalar_teklifli":
			adi.SetText("|cFF32CD32|H|h"+str(item.GetItemName()))
		elif itemKimin == "benim":
			adi.SetText("|cFFFF0000|H|h"+str(item.GetItemName()))
		elif itemKimin == "benim_teklifli":
			adi.SetText("|cFFFFFF00|H|h"+str(item.GetItemName()))
		adi.SetFeather()
		adi.SetOutline()
		adi.Show()
		
		adet = TextLine_Alisveris()
		adet.SetParent(self)
		adet.SetPosition(20, 3)
		if itemKimin == "esyalar":
			adet.SetText(str(itemAdet))
		elif itemKimin == "esyalar_teklifli":
			adet.SetText("|cFF32CD32|H|h"+str(itemAdet))
		elif itemKimin == "benim":
			adet.SetText("|cFFFF0000|H|h"+str(itemAdet))
		elif itemKimin == "benim_teklifli":
			adet.SetText("|cFFFFFF00|H|h"+str(itemAdet))
		adet.Show()
		
		fiyat = TextLine_Alisveris()
		fiyat.SetParent(self)
		fiyat.SetPosition(20+20, 3)
		if itemKimin == "esyalar":
			fiyat.SetText(str(locale.NumberToMoneyString(itemFiyat)))
		elif itemKimin == "esyalar_teklifli":
			fiyat.SetText("|cFF32CD32|H|h"+str(locale.NumberToMoneyString(itemFiyat)))
		elif itemKimin == "benim":
			fiyat.SetText("|cFFFF0000|H|h"+str(locale.NumberToMoneyString(itemFiyat)))
		elif itemKimin == "benim_teklifli":
			fiyat.SetText("|cFFFFFF00|H|h"+str(locale.NumberToMoneyString(itemFiyat)))
		fiyat.Show()

		satici = TextLine_Alisveris()
		satici.SetParent(self)
		satici.SetPosition(20+20, 3)
		if itemKimin == "esyalar":
			satici.SetText(str(itemSatici))
		elif itemKimin == "esyalar_teklifli":
			satici.SetText("|cFF32CD32|H|h"+str(itemSatici))
		elif itemKimin == "benim":
			satici.SetText("|cFFFF0000|H|h"+str(itemSatici))
		elif itemKimin == "benim_teklifli":
			satici.SetText("|cFFFFFF00|H|h"+str(itemSatici))
		satici.Show()

		if itemKimin == "esyalar":
			satinAlButton = Button()
			satinAlButton.SetParent(self)
			satinAlButton.SetPosition(352, 10)
			satinAlButton.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
			satinAlButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
			satinAlButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
			satinAlButton.SetText("Buy")
			satinAlButton.SetToolTipText(localegame.ACIKARTTIRMA_SATINAL_TEXT)
			satinAlButton.Show()
			satinAlButton.kimin = "esyalar"
			satinAlButton.SetEvent(lambda : self.SatinAl(itemSiraNo, itemKodu, itemSatici, itemFiyat))

			teklifVerButton = Button()
			teklifVerButton.SetParent(self)
			teklifVerButton.SetPosition(382, 10)
			teklifVerButton.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
			teklifVerButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
			teklifVerButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
			teklifVerButton.SetText("Bid")
			teklifVerButton.SetToolTipText(localegame.ACIKARTTIRMA_TEKLIFVER_TEXT)
			teklifVerButton.Show()
			teklifVerButton.kimin = "esyalar"
			teklifVerButton.SetEvent(lambda : self.TeklifVer(itemSiraNo, itemKodu, itemSatici, itemFiyat))
		elif itemKimin == "esyalar_teklifli":
			satinAlButton = Button()
			satinAlButton.SetParent(self)
			satinAlButton.SetPosition(352, 10)
			satinAlButton.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
			satinAlButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
			satinAlButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
			satinAlButton.SetText("Buy")
			satinAlButton.SetToolTipText(localegame.ACIKARTTIRMA_SATINAL_TEXT)
			satinAlButton.Show()
			satinAlButton.kimin = "esyalar_teklifli"
			satinAlButton.SetEvent(lambda : self.SatinAl(itemSiraNo, itemKodu, itemSatici, itemFiyat))

			teklifVerButton = Button()
			teklifVerButton.SetParent(self)
			teklifVerButton.SetPosition(382, 10)
			teklifVerButton.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
			teklifVerButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
			teklifVerButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
			teklifVerButton.SetText("Cancel To Offer")
			teklifVerButton.SetToolTipText("Cancel to Offer.")
			teklifVerButton.Show()
			teklifVerButton.kimin = "esyalar_teklifli"
			teklifVerButton.SetEvent(lambda : self.TeklifIptal(itemSiraNo, itemKodu, itemSatici, itemFiyat))
		elif itemKimin == "benim":
			satinAlButton = Button()
			satinAlButton.SetParent(self)
			satinAlButton.SetPosition(360, 10)
			satinAlButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
			satinAlButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
			satinAlButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
			satinAlButton.SetText("Take Back")
			satinAlButton.Show()
			satinAlButton.kimin = "benim"
			satinAlButton.SetEvent(lambda : self.GeriAl(itemSiraNo, itemKodu, itemSatici))

			teklifVerButton = Button()
			teklifVerButton.SetParent(self)
			teklifVerButton.SetPosition(382, 10)
			teklifVerButton.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
			teklifVerButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
			teklifVerButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
			teklifVerButton.SetText("Bid")
			teklifVerButton.SetToolTipText(localegame.ACIKARTTIRMA_TEKLIFVER_TEXT)
			teklifVerButton.Show()
			teklifVerButton.kimin = "benim"
			teklifVerButton.SetEvent(lambda : self.TeklifVer(itemSiraNo, itemKodu, itemSatici, itemFiyat))
		elif itemKimin == "benim_teklifli":
			satinAlButton = Button()
			satinAlButton.SetParent(self)
			satinAlButton.SetPosition(352, 10)
			satinAlButton.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
			satinAlButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
			satinAlButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
			satinAlButton.SetText("Take Back")
			satinAlButton.SetToolTipText(localegame.ACIKARTTIRMA_SATINAL_TEXT)
			satinAlButton.Show()
			satinAlButton.kimin = "benim_teklifli"
			satinAlButton.SetEvent(lambda : self.GeriAl(itemSiraNo, itemKodu, itemSatici))

			teklifVerButton = Button()
			teklifVerButton.SetParent(self)
			teklifVerButton.SetPosition(382, 10)
			teklifVerButton.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
			teklifVerButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
			teklifVerButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
			teklifVerButton.SetText("My Offers")
			teklifVerButton.SetToolTipText("Incoming Offers")
			teklifVerButton.Show()
			teklifVerButton.kimin = "benim_teklifli"
			teklifVerButton.SetEvent(lambda : self.TeklifleriGor(itemSiraNo, itemKodu, itemSatici, itemFiyat))

		self.arkaPlanList.append(arkaplan)
		self.item.append("ekle")
		self.itemNameList.append(adi)
		self.itemIconList.append(self.itemIcon)
		self.itemAdetList.append(adet)
		self.itemFiyatList.append(fiyat)
		self.itemSaticiList.append(satici)
		self.SatinAlButtonList.append(satinAlButton)
		self.TeklifVerButtonList.append(teklifVerButton)

		self._LocateItem()

	def SatinAl(self, sira, kod, satici, fiyat):
		import player
		import uiacikarttirma
		uiacikarttirma.YENILE = 0
		gameInfo.PYTHONISLEM = "acikarttirma_satinal#"+str(sira)+"#"+str(kod)+"#"+str(satici)+"#"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)

	def GeriAl(self, sira, kod, satici):
		import uiacikarttirma
		uiacikarttirma.YENILE = 0
		gameInfo.PYTHONISLEM = "acikarttirma_gerial#"+str(sira)+"#"+str(kod)+"#"+str(satici)+"#"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)

	def TeklifVer(self, sira, kod, satici, fiyat):
		import uiacikarttirma
		self.ac = uiacikarttirma.ParaManager()
		self.ac.Open(3, sira, kod, satici, fiyat) #islem, item sira, item kodu, item satici, fiyat

	def TeklifIptal(self, sira, kod, satici, fiyat):
		import uiacikarttirma
		#if "sira_"+str(sira) in gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER.keys():
		i = 0
		while i < len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER):
			if gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER[i].split("#")[27] == sira:
				del gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER[i]
				break
			else:
				i += 1
		#del gameInfo.ACIKARTTIRMA_ITEMLER_LIST_VERILEN_TEKLIFLER["sira_"+str(sira)]
		gameInfo.ACIKARTTIRMA_SATIN_AL = 1
		uiacikarttirma.YENILE = 0

		gameInfo.PYTHONISLEM = "acikarttirma_teklifiptal#"+str(sira)+"#"+str(kod)+"#"+str(satici)+"#"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)

	def TeklifleriGor(self, sira, kod, satici, fiyat):
		self.Board = BoardWithTitleBar()
		self.Board.SetSize(241+30, 271+40+40-17)
		self.Board.SetCenterPosition()
		self.Board.AddFlag('movable')
		self.Board.AddFlag('float')
		item.SelectItem(int(kod))
		self.Board.SetTitleName('Incoming Offers')
		self.Board.SetCloseEvent(self.Kapat)
		self.Board.Show()

		self.TekliflerText = TextLine_Alisveris()
		self.TekliflerText.SetParent(self.Board)
		self.TekliflerText.SetPosition(0, 30)
		self.TekliflerText.SetText(str(item.GetItemName()) + ' - Number : ' + str(sira))
		self.TekliflerText.SetWindowHorizontalAlignCenter()
		self.TekliflerText.SetHorizontalAlignCenter()
		self.TekliflerText.Show()

		self.ThinBoard = ThinBoard()
		self.ThinBoard.SetParent(self.Board)
		self.ThinBoard.SetSize(241-18+26, 250)
		self.ThinBoard.SetPosition(10+9-5-3, 48)
		self.ThinBoard.Show()

		self.ListBox=ListBox_Scroll()
		self.ListBox.SetParent(self.Board)
		self.ListBox.SetPosition(10+9, 50)
		self.ListBox.SetSize(241-18+26-8, 250)
		self.ListBox.SetEvent(__mem_func__(self.__OnSelectListBox))
		self.ListBox.Show()

		self.teklifKabulButton = Button()
		self.teklifKabulButton.SetParent(self.Board)
		self.teklifKabulButton.SetPosition(69, 301)
		self.teklifKabulButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.teklifKabulButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.teklifKabulButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.teklifKabulButton.SetText("Accept")
		self.teklifKabulButton.SetToolTipText("Accept to Offer")
		self.teklifKabulButton.Show()
		self.teklifKabulButton.Down()
		self.teklifKabulButton.SetEvent(lambda : self.TeklifKabulEt(sira, kod, satici))

		self.teklifRedButton = Button()
		self.teklifRedButton.SetParent(self.Board)
		self.teklifRedButton.SetPosition(80+120-56, 301)
		self.teklifRedButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.teklifRedButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.teklifRedButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.teklifRedButton.SetText("Refuse")
		self.teklifRedButton.SetToolTipText("Refuse to Offer")
		self.teklifRedButton.Show()
		self.teklifRedButton.Down()
		self.teklifRedButton.SetEvent(lambda : self.TeklifRedEt(sira, kod, satici))

		self.ListBox.ClearItem()
		x = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER
		pos = 0
		if len(x) != 0:
			for i in xrange(0, len(x)):
				bol = x[i].split("#")
				#if bol[26] == sira:
				if bol[1] == "sira_"+sira:
					self.ListBox.InsertItem(pos, str(bol[30]) + " : " + locale.NumberToMoneyString(str(bol[29])))
					pos += 1

	def __OnSelectListBox(self):
		if self.teklifKabulButton.IsDown() or self.teklifKabulButton.IsDown():
			self.teklifKabulButton.Enable()
			self.teklifKabulButton.SetUp()
			self.teklifRedButton.SetUp()
			self.teklifRedButton.SetUp()

	def TeklifKabulEt(self, sira, kod, satici):
		import uiacikarttirma
		secilen = self.ListBox.GetSelectedItemAdi()

		i = 0
		while i < len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER):
			bol = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER[i].split("#")
			if bol[27] == sira and bol[30] == secilen.split(" :")[0]:
				del gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER[i]
				chat.AppendChat(chat.CHAT_TYPE_INFO, '<Offers> : Offer accepted.')
				break
			else:
				i += 1

		self.ListBox.ClearItem()
		x = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER
		pos = 0
		if len(x) != 0:
			for i in xrange(0, len(x)):
				bol = x[i].split("#")
				if bol[1] == "sira_"+sira:
					self.ListBox.InsertItem(pos, str(bol[30]) + " : " + locale.NumberToMoneyString(str(bol[29])))
					pos += 1

		## Kabul ettiðinde "Geri al" Butonunu kapatma Fix ##
		xdd = 0
		while i < len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST):
			bol = gameInfo.ACIKARTTIRMA_ITEMLER_LIST[xdd].split("#")
			if bol[27] == sira and bol[1] == kod and bol[24] == satici and satici == player.GetName():
				del gameInfo.ACIKARTTIRMA_ITEMLER_LIST[xdd]
				break
			else:
				xdd += 1

		gameInfo.PYTHONISLEM = "acikarttirma_teklifkabulet#"+str(sira)+"#"+str(kod)+"#"+str(satici)+"#"+str(secilen.split(" :")[0])
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		gameInfo.ACIKARTTIRMA_SATIN_AL = 1
		uiacikarttirma.YENILE = 0

	def TeklifRedEt(self, sira, kod, satici):
		import uiacikarttirma
		secilen = self.ListBox.GetSelectedItemAdi()
		#chat.AppendChat(chat.CHAT_TYPE_INFO, str(secilen))
		#chat.AppendChat(chat.CHAT_TYPE_INFO, str(secilen.split(" :")[0]) + " VE " + str(secilen.split(": ")[1]))
		#secilen = self.ChannelList.GetSelectedItemAdi()
		i = 0
		while i < len(gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER):
			bol = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER[i].split("#")
			#if bol[27] == sira and bol[30] == secilen.split(" :")[0] and bol[29] == secilen.split(": ")[1].split(" Altýn")[0]:
			if bol[27] == sira and bol[30] == secilen.split(" :")[0]:
				del gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER[i]
				chat.AppendChat(chat.CHAT_TYPE_INFO, '<Offers> : Offer refused.')
				break
			else:
				i += 1

		self.ListBox.ClearItem()
		x = gameInfo.ACIKARTTIRMA_ITEMLER_LIST_GELEN_TEKLIFLER
		pos = 0
		if len(x) != 0:
			for i in xrange(0, len(x)):
				bol = x[i].split("#")
				#if bol[26] == sira:
				if bol[1] == "sira_"+sira:
					self.ListBox.InsertItem(pos, str(bol[30]) + " : " + locale.NumberToMoneyString(str(bol[29])))
					pos += 1


		gameInfo.PYTHONISLEM = "acikarttirma_teklifreddet#"+str(sira)+"#"+str(kod)+"#"+str(satici)+"#"+str(secilen.split(" :")[0])
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		gameInfo.ACIKARTTIRMA_SATIN_AL = 1
		uiacikarttirma.YENILE = 0

	def Kapat(self):
		self.Board.Hide()
		self.TekliflerText.Hide()
		self.ThinBoard.Hide()
		self.ListBox.Hide()

	def ChangeItem(self, number, text, tooltipText, textlineText, width):
		for key, value in self.keyDict.items():
			if value == number:
				self.textDict[key] = text + tooltipText + textlineText + width

				if number < len(self.itemList):
					self.itemList[key].SetText(text)

				return

	def LocateItem(self):
		self._LocateItem()

	def _LocateItem(self):

		skipCount = self.basePos
		yPos = 25
		self.showLineCount = 0

		for i in xrange(0, len(self.item)):
			arkaPlan = self.arkaPlanList[i]
			itemIcon = self.itemIconList[i]
			nameLine = self.itemNameList[i]
			adetTextLine = self.itemAdetList[i]
			fiyatTextLine = self.itemFiyatList[i]
			saticiTextLine = self.itemSaticiList[i]
			satinAlButton = self.SatinAlButtonList[i]
			teklifVerButton = self.TeklifVerButtonList[i]

			arkaPlan.Hide()
			itemIcon.Hide()
			nameLine.Hide()
			adetTextLine.Hide()
			fiyatTextLine.Hide()		
			saticiTextLine.Hide()
			satinAlButton.Hide()
			teklifVerButton.Hide()
			
			if skipCount > 0:
				skipCount -= 1
				continue
	
			ek = 8
	
			arkaPlan.SetPosition(18-ek, yPos + 3)
			if itemIcon.h == 1:
				itemIcon.SetPosition(25-ek, yPos + 14)
			else:
				itemIcon.SetPosition(25-ek, yPos + 14 - 9 - 5)
			nameLine.SetPosition(50+55-21-13-ek-7, yPos + 18)
			adetTextLine.SetPosition(162+55-21-ek, yPos + 18)
			fiyatTextLine.SetPosition(192+55-ek, yPos + 18)
			saticiTextLine.SetPosition(277+55+53-ek, yPos + 18)
			if satinAlButton.kimin == "esyalar" or satinAlButton.kimin == "esyalar_teklifli":
				satinAlButton.SetPosition(497+15-ek, yPos + 17)
			elif satinAlButton.kimin == "benim":
				satinAlButton.SetPosition(497+15-ek+9, yPos + 17)
			elif satinAlButton.kimin == "benim_teklifli":
				satinAlButton.SetPosition(497+15-ek, yPos + 17)
			teklifVerButton.SetPosition(497+43+15-ek, yPos + 17)

			yPos += 63

			if yPos <= self.GetHeight():
				arkaPlan.Show()
				itemIcon.Show()
				nameLine.Show()
				adetTextLine.Show()
				fiyatTextLine.Show()		
				saticiTextLine.Show()
				satinAlButton.Show()
				if teklifVerButton.kimin == "esyalar" or teklifVerButton.kimin == "esyalar_teklifli":
					teklifVerButton.Show()
				elif teklifVerButton.kimin == "benim":
					teklifVerButton.Hide()
				elif teklifVerButton.kimin == "benim_teklifli":
					teklifVerButton.Show()

	def ArrangeItem(self):
		self.SetSize(self.width)
		self.SetSize(self.width, len(self.itemList) * 17)
		self._LocateItem()

	def GetViewItemCount(self):
		return self.showLineCount

	def GetItemCount(self):
		return len(self.itemList)

	def SetEvent(self, event):
		self.event = event

	def SelectItem(self, line):

		if not self.keyDict.has_key(line):
			return

		if line == self.selectedLine:
			return

		self.selectedLine = line
		self.event(self.keyDict.get(line, 0), self.textDict.get(line, "None"))
		
		x, y = self.GetGlobalPosition()

	def GetSelectedItem(self):
		return self.keyDict.get(self.selectedLine, 0)

	def OnMouseLeftButtonDown(self):
		if self.overLine < 0:
			return

	def OnMouseLeftButtonUp(self):
		if self.overLine >= 0:
			self.SelectItem(self.overLine+self.basePos)

	def OnUpdate(self):

		x, y = self.GetGlobalPosition()
		xMouse, yMouse = wndMgr.GetMousePosition()
		loc_x, loc_y = xMouse-x, yMouse-y

		#loc_x_img, loc_y_img = 10 + 32 - self.INFO_IMG_WIDTH, self.GetHeight() / 2 - 32 / 2
		#img_width, img_height = self.INFO_IMG_WIDTH, self.INFO_IMG_HEIGHT
		#if self.itemIcon.IsShow() and loc_x >= loc_x_img and loc_x <= loc_x_img+img_width and loc_y >= loc_y_img and loc_y <= loc_y_img+img_height:
			#self.defaultToolTip.ShowToolTip()
		#	self.imageToolTip.ShowToolTip()
		#else:
		#	#self.defaultToolTip.HideToolTip()
		#	loc_x_img, loc_y_img = 10, self.GetHeight() / 2 - 16
		#	img_width, img_height = self.itemWidth*32, self.IMAGE_HEIGHT
		#	if loc_x >= loc_x_img and loc_x <= loc_x_img+img_width and loc_y >= loc_y_img and loc_y <= loc_y_img+img_height:
		#		self.imageToolTip.ShowToolTip()
		#	else:
		#		self.imageToolTip.HideToolTip()

		self.overLine = -1

		if self.IsIn():
			self.SelectItem(self.overLine+self.basePos)
			x, y = self.GetGlobalPosition()
			height = self.GetHeight()
			xMouse, yMouse = wndMgr.GetMousePosition()

			if yMouse - y < height - 1:
				self.overLine = (yMouse - y) / self.stepSize

				if self.overLine < 0:
					self.overLine = -1
				if self.overLine >= len(self.itemList):
					self.overLine = -1

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		yRender -= self.TEMPORARY_PLACE
		widthRender = self.width
		heightRender = self.height + self.TEMPORARY_PLACE*2

		if locale.IsCIBN10:
			if -1 != self.overLine and self.keyDict[self.overLine] != -1:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3, self.stepSize)

			if -1 != self.selectedLine and self.keyDict[self.selectedLine] != -1:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3, self.stepSize)

		else:		
			if -1 != self.overLine:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3, self.stepSize)				

			if -1 != self.selectedLine:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3, self.stepSize)
		
class ListBox_Scroll_Alisveris(Listbox_Alisveris):
	def __init__(self):
		Listbox_Alisveris.__init__(self)
		
		self.viewItemCount=7
		self.basePos=0
		self.itemHeight=6
		self.itemStep=6
		self.scrollBar = ScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar.Hide()

	def SetSize(self, width, height):
		Listbox_Alisveris.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
		Window.SetSize(self, width, height)
		
		self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH + 5, 5)
		self.scrollBar.SetScrollBarSize(height)

	def ClearItem(self):
		Listbox_Alisveris.ClearItem(self)
		self.scrollBar.SetPos(0)

	def ClearItem_Yenile(self):
		scrollLen = self.GetItemCount()-self.GetViewItemCount()
		if scrollLen < 0:
			scrollLen = 0
		Listbox_Alisveris.ClearItem(self)
		self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))
		Listbox_Alisveris._LocateItem(self)
		#self.scrollBar.SetPos(0)

	def _LocateItem(self):
		Listbox_Alisveris._LocateItem(self)
		
		if self.showLineCount < len(self.item):
			self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			#self.scrollBar.SetPos(0)
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()

		if len(self.item) < 8:
			self.scrollBar.Hide()

	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollEvent(__mem_func__(self.__OnScroll))
		self.scrollBar=scrollBar
		
	def __OnScroll(self):
		scrollLen = self.GetItemCount()-self.GetViewItemCount()
		if scrollLen < 0:
			scrollLen = 0
		self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))
		Listbox_Alisveris._LocateItem(self)

	def __GetScrollLen(self):
		scrollLen=self.__GetItemCount()-self.__GetViewItemCount()
		if scrollLen<0:
			return 0

		return scrollLen
		

	def GetViewItemCount(self):
		return self.viewItemCount

	def GetItemCount(self):
		return len(self.item)

	def GetItemViewCoord(self, pos, itemWidth):
		if locale.IsARABIC():
			return (self.GetWidth()-itemWidth-15, (pos-self.basePos)*self.itemStep)
		else:
			return (0, (pos-self.basePos)*self.itemStep)
			
	def __IsInViewRange(self, pos):
		if pos<self.basePos:
			return 0
		if pos>=self.basePos+self.viewItemCount:
			return 0
		return 1