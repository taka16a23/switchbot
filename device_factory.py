#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""device_factory --

"""
from switchbot.devices import (
    AirPurifilerTablePM25,
    AirPurifilerVOC,
    BatteryCirculatorFan,
    BlindTilt,
    Bot,
    CeilingLightPro,
    CeilingLight,
    CirculatorFan,
    ColorBulb,
    Curtain3,
    Curtain,
    FloorCleaningRobotS10,
    Humidifier2,
    Humidifier,
    K10ProCombo,
    Keypad,
    KeypadTouch,
    LockPro,
    Lock,
    MiniRobotVacuumCleanerK10Pro,
    MiniRobotVacuumCleanerK10,
    PlugMiniJP,
    PlugMiniUS,
    Plug,
    RelaySwitch1PM,
    RelaySwitch1,
    RobotVacuumCleanerS1Plus,
    RobotVacuumCleanerS1,
    RollerShade,
    StripLight,
)


class DeviceFactory(object):
    """DeviceFactory

    DeviceFactory is a object.
    Responsibility:
    """
    DEVICES = {
        AirPurifilerTablePM25.DEVICE_TYPE: AirPurifilerTablePM25,
        AirPurifilerVOC.DEVICE_TYPE: AirPurifilerVOC,
        BatteryCirculatorFan.DEVICE_TYPE: BatteryCirculatorFan,
        BlindTilt.DEVICE_TYPE: BlindTilt,
        Bot.DEVICE_TYPE: Bot,
        CeilingLightPro.DEVICE_TYPE: CeilingLightPro,
        CeilingLight.DEVICE_TYPE: CeilingLight,
        CirculatorFan.DEVICE_TYPE: CirculatorFan,
        ColorBulb.DEVICE_TYPE: ColorBulb,
        Curtain3.DEVICE_TYPE: Curtain3,
        Curtain.DEVICE_TYPE: Curtain,
        FloorCleaningRobotS10.DEVICE_TYPE: FloorCleaningRobotS10,
        Humidifier2.DEVICE_TYPE: Humidifier2,
        Humidifier.DEVICE_TYPE: Humidifier,
        K10ProCombo.DEVICE_TYPE: K10ProCombo,
        Keypad.DEVICE_TYPE: Keypad,
        KeypadTouch.DEVICE_TYPE: KeypadTouch,
        LockPro.DEVICE_TYPE: LockPro,
        Lock.DEVICE_TYPE: Lock,
        MiniRobotVacuumCleanerK10Pro.DEVICE_TYPE: MiniRobotVacuumCleanerK10Pro,
        MiniRobotVacuumCleanerK10.DEVICE_TYPE: MiniRobotVacuumCleanerK10,
        PlugMiniJP.DEVICE_TYPE: PlugMiniJP,
        PlugMiniUS.DEVICE_TYPE: PlugMiniUS,
        Plug.DEVICE_TYPE: Plug,
        RelaySwitch1PM.DEVICE_TYPE: RelaySwitch1PM,
        RelaySwitch1.DEVICE_TYPE: RelaySwitch1,
        RobotVacuumCleanerS1Plus.DEVICE_TYPE: RobotVacuumCleanerS1Plus,
        RobotVacuumCleanerS1.DEVICE_TYPE: RobotVacuumCleanerS1,
        RollerShade.DEVICE_TYPE: RollerShade,
        StripLight.DEVICE_TYPE: StripLight,
    }

    @staticmethod
    def create(device_info, client):
        device_type = device_info.get('deviceType', None)
        if device_type is None:
            return None
        klass = DeviceFactory.DEVICES.get(device_type, None)
        if klass is None:
            return None
        device_id = device_info.get('deviceId', None)
        device_name = device_info.get('deviceName', '')
        cloud_enabled = device_info.get('enableCloudService', None)
        hubdevice_id = device_info.get('hubDeviceId', None)
        return klass(client, device_id, device_name=device_name,
                     cloud_enabled=cloud_enabled, hub_id=hubdevice_id)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# device_factory.py ends here
