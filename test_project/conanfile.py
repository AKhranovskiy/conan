from conans import ConanFile


def hello_from_conanfile(name):
    return "Hello, {}".format(name)

class TestProjectConan(ConanFile):
    name = "test_project"
    version = "1.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Testproject here>"
