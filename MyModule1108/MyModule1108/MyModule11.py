class My_Data_Point:
    def __init__(self):
        @property #ゲッター
        def label(self):
            return self.__label

        @label.setter #セッター
        def label(self,label):
            self.__label=label

        @property #ゲッター
        def coordinate(self):
            return self.__coordinate

        @coordinate.setter #セッター
        def coordinate(self,coordinate):
            self.__coordinate=coordinate