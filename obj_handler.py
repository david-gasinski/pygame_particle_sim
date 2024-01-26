class ObjHandler:
    def __init__(self):
        self.objects = []
    
    # appends to the end
    def add_object(self, obj):
        self.objects.append(obj)

    # removes first occurence
    def remove_object(self, obj):
        self.objects.remove(obj)

    def get_objects(self):
        return self.objects