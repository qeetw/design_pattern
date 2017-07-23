from remote_control import RemoteControl
from command import LightOnCommand, LightOffCommand, \
CellingFanHighCommand, CellingFanLowCommand, CellingFanOffCommand
from light import Light
from celling_fan import CellingFan

def main():
    remote_control = RemoteControl()
    
    light = Light()
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)

    fan = CellingFan()
    celling_fan_high_command = CellingFanHighCommand(fan)
    celling_fan_low_command = CellingFanLowCommand(fan)
    celling_fan_off_command = CellingFanOffCommand(fan)

    remote_control.set_command(2, light_on_command, light_off_command)
    remote_control.set_command(5, celling_fan_high_command, celling_fan_off_command)
    remote_control.set_command(6, celling_fan_low_command, celling_fan_off_command)

    remote_control.on_button_pushed(1) 
    remote_control.off_button_pushed(1)
    remote_control.undo_button_pushed()

    remote_control.on_button_pushed(2) 
    remote_control.off_button_pushed(2)
    remote_control.undo_button_pushed()

    remote_control.on_button_pushed(6) 
    remote_control.off_button_pushed(6)
    remote_control.undo_button_pushed()

    remote_control.on_button_pushed(5)
    remote_control.undo_button_pushed() 

if __name__ == '__main__':
    main()