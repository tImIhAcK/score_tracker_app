from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.metrics import dp


class MainScreen(Screen):
    category_spinner = ObjectProperty(None)
    score_input = ObjectProperty(None)
    note_input = ObjectProperty(None)
    score_grid = ObjectProperty(None)   
    status_label = StringProperty("")
    def __init__(self, db_manager, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.db_manager = db_manager
    
    def on_start(self):
        self.update_scores_display()
    
    def add_score(self):
        category = self.category_spinner.text
        score = self.score_input.text
        note = self.note_input.text
        
        if not score or not note or not category:
            self.status_label = "Please enter all fields."
            return
        
        try:
            score = float(score)
        except ValueError:
            self.status_label = "Score must be a number."
            return
        
        if score < 0 or score > 100:
            self.status_label = "Score must be between 0 and 100."
            return
        
        self.db_manager.add_score(category, score, note)
        self.clear_inputs()
        self.update_scores_display()
        self.status_label = "Score added successfully."
        
    def update_scores_display(self):
        scores = self.db_manager.get_scores()
        self.score_grid.clear_widgets()
        
        headers = ["Date", "Category", "Score", "Notes"]
        for header in headers:
            label = Label(text=header, font_size=24, bold=True)
            self.score_grid.add_widget(label)
        
        # Display the scores
        for score in scores:
            for item in score[1:]:
                label = Label(text=str(item), size_hint_y= None, height= dp(40))
                self.score_grid.add_widget(label)
        
    def clear_inputs(self):
        self.category_spinner.text = "General"
        self.score_input.text = ""
        self.note_input.text = ""

        
