from enum import IntEnum


class ItemClasses(IntEnum):
    ITEM_CLASS_CONSUMABLE = 0
    ITEM_CLASS_CONTAINER = 1
    ITEM_CLASS_WEAPON = 2
    ITEM_CLASS_JEWELRY = 3
    ITEM_CLASS_ARMOR = 4
    ITEM_CLASS_REAGENT = 5
    ITEM_CLASS_PROJECTILE = 6
    ITEM_CLASS_TRADE_GOODS = 7
    ITEM_CLASS_GENERIC = 8
    ITEM_CLASS_BOOK = 9
    ITEM_CLASS_MONEY = 10
    ITEM_CLASS_QUIVER = 11
    ITEM_CLASS_QUEST = 12
    ITEM_CLASS_KEY = 13
    ITEM_CLASS_PERMANENT = 14
    ITEM_CLASS_JUNK = 15


class ItemSubClasses(IntEnum):
    # Consumable
    ITEM_SUBCLASS_CONSUMABLE = 0
    ITEM_SUBCLASS_FOOD = 1
    ITEM_SUBCLASS_LIQUID = 2
    ITEM_SUBCLASS_POTION = 3
    ITEM_SUBCLASS_SCROLL = 4
    ITEM_SUBCLASS_BANDAGE = 5
    ITEM_SUBCLASS_HEALTHSTONE = 6
    ITEM_SUBCLASS_COMBAT_EFFECT = 7

    # Container
    ITEM_SUBCLASS_BAG = 0
    ITEM_SUBCLASS_SOUL_BAG = 1
    ITEM_SUBCLASS_HERB_BAG = 2
    ITEM_SUBCLASS_ENCHANTING_BAG = 3

    # Weapon
    ITEM_SUBCLASS_AXE = 0
    ITEM_SUBCLASS_TWOHAND_AXE = 1
    ITEM_SUBCLASS_BOW = 2
    ITEM_SUBCLASS_GUN = 3
    ITEM_SUBCLASS_MACE = 4
    ITEM_SUBCLASS_TWOHAND_MACE = 5
    ITEM_SUBCLASS_POLEARM = 6
    ITEM_SUBCLASS_SWORD = 7
    ITEM_SUBCLASS_TWOHAND_SWORD = 8
    ITEM_SUBCLASS_WEAPON_obsolete = 9
    ITEM_SUBCLASS_STAFF = 10
    ITEM_SUBCLASS_WEAPON_EXOTIC = 11
    ITEM_SUBCLASS_WEAPON_EXOTIC2 = 12
    ITEM_SUBCLASS_FIST_WEAPON = 13
    ITEM_SUBCLASS_MISC_WEAPON = 14
    ITEM_SUBCLASS_DAGGER = 15
    ITEM_SUBCLASS_THROWN = 16
    ITEM_SUBCLASS_SPEAR = 17
    ITEM_SUBCLASS_CROSSBOW = 18
    ITEM_SUBCLASS_WAND = 19
    ITEM_SUBCLASS_FISHING_POLE = 20

    # Armor
    ITEM_SUBCLASS_MISC = 0
    ITEM_SUBCLASS_CLOTH = 1
    ITEM_SUBCLASS_LEATHER = 2
    ITEM_SUBCLASS_MAIL = 3
    ITEM_SUBCLASS_PLATE = 4
    ITEM_SUBCLASS_BUCKLER = 5
    ITEM_SUBCLASS_SHIELD = 6
    ITEM_SUBCLASS_LIBRAM = 7
    ITEM_SUBCLASS_IDOL = 8
    ITEM_SUBCLASS_TOTEM = 9

    # Projectile
    ITEM_SUBCLASS_WAND_obslete = 0
    ITEM_SUBCLASS_BOLT_obslete = 1
    ITEM_SUBCLASS_ARROW = 2
    ITEM_SUBCLASS_BULLET = 3
    ITEM_SUBCLASS_THROWN_obslete = 4

    # Trade goods
    ITEM_SUBCLASS_TRADE_GOODS = 0
    ITEM_SUBCLASS_PARTS = 1
    ITEM_SUBCLASS_EXPLOSIVES = 2
    ITEM_SUBCLASS_DEVICES = 3
    ITEM_SUBCLASS_GEMS = 4
    ITEM_SUBCLASS_CLOTHS = 5
    ITEM_SUBCLASS_LEATHERS = 6
    ITEM_SUBCLASS_METAL_AND_STONE = 7
    ITEM_SUBCLASS_MEAT = 8
    ITEM_SUBCLASS_HERB = 9
    ITEM_SUBCLASS_ELEMENTAL = 10
    ITEM_SUBCLASS_OTHERS = 11
    ITEM_SUBCLASS_ENCHANTANTS = 12
    ITEM_SUBCLASS_MATERIALS = 13

    # Recipe
    ITEM_SUBCLASS_BOOK = 0
    ITEM_SUBCLASS_LEATHERWORKING = 1
    ITEM_SUBCLASS_TAILORING = 2
    ITEM_SUBCLASS_ENGINEERING = 3
    ITEM_SUBCLASS_BLACKSMITHING = 4
    ITEM_SUBCLASS_COOKING = 5
    ITEM_SUBCLASS_ALCHEMY = 6
    ITEM_SUBCLASS_FIRST_AID = 7
    ITEM_SUBCLASS_ENCHANTING = 8
    ITEM_SUBCLASS_FISHING = 9
    ITEM_SUBCLASS_JEWELCRAFTING = 10

    # Quiver
    ITEM_SUBCLASS_QUIVER0_obslete = 0
    ITEM_SUBCLASS_QUIVER1_obslete = 1
    ITEM_SUBCLASS_QUIVER = 2
    ITEM_SUBCLASS_AMMO_POUCH = 3

    # Keys
    ITEM_SUBCLASS_KEY = 0
    ITEM_SUBCLASS_LOCKPICK = 1

    # Misc
    ITEM_SUBCLASS_JUNK = 0
    ITEM_SUBCLASS_REAGENT = 1
    ITEM_SUBCLASS_PET = 2
    ITEM_SUBCLASS_HOLIDAY = 3
    ITEM_SUBCLASS_OTHER = 4
    ITEM_SUBCLASS_MOUNT = 5


class BagFamilies(IntEnum):
    NONE = 0
    ARROWS = 1
    BULLETS = 2
    SOUL_SHARDS = 3
    UNKNOWN1 = 4
    UNKNOWN2 = 5
    HERBS = 6
    ENCHANTING_SUPP = 7
    ENGINEERING_SUPP = 8
    KEYS = 9


class InventoryTypes(IntEnum):
    NONE_EQUIP = 0x00
    HEAD = 0x01
    NECK = 0x02
    SHOULDER = 0x03
    BODY = 0x04
    CHEST = 0x05
    WAIST = 0x06
    LEGS = 0x07
    FEET = 0x08
    WRIST = 0x09
    HAND = 0x0A
    FINGER = 0x0B
    TRINKET = 0x0C
    WEAPON = 0x0D
    SHIELD = 0x0E
    RANGED = 0x0F
    CLOAK = 0x10
    TWOHANDEDWEAPON = 0x11
    BAG = 0x12
    TABARD = 0x13
    ROBE = 0x14
    WEAPONMAINHAND = 0x15
    WEAPONOFFHAND = 0x16
    HOLDABLE = 0x17
    AMMO = 0x18
    THROWN = 0x19
    RANGEDRIGHT = 0x1A
    NUM_TYPES = 0x1B


class InventorySlots(IntEnum):
    SLOT_HEAD = 0
    SLOT_NECK = 1
    SLOT_SHOULDERS = 2
    SLOT_SHIRT = 3
    SLOT_CHEST = 4
    SLOT_WAIST = 5
    SLOT_LEGS = 6
    SLOT_FEET = 7
    SLOT_WRISTS = 8
    SLOT_HANDS = 9
    SLOT_FINGERL = 10
    SLOT_FINGERR = 11
    SLOT_TRINKETL = 12
    SLOT_TRINKETR = 13
    SLOT_BACK = 14
    SLOT_MAINHAND = 15
    SLOT_OFFHAND = 16
    SLOT_RANGED = 17
    SLOT_TABARD = 18

    # Misc Types
    SLOT_BAG1 = 19
    SLOT_BAG2 = 20
    SLOT_BAG3 = 21
    SLOT_BAG4 = 22
    SLOT_INBACKPACK = 23

    SLOT_ITEM_START = 23
    SLOT_ITEM_END = 39

    SLOT_BANK_ITEM_START = 39
    SLOT_BANK_ITEM_END = 63
    SLOT_BANK_BAG_1 = 63
    SLOT_BANK_BAG_2 = 64
    SLOT_BANK_BAG_3 = 65
    SLOT_BANK_BAG_4 = 66
    SLOT_BANK_BAG_5 = 67
    SLOT_BANK_BAG_6 = 68
    SLOT_BANK_END = 69


class InventoryStats(IntEnum):
    MANA = 0
    HEALTH = 1
    AGILITY = 3
    STRENGTH = 4
    INTELLECT = 5
    SPIRIT = 6
    STAMINA = 7


class InventoryError(IntEnum):
    BAG_OK = 0
    BAG_LEVEL_MISMATCH = 1
    BAG_SKILL_MISMATCH = 2
    BAG_SLOT_MISMATCH = 3
    BAG_FULL = 4
    BAG_NO_BAGS_IN_BAGS = 5
    BAG_AMMO_ONLY = 6
    BAG_PROFICIENCY_NEEDED = 7
    BAG_NO_SLOTS_AVAILABLE = 8
    BAG_CLASS_NOTALLOWED = 9
    BAG_RACE_NOTALLOWED = 10
    BAG_2HWEAPON_ITEMEXISTSINOFFHAND = 11
    BAG_2HWEAPONBEINGWIELDED = 12
    BAG_2HWEAPON_SKILLNOTFOUND = 13
    BAG_ITEM_CLASS_MISMATCH = 14
    BAG_ITEM_SUBTYPE_MISMATCH = 15
    BAG_ITEM_MAX_COUNT_EXCEEDED = 16
    BAG_SLOT_NOT_EMPTY = 17
    BAG_CANT_STACK = 18
    BAG_NOT_EQUIPPABLE = 19
    BAG_CANT_SWAP = 20
    BAG_SLOT_EMPTY = 21
    BAG_ITEM_NOT_FOUND = 22
    BAG_ITEM_ALREADY_BOUND = 23
    BAG_DROP_TOO_FAR_AWAY = 24
    BAG_ITEM_TOO_FEW_TO_SPLIT = 25
    BAG_ITEM_SPLIT_FAILED = 26
    BAG_CANT_CAST_ENCHANTMENT = 27
    BAG_NOT_ENOUGH_GOLD = 28
    BAG_NOT_A_CONTAINER = 29
    BAG_NOT_EMPTY = 30
    BAG_NOT_OWNER = 31
    BAG_ONLY_ONE_QUIVER = 32
    BAG_NOBANKSLOT = 33
    BAG_NOBANKHERE = 34
    BAG_ITEM_LOCKED = 35
    BAG_NOT_WHILE_DEAD = 36
    BAG_CLIENT_LOCKED_OUT = 37
    BAG_ERROR = 38
    BAG_ONLY_ONE_BOLT = 39
    BAG_ONLY_ONE_AMMO = 40
    BAG_CANT_WRAP_STACKABLE = 41
    BAG_CANT_WRAP_EQUIPPED = 42
    BAG_CANT_WRAP_WRAPPED = 43
    BAG_CANT_WRAP_BOUND = 44
    BAG_CANT_WRAP_UNIQUE = 45
    BAG_CANT_WRAP_BAGS = 46
    BAG_LOOT_GONE = 47
    BAG_INV_FULL = 48
    BAG_SOLD_OUT = 49
    BAG_DONT_LIKE_YOU = 50
    BAG_UNKNOWN_ITEM = 51
    BAG_STACK_COUNT_EXCEEDED = 52
    BAG_QUANTITY_ZERO = 53
    BAG_DONT_HAVE_THAT_MANY = 54


class PetitionError(IntEnum):
    PETITION_SUCCESS = 0
    PETITION_ALREADY_SIGNED = 1
    PETITION_ALREADY_IN_GUILD = 2
    PETITION_CHARTER_CREATOR = 3
    PETITION_NOT_ENOUGH_SIGNATURES = 4
    PETITION_UNKNOWN_ERROR = 5


class ItemFlags(IntEnum):
    ITEM_FLAG_NO_PICKUP = 0x1
    ITEM_FLAG_CONJURED = 0x2
    ITEM_FLAG_HAS_LOOT = 0x4
    ITEM_FLAG_EXOTIC = 0x8
    ITEM_FLAG_DEPRECATED = 0x10
    ITEM_FLAG_OBSOLETE = 0x20
    ITEM_FLAG_PLAYERCAST = 0x40
    ITEM_FLAG_NO_EQUIPCOOLDOWN = 0x80
    ITEM_FLAG_INTBONUSINSTEAD = 0x100
    ITEM_FLAG_IS_WRAPPER = 0x200
    ITEM_FLAG_USES_RESOURCES = 0x400
    ITEM_FLAG_MULTI_DROP = 0x800
    ITEM_FLAG_BRIEFSPELLEFFECTS = 0x1000
    ITEM_FLAG_PETITION = 0x2000
    MAX_ITEM_FLAG = 0x8000


class ItemDynFlags(IntEnum):
    ITEM_DYNFLAG_BOUND = 0x1  # set in game at binding
    ITEM_DYNFLAG_TRANSLATED = 0x2
    ITEM_DYNFLAG_UNLOCKED = 0x4  # have meaning only for item with proto->LockId, if not set show as "Locked, req. lockpicking N"
    ITEM_DYNFLAG_WRAPPED = 0x8  # mark item as wrapped into wrapper container


# Only 4 types in 0.5.3.
class ItemEnchantmentType(IntEnum):
    NONE = 0
    PROC_SPELL = 1
    DAMAGE = 2
    BUFF_EQUIPPED = 3
    RESISTANCE = 4


class EnchantmentSlots(IntEnum):
    PERMANENT_SLOT = 0
    TEMPORARY_SLOT = 1
    OPTIONAL_ENCHANTMENT_0 = 2
    OPTIONAL_ENCHANTMENT_1 = 3
    OPTIONAL_ENCHANTMENT_2 = 4
