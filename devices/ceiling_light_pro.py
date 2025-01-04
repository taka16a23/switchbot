from switchbot.devices.device import Device


class CeilingLightPro(Device):
    """CeilingLightPro

    CeilingLightPro is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Ceiling Light Pro'

    def turn_on(self, ):
        """set to ON state

        turn_on()

        @Return:

        @Error:
        """
        return self.command('turnOn')

    def turn_off(self, ):
        """set to OFF state

        turn_off()

        @Return:

        @Error:
        """
        return self.command('turnOff')

    def toggle(self, ):
        """toggle state

        toggle()

        @Return:

        @Error:
        """
        return self.command('toggle')

    def set_brightness(self, value):
        """set brightness

        set_brightness(value)

        @Arguments:
        - `value`: {1-100}

        @Return:

        @Error:
        """
        # require

        # do

        # ensure
        return self.command('setBrightness', value)

    def set_color_temperature(self, value):
        """set color temperature

        set_color_temperature(value)

        @Arguments:
        - `value`: {2700-6500}

        @Return:

        @Error:
        """
        # require

        # do

        # ensure
        return self.command('setColorTemperature', value)
