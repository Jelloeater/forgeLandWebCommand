modemSide = "left"
rednet.open(modemSide)
rednet.broadcast("serverRebootAlarm-off","serveralarm")
rednet.close(modemSide)
while true do
	os.pullEvent =os.pullEventRaw
	term.clear()
	term.setCursorPos(1, 1)
	print("Reboot Server? (y/n)")
	local input = read()
	if input == "y" or input == "yes" then
		rednet.open(modemSide)
		rednet.broadcast("serverRebootAlarm-on","serveralarm")
		rednet.close(modemSide)

		redstone.setOutput("right", true)
		redstone.setOutput("left", true)
		print("Please Enter Password: ")
		local input = read("*")

		if input == "fuckthisshit" then
			redstone.setOutput("bottom", true)
			print("Reboot Sequence started!!!")
			for i=1,13 do
				print(14-i)
				os.sleep(1)
			end

			print("REBOOTING!!!")
			print("Good bye...")
			os.sleep(2)
			--http.get("http://127.0.1.1:9000/rebootForgeLand")
		else
			print("Incorrect!")
			sleep(1)
			print("Shutting Down")
			sleep(1)
			os.reboot()
		end
	end
end
