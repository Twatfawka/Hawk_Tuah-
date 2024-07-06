from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
import pyrebase

firebaseConfig = {
    'apiKey': "YOUR_API_KEY",
    'authDomain': "YOUR_PROJECT_ID.firebaseapp.com",
    'databaseURL': "https://YOUR_PROJECT_ID.firebaseio.com",
    'projectId': "YOUR_PROJECT_ID",
    'storageBucket': "YOUR_PROJECT_ID.appspot.com",
    'messagingSenderId': "YOUR_SENDER_ID",
    'appId': "YOUR_APP_ID",
    'measurementId': "YOUR_MEASUREMENT_ID"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

class LoginScreen(Screen):
    def do_login(self):
        email = self.ids.email.text
        password = self.ids.password.text

        try:
            auth.sign_in_with_email_and_password(email, password)
            self.manager.current = 'home'
        except:
            self.show_alert_dialog()

    def show_alert_dialog(self):
        self.dialog = MDDialog(
            title="Login Failed",
            text="Invalid email or password.",
            buttons=[
                MDRaisedButton(
                    text="OK", on_release=self.close_dialog
                ),
            ],
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

class HomeScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('main.kv')

sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(HomeScreen(name='home'))

if __name__ == '__main__':
    MainApp().run()
