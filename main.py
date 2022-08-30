from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader


class PrimaryScreen(Screen):

    image_locations = {'island':
                           {'source': 'maps/map.jpg',
                            'labels': [],
                            'buttons': []
                            },
                       'mansion':
                           {'source': 'maps/map2.jpg',
                            'labels': [],
                            'buttons': [{'size': (0.5, 0.5),
                                         'pos': {'center_x': 0.5, 'center_y': 0.75},
                                         'text': 'Sound',
                                         'func': 'play_sound',
                                         'background': [0.5, 0.5, 0, 0.2],
                                         'my_id': 1}]
                            }
                       }

    def change_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'secondary'

    def map_change(self, caller):
        area = self.ids['game_area']
        area.clear_widgets()
        area.add_widget(Image(source=self.image_locations[caller.my_id]['source']))
        label_loc = self.image_locations[caller.my_id]['labels']
        for item in label_loc:
            pass
        button_loc = self.image_locations[caller.my_id]['buttons']
        for item in button_loc:
            button = (MDRaisedButton(
                size=item['size'],
                pos_hint=item['pos'],
                text=item['text'],
                my_id=f'button{item["my_id"]}',
                on_release=self.print_id
            ))
            area.add_widget(button)

    def print_id(self, instance):
        try:
            print(instance.my_id)
        except:
            pass

    def play_sound(self):
        sound = SoundLoader.load('sounds/ring.wav')
        if sound:
            sound.play()


class SecondaryScreen(Screen):
    pass

class TertiaryScreen(Screen):

    pass

class GameArea(MDFloatLayout):
    pass

class fruitinhouse(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.id = 'screen manager'
        sm.add_widget(PrimaryScreen(name='primary'))
        sm.add_widget(SecondaryScreen(name='secondary'))

        return sm

if __name__ =='__main__':

    fruitinhouse().run()

