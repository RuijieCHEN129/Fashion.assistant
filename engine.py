from modules.storage import save_history

# Age group definitions
AGE_GROUP_LABELS = {
    'child': (0, 17),
    'youth': (18, 30),
    'adult': (31, 60),
    'senior': (61, 120)
}

class BaseFashionAssistant:
    def __init__(self):
        self.database = []

    def suggest_outfits(self, prefs):
        matches = [item for item in self.database
                   if item['weather'] == prefs['weather'] and item['occasion'] == prefs['occasion']]
        save_history(prefs, matches)
        return matches

class ChildFashionAssistant(BaseFashionAssistant):
    def __init__(self):
        super().__init__()
        self.database = [
            {'weather': 'sunny', 'occasion': 'casual', 'top': 'T-shirt', 'bottom': 'jeans', 'shoes': 'Nike sneakers', 'image': 'assets/images/sunday_relax.jpg'},
            {'weather': 'rainy', 'occasion': 'casual', 'top': 'trench coat', 'bottom': 'skirt', 'shoes': 'leather shoes', 'image': 'assets/images/rainy_relax.jpg'}
        ]

class YouthFashionAssistant(BaseFashionAssistant):
    def __init__(self):
        super().__init__()
        self.database = [
            {'weather': 'sunny', 'occasion': 'casual', 'top': 'T-shirt', 'bottom': 'jeans', 'shoes': 'Nike sneakers', 'image': 'assets/images/sunday_relax.jpg'},
            {'weather': 'sunny', 'occasion': 'outside for night', 'top': 'T-shirt', 'bottom': 'skirt', 'shoes': 'sandals', 'image': 'assets/images/sunday_outside_for_night.jpg'},
            {'weather': 'hot', 'occasion': 'outside for night', 'top': 'athletic wear', 'bottom': 'shorts', 'shoes': 'sandals', 'image': 'assets/images/hot_outside_for_night.jpg'}
        ]

class AdultFashionAssistant(BaseFashionAssistant):
    def __init__(self):
        super().__init__()
        self.database = [
            {'weather': 'sunny', 'occasion': 'outside for night', 'top': 'T-shirt', 'bottom': 'skirt', 'shoes': 'sandals', 'image': 'assets/images/sunday_outside_for_night.jpg'},
            {'weather': 'cold', 'occasion': 'work', 'top': 'sweater', 'bottom': 'jeans', 'shoes': 'leather shoes', 'image': 'assets/images/cold_work.jpg'},
            {'weather': 'rainy', 'occasion': 'casual', 'top': 'trench coat', 'bottom': 'skirt', 'shoes': 'leather shoes', 'image': 'assets/images/rainy_relax.jpg'}
        ]

class SeniorFashionAssistant(BaseFashionAssistant):
    def __init__(self):
        super().__init__()
        self.database = [
            {'weather': 'cold', 'occasion': 'casual', 'top': 'leather jacket', 'bottom': 'jeans', 'shoes': 'leather shoes', 'image': 'assets/images/cold_relax.jpg'},
            {'weather': 'rainy', 'occasion': 'work', 'top': 'rain coat', 'bottom': 'waterproof pants', 'shoes': 'rain boots', 'image': 'assets/images/rainy_work.jpg'},
            {'weather': 'hot', 'occasion': 'work', 'top': 'T-shirt', 'bottom': 'shorts', 'shoes': 'slippers', 'image': 'assets/images/hot_work.jpg'}
        ]

class FashionAssistantFactory:
    @staticmethod
    def get_age_group(age):
        for label, (min_age, max_age) in AGE_GROUP_LABELS.items():
            if min_age <= age <= max_age:
                return label
        return 'adult'

    @staticmethod
    def get_assistant(age):
        group = FashionAssistantFactory.get_age_group(age)
        if group == 'child':
            return ChildFashionAssistant()
        elif group == 'youth':
            return YouthFashionAssistant()
        elif group == 'adult':
            return AdultFashionAssistant()
        else:
            return SeniorFashionAssistant()


