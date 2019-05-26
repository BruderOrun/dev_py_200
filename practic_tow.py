class Glass:

    def __init__(self, capacity_volume, occupied_volume):
        '''


        '''

        # self.is_valid_date(year, month, day)
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    @classmethod
    def is_valid_glass(cls, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, int):
            raise TypeError('capacity_volume must be int')
        if not isinstance(occupied_volume, int):
            raise TypeError('occupied_volume must be int')

        if not 0 < capacity_volume or capacity_volume > 10.0:
            raise ValueError('capacity_volume must be >0 and < 10.0')

        if not 0 < occupied_volume or occupied_volume > 10.0:
            raise ValueError('occupied_volume must be >0 and < 10.0')


glass_1 = Glass(8, 10)
# print(glass_1.capacity_volume)
glass_2 = Glass(2.0, 9.0)


# print(glass_2.capacity_volume)


class GlassDefaultArg:
    def __init__(self, occupied_volume=0):
        self.occupied_volume = occupied_volume

    @classmethod
    def is_valid_deffault(cls, occupied_volume):
        if not isinstance(occupied_volume, int):
            raise TypeError('occupied_volume must be int')
        if not 0 < occupied_volume or occupied_volume > 10.0:
            raise ValueError('occupied_volume must be >0 and < 10.0')


glas_def_arg_1 = GlassDefaultArg()
glas_def_arg_2 = GlassDefaultArg(200)


# print(glas_def_arg_1.occupied_volume)
# print(glas_def_arg_2.occupied_volume)

class GlassDefaultListArg:

    def __init__(self, capacity_volume, occupied_volume=[]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(capacity_volume)
        # self.x = input()
        # self.occupied_volume.append(self.x)

#
# glassDefaultListAr_1 = GlassDefaultListArg(2)
#
# print(glassDefaultListAr_1.occupied_volume)
#
# glassDefaultListAr_2 = GlassDefaultListArg(2)
# print(glassDefaultListAr_2.occupied_volume)
#
# glassDefaultListAr_3 = GlassDefaultListArg(2)
# print(glassDefaultListAr_3.occupied_volume)
# print(glassDefaultListAr_1.occupied_volume)
# print(glassDefaultListAr_2.occupied_volume)
# glassDefaultListAr_3 = GlassDefaultListArg(6)
# print(glassDefaultListAr_2.occupied_volume)


class GlassAddRemove:
    def __init__(self,occupied_volume=0,water=0):
        self.occupied_volume = occupied_volume
        self.water = water

    def add_water(self):
        self.occupied_volume+=self.water
        return self.occupied_volume


    def remove_water(self):

        pass

glassAddRemove_1=GlassAddRemove(3,5)
# print(glassAddRemove_1.add_water())
print(glassAddRemove_1.add_water())
glassAddRemove_1.add_water()
print(glassAddRemove_1.add_water())
print(glassAddRemove_1.add_water())


def f():
    ...