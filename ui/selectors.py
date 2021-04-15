class NotificationDrawerSelectors:
    SETTINGS_BUTTON = {'resourceId': 'com.android.systemui:id/settings_button'}


class SettingsSelectors:
    ABOUT_PHONE_BUTTON = {'resourceId': 'android:id/title',
                          'text': 'About phone'}


class AboutPhoneSelectors:
    TITLE = {'text': 'About phone'}


# ------ KF -------
class MainScreenKingfisherSelectors:
    HVAC_BUTTON = {'resourceId': 'com.android.systemui:id/navi_bar_fan_img'}


class HvacPanelPageSelectors:
    HVAC_PANEL = {'resourceId': 'com.vinfast.ivi.hvac:id/hvac_screen'}