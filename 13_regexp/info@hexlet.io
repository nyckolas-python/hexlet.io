# Часть до @ должна содержать не менее одного символа класа \w. Пример: info
# Часть от @ до . , должна содержать только буквы и быть не короче трех символов.
# Часть после . , должна содержать только буквы и быть от 2 до 5 символов в длину. Пример: info

"\w+@[a-z]{3,}.[a-z]{2,5}"gm