from datetime import date
from application import *
if __name__ == '__main__':
    calculate_salary()
    db.get_employees()
    print(date.today())
