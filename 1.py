class Data:

    @classmethod
    def type(cls, data):
            split_data = data.split('-')
            print(*split_data)

    @staticmethod
    def validation(data):
        split_data = data.split('-')
        if 0 < int(split_data[0]) < 31:
            if 0 < int(split_data[1]) < 13:
                if int(split_data[2]) < 2022:
                    print('Дата введена верно')
                else:
                    print('Дата введена неверно')
            else:
                print('Дата введена неверно')
        else:
            print('Дата введена неверно')


Data.type("25-2-2020")
Data.validation("25-2-2020")
Data.validation("35-12-2020")
Data.validation("12-14-2020")
Data.validation("9-11-2023")