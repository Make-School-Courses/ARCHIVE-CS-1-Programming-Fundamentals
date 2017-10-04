import student
import pytest

def test_student_creation():
    student = Student("Sky")
    assert student

def setup_for_test():
    student = Student("Sky")
    student.add_assignment("Quiz 1": 80)
    student.add_assignment("HW3": 100)
    return student


def test_delete_assignment():
    student = setup_for_test()
