ds.models.section = function(data) {
  'use strict'

  var self = limivorous.observable()
                       .property('layout', {init: 'fixed'})
                       .extend(ds.models.item, {item_type: 'section'})
                       .extend(ds.models.container)
                       .build()

  if (data) {
    self.layout = data.layout || layout
  }
  ds.models.item.init(self, data)
  ds.models.container.init(self, data)

  self.interactive_properties = function() {
    return [
      ds.models.property({name: 'layout'}),
      ds.models.property({name: 'style'}),
      ds.models.property({name: 'css_class'})
    ]
  }

  self.toJSON = function() {
    var data = ds.models.container.json(self, ds.models.item.json(self))
    if (self.layout)
      data.layout = self.layout
    return data
  }

  return self
}

ds.models.section.Layout = {
  FIXED: 'fixed',
  FLUID: 'fluid',
  NONE:  'none'
}
