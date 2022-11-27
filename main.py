"""import libraries"""

from typing import Dict, List, TYPE_CHECKING, Any
from datetime import datetime
from dataclasses import dataclass
from random import randint
from collections import defaultdict
from abc import ABC
from abc import abstractclassmethod
from abc import ABCMeta, abstractmethod


@dataclass
class PersonalInfo:
    """
    Attributes:
    _id (int): Developers ID, is incremented for each instance.
    first_name (str): First name
    second_name (str): Second name
    address (str): address
    phone_number (str): Phone number
    email (str): Email
    position (int): Position
    rank (str): Rank
    salary (float): Salary
    """

    def __init__(self, _id: int, first_name: str, second_name: str, address: str, phone_number: str,
                 email: str, position: int, rank: str, salary: float):
        self.main_id = _id
        self.first_name = first_name
        self.second_name = second_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.rank = rank
        self.salary = salary

    """Getter"""

    @property
    def full_name(self):
        return self.first_name + " " + self.second_name

    """Setter"""

    @full_name.setter
    def full_name(self, fullname):
        try:
            buffer_full_name = fullname.split(" ")
            self.first_name = buffer_full_name[0]
            self.second_name = buffer_full_name[1]
        except NameError:
            print("Most likely, the data was entered incorrectly.\n It should look like this:")
            print("first_name + " " + second_name")


@dataclass
class Employee:
    """
    Attributes:
    personal_info (PersonalInfo): Personal info
    """
    def __init__(self, personal_info: PersonalInfo = None, projects=None):
        """
        :param personal_info:  Personal info
        :param projects:       Project
        """
        self.personal_info = personal_info
        if projects is None:
            projects = []
        self.projects: [Project] = projects

    # There are two methods which should be abstract

    def calculate_salary(self) -> None:  # Use isinstance
        if isinstance(self.personal_info.salary, (int, float)):
            print(f"Monthly salary =  {self.personal_info.salary}$")
            print(f"Annual salary =  {self.personal_info.salary * 12}$")
            print(f"Annual salary with bonus 10% =  {self.personal_info.salary * 12 * 1.1}$")
        else:
            print("An error occurred.")
            print("Most likely, the Salary variable is not an INT or a FLOAT.")

    def ask_sick_leave(self, project_manager) -> bool:  # project_manager: ProjectManager
        random_int = randint(0, 10)
        if random_int == 5:
            return True
        else:
            return False


class Project(metaclass=ABCMeta):
    """
    Attributes:
        task_list (list[int]) Task list
    """

    def __init__(self, task_list: list[int], title="Title"):
        """
        :param task_list: Task list
        :param title:     Project title
        """
        self.title = title
        self.task_list = task_list

    @abstractmethod
    def add_employee(self, emp: Employee):
        """
        Adds employee to project
        """
        pass

    @abstractmethod
    def remove_employee(self, emp: Employee):
        """
        Removes employee to project
        """
        pass

    def get_specific_employees(self, employee_type) -> List[Employee]:
        pass

class Mobile(Project):
    """Mobile project subtype"""
    def __init__(self, _id, title="Title", start_date=None, task_list=None, team=None, limit=-1, is_crossplatform: bool = True):
        """
        :param _id:         Mobile project id
        :param title:       Mobile project title
        :param start_date:  Start_date
        :param task_list:   Task_list
        :param team:        Team
        :param limit:       Limit
        :param open_source: Open_source
        """
        super().__init__()
        self.main_id = _id
        self.title = title
        self.start_date = start_date
        self.task_list = task_list
        self.limit = limit
        self.team = team
        self.is_crossplatform = is_crossplatform

    def add_employee(self, emp: Employee):
        mgn = AssignManagement()
        mgn.assign(self.main_id, self.title)

    def remove_employee(self, emp: Employee):
        mgn = AssignManagement()
        mgn.unassign(self.main_id, self.title)

class Web(Project):
    """Web project subtype"""
    def __init__(self, _id, title="Title", start_date=None, task_list=None, team=None, limit=-1, domain="/", host_provider="host name"):
        """
        :param _id:         Web project id
        :param title:       Web project title
        :param start_date:  Start_date
        :param task_list:   Task_list
        :param team:        Team
        :param limit:       Limit
        :param open_source: Open_source
        """
        super().__init__()
        self.main_id = _id
        self.title = title
        self.start_date = start_date
        self.task_list = task_list
        self.team = team
        self.limit = limit
        self.domain = domain
        self.host_provider = host_provider

    def add_employee(self, emp: Employee):
        mgn = AssignManagement()
        mgn.assign(self.main_id, self.title)

    def remove_employee(self, emp: Employee):
        mgn = AssignManagement()
        mgn.unassign(self.main_id, self.title)



class ProjectManager(Employee):
    """
    Attributes:
    employee_requests (Any): Employee requests
    """

    def __init__(self, employee_requests: Any):
        super().__init__()
        self.employee_requests = employee_requests

    def calculate_salary(self) -> None:
        if isinstance(self.personal_info.salary, (int, float)):
            print(f"Monthly salary =  {self.personal_info.salary}$")
            print(f"Annual salary =  {self.personal_info.salary * 12}$")
            print(f"Annual salary with bonus 10% =  {self.personal_info.salary * 12 * 1.1}$")
        else:
            print("An error occurred.")
            print("Most likely, the Salary variable is not an INT or a FLOAT.")

    def discuss_progress(self, engineer: Employee) -> None:  # we will fill this method then, leave it blank.
        pass

class Embedded(Project):
    """Embedded project subtype"""
    def __init__(self, _id, title="Title", start_date=None, task_list=None, team=None, limit=-1, open_source: bool = True):
        """
        :param _id:         Embedded project id
        :param title:       Embedded project title
        :param start_date:  Start_date
        :param task_list:   Task_list
        :param team:        Team
        :param limit:       Limit
        :param open_source: Open_source
        """
        super().__init__()
        self.main_id = _id
        self.title = title
        self.start_date = start_date
        self.task_list = task_list
        self.limit = limit
        self.team = team
        self.open_source = open_source

    def add_employee(self, emp: Employee):
        mgn = AssignManagement()
        mgn.assign(self.main_id, self.title)

    def remove_employee(self, emp: Employee):
        mgn = AssignManagement()
        mgn.unassign(self.main_id, self.title)




class Developer(Employee):

    def calculate_salary(self) -> None:  # Use isinstance
        if isinstance(self.personal_info.salary, (int, float)):
            print(f"Monthly salary =  {self.personal_info.salary}$")
            print(f"Annual salary =  {self.personal_info.salary * 12}$")
            print(f"Annual salary with bonus 10% =  {self.personal_info.salary * 12 * 1.1}$")
        else:
            print("An error occurred.")
            print("Most likely, the Salary variable is not an INT or a FLOAT.")

    def ask_sick_leave(self, project_manager) -> bool:  # project_manager: ProjectManager
        random_int = randint(0, 10)
        if random_int == 5:
            return True
        else:
            return False


class AssignManagement:
    """
    Attributes:
    employee (Employee): Employee
    project (Project): Project
    """

    def __init__(self) -> None:
        self.project_employee = defaultdict(list)
        self.employee_project = defaultdict(list)

    def assign(self, employee_id, project_title) -> None:
        self.project_employee[employee_id].append(project_title)
        self.employee_project[project_title].append(employee_id)

    def unassign(self, employee_id, project_title) -> None:
        if project_title in self.project_employee and employee_id in self.employee_project:
            self.project_employee[employee_id].remove(project_title)
            self.employee_project[project_title].remove(employee_id)
        else:
            print("It is not possible to retrieve a connection that does not exist!")

class Assignment:
    """
    Attributes:
    received_tasks (dict[Task]): Received tasks
    """

    def __init__(self, received_tasks: dict[Task]):
        self.received_tasks = received_tasks

    @staticmethod
    def get_tasks_to_date(self, date: datetime) -> List:  # Returns all tasks before date in arguments.
        """
        Arguments:
            date: datatime
        """
        return [value for key, value in dict.items() if key <= date]

class Task:
    """
    Attributes:
    _id (int): Developers ID, is incremented for each instance.
    title (str): Task name
    deadline (datetime): Deadline date
    items (List[str]): Items
    status (Any): # is_done or in_progress
    related_project (str): # project title
    """

    def __init__(self, _id: int, title: str, deadline: datetime, items: List[str], status: List[str],
                 related_project: str):
        self.main_id = _id
        self.title = title
        self.deadline = deadline
        self.items = items
        self.status = status
        self.related_project = related_project

    def implement_item(self, item_name: str) -> str:
        self.items.append(item_name)
        return f"Added part with title {item_name}"

    def add_comment(self, comment: str) -> None:
        self.status = comment





class QualityAssurance(Employee):

    def calculate_salary(self) -> None:  # Use isinstance
        if isinstance(self.personal_info.salary, (int, float)):
            print(f"Monthly salary =  {self.personal_info.salary}$")
            print(f"Annual salary =  {self.personal_info.salary * 12}$")
            print(f"Annual salary with bonus 10% =  {self.personal_info.salary * 12 * 1.1}$")
        else:
            print("An error occurred.")
            print("Most likely, the Salary variable is not an INT or a FLOAT.")

    def ask_sick_leave(self, project_manager) -> bool:  # project_manager: ProjectManager
        random_int = randint(0, 10)
        if random_int == 5:
            return True
        else:
            return False

    def add_ticket(self) -> None:  # we will fill this method then, leave it blank.
        pass


@dataclass
class Team:
    def __init__(self, main_id: int, title: str, member_list: list[str], project_id: int):
        """
        :param main_id:     Team id
        :param title:       Team title
        :param member_list: Member_list
        :param project_id:  Project_id
        """
        self.main_id = main_id
        self.title = title
        self.member_list = member_list
        self.project_id = project_id


class SoftwareArchitect(Employee, metaclass=ABCMeta):

    def fill_project(self, team: Team, project: Project):
        """
        :param team:    Team
        :param project: Project
        :return:
        """
        try:
            if project not in self.projects:
                raise ValueError(f"Architect has no access to '{project.title}'!")
            map(lambda emp: emp.projects.append(project), project.team.member_list)
            project.team = team
        except ValueError as e:
            raise ValueError(f"Filling project failed! {e}")

    @abstractmethod
    def create_project(self):
        pass


class WebArchitect(SoftwareArchitect):

    def create_project(self, *args, **kwargs):
        project = Web(*args, **kwargs)
        self.projects.append(project)
        return project


class MobileArchitect(SoftwareArchitect):

    def create_project(self, *args, **kwargs):
        project = Mobile(*args, **kwargs)
        self.projects.append(project)
        return project


class EmbeddedArchitect(SoftwareArchitect):

    def create_project(self, *args, **kwargs):
        project = Embedded(*args, **kwargs)
        self.projects.append(project)
        return project



person_01 = PersonalInfo(0, "Alina", "Myron", "Lviv", "+380-96-453-13-32", "myronvika@gmail.com", 3, "Junior", 3600)
print(person_01.first_name)
person_01.full_name = "Ivan Muzychuk"
print(person_01.full_name)
person_01_employee = Employee(person_01)
person_01_employee.calculate_salary()
print(person_01_employee.ask_sick_leave(person_01))
task_01 = Task(1, "Task_01", (2034, 1, 12), ["Item_01", "Item_02", "Item_03", "Item_04"], ["is_done"], "Project_01")
managment = AssignManagement()
managment.assign(person_01.main_id, task_01.related_project)
