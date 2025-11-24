class Diet:
    def __init__(self, id, name, description, datetime, is_diet=True) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.datetime = datetime
        self.is_diet = is_diet
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "datetime": self.datetime,
            "is_diet": self.is_diet,
        }