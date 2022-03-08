import uiScriptLocale
import gameInfo

ICON_PATH = "icon/item/"
ROOT_PATH = "d:/ymir work/ui/public/"
ROOT_PATH2 = "d:/ymir work/ui/game/windows/"
SLOT_PATH = "d:/ymir work/ui/public/Slot_Base.sub"

EK_X = 76
BUTTON_EK_X = 7

window = {
	"name" : "AcikArttirmaDialog",

	"x" : SCREEN_WIDTH/2 - 120,
	"y" : 94,

	"style" : ("movable", "float",),

	"width" : 724 + EK_X,
	"height" : 615-19,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 724 + EK_X,
			"height" : 615-19,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : 724 + EK_X - 15,
					"color" : "gray",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":314+76, "y":4, "text":"Auction House", "text_horizontal_align":"center" },
					),
				},

				## Para Slot ##
				{
					"name":"Money_Slot",
					"type":"button",

					"x":42,
					"y":42,


					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

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
							"name" : "Money",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",

							"text" : "158.312.756 Yang",
						},
					),
				},
				
				{ "name" : "Money_Yatir", "type":"button", "tooltip_text" : "Deposit money to Auction House", "x": 176, "y": 45, "default_image" : ROOT_PATH2+"btn_plus_up.sub", "over_image" : ROOT_PATH2+"btn_plus_over.sub", "down_image" : ROOT_PATH2+"btn_plus_down.sub", },
				{ "name" : "Money_Cek", "type":"button", "tooltip_text" : "Withdraw money from Auction House", "x": 194, "y": 45, "default_image" : ROOT_PATH2+"btn_minus_up.sub", "over_image" : ROOT_PATH2+"btn_minus_over.sub", "down_image" : ROOT_PATH2+"btn_minus_down.sub", },

				## Butonlar ##
				{
					"name" : "AnaSayfa",
					"type" : "button",

					"x" : 410 + EK_X - 45 + 34,
					"y" : 40,

					"width" : 61,
					"height" : 21,

					"text" : "Home",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "Itemlerim",
					"type" : "button",

					"x" : 474 + EK_X - 45 + 34,
					"y" : 40,

					"width" : 61,
					"height" : 21,

					"text" : "My Items",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "Siparisler",
					"type" : "button",

					"x" : 538 + EK_X - 45 + 9000,
					"y" : 40,

					"width" : 61,
					"height" : 21,

					"text" : "Sipariþler", #Disable.

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "Teklifler",
					"type" : "button",

					#"x" : 601 + EK_X - 45,
					"x" : 538 + EK_X - 45 + 34,
					"y" : 40,

					"width" : 61,
					"height" : 21,

					"text" : "For Bidding",
					"tooltip_text" : "Your gave offers",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				{
					"name" : "Yenile",
					"type" : "button",

					#"x" : 674 + EK_X - 45 - 10,
					"x" : 601 + EK_X - 45 + 34,
					"y" : 40,

					"width" : 61,
					"height" : 21,

					"text" : "Refresh",

					"default_image" : "d:/ymir work/ui/public/small_thin_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_thin_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_thin_button_03.sub",
				},

				## Sipariþler Menüsü Butonlarý ##

				{
					"name" : "Siparis_Ekle",
					"type" : "button",

					"x" : 674 + EK_X - 45 - 10 - 134 - 20 - 64 + 9,
					"y" : 40 + 25 + 8,

					"width" : 61,
					"height" : 21,

					"text" : "Sipariþ Ver",
					"tooltip_text" : "Hemen item sipariþi ver!",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},


				{
					"name" : "Siparis_Benim",
					"type" : "button",

					"x" : 674 + EK_X - 45 - 10 - 134 - 20 + 9,
					"y" : 40 + 25 + 8,

					"width" : 61,
					"height" : 21,

					"text" : "Benim",
					"tooltip_text" : "Sipariþ verdiðin itemler listesi",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				{
					"name" : "Siparis_Liste",
					"type" : "button",

					"x" : 674 + EK_X - 45 - 10 - 134 + 64 - 20 + 9,
					"y" : 40 + 25 + 8,

					"width" : 61,
					"height" : 21,

					"text" : "Sipariþ L.",
					"tooltip_text" : "Sipariþ listesi",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## Eþya Arama ##
				{
				"name" : "findtext", "type" : "text", "x" : 408 + EK_X, "y" : 70, "text" : "Search: " , "fontsize" : "LARGE"
				},

				{
					"name" : "FindSlot",
					"type" : "slotbar",
					"x" : 458 + EK_X,
					"y" : 68,
					"width" : 150,
					"height" : 18,

					"children" :
					(
						{
							"name" : "FindValue",
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
					"name" : "AraButton",
					"type" : "button",

					"x" : 613 + EK_X,
					"y" : 67,

					"text" : "Search",

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				},

				## Geliþmiþ Seçenekler ##
				{
				"name" : "gelismistext", "type" : "text", "x" : 18, "y" : 81, "text" : "Advanced Options: " , "fontsize" : "LARGE"
				},

				{
				"name" : "listelenenitem", "type" : "text", "x" : 18+137, "y" : 81, "text" : "Total Item" , "fontsize" : "LARGE"
				},

				{
				"name" : "listelenenitem_sayi", "type" : "text", "x" : 18+137+115-32, "y" : 81, "text" : "(21)" , "fontsize" : "LARGE", "text_color" : 0xffF8BF24
				},

				{
					"name" : "gelismis_thinboard",
					"type" : "thinboard",
		
					"x" : 19,
					"y" : 111,
					
					"width" : 104,
					"height" : 240,

				},

				## Renk Bilgilendirmesi

				{ "name" : "renk_thinboard", "type" : "thinboard", "x" : 19, "y" : 244+111+9+21, "width" : 104, "height" : 72, },
				{
				"name" : "renk_title", "type" : "text", "x" : 18, "y" : 244+111+9, "text" : "Color Notes:", "fontsize" : "LARGE"
				},
				{
				"name" : "renk_rakip", "type" : "text", "x" : 25+5+4+2+3-2, "y" : 244+111+9+15+21-10, "text" : "Baþkasýnýn", "fontsize" : "LARGE",
				},
				{
				"name" : "renk_senin", "type" : "text", "x" : 25+9+5+5+2+2+3, "y" : 244+111+9+9+12+17+4+2+21-10+17, "text" : "Senin", "fontsize" : "LARGE",
				},
				{ 
				"name" : "renk_teklif_verdigin", "type" : "text", "x" : 25+4+1+2+3-4, "y" : 244+111+9+12+19+21-10, "text" : "Teklif Verdiðin" , "fontsize" : "LARGE",
				},
				{ 
				"name" : "renk_teklif", "type" : "text", "x" : 25+4+1+2+3, "y" : 244+111+9+12+19+21-10+17, "text" : "Senin(Teklif)" , "fontsize" : "LARGE",
				},

				{ 
					"name":"ItemBaslik", 
					"type":"horizontalbar", 

					"x":149, 
					"y":74+17 + 14, 

					"width":608, 

					"children" : 
					(

						{ "name" : "item_adi", "type" : "text", "x" : 90+18-27, "y" : 1, "text" : "Name " , "fontsize" : "LARGE" },
						{ "name" : "item_adeti", "type" : "text", "x" : 90+75+7, "y" : 1, "text" : "Count " , "fontsize" : "LARGE" },
						{ "name" : "item_fiyati", "type" : "text", "x" : 90+75+75+13, "y" : 1, "text" : "Price" , "fontsize" : "LARGE" },
						{ "name" : "item_satici", "type" : "text", "x" : 90+75+75+75+60, "y" : 1, "text" : "Owner" , "fontsize" : "LARGE" },
						
					),
				},

				{ "name" : "hepsi", "type":"button", "text" : "All", "x": 27, "y": 121, "default_image" : ROOT_PATH+"large_button_01.sub", "over_image" : ROOT_PATH+"large_button_02.sub", "down_image" : ROOT_PATH+"large_button_03.sub", },
				{ "name" : "silahlar", "type":"button", "text" : "Weapons", "x": 27, "y": 151, "default_image" : ROOT_PATH+"large_button_01.sub", "over_image" : ROOT_PATH+"large_button_02.sub", "down_image" : ROOT_PATH+"large_button_03.sub", },
				{ "name" : "zirhlar", "type":"button", "text" : "Armors", "x": 27, "y": 175, "default_image" : ROOT_PATH+"large_button_01.sub", "over_image" : ROOT_PATH+"large_button_02.sub", "down_image" : ROOT_PATH+"large_button_03.sub", },
				{ "name" : "kalkanlar", "type":"button", "text" : "Shields", "x": 27, "y": 199, "default_image" : ROOT_PATH+"large_button_01.sub", "over_image" : ROOT_PATH+"large_button_02.sub", "down_image" : ROOT_PATH+"large_button_03.sub", },
				{ "name" : "kasklar", "type":"button", "text" : "Heads", "x": 27, "y": 224, "default_image" : ROOT_PATH+"large_button_01.sub", "over_image" : ROOT_PATH+"large_button_02.sub", "down_image" : ROOT_PATH+"large_button_03.sub", },
				{ "name" : "kupeler", "type":"button", "text" : "Ears", "x": 27, "y": 248, "default_image" : ROOT_PATH+"large_button_01.sub", "over_image" : ROOT_PATH+"large_button_02.sub", "down_image" : ROOT_PATH+"large_button_03.sub", },
				{ "name" : "ayakkabilar", "type":"button", "text" : "Shoes", "x": 27, "y": 272, "default_image" : ROOT_PATH+"large_button_01.sub", "over_image" : ROOT_PATH+"large_button_02.sub", "down_image" : ROOT_PATH+"large_button_03.sub", },
				{ "name" : "bilezikler", "type":"button", "text" : "Bracelets", "x": 27, "y": 296, "default_image" : ROOT_PATH+"large_button_01.sub", "over_image" : ROOT_PATH+"large_button_02.sub", "down_image" : ROOT_PATH+"large_button_03.sub", },
				{ "name" : "diger", "type":"button", "text" : "Other", "x": 27, "y": 320, "default_image" : ROOT_PATH+"large_button_01.sub", "over_image" : ROOT_PATH+"large_button_02.sub", "down_image" : ROOT_PATH+"large_button_03.sub", },

				## Eþya Listesi ##
				
				{ "name" : "esyalar_thinboard", "type" : "thinboard", "x" : 136, "y" : 109+15, "width" : 566 + EK_X - 13, "height" : 492-15-16 },

				
				## Loading Text
				{
				"name" : "yukleniyor", "type" : "text", "x" : 400-15, "y" : 275+16, "text" : "%0 " , "fontsize" : "LARGE"
				}, 

				## CopyRight ##
				{ 
				"name" : "copyright", "type" : "text", "x" : 20, "y" : 585-29, "text" : "© Copyright 2015" , "fontsize" : "LARGE",
				},

				{ 
				"name" : "copyright_name", "type" : "text", "x" : 20+5, "y" : 585+15-29, "text" : "Auction House " , "fontsize" : "LARGE",
				},
			
			),
		},
	),
}