--Phantom by Sniper9143--

initial_Class = "class_1"

initial_Weapon = "sample_1"

toggleNoRecoil_gKey = 2

switchWeapon_gKey = 3

switchClass_gKey = 4

--Gun presets -- X, Y, delay

local presets = {
    ["sample_1"] = {0, 1, 45},
    ["sample_2"] = {0, 10, 40},
    ["sample_3"] = {0, 122, 45},
    ["sample_4"] = {0, 1022, 40},
}

--Clases to change attributes

local classes = {
    ["class_1"] = {["sample_1"] = presets.sample_1, ["sample_2"] = presets.sample_2},
    ["class_2"] = {["sample_3"] = presets.sample_3, ["sample_4"] = presets.sample_4},
}

local NoRecoil = {}
NoRecoil.__index = NoRecoil

setmetatable( NoRecoil, {
    __call = function (cls, ...)
        return cls.new(...)
    end,
})
--constructor-- 

function NoRecoil.new(selectedClass, selectedGun, presets, classes)
    local self = setmetatable({}, NoRecoil)
    self.Presets = presets
    self.Classes = classes
    self.selectedClassIndex = selectedClass
    self.selectedGunIndex = selectedGun
    self.selectedGun = self.Classes[self.selectedClassIndex][self.selectedGunIndex]
    self.noRecoilBool = false
    return self
end

function NoRecoil:compensateRecoil()
    MoveMouseRelative(self.selectedGun[1], self.selectedGun[2])
    Sleep(self.selectedGun[3])
end

--getters--

function NoRecoil:currentWeapon()
    return self.selectedGunIndex
end

function NoRecoil:currentClass()
    return self.selectedClassIndex
end

function NoRecoil:scriptState()
    return self.noRecoilBool
end

--setters--

function NoRecoil_setScriptState()
    self.noRecoilBool = not self.noRecoilBool
end

function NoRecoil:setGun()
    repeat
        gun_Id, gun_Attributes = next(self.Classes[self.selectedClassIndex], self.selectedGunIndex)
        self.selectedGunIndex = gun_Id, gun_Attributes
    until (self.selectedGunIndex == nil)
    self.selectedGun = self.Classes[self.selectedClassIndex][self.selectedGunIndex]
end

function NoRecoil:setClass()
    repeat
        class_Id, class_Attributes = next(self.Classes, self.selectedClassIndex)
        self.selectedClassIndex = class_Id, class_Attributes
    until (self.selectedClassIndex == nil)
    self.selectedGunIndex = self.Classes[self.selectedClassIndex][1]
    self.selectedGun = self.Classes[self.selectedClassIndex][self.selectedGunIndex]
end

--start the main program--

EnablePrimaryMouseButtonEvents(true)

local NoRecoilObject = NoRecoil(initial_Class, initial_Weapon, presets, classes)

OutputLogMessage("This is a welcome message\n")

OutputLogMessage("[+] You are currently using the preset '%s' in '%s'\n", NoRecoilObject:currentWeapon(), NoRecoilObject:currentClass())

function OnEvent(event, arg)
    --switch weapon--
    if (event == "G_PRESSED" and arg == switchWeapon_gKey) then
        NoRecoilObject:setGun()

        OutputLogMessage("[+] You have switched weapons: %s\n", NoRecoilObject:currentWeapon())
    end
    --switch class--
    if (event == "G_PRESSED" and arg == switchClass_gKey) then
        NoRecoilObject:setClass()

        OutputLogMessage("[+] You have switched class: %s\n", NoRecoilObject:currentClass())
    end
    --toggle script--
    if (event == "G_PRESSED" and arg == toggleNoRecoil_gKey) then
        NoRecoilObject:setScriptState()
        if (NoRecoilObject:scriptState() == true) then
            OutputLogMessage("[+] No recoil is ON\n")
        else
            OutputLogMessage("[+] No recoil is OFF\n")
        end
    end
    --execute script--
    if (event == "MOUSE_BUTTON_PRESSED" and arg == 1 and NoRecoilObject:scriptState() == true) then
        repeat
            NoRecoilObject:compensateRecoil()
        until not IsMousButtonPressed(1)
    end
end

--[[Tienes que configurar que el usuario pueda elegir dos armas
y que cambie de perfiles aprovechando la rueda del ratón

También puedes crear, por ejemplo, un arreglo de posiciones y tiempos para la flatline, 
una corrección para cada parte importante del recoil

correos
code1.spectra@gmail.com
]]
