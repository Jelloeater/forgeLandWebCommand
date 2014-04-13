rednet.open("top")
while true do
	ID, msg=rednet.receive("serveralarm")
	print(msg)
	if msg == "serverRebootAlarm-off" then redstone.setOutput("back", false) print("Alarm OFF") end
	if msg == "serverRebootAlarm-on" then redstone.setOutput("back", true) print("Alarm ON")end
end