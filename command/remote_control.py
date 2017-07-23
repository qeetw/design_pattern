from command import NoCommand, LightOnCommand, LightOffCommand, \
CellingFanHighCommand, CellingFanLowCommand, CellingFanOffCommand

class RemoteControl():
    SLOT_COUNT = 7

    def __init__(self):
        self.on_commands = []
        self.off_commands = []
        self.undo_command = NoCommand()

        for i in range(0, RemoteControl.SLOT_COUNT):
            self.on_commands.append(NoCommand())
            self.off_commands.append(NoCommand())

    def set_command(self, slot, on_command, off_command):
        if slot >= RemoteControl.SLOT_COUNT:
            print('Slot Range is 0 ~ 6')
            return

        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pushed(self, slot):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_pushed(self, slot):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_pushed(self):
        self.undo_command.undo()