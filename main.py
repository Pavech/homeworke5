import random
from abc import ABC, abstractmethod
from random import randint

print("Герой, добро пожаловать!")
monster_counter = 0


# Абстрактный продукт
class Enemy(ABC):
    """Абстрактный класс игрового противника."""

    @abstractmethod
    def create(self) -> dict:
        """Метод, наличие которого обязательно у всех"""
        ...


# Конкретный продукт
class Ogre(Enemy):

    def create(self) -> dict:
        return {'hp': randint(7, 15), 'race': 'Ogre', 'type': 'sword', 'damage': randint(7, 15)}


# Конкретный продукт
class BloodElf(Enemy):
    bow = True

    def create(self) -> dict:
        return {'hp': randint(7, 15), 'race': 'BloodElf', 'type': 'bow', 'damage': randint(7, 15)}


# Конкретный продукт
class Troll(Enemy):

    def create(self) -> dict:
        return {'hp': randint(7, 15), 'race': 'Troll', "type": 'fireball', 'damage': randint(7, 15)}


# Абстрактная фабрика
class EnemyFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    @abstractmethod
    def create_enemy(self) -> dict:
        """Создание абстрактного продукта."""
        pass


# Конеретная фабрика
class OgreFactory(EnemyFactory):
    """Конкретная фабрика игрового противника."""

    def create_enemy(self):
        return Ogre()


# Конеретная фабрика
class TrollFactory(EnemyFactory):
    """Конкретная фабрика игрового противника."""

    def create_enemy(self):
        return Troll()


# Конеретная фабрика
class BloodElfFactory(EnemyFactory):
    """Конкретная фабрика игрового противника."""

    def create_enemy(self):
        return BloodElf()


def spawner_enemy() -> dict:
    """Спаун врагов"""
    spawner_to_factory_mapping = {
        "Ogre": OgreFactory,
        "Troll": TrollFactory,
        "BloodElf": BloodElfFactory
    }

    enemy_type_list = ["Ogre", "Troll", "BloodElf"]

    for i in range(1):
        SPAWNER_TYPE = random.choice(enemy_type_list)
        spawner_en = spawner_to_factory_mapping[SPAWNER_TYPE]()
        enemy = spawner_en.create_enemy()
        action = enemy.create()
        return action


class Hero(ABC):
    """Абстрактный класс игрового противника."""

    @abstractmethod
    def create_hero(self):
        """Метод, наличие которого обязательно у всех"""
        ...


# Конкретный продукт
class War(Hero):

    def create_hero(self) -> dict:
        return {'hp': 15, 'class': 'War', 'type': 'sword', 'items': {'sword': 5}}


# Конкретный продукт
class Hunter(Hero):

    def create_hero(self) -> dict:
        return {'hp': 15, 'class': 'Hunter', 'type': 'bow', 'items': {'sword': 5}}


# Конкретный продукт
class Mage(Hero):

    def create_hero(self) -> dict:
        return {'hp': 15, 'class': 'Mage', 'type': 'fireball', 'items': {'sword': 5}}


# Абстрактная фабрика
class HeroFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    @abstractmethod
    def create(self) -> dict:
        """Создание абстрактного продукта."""
        pass


# Конеретная фабрика
class WarFactory(HeroFactory):
    """Конкретная фабрика игрового противника."""

    def create(self):
        return War()


# Конеретная фабрика
class HunterFactory(HeroFactory):
    """Конкретная фабрика игрового противника."""

    def create(self):
        return Hunter()


# Конеретная фабрика
class MageFactory(HeroFactory):
    """Конкретная фабрика игрового противника."""

    def create(self):
        return Mage()


def spawner_hero() -> dict:
    """Спаун героев."""
    spawner_to_factory_mapping = {
        "War": WarFactory,
        "Hunter": HunterFactory,
        "Mage": MageFactory
    }
    while True:
        choice = input('Выберите героя: 1-Воин, 2-Лучник, 3-Маг: ')
        if choice == '1':
            hero = spawner_to_factory_mapping["War"]()
            h = hero.create()
            return h.create_hero()
        if choice == '2':
            hero = spawner_to_factory_mapping["Hunter"]()
            h = hero.create()
            return h.create_hero()
        if choice == '3':
            hero = spawner_to_factory_mapping["Mage"]()
            h = hero.create()
            return h.create_hero()
        else:
            print("На выбор доступны только три персонажа, выбери из них")


# Абстрактный продукт
class Items(ABC):
    """Абстрактный класс игрового противника."""

    @abstractmethod
    def create(self):
        """Метод, наличие которого обязательно у всех"""
        ...


# Конкретный продукт
class Sword(Items):

    def create(self) -> dict:
        return {'sword': randint(2, 6)}


# Конкретный продукт
class Arrows(Items):

    def create(self) -> dict:
        return {'arrows': randint(2, 6)}


# Конкретный продукт
class Bow(Items):

    def create(self) -> dict:
        return {'bow': randint(2, 6)}


class Magick_book(Items):

    def create(self) -> dict:
        return {'magick_book': randint(2, 6)}


class Totem(Items):

    def create(self) -> dict:
        return {'totem': {}}


# Абстрактная фабрика
class ItemsFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    @abstractmethod
    def create_items(self):
        """Создание абстрактного продукта."""
        pass


# Конеретная фабрика
class SwordFactory(ItemsFactory):
    """Конкретная фабрика игрового противника."""

    def create_items(self):
        return Sword()


# Конеретная фабрика
class ArrowsFactory(ItemsFactory):
    """Конкретная фабрика игрового противника."""

    def create_items(self):
        return Arrows()


# Конеретная фабрика
class BowFactory(ItemsFactory):
    """Конкретная фабрика игрового противника."""

    def create_items(self):
        return Bow()


class Magick_bookFactory(ItemsFactory):
    """Конкретная фабрика игрового противника."""

    def create_items(self):
        return Magick_book()


class TotemFactory(ItemsFactory):
    """Конкретная фабрика игрового противника."""

    def create_items(self):
        return Totem()


def spawner_items(hero) -> dict:
    """Спаун предметов."""
    bonus = 10
    spawner_to_factory_mapping = {
        "Sword": SwordFactory,
        "Bow": BowFactory,
        "Arrow": ArrowsFactory,
        "Magick_book": Magick_bookFactory,
        "Totem": TotemFactory
    }

    items_type_list = ["Totem", "Sword", "Bow", "Arrow", "Magick_book"]

    SPAWNER_TYPE = random.choice(items_type_list)
    spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
    items = spawner.create_items()
    action = items.create()
    if list(action.keys()) == ['sword'] and hero['class'] == 'War':
        print(f'Выпал меч {action} и т.к. вы воин, вы удостоины более сильного меча')
        action.update({'sword': action['sword'] + bonus})
        return action
    elif list(action.keys()) == ['bow'] and hero['class'] == 'Hunter':
        print(f'Выпал лук {action} и т.к. вы великий лучник, вы удостоины более сильного лука')
        action.update({'bow': action['bow'] + bonus})
        return action
    elif list(action.keys()) == ['magick_book'] and hero['class'] == 'Mage':
        print(f'Выпала книга заклинаний {action}, о вас слагают легенды, получайте более сильные заклинания')
        action.update({'magick_book': action['magick_book'] + bonus})
        return action
    elif list(action.keys()) == ['totem']:
        print("Какая находка, вам выпал тотем, при помощи тотема вы сможете восстановить свою жизнь")
        return action
    elif list(action.keys()) == ['arrows']:
        print("Вы нашли необходимые стрелы для лука")
        return action
    else:
        print(f'Вам выпал {action}')
        return action


def fight_items(hero: dict) -> list:
    """Функция создающая список доступного оружия"""
    hero_ = hero['items']
    hero_list = list(hero_.items())
    fight_list = list()
    if 'bow' and 'arrow' in hero_:
        for index, value in enumerate(hero_list):
            if value[0] in ('sword', 'bow', 'magick_book'):
                fight_list.append(value)
        return fight_list
    else:
        for index, value in enumerate(hero_list):
            if value[0] in ('sword', 'magick_book'):
                fight_list.append(value)
        return fight_list


def userChoice() -> int:
    """Выбор действия."""
    i = int(input())
    while i != 1 or i != 2:
        if i == 1 or i == 2:
            break
        else:
            print('Необходимо выбрать значения: "1" или "2"')
            i = int(input())
    return i


def choice_item(hero_items: dict) -> str:
    """Функция выбора предмета из инвентаря."""
    print(list(hero_items))
    items = list(hero_items)
    while True:
        item_ = input(f"Введите номер предмета от 1 до {len(items)}: ")
        if 1 <= int(item_) < len(items) + 1:
            x = (items[int(item_) - 1])
            print(f'Ваш выбор пал на данный предмет {x}')
            return x
        print("Данный предмет отсутствует в инвентаре")


def fight(hero: dict) -> int:
    """Функция боя."""
    passive_spell = 2
    hero_ = hero
    hero_hp = hero_['hp']
    enemy = spawner_enemy()
    enemy_race = enemy['race']
    hp_enemy = enemy['hp']
    type_attack = enemy["type"]
    damage_enemy = enemy['damage']

    print(
        f"БОЙ! Вы встречаете {enemy_race} со здоровьем равным {hp_enemy} видом атаки {type_attack} "
        f"и уроном равным {damage_enemy} "
    )
    print(f'Твое здоровье {hero_hp} и твои предметы {(fight_items(hero_))}')
    print("Сделайте свой выбор: 1 - Вступить в бой; 2 - Покинуть поле сражения")
    otv1 = userChoice()
    if otv1 == 1:

        if hero_['type'] == enemy['type'] == 'sword':
            while hero_hp > 0 and hp_enemy > 0:
                print('Идем в бой? 1 - Да, 2 - Нет ')
                otv2 = userChoice()
                if otv2 == 1:
                    print(f'Твое здоровье {hero_hp}')
                    print(f'Какое оружие берем?')
                    choice_weapon = choice_item(fight_items(hero_))
                    print(choice_weapon)
                    my_choice_weapon = choice_weapon[0]
                    hero_attack = choice_weapon[1]
                    if my_choice_weapon == 'magick_book':
                        hp_enemy -= hero_attack
                        hero_hp -= damage_enemy / passive_spell

                    if my_choice_weapon == 'arrow':
                        hp_enemy -= hero_attack
                        hero_hp -= (damage_enemy / passive_spell)

                    if my_choice_weapon == 'sword':
                        hero_hp -= (damage_enemy / passive_spell)
                        hp_enemy -= hero_attack
                if otv2 == 2:
                    print(f"Вы убегаете с поля боя :( Ваше здоровье равно {hero_hp}")
                    return 2
            if hp_enemy <= 0 and hero_hp >= 1:
                print(f"Вы победили этого монстра! Ваше здоровье равно {hero_hp}")
                return 1
            else:
                print("ПОРАЖЕНИЕ!")
                return 0

        elif hero_['type'] == enemy['type'] == 'bow':
            while hero_hp > 0 and hp_enemy > 0:
                print('Идем в бой? 1 - Да, 2 - Нет ')
                otv2 = userChoice()
                if otv2 == 1:
                    print(f'Какое оружие берем?')
                    choice_weapon = choice_item(fight_items(hero_))
                    print(choice_weapon)
                    my_choice_weapon = choice_weapon[0]
                    hero_attack = choice_weapon[1]
                    if my_choice_weapon == 'magick_book':
                        hp_enemy -= hero_attack
                        hero_hp -= damage_enemy / passive_spell

                    if my_choice_weapon == 'arrow':
                        hp_enemy -= hero_attack
                        hero_hp -= damage_enemy / passive_spell

                    if my_choice_weapon == 'sword':
                        hero_hp -= damage_enemy / passive_spell
                        hp_enemy -= hero_attack
                if otv2 == 2:
                    print(f"Вы убегаете с поля боя :( Ваше здоровье равно {hero_hp}")
                    return 2
            if hp_enemy <= 0 and hero_hp >= 1:
                print(f"Вы победили этого монстра! Ваше здоровье равно {hero_hp}")
                return 1
            else:
                print("ПОРАЖЕНИЕ!")
                return 0

        if hero_['type'] == enemy['type'] == 'fireball':

            while hero_hp > 0 and hp_enemy > 0:
                print('Идем в бой? 1 - Да, 2 - Нет ')
                otv2 = userChoice()
                if otv2 == 1:
                    print(f'Какое оружие берем?')
                    choice_weapon = choice_item(fight_items(hero_))
                    print(choice_weapon)
                    my_choice_weapon = choice_weapon[0]
                    hero_attack = choice_weapon[1]
                    if my_choice_weapon == 'magick_book':
                        hp_enemy -= hero_attack
                        hero_hp -= damage_enemy / passive_spell

                    if my_choice_weapon == 'arrow':
                        hero_hp -= damage_enemy / passive_spell
                        hp_enemy -= hero_attack

                    if my_choice_weapon == 'sword':
                        hero_hp -= damage_enemy / passive_spell
                        hp_enemy -= hero_attack
                if otv2 == 2:
                    print(f"Вы убегаете с поля боя :( Ваше здоровье равно {hero_hp}")
                    return 2
            if hp_enemy <= 0 and hero_hp >= 1:
                print(f"Вы победили этого монстра! Ваше здоровье равно {hero_hp}")
                return 1
            else:
                print("ПОРАЖЕНИЕ!")
                return 0

        if hero_['type'] != enemy['type']:
            while hero_hp > 0 and hp_enemy > 0:
                print('Идем в бой? 1 - Да, 2 - Нет ')
                otv2 = userChoice()
                if otv2 == 1:
                    print(f'Какое оружие берем?')
                    choice_weapon = choice_item(fight_items(hero_))
                    print(choice_weapon)
                    my_choice_weapon = choice_weapon[0]
                    hero_attack = choice_weapon[1]
                    if my_choice_weapon == 'magick_book':
                        hp_enemy -= hero_attack
                        hero_hp -= damage_enemy

                    if my_choice_weapon == 'arrow' and enemy['type'] == 'sword':
                        hp_enemy -= hero_attack
                        hero_hp -= damage_enemy

                    if my_choice_weapon == 'sword':
                        hero_hp -= damage_enemy
                        hp_enemy -= hero_attack

                    else:
                        hero_hp -= damage_enemy
                        hp_enemy -= hero_attack
                if otv2 == 2:
                    print(f"Вы убегаете с поля боя :( Ваше здоровье равно {hero_hp}")
                    return 2
            if hp_enemy <= 0 and hero_hp >= 1:
                print(f"Вы победили этого монстра! Ваше здоровье равно {hero_hp}")
                return 1
            else:
                print("ПОРАЖЕНИЕ!")
                return 0
    if otv1 == 2:
        print("Вы убегаете с поля боя :(")
        return 2
    return 0


def box(hero: dict) -> dict:
    """Функция генерации предметов"""
    print(f'Ого, ты наткнулся на новый крутой шмот.1-Подобрать, 2-Пройти мимо')
    box_item = spawner_items(hero)
    otv = userChoice()
    if otv == 1:
        if len(hero['items']) == 4:
            print(
                f'Хм...твой инвентарь полон, посмотри {hero["items"]}. '
                f'1 - Что-нибудь выбросить, 2 - Оставить все как есть')
            otv3 = userChoice()
            if otv3 == 1:
                remove_ = hero['items']
                print(f'Какой предмет выкинуть?')
                delete = choice_item(remove_)
                hero['items'].pop(delete)
                hero['items'].update(box_item)
                print(f'Инвентарь теперь выглядит так: {hero["items"]}')
                return hero
        if list(box_item.keys()) == ['totem']:
            for value in list(hero['items']):
                if value == 'totem':
                    print("У тебя уже присутствует тотем в инвентаре. Хочешь его обновить? 1 - Берем, 2 - Идем мимо")
                    otv2 = userChoice()
                    if otv2 == 1:
                        hero['items'].pop('totem')
                        hero['items'].update({'totem': {}})
                        print(f'Тотем в рюкзаке, теперь твой инвентарь выглядит так, {hero["items"]}')
                        return hero
                else:
                    hero['items'].update(box_item)
                    print(f'Инвентарь теперь выглядит так: {hero["items"]}')
                    return hero
        else:
            hero['items'].update(box_item)
            print(f'Инвентарь теперь выглядит так: {hero["items"]}')
            return hero


def game() -> None:
    """Главная функция."""
    global monster_counter
    hero_ = spawner_hero()
    health = randint(1, 5)
    while monster_counter != 10:
        i = random.randint(1, 3)
        if i == 1:
            f = fight(hero_)
            if f == 1:
                monster_counter += 1
                print(f'Монстров убито {monster_counter}')
            elif f == 2:
                print("Герой наберись сил")
            else:
                break
        elif i == 2:
            box(hero_)
        else:
            print(f'Ты нашел яблоко!!!')
            hero_.update({'hp': hero_['hp'] + health})
            print(f'Герой, твое здоровье попраивлось теперь оно равно: {hero_["hp"]}')
    if monster_counter == 10:
        print("ПОБЕДА")


game()
