import student
import pytest

def setup_for_test():
    student = Student("Student McStudentFace")
    return student

def test_setup():
    student = setup_for_test()
    assert student.name == "Student McStudentFace"
    assert student.grade_in_class == None
    assert len(student.assignments) == 0

def test_give_student_assignment():
    '''test adding a new assignment to a student '''
    student = setup_for_test()
    student.add_assignment('HW1', 100)
    assert student.assignments['HW1'] == 100
    student.add_assignment('Test1', )

def test_get_grade_on_assignment():
    '''test retreiving student grade on assignment '''
    student = setup_for_test()

def test_delete_assignment():
    student = setup_for_test()

def test_update_grade_for_assignment():
    '''test updating a grade for a student's assignment '''
    student = setup_for_test()

def test_get_GPA():
    '''tests getting student's average in the class '''
    student = setup_for_test()

def test__update_grade_in_class():
    '''tests helper method _update_grade_in_class().  Any time an assignment and grade are added to a dictionary,
    this method is called.  It recalculates the student's GPA for the class and then updates the value of self.grade_in_class '''
    student = setup_for_test()
