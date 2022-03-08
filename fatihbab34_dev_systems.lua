--[[

TR: Tüm özel sistemler, fonksiyonlar, methodlar, ve yol...
TRL : All Special Systems, funcs, method and the way to...

Geliþtirici : .. Fatihbab34™ ..
Paketler ; LuaToPython, PythonToLua, PythonIslem
Fonksiyonlar ; "split('#blabla#blabla#', '#'), systems.getinput('PythonIslem'), io funcs(open, remove, write, read, readline, readlines), table forms, pc.getqf(), pc.setqf()"

--]]

quest fatihbab34_dev_systems begin
	state start begin

		function getinput(gelen)
			local input1 = "#quest_input#"
			local input0 = "#quest_inputbitir#"
			cmdchat("LuaToPython "..input1)
			local al = input(cmdchat("PythonIslem "..gelen))
			cmdchat("LuaToPython "..input0)
			return al
		end

		function split(command_, ne)
			return fatihbab34_dev_systems.split_(command_,ne)
		end
		
		function split_(string_,delimiter)
			local result = { }
			local from  = 1
			local delim_from, delim_to = string.find( string_, delimiter, from  )
			while delim_from do
				table.insert( result, string.sub( string_, from , delim_from-1 ) )
				from  = delim_to + 1
				delim_from, delim_to = string.find( string_, delimiter, from  )
			end
			table.insert( result, string.sub( string_, from  ) )
			return result
		end

		function acikarttirma_itemisil_itemiver(sira, kod, satici, durum)
			local items = {}

			local oku = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/esyalar.cfg", "r")
			for item in oku:lines() do
				table.insert(items, item)
			end
			
			for i = 1, table.getn(items) do
				if fatihbab34_dev_systems.split(items[i], "#")[27] == sira and fatihbab34_dev_systems.split(items[i], "#")[2] == kod and fatihbab34_dev_systems.split(items[i], "#")[25] == satici then
					if durum != 2 then
						local ac = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'r')
						local yeni = tonumber(ac:read())-tonumber(fatihbab34_dev_systems.split(items[i], "#")[26])
						local ac_ = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'w')
						ac_:write(yeni)
						ac_:close()
						ac:close()
						cmdchat("LuaToPython #acikarttirma_para#"..yeni)
					end

					--[[ --- Teklifleri vb silme inaktiv.
					local gelen_tablo = {}
					local gelen_isim = {}
					local gelen_sira = {}
					local verilen_tablo = {}
					if durum == 2 then -- Gelen Teklifleri siler...
						local ac_gelen = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/gelen_tekliflerim/'..pc.get_name()..'.cfg', 'r')
						if ac_gelen then
							for liness in ac_gelen:lines() do
								local bol = fatihbab34_dev_systems.split(liness, "#")
								if bol[27] != sira then
									table.insert(gelen_tablo, liness)
								else
									table.insert(gelen_isim, bol[30])
									table.insert(gelen_sira, bol[27])
								end
							end
							ac_gelen:close()
						end

						local ac_gelen_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/gelen_tekliflerim/'..pc.get_name()..'.cfg', 'w+')
						for ix = 1, table.getn(gelen_tablo) do
							ac_gelen_yaz:write(gelen_tablo[ix].."\\n")
						end
						ac_gelen_yaz:close()

						for xc = 1, table.getn(gelen_isim) do
							local ac_verilen = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/'..gelen_isim[xc]..'.cfg', 'r')
							for x2 in ac_verilen:lines() do
								--if fatihbab34_dev_systems.split(x2, "#")[27] != pc.get_name() and fatihbab34_dev_systems.split(x2, "#")[30] == gelen_isim[xc] then
								--if fatihbab34_dev_systems.split(x2, "#")[27] != sira and fatihbab34_dev_systems.split(x2, "#")[25] != pc.get_name() then 
								if fatihbab34_dev_systems.split(x2, "#")[27] == sira and fatihbab34_dev_systems.split(x2, "#")[25] == pc.get_name() then
									print "birþey yapma..."
								else
									table.insert(verilen_tablo, x2)
								end
							end
							ac_verilen:close()

							local ac_verilen_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/'..gelen_isim[xc]..'.cfg', 'w+')
							for xd = 1, table.getn(verilen_tablo) do
								ac_verilen_yaz:write(verilen_tablo[xd].."\\n")
							end
							ac_verilen_yaz:close()

							verilen_tablo = {}
						end
						
					end --]]

					local item = fatihbab34_dev_systems.split(items[i], "#")
					local bug_fixed = item[4]..'#'..item[2]..'#'..item[3]..'#'..item[5]..'#'..item[6]..'#'..item[7]..'#'..item[8]..'#'..item[9]..'#'..item[10]..'#'..item[11]..'#'..item[12]..'#'..item[13]..'#'..item[14]..'#'..item[15]..'#'..item[16]..'#'..item[17]..'#'..item[18]..'#'..item[19]..'#'..item[20]..'#'..item[21]..'#'..item[22]..'#'..item[23]..'#'..item[24]..'#'..item[25]..'#'..item[26]..'#'..item[27]..'#'..item[28]
					fatihbab34_dev_systems.acikarttirma_itemiver(bug_fixed, items, i, item[27])
					table.remove(items,i)
				end
			end

		end

		function acikarttirma_teklif_itemiver(sira, kod, satici, fiyat, durum)
			local items = {}
	
			local oku = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/"..pc.get_name()..".cfg", "r")
			for item in oku:lines() do
				table.insert(items, item)
			end
			
			for i = 1, table.getn(items) do
				if fatihbab34_dev_systems.split(items[i], "#")[27] == sira and fatihbab34_dev_systems.split(items[i], "#")[2] == kod and fatihbab34_dev_systems.split(items[i], "#")[25] == satici then
					if durum != 2 then
						local ac = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'r')
						local yeni = tonumber(ac:read())-tonumber(fatihbab34_dev_systems.split(items[i], "#")[26])
						local ac_ = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'w')
						ac_:write(yeni)
						ac_:close()
						ac:close()
						syschat('<Auction House Offers> : Your for bidding by '..satici.. ' accept. Number : '..sira .. ' Your Auction House Money : '..yeni)
						--cmdchat("LuaToPython #acikarttirma_para#"..yeni)
					end

					local item = fatihbab34_dev_systems.split(items[i], "#")
					local bug_fixed = item[4]..'#'..item[2]..'#'..item[3]..'#'..item[5]..'#'..item[6]..'#'..item[7]..'#'..item[8]..'#'..item[9]..'#'..item[10]..'#'..item[11]..'#'..item[12]..'#'..item[13]..'#'..item[14]..'#'..item[15]..'#'..item[16]..'#'..item[17]..'#'..item[18]..'#'..item[19]..'#'..item[20]..'#'..item[21]..'#'..item[22]..'#'..item[23]..'#'..item[24]..'#'..item[25]..'#'..item[26]..'#'..item[27]..'#'..item[28]
					fatihbab34_dev_systems.acikarttirma_itemiver_pc(bug_fixed, items, i, item[27])
					table.remove(items,i)
				end
			end

		end

		function acikarttirma_itemiver_pc(itemTab, items, i, sira)

			pc.give_item2_select(tonumber(fatihbab34_dev_systems.split(itemTab, "#")[2]),tonumber(fatihbab34_dev_systems.split(itemTab, "#")[3]))
			local attr,socket = {},{}
			for i = 10,23 do table.insert(attr,{fatihbab34_dev_systems.split(itemTab, "#")[i],fatihbab34_dev_systems.split(itemTab,"#")[i+1]}) i = i+1 end
			for i = 4,6 do table.insert(socket,fatihbab34_dev_systems.split(itemTab, "#")[i]) end
			for i = 1, table.getn(attr) do 
				item2.set_attr(i-1, attr[i][1], attr[i][2]) 
			end 
			for i = 1, table.getn(socket) do if tonumber(socket[i]) > 0 then item.set_socket(i-1, socket[i]) end end
		end

		function acikarttirma_itemiver(itemTab, items, i, sira)
			items = items
			cmdchat("LuaToPython alisxveris_itemler_yenile#"..sira)
			table.remove(items, i)
			local ci = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/esyalar.cfg", "w+")
			for i = 1, table.getn(items) do
				ci:write('#'..fatihbab34_dev_systems.split(items[i], "#")[2]..'#'..fatihbab34_dev_systems.split(items[i], "#")[3]..'#'..fatihbab34_dev_systems.split(items[i], "#")[4]..'#'..fatihbab34_dev_systems.split(items[i], "#")[5]..'#'..fatihbab34_dev_systems.split(items[i], "#")[6]..'#'..fatihbab34_dev_systems.split(items[i], "#")[7]..'#'..fatihbab34_dev_systems.split(items[i], "#")[8]..'#'..fatihbab34_dev_systems.split(items[i], "#")[9]..'#'..fatihbab34_dev_systems.split(items[i], "#")[10]..'#'..fatihbab34_dev_systems.split(items[i], "#")[11]..'#'..fatihbab34_dev_systems.split(items[i], "#")[12]..'#'..fatihbab34_dev_systems.split(items[i], "#")[13]..'#'..fatihbab34_dev_systems.split(items[i], "#")[14]..'#'..fatihbab34_dev_systems.split(items[i], "#")[15]..'#'..fatihbab34_dev_systems.split(items[i], "#")[16]..'#'..fatihbab34_dev_systems.split(items[i], "#")[17]..'#'..fatihbab34_dev_systems.split(items[i], "#")[18]..'#'..fatihbab34_dev_systems.split(items[i], "#")[19]..'#'..fatihbab34_dev_systems.split(items[i], "#")[20]..'#'..fatihbab34_dev_systems.split(items[i], "#")[21]..'#'..fatihbab34_dev_systems.split(items[i], "#")[22]..'#'..fatihbab34_dev_systems.split(items[i], "#")[23]..'#'..fatihbab34_dev_systems.split(items[i], "#")[24]..'#'..fatihbab34_dev_systems.split(items[i], "#")[25]..'#'..fatihbab34_dev_systems.split(items[i], "#")[26]..'#'..fatihbab34_dev_systems.split(items[i], "#")[27]..'#'..fatihbab34_dev_systems.split(items[i], "#")[28]..'#'..'\\n')
			end
			ci:flush()
			ci:close()

			pc.give_item2_select(tonumber(fatihbab34_dev_systems.split(itemTab, "#")[2]),tonumber(fatihbab34_dev_systems.split(itemTab, "#")[3]))
			local attr,socket = {},{}
			for i = 10,23 do table.insert(attr,{fatihbab34_dev_systems.split(itemTab, "#")[i],fatihbab34_dev_systems.split(itemTab,"#")[i+1]}) i = i+1 end
			for i = 4,6 do table.insert(socket,fatihbab34_dev_systems.split(itemTab, "#")[i]) end
			for i = 1, table.getn(attr) do 
				item2.set_attr(i-1, attr[i][1], attr[i][2]) 
			end 
			for i = 1, table.getn(socket) do if tonumber(socket[i]) > 0 then item.set_socket(i-1, socket[i]) end end
		end

		when login begin
			cmdchat("PythonToLua "..q.getcurrentquestindex())

			-- Açýk Arttýrma Ýtem Kontrol --
			local ac_acikarttirma = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/'..pc.get_name()..'.cfg', 'r')
			local ac_acikarttirma_para = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'r')
			if ac_acikarttirma then
				syschat('<Auction House> : '..ac_acikarttirma:read()..' count My item was sold. Your total auction house money is : '..ac_acikarttirma_para:read())
				os.remove('/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/'..pc.get_name()..'.cfg')
			end
			-- Açýk Arttýrma Teklif Kabul Kontrol --
			local ac_verilen = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/"..pc.get_name()..".cfg", "r")
			if ac_verilen then
				local items_tablo = {}
				for line_verilen in ac_verilen:lines() do
					local bol = fatihbab34_dev_systems.split(line_verilen,"#")
					local item = fatihbab34_dev_systems.split(line_verilen,"#")
					if bol[31] == "1" then
						fatihbab34_dev_systems.acikarttirma_teklif_itemiver(bol[27], bol[2], bol[25], bol[26], 0)
					else
						table.insert(items_tablo, line_verilen)
					end
				end

				local yaz_verilen = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/"..pc.get_name()..".cfg", "w+")
				for i = 1, table.getn(items_tablo) do
					yaz_verilen:write(items_tablo[i]..'\\n')
				end
				yaz_verilen:close()
			end
		end


		when 20092.chat."What is the Auction House System?" begin
			say_title("Auction Agent:")
			say("So you want to get information about the auction system.[ENTER]PThe purpose of the auction system is not only to develop trade outside of the game within the game.[ENTER]In this way we can offer the goods you put buyers shopping offline, you can trade with them.[ENTER]Shopping money when you return the purchased items in shopping[ENTER]You can convert their money in gold from the shopping menu shopping.")
		end

		when 20092.chat."Add the item to Auction House" begin
			say_title("<Auction Agent>")
			say("Hmm... So you want to add light to increase the goods?")
			local s = select("Yes", "No")
			if s == 2 then
				return
			elseif s == 1 then
				cmdchat("LuaToPython alisveris_item_ekle#")
			end
		end

		-- Button Fonksiyonlarý --
		when button begin
			local gelen = fatihbab34_dev_systems.getinput("PYTHONISLEM")

			if string.find(gelen, "acikarttirma_teklifiptal#") then
				local bol = fatihbab34_dev_systems.split(gelen, "#")
				local tablo = {}
				local tablo_verilen = {}
				local sira = bol[2]
				local kod = bol[3]
				local ad = bol[4]
				local xread = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/gelen_tekliflerim/"..ad..".cfg", "r")
				for xxx in xread:lines() do
					local splitt = fatihbab34_dev_systems.split(xxx, "#")
					if splitt[30] == pc.get_name() and splitt[27] == sira then
						print "bir þey yapma..."
					else
						table.insert(tablo, xxx)
					end
				end
				xread:close()
				local ac_yaz = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/gelen_tekliflerim/"..ad..".cfg", "w+")
				for i=1, table.getn(tablo) do
					ac_yaz:write(tablo[i]..'\\n')
				end
				ac_yaz:close()

				local ac_read_verilen = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/"..pc.get_name()..".cfg", "r")
				for line2 in ac_read_verilen:lines() do
					local splitt_verilen = fatihbab34_dev_systems.split(line2, "#")
					if splitt_verilen[30] == pc.get_name() and splitt_verilen[27] == sira then
						print "bir þey yapma..."
					else
						table.insert(tablo_verilen, line2)
					end
				end
				ac_read_verilen:close()
				local ac_yaz_verilen = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/"..pc.get_name()..".cfg", "w+")
				for i=1, table.getn(tablo_verilen) do
					ac_yaz_verilen:write(tablo_verilen[i]..'\\n')
				end
				ac_yaz_verilen:close()

				chat("<Auction House> Your offer has been canceled.")
			end

			if string.find(gelen, "acikarttirma_teklifkabulet") then
				local bol = fatihbab34_dev_systems.split(gelen, "#")
				local sira = bol[2]
				local kod = bol[3]
				local satici = bol[4]
				local teklif_eden = bol[5]
				local gelen_tablo = {}
				local verilen_tablo = {}
				local item_tablo = {}
				local ac = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/gelen_tekliflerim/"..pc.get_name()..".cfg", "r")
				for line in ac:lines() do
					local bol = fatihbab34_dev_systems.split(line,"#")
					local item = fatihbab34_dev_systems.split(line,"#")
					
					if bol[27] == sira and bol[2] == kod and bol[25] == satici and satici == pc.get_name() and bol[30] == teklif_eden then
						local ac = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'r')
						local yeni = tonumber(ac:read())+tonumber(bol[29])
						if yeni > 1999999999 then
							syschat("<Auction House> : Because now the money the auction came to 2T'y money inventory.")
						else
							local ac_ = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'w')
							ac_:write(yeni)
							ac_:close()
							ac:close()
							syschat("<Açýk arttýrma> : Your total auction house money is : "..yeni)
							cmdchat("LuaToPython #acikarttirma_para#"..yeni)
						end
					else
						table.insert(gelen_tablo, line)
						
					end
				end
				ac:close()
				local ac_yaz = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/gelen_tekliflerim/"..pc.get_name()..".cfg", "w+")
				for ix = 1, table.getn(gelen_tablo) do
					local bol = fatihbab34_dev_systems.split(gelen_tablo[ix], "#")
					ac_yaz:write(gelen_tablo[ix]..'\\n')
				end
				ac_yaz:close()

				local ac_verilen = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/"..teklif_eden..".cfg", "r")
				for line_verilen in ac_verilen:lines() do
					local bol = fatihbab34_dev_systems.split(line_verilen,"#")
					local item = fatihbab34_dev_systems.split(line_verilen,"#")
					if bol[27] == sira and bol[2] == kod and bol[25] == satici and satici == pc.get_name() and bol[30] == teklif_eden then
						local satir = '#'..item[2]..'#'..item[3]..'#'..item[4]..'#'..item[5]..'#'..item[6]..'#'..item[7]..'#'..item[8]..'#'..item[9]..'#'..item[10]..'#'..item[11]..'#'..item[12]..'#'..item[13]..'#'..item[14]..'#'..item[15]..'#'..item[16]..'#'..item[17]..'#'..item[18]..'#'..item[19]..'#'..item[20]..'#'..item[21]..'#'..item[22]..'#'..item[23]..'#'..item[24]..'#'..item[25]..'#'..item[26]..'#'..item[27]..'#'..item[28]..'#'..item[29]..'#'..item[30]..'#1#' -- 1 : kabul et, 2 : kabul etme
						table.insert(verilen_tablo, satir)
					else
						table.insert(verilen_tablo, line_verilen)
					end
				end
				local ac_yaz_verilen = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/"..teklif_eden..".cfg", "w+")
				for i2 = 1, table.getn(verilen_tablo) do
					ac_yaz_verilen:write(verilen_tablo[i2]..'\\n')
				end
				ac_yaz_verilen:close()

				local ac_items = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/esyalar.cfg", "r")
				if ac_items then
					for i in ac_items:lines() do
						local bol = fatihbab34_dev_systems.split(i, "#")
						if bol[27] == sira and bol[2] == kod and bol[25] == satici and satici == pc.get_name() then
							print "birþey yapma..."
						else
							table.insert(item_tablo, i)
						end
					end
					ac_items:close()
					local ac_items2 = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/esyalar.cfg", "w+")
					for x = 1, table.getn(item_tablo) do
						ac_items2:write(item_tablo[x]..'\\n')
					end
					ac_items2:close()
				end
			end

			if string.find(gelen, "acikarttirma_teklifreddet") then
				local bol = fatihbab34_dev_systems.split(gelen, "#")
				local sira = bol[2]
				local kod = bol[3]
				local satici = bol[4]
				local teklif_eden = bol[5]
				local gelen_tablo = {}
				local verilen_tablo = {}
				local ac = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/gelen_tekliflerim/"..pc.get_name()..".cfg", "r")
				for line in ac:lines() do
					local bol = fatihbab34_dev_systems.split(line,"#")
					local item = fatihbab34_dev_systems.split(line,"#")
					
					if bol[27] == sira and bol[2] == kod and bol[25] == satici and satici == pc.get_name() and bol[30] == teklif_eden then
						print "birþey yapma..."
					else
						table.insert(gelen_tablo, line)
						
					end
				end
				ac:close()
				local ac_yaz = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/gelen_tekliflerim/"..pc.get_name()..".cfg", "w+")
				for ix = 1, table.getn(gelen_tablo) do
					ac_yaz:write(gelen_tablo[ix]..'\\n')
					
				end
				ac_yaz:close()

				local ac_verilen = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/"..teklif_eden..".cfg", "r")
				for line_verilen in ac_verilen:lines() do
					local bol = fatihbab34_dev_systems.split(line_verilen,"#")
					local item = fatihbab34_dev_systems.split(line_verilen,"#")
					if bol[27] == sira and bol[2] == kod and bol[25] == satici and satici == pc.get_name() and bol[30] == teklif_eden then
						local satir = '#'..item[2]..'#'..item[3]..'#'..item[4]..'#'..item[5]..'#'..item[6]..'#'..item[7]..'#'..item[8]..'#'..item[9]..'#'..item[10]..'#'..item[11]..'#'..item[12]..'#'..item[13]..'#'..item[14]..'#'..item[15]..'#'..item[16]..'#'..item[17]..'#'..item[18]..'#'..item[19]..'#'..item[20]..'#'..item[21]..'#'..item[22]..'#'..item[23]..'#'..item[24]..'#'..item[25]..'#'..item[26]..'#'..item[27]..'#'..item[28]..'#'..item[29]..'#'..item[30]..'#2#' -- 1 : kabul et, 2 : kabul etme
						table.insert(verilen_tablo, satir)
					else
						table.insert(verilen_tablo, line_verilen)
					end
				end
				local ac_yaz_verilen = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/"..teklif_eden..".cfg", "w+")
				for i2 = 1, table.getn(verilen_tablo) do
					ac_yaz_verilen:write(verilen_tablo[i2]..'\\n')
				end
				ac_yaz_verilen:close()
			end
			
			if string.find(gelen, "acikarttirma_teklifver#") then
				local bol = fatihbab34_dev_systems.split(gelen, "#")
				local sira = bol[3]
				local verilen_teklif = bol[2]
				local kod = bol[4]
				local satici = bol[5]
				local oku = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/esyalar.cfg", "r")
				local kontrol = 0
				for item in oku:lines() do
					local items = fatihbab34_dev_systems.split(item,"#")
					if items[27] == sira and items[2] == kod and items[25] == satici then
						local ac = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/gelen_tekliflerim/"..satici..".cfg", "a+")
						ac:write(item..verilen_teklif.."#"..pc.get_name().."#0#"..'\\n')
						ac:close()

						local ac_ = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/"..pc.get_name()..".cfg", "a+")
						ac_:write(item..verilen_teklif.."#"..pc.get_name().."#0#"..'\\n')
						ac_:close()
						kontrol = 1
						chat("<Auctions>: Offer has been successfully placed, people will accept the offer if the item you purchase will be realized.")
					end
				end
				oku:close()

				if kontrol == 0 then
					syschat('<Auctions>: This item was purchased, this offer you can not give it up. You refresh the page ...')
				end

			end

			if string.find(gelen, "acikarttirma_satinal#") then
				local slot = fatihbab34_dev_systems.split(gelen, "#")
				local oku = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/esyalar.cfg", "r")
				local kontrol = 0
				for item in oku:lines() do
					local items = fatihbab34_dev_systems.split(item,"#") --items[26]
					if items[27] == slot[2] and items[2] == slot[3] and items[25] == slot[4] then
						if items[25] == pc.get_name() then
							syschat('<Auctions>: You can not buy your own items.')
							return
						end

						local benim_para = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'r')
						if tonumber(items[26]) < tonumber(benim_para:read()) then
							if not pc.enough_inventory(tonumber(items[2])) then
								syschat("<Auction>: not enough inventory to purchase this item.")
								return
							end
							syschat('<Auction>: Item successfully purchased.')
							local ac = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..items[25]..'.cfg', 'r')
							if ac then
								local suan = tonumber(ac:read())+tonumber(items[26])
								local ac_to = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..items[25]..'.cfg', 'w')
								ac_to:write(suan)
								ac_to:close()
								ac:close()
							else
								local ac_to2 = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..items[25]..'.cfg', 'w')
								ac_to2:write(items[26])
								ac_to2:close()
							end

							local ac_to3 = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/'..items[25]..'.cfg', 'r')
							if ac_to3 then
								local snn = ac_to3:read()
								local ac_to3_2 = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/'..items[25]..'.cfg', 'w')
								ac_to3_2:write(snn+1)
								ac_to3_2:close()
								ac_to3:close()
							else
								local ac_to3_3 = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/'..items[25]..'.cfg', 'w')
								ac_to3_3:write("1")
								ac_to3_3:close()
							end
							fatihbab34_dev_systems.acikarttirma_itemisil_itemiver(slot[2], slot[3], slot[4], 0)
							kontrol = 1
						else
							cmdchat("LuaToPython acikarttirma_para_yok")
							kontrol = 1
						end
						benim_para:close()
					end
				end
				if kontrol == 0 then
					syschat('<Auctions>: This item was purchased, please refresh the page ...')
				end
			end

			if string.find(gelen, "acikarttirma_gerial#") then
				local slot = fatihbab34_dev_systems.split(gelen, "#")
				local oku = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/esyalar.cfg", "r")
				local kontrol = 0
				for item in oku:lines() do
					local items = fatihbab34_dev_systems.split(item,"#") --items[26]
					if items[27] == slot[2] and items[2] == slot[3] and items[25] == slot[4] then
						if items[25] == pc.get_name() then
							if not pc.enough_inventory(tonumber(items[2])) then
								syschat("<Auction>: There is not enough inventory to get back to the place of these items.")
								return
							end

							fatihbab34_dev_systems.acikarttirma_itemisil_itemiver(slot[2], slot[3], slot[4], 2)
							kontrol = 1
						end
					end
				end
				if kontrol == 0 then
					syschat('<Auctions>: Item has encountered a problem retrieving ...')
				end
			end

			if string.find(gelen, "acikarttirma_itemkoy#") then
				local bol = fatihbab34_dev_systems.split(gelen, "#")
				local bug_fixed = 0
				local sira = 0
				item.select_cell(bol[2])
				--local attr = {{item2.get_attr(0)}, {item2.get_attr(1)}, {item2.get_attr(2)}, {item2.get_attr(3)},{item2.get_attr(4)},{item2.get_attr(5)}, {item2.get_attr(6)}}
				local attr = item.get_attr()
				local socket, itemVnum, itemCount = {item.get_socket(0), item.get_socket(1), item.get_socket(2),item.get_socket(3),item.get_socket(4),item.get_socket(5)}, item.get_vnum(), item.get_count()
				if bug_fixed == 0 then
					local ac_oku = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/esyalar.cfg', 'r')
					if ac_oku then
						for i in ac_oku:lines() do
							local no = fatihbab34_dev_systems.split(i, "#")[27]
							sira = no
						end
						local ac = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/esyalar.cfg', 'a+')
						ac:write("#"..itemVnum.."#"..itemCount.."#"..(bol[2]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[4]).."#"..(sira+1).."#"..(bol[5]).."#".."\\n")
						ac:close()
					else
						local ac = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/esyalar.cfg', 'w')
						ac:write("#"..itemVnum.."#"..itemCount.."#"..(bol[2]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[4]).."#1#"..(bol[5]).."#".."\\n")
						ac:close()
					end
					ac_oku:close()
					bug_fixed = 1
				end
				item.remove()
				syschat('<Auctions>: Item successfully added the auction.')
			end

			if gelen == "#acikarttirma_para_ve_itemler#" then

				local ac_itemler = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/esyalar.cfg', 'r')
				if ac_itemler then
					for i in ac_itemler:lines() do
						cmdchat("LuaToPython alisveris_itemler|"..i)
					end
				end

				local ac_gelen_teklifler = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/gelen_tekliflerim/"..pc.get_name()..".cfg", "r")
				if ac_gelen_teklifler then
					for i in ac_gelen_teklifler:lines() do
						local bol = fatihbab34_dev_systems.split(i, "#")
						if bol[31] == "0" then
							cmdchat("LuaToPython alisxveris_itemler_gelen_teklifler|"..i)
						end
					end
				end

				local ac_verilen_teklifler = io.open("/usr/game/share/locale/turkey/quest/systems/acikarttirma/item_durumlari/verilen_tekliflerim/"..pc.get_name()..".cfg", "r")
				if ac_verilen_teklifler then
					for i in ac_verilen_teklifler:lines() do
						local bol = fatihbab34_dev_systems.split(i, "#")
						if bol[31] == "0" then
							cmdchat("LuaToPython alisxveris_itemler_verilen_teklifler|"..i)
						end
					end
				end

				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'r')
				if ac then
					local suan = ac:read()
					cmdchat("LuaToPython #acikarttirma_para#"..suan)
				end

			end

			if string.find(gelen, "acikarttirma_para_ekle#") then
				local bol = fatihbab34_dev_systems.split(gelen, "#")
				if tonumber(bol[2]) <= pc.get_money() then
					local ac = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'r')
					if ac then
						local suan = ac:read()
						local yeni = tonumber(suan)+tonumber(bol[2])
						local ac_2 = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'w')
						if yeni > 1999999999 then
							syschat("<Auction>: 2T' not carry more than auction money.")
							ac_2:close()
						else
							ac_2:write(yeni)
							ac_2:close()
							pc.change_money(-tonumber(bol[2]))
						end
					else
						local ac_ = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'w')
						if tonumber(bol[2]) > 1999999999 then
							syschat("<Auction>: 2T' not carry more than auction money.")
							ac_:close()
						else
							ac_:write(bol[2])
							ac_:close()
							pc.change_money(-tonumber(bol[2]))
						end
					end
					ac:close()
				end
			end

			if string.find(gelen, "acikarttirma_para_cek") then
				local bol = fatihbab34_dev_systems.split(gelen, "#")
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'r')
				if ac then
					local para = ac:read()
					if tonumber(para) > tonumber(bol[2]) or tonumber(para) == tonumber(bol[2]) then
						local acx = io.open('/usr/game/share/locale/turkey/quest/systems/acikarttirma/para/'..pc.get_name()..'.cfg', 'w')
						acx:write(tonumber(para)-tonumber(bol[2]))
						acx:close()
						pc.change_money(tonumber(bol[2]))
					end
				end
				ac:close()
			end

		end
	end
end