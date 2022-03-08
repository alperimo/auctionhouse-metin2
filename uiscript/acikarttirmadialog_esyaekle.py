import uiScriptLocale

ICON_PATH = "icon/item/"
ROOT_PATH = "d:/ymir work/ui/public/"
ROOT_PATH2 = "d:/ymir work/ui/game/windows/"
SLOT_PATH = "d:/ymir work/ui/public/Slot_Base.sub"

EK_X = 76
BUTTON_EK_X = 7

EK_Y = 0

window = {
	"name" : "AcikArttirmaDialog_EsyaEkle",

	"x" : SCREEN_WIDTH/2 - 120,
	"y" : 94,

	"style" : ("movable", "float",),

	"width" : 185,
	"height" : 180 + EK_Y,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 185,
			"height" : 180 + EK_Y,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : 185 - 15,
					"color" : "gray",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":86-5, "y":4, "text":"Add the item to Auction House", "text_horizontal_align":"center" },
					),
				},

				## Item Slot ##
				{
					"name" : "Item_Slot",
					"type" : "grid_table",

					"x" : 14,
					"y" : 40-7,

					"start_index" : 0,
					"x_count" : 1,
					"y_count" : 3,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},

				## Eþya Arama ##
				{
				"name" : "findtext", "type" : "text", "x" : 10+7, "y" : 159-13-8-5, "text" : "Fiyat: " , "fontsize" : "LARGE"
				},

				{
					"name" : "FindSlot",
					"type" : "slotbar",
					"x" : 70-49+4,
					"y" : 159-7,
					"width" : 150,
					"height" : 18,

					"children" :
					(

						{
							"name":"Money_Icon",
							"type":"image",

							"x":-18,
							"y":2,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
						},
						
						{
							"name" : "ParaValue",
							"type" : "editline",
							"x" : 2,
							"y" : 3,
							"width" : 150,
							"height" : 16,
							"input_limit" : 20,
							"text" : "",
						},

					),
				},

				{
					"name" : "TamamButton",
					"type" : "button",

					"x" : 85,
					"y" : 85+8 - 9,

					"text" : "Add",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				{
					"name" : "IptalButton",
					"type" : "button",

					"x" : 85,
					"y" : 85+24+8 - 9,

					"text" : "Cancel",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## Geliþmiþ Seçenekler ##
				{
				"name" : "gelismistext", "type" : "text", "x" : 18+42-10, "y" : 81-15 - 9, "text" : "Do you want to add? " , "fontsize" : "LARGE"
				},



				#"""
				## Loading Text
				#{
				#"name" : "yukleniyor", "type" : "text", "x" : 150-30, "y" : 140+30, "text" : "%0 " , "fontsize" : "LARGE"
				#}, """

				#"""
				#{
				#"name" : "textsort", "type" : "text", "x" : 23, "y" : 430, "text" : "Sirala: " , "fontsize" : "LARGE"
				#}, """
			
			),
		},
	),
}