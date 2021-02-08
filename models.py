import mongoengine as me


class Label(me.DynamicDocument):
    label = me.StringField(required=True)
    _type = me.StringField()
    geometry = me.DynamicField()
    properties = me.DynamicField()
    style = me.DynamicField()

    def to_json(self):
        return {
            "label": self.label,
            "type": self._type,
            "properties": self.properties,
            "geometry": self.geometry,
            "style": self.style
        }
