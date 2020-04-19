local doTheThing = false
local tempo = false

function OnEvent(event, arg)
    if arg == 6 then
        if event == "MOUSE_BUTTON_PRESSED" then
            doTheThing = true
	if (doTheThing) then
		MoveMouseRelative(0, 100)
		MoveMouseRelative(0, 100)
		Sleep(25)
		PressAndReleaseMouseButton(1)
		Sleep(25)
		
		
		if (not tempo) then
			OutputLogMessage("Not tempo\n")
			MoveMouseRelative(100, -100)
			MoveMouseRelative(100, -100)
			MoveMouseRelative(100, -100)
			MoveMouseRelative(100, 0)
			Sleep(25)
			PressAndReleaseMouseButton(1)
		else
			OutputLogMessage("Tempo\n")
			MoveMouseRelative(100, -100)
			MoveMouseRelative(100, -100)
			MoveMouseRelative(100, -100)
			MoveMouseRelative(100, -100)
			MoveMouseRelative(100, -100)
			MoveMouseRelative(100, 0)
			Sleep(25)
			PressAndReleaseMouseButton(1)
		end
		tempo = not tempo
	end
        elseif event == "MOUSE_BUTTON_RELEASED" then
            doTheThing = false
        end
    end
end