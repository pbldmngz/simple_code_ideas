local b = false

function autoClicker()
    PressMouseButton(1)
    Sleep(75)
    ReleaseMouseButton(1)
end

function the_switcher()
    if (b == true) then
        OutputLogMessage("Apagado\n")
    else
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
        repeat
            autoClicker()
        until not IsMouseButtonPressed(1)
    end
end