def latlng(self):
    return self.context.latlng
    
def etasje(self):
    list = []
    cords = self.context.latlng
    for cord in cords:
        if cord[0] not in list:
            list.append(cord[0]) 
    return list