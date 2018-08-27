import datetime

YEARS = tuple([(x, str(x)+'年') for x in range(2015, datetime.datetime.now().year+1)])

MONTHS = (
    (1, '1月'),
    (2, '2月'),
    (3, '3月'),
    (4, '4月'),
    (5, '5月'),
    (6, '6月'),
    (7, '7月'),
    (8, '8月'),
    (9, '9月'),
    (10, '10月'),
    (11, '11月'),
    (12, '12月'),
)

# 技术栈
TECH_STACK = (
    ('JAVA', 'JAVA'),
    ('PYTHON', 'PYTHON'),
    ('PHP', 'PHP'),
)


def enum_to_dict(enum):
    dict = {}
    for item in enum:
        dict[item[0]] = item[1]
    return dict


all_enums = {
    'YEARS': enum_to_dict(YEARS),
    'MONTHS': enum_to_dict(MONTHS),
    'TECH_STACK':enum_to_dict(TECH_STACK),
}
