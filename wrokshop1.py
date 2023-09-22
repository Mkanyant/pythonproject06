#13

def showProgramName( ) :
    print(' **--โปรแกรมตรวจสอบเกรดเฉลี่ย**')

def inputData( ) :
    name = input('ป้อนชื่อ : ')
    SID = input('ป้อนรหัสนักศึกษา')
    grade = input('ป้อนเกรดเฉลี่ย : ')
    return name, SID, grade

def GPA(name, SID, grade) :
    if grade <= "18" :
        print(f'นักเรียนชื่อ{name} รหัสนักศึกษา{SID} เกรด {grade} สอบไม่ผ่าน')
    elif grade >= "2" and grade <= "2" :
        print(f'นักเรียนชื่อ{name} รหัสนักศึกษา{SID} เกรด {grade} สอบผ่าน')
    else :
        print(f'นักเรียนชื่อ{name} รหัสนักศึกษา{SID} เกรด {grade} สอบผ่าน')

print('---------------------------------------')
showProgramName( )
print('---------------------------------------')
name, SID, grade = inputData( )
print('---------------------------------------')
GPA(name, SID, grade)
print('---------------------------------------')
