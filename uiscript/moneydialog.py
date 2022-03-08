import uiScriptLocale
BOARDWIDTH = 210+68
BOARDHEIGHT = 70+20

window = {
	"name" : "depo_para_manager",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH/2-BOARDWIDTH/2,
	"y" : SCREEN_HEIGHT/2-BOARDHEIGHT/2,

	"width" : BOARDWIDTH,
	"height" : BOARDHEIGHT,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARDWIDTH,
			"height" : BOARDHEIGHT,

			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : BOARDWIDTH-15,
					"color" : "red",

					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",
							"text" : "Depo yang iþlemleri",
							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"x" : 0,
							"y" : 3,
						},
					),
				},
				{
					"name" : "yang_girilen",
					"type" : "text",
					"text" : "Yang",
					"horizontal_align" : "Center",
					"x" : 15,
					"y" : 40+20,
				},
				{
					"name" : "yang_resim",
					"type" : "image",
					"horizontal_align" : "Center",
					"x" : 48,
					"y" : 40+20,
	
					"image" : "d:/ymir work/ui/public/Parameter_Slot_03.sub",
				},
				{
					"name" : "Input",
					"type" : "editline",
					"text" : "1",
					"horizontal_align" : "Center",
					"width" : 90,
					"height" : 18,
					"input_limit" : 9,
					"enable_codepage" : 0,
					"x" : 50,
					"y" : 40+20,
					
					"children" :
					(
						{
							"name" : "YangText",
							"type" : "text",
							"text" : "Yang",
							"x" : 60,
							"y" : 2,
						},
					),
				},
				{
					"name" : "yatirButton",
					"type" : "button",

					"x" : 140,
					"y" : 40+20,
					"text" : "+",
					"tooltip_text" : "Depo'ya yatýr",
					"tooltip_x" : 0,
					"tooltip_y" : 35,


					"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
				},
				{
					"name" : "cekButton",
					"type" : "button",

					"x" : 140+65,
					"y" : 40+20,
					"text" : "-",
					"tooltip_text" : "Depo'ndan para çek",
					"tooltip_x" : 0,
					"tooltip_y" : 35,

					"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
				},
			),
		},
	),
}