import student
import pytest

def test_student_creation():
    student = Student("Sky")
    assert student

def setup_for_test():
    student = Student("Sky")
    return student

def test_give_student_assignment():
    '''test adding a new assignment to a student '''
    student = setup_for_test()

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
