from conans import ConanFile


class TestprojectTestConan(ConanFile):
    def test(self):
        self_pr = self.python_requires.get("self")
        assert(self_pr)
        self.output.warn("{}\n".format(self_pr.hello_from_conanfile("dave")))
