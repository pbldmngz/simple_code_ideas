--Gun presets -- X, Y, delay
local n = 0
local b = false
local f = 1
--adecuado es 6/4--
local horizontal =  100 * f * 16
local vertical = 100 * f * 9

local y = vertical
local x = horizontal

local tempo_flatline = {
    --x--
    [1] = {0, 17, 1, 36, 26, 23, -3, -6, -47, -17, -10, -15, 7, 35, 24, 31, 25, -7, 10, 35, 29, 26, 4, -17, -25, -37, -27, -16, -30, -11},
    --y--
    [2] = {0, 105, 43, 62, 37, 61, 41, 22, 6, -19, 13, 41, 12, 20, -7, -9, 4, 38, 29, 36, 2, 6, 39, 11, 6, 16, 12, -24, 25, 28},
}

function compensateRecoil()
    n = n + 1
    MoveMouseRelative(tempo_flatline[1][n] * x, tempo_flatline[2][n] * y)
    Sleep(100)
OutputLogMessage(n)
end

function the_switcher()
    if (b == true) then
        y = 0
        x = 0
        OutputLogMessage("Apagado\n")
    else
        y = vertical
        x = horizontal
        OutputLogMessage("Prendido\n")
    end
    b = not b
end

--start the main program--

EnablePrimaryMouseButtonEvents(true)

OutputLogMessage("This is a welcome message\n")


function OnEvent(event, arg)
    --execute script--
    if (event == "MOUSE_BUTTON_PRESSED" and arg == 6) then
        the_switcher()
    end
    if (event == "MOUSE_BUTTON_PRESSED" and arg == 1 and b == true) then
        n = 0
        repeat
            compensateRecoil()
        until not IsMouseButtonPressed(1)
    end
end