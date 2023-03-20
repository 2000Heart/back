def checkUser(db_all: list, element):
    db_e = []
    for e in db_all:
        if e.userId is not None:
            for item in e.userId.split(","):
                if f"{element}" == item:
                    db_e.append(e)
    return db_e


def checkTeacher(db_all: list, element):
    db_e = []
    for e in db_all:
        if e.teacherId is not None:
            for item in e.teacherId.split(","):
                if item == f"{element}":
                    db_e.append(e)
    return db_e


def checkClass(db_all: list, element: list, schoolName: str):
    db_e = []
    for e in db_all:
        if e.schoolName == schoolName:
            for x in element:
                if e.className == x:
                    db_e.append(e)
    return db_e


def updateList(data: str, element: int):
    if element == 0:
        return data
    db_e = data.split(',')
    for e in db_e:
        if e == f"{element}":
            return data
    db_e.append(f'{element}')
    return ','.join(db_e)
