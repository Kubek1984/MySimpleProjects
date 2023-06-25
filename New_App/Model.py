from Objects import MainObject, FlashCard, Lesson


class Model:

    def __init__(self):
        self.main_dictionary = {}

    def load_dictionary(self):
        pass

    def make_flashcard_object(self, subject, topic, name, text):
        flash_object = FlashCard(subject, topic, name, text)
        return flash_object

    def add_object_to_dictionary(self):
        pass

    def save_dictionary(self):
        pass

    def edit_object(self):
        pass

    def delete_object(self):
        pass


