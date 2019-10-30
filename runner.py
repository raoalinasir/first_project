class Runner:
    # Creating some global variables
    __PROJECT_NAME__ = None

    def __init__(self):
        """
        Init function for runner class
        """

        self.__PROJECT_NAME__ = 'My first project git'

    def check_project_name(self):
        """
        Simple function to check what value is set in global class variable for project name
        :return:
        """
        print(self.__PROJECT_NAME__)
