
def checkUser(db_all: list, element):
    db_e = []
    for e in db_all:
        if e.userId is None:
            if e.userId == element:
                db_e.append(e)
        else:
            if any(f"{element}" in item for item in e.userId.split(",")):
                db_e.append(e)
    return db_e


def checkTeacher(db_all: list, element):
    db_e = []
    for e in db_all:
        if e.teacherId is None:
            if e.teacherId == element:
                db_e.append(e)
        else:
            if any(f"{element}" in item for item in e.teacherId.split(",")):
                db_e.append(e)
    return db_e
