from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import ILeftBodyTouch, OneLineIconListItem


Builder.load_string('''
<ItemForList>
    text: root.text

    IconLeftSampleWidget:
        icon: root.icon


<Example@MDFloatLayout>

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: app.title
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            elevation: 4
            left_action_items: [['menu', lambda x: x]]

        MDScrollView:
            id: refresh_layout
            
            root_layout: root

            MDGridLayout:
                id: box
                adaptive_height: True
                cols: 1
''')


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class ItemForList(OneLineIconListItem):
    icon = StringProperty()


class Example(MDApp):
    title = 'Example Refresh Layout'
    screen = None
    x = 500
    y = 610

    def build(self):
        self.screen = Factory.Example()
        self.set_list()

        return self.screen

    def set_list(self):
        
            names_icons_list = list(md_icons.keys())[self.x:self.y]
            for name_icon in names_icons_list:
                
                self.screen.ids.box.add_widget(
                    ItemForList(icon=name_icon, text=name_icon))
        

    


Example().run()
