from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from verbs import verbes, items

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''

class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected=BooleanProperty(False)
    selectable=BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected=is_selected
        # if is_selected:
        #     print("selection changed to {0}".format(rv.data[index]))
        # else:
        #     print("selection removed for {0}".format(rv.data[index]))

class RV(GridLayout):
    data=ListProperty([])
    entry_text=ObjectProperty
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in items]
    def search(self):
        txt=self.entry_text.text
        val=verbes.values()
        typ = "Type a verb"
        eror= "no verb"
        #ver = verbes.keys()
        for ver in verbes.keys():
            if txt==ver:
                result=verbes.get(ver)
                self.ids.present.text=result[0]
                self.ids.past.text=result[1]
                self.ids.Pparticiple.text=result[2]

            if txt=='' and txt!=ver:
                self.ids.present.text = eror
                self.ids.past.text = eror
                self.ids.Pparticiple.text = eror

class Verb_RecyApp(App):
    def build(self):
        return RV()
if __name__=="__main__":
    Verb_RecyApp().run()


