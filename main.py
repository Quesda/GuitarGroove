from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class HomeScreen(Screen):
    pass


class GuitarScreen(Screen):
    pass


class UkuleleScreen(Screen):
    pass


class GSongsScreen(Screen):
    pass


class USongsScreen(Screen):
    pass


class GAccordsScreen(Screen):
    pass


class UAccordsScreen(Screen):
    pass


class GSong1(Screen):
    gsong1 = open('GuitarSongs/song1.txt', encoding='UTF-8').read()


class GSong2(Screen):
    gsong2 = open('GuitarSongs/song2.txt', encoding='UTF-8').read()


class GSong3(Screen):
    gsong3 = open('GuitarSongs/song3.txt', encoding='UTF-8').read()


class GSong4(Screen):
    gsong4 = open('GuitarSongs/song4.txt', encoding='UTF-8').read()


class GSong5(Screen):
    gsong5 = open('GuitarSongs/song5.txt', encoding='UTF-8').read()


class USong1(Screen):
    usong1 = open('UkuleleSongs/song1.txt', encoding='UTF-8').read()


class USong2(Screen):
    usong2 = open('UkuleleSongs/song2.txt', encoding='UTF-8').read()


class USong3(Screen):
    usong3 = open('UkuleleSongs/song3.txt', encoding='UTF-8').read()


class USong4(Screen):
    usong4 = open('UkuleleSongs/song4.txt', encoding='UTF-8').read()


class USong5(Screen):
    usong5 = open('UkuleleSongs/song5.txt', encoding='UTF-8').read()


kv = Builder.load_file("gg.kv")


class GGApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))

        sm.add_widget(GuitarScreen(name='guitar'))
        sm.add_widget(UkuleleScreen(name='ukulele'))

        sm.add_widget(GAccordsScreen(name='gaccords'))
        sm.add_widget(UAccordsScreen(name='uaccords'))

        sm.add_widget(GSongsScreen(name='gsongs'))
        sm.add_widget(USongsScreen(name='usongs'))

        sm.add_widget(GSong1(name='gsong1'))
        sm.add_widget(GSong2(name='gsong2'))
        sm.add_widget(GSong3(name='gsong3'))
        sm.add_widget(GSong4(name='gsong4'))
        sm.add_widget(GSong5(name='gsong5'))

        sm.add_widget(USong1(name='usong1'))
        sm.add_widget(USong2(name='usong2'))
        sm.add_widget(USong3(name='usong3'))
        sm.add_widget(USong4(name='usong4'))
        sm.add_widget(USong5(name='usong5'))

        return sm


if __name__ == "__main__":
    GGApp().run()
