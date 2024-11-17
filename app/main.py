from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from database.db_manager import DatabaseManager
from views.screen import MainScreen
from kivy.lang import Builder
from kivy.core.window import Window

class ScoreTrackerApp(App):
    def build(self):
        Window.size = (600, 800)
        self.dd_manager = DatabaseManager()
        sm = ScreenManager()
        main_screen = MainScreen(self.db_manager, name='main')
        sm.add_widget(main_screen)
        return sm
    
    def on_stop(self):
        self.db_manager.close_connection()
        
if __name__ == '__main__':
    ScoreTrackerApp().run()