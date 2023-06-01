class Set:
    def __init__(self, *args) -> None:
        self.__items: tuple[int, ...] = args
        self.__dict_items: dict[int, int] = {}

    def show(self) -> tuple[int, ...]:
        for item in self.__items:
            if item not in self.__dict_items:
                self.__dict_items[item] = 0

            self.__dict_items[item] = 1

        self.__items = tuple(self.__dict_items.keys())

        return self.__items

    def add(self, val: int) -> str:
        if val in self.__items:
            return f"val {val} is exist"

        self.__dict_items[val] = 1
        return f"insert {val}"

    def remove(self, val: int) -> str:
        if val not in self.__items:
            return "val isn't exist"

        self.__dict_items.pop(val)
        return f"remove {val}"


sets = Set(1, 2, 3, 4, 5, 4, 3, 1)
print(sets.show())
print(sets.add(1))
print(sets.add(10))
print(sets.add(10))
print(sets.add(10))
print(sets.add(-10))
print(sets.show())
print(sets.remove(-10))
print(sets.show())
