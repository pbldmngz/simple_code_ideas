--Gun presets -- X, Y, delay
local a = 1
local m = 1
local presets = {
    [1] = {0, 0, 100},
    [2] = {0 * m, 0 * m, 100}, --flatline--
    [3] = {0 * m, 70 * m, 45}, --r99--
    [4] = {0 * m, 30 * m, 40}, --havoc--
}


function compensateRecoil()
    MoveMouseRelative(presets[a][1], presets[a][2])
    Sleep(presets[a][3])
end

function setGun()
	a = a + 1
	if (a > 4) then
		a = 1
	end
end

--start the main program--

EnablePrimaryMouseButtonEvents(true)

OutputLogMessage("This is a welcome message\n")


function OnEvent(event, arg)
    --switch weapon--
    if (event== "MOUSE_BUTTON_PRESSED" and arg == 6) then
        setGun()

        OutputLogMessage("[+] You have switched weapons: %s\n", a)
    end

    --execute script--
    if (event == "MOUSE_BUTTON_PRESSED" and arg == 1) then
        repeat
            compensateRecoil()
        until not IsMouseButtonPressed(1)
    end
end