class StructureInfo:
    def __init__(self):
        # Default verse order for songs
        self.order_list = ['verse1', 'verse1',
                           'chorus', 'chorus',
                           'verse2', 'verse2',
                           'chorus', 'chorus',
                           'bridge',
                           'chorus', 'chorus', "finalChorus"]

    def setOrderList(self, new_order_list):
        self.order_list = new_order_list

    def getOrderList(self):
        return self.order_list
