from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class VideoTrackerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(text="VIDEO TRACKER", font_size='24sp', size_hint=(1, 0.2))
        layout.add_widget(title)
        
        select_btn = Button(text="📁 ВЫБРАТЬ ВИДЕО", size_hint=(1, 0.15))
        layout.add_widget(select_btn)
        
        info_label = Label(text="Файл не выбран", size_hint=(1, 0.1))
        layout.add_widget(info_label)
        
        process_btn = Button(text="▶ СТАРТ", size_hint=(1, 0.15), disabled=True)
        layout.add_widget(process_btn)
        
        return layout

if __name__ == '__main__':
    VideoTrackerApp().run()
