# Choise

# Network
NETMASK_CHOICES = (
        (24, ("24 - 255.255.255.0")),
        (25, ("25 - 255.255.255.128")),
        (26, ("26 - 255.255.255.192")),
        (27, ("27 - 255.255.255.224")),
        (28, ("28 - 255.255.255.240")),
        (29, ("29 - 255.255.255.248")),
        (30, ("30 - 255.255.255.252")),
    )

# State
WAREHOUSE_NEW = 'WN'
WAREHOUSE_USED = 'WU'
WAREHOUSE_BROKEN = 'WB'
INSTALLED = 'I'
UNDER_REPAIT = 'UR'
WRITEN_OFF = 'WO'

STATE_CHOICES = (
    (WAREHOUSE_NEW, 'Склад (новое)'),
    (WAREHOUSE_USED, 'Склад (б/у)'),
    (WAREHOUSE_BROKEN, 'Склад (сломано)'),
    (INSTALLED, 'Установлено'),
    (UNDER_REPAIT, 'В ремонте'),
    (WRITEN_OFF, 'Списано'),
)
