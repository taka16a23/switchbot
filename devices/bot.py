from switchbot.devices.device import Device


class Bot(Device):
    """Bot

    Bot is a Device.
    Short for SwitchBot Bot.
    Model No: SwitchBot S1.
    """
    DEVICE_TYPE = 'Bot'

    def turn_off(self, ):
        """set to OFF state

        turn_off()

        @Return:

        @Error:
        """
        return self.command('turnOff')

    def turn_on(self, ):
        """set to ON state

        turn_on()

        @Return:

        @Error:
        """
        return self.command('turnOn')

    def press(self, ):
        """trigger press

        press()

        @Return:

        @Error:
        """
        return self.command('press')
