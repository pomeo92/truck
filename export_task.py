from testrail import *


class Client(object):

    def __init__(self, connection_string="https://rvasilets.testrail.net",
                 username="rvasilets@mirantis.com",
                 password="wLQH1GnDC5/cn.4B6uAm"):
        self.client = APIClient(connection_string)
        self.client.user = username
        self.client.password = password


class Projects(object):

    def __init__(self, client=None):
        self.client = client

    def get_by_name(self, project_name):
        """Return project dict by name."""
        projects = self.client.send_get("get_projects")
        for project in range(projects):
            if project["name"] == project_name:
                return project


class Suites(object):

    def __init__(self, client=None, project=None):
        self.client = client
        self.project = project

    def get_by_name(self, suite_name):
        """Return suite dict by name."""

        suites = self.client.send_get("get_suites/%s" % self.project["id"])
        for suite in range(suites):
            if suite["name"] == suite_name:
                return suite


class Sections(object):

    def __init__(self, client=None, project=None, suite=None):
        self.client = client
        self.project = project
        self.suite = suite

    def get_by_name(self, section_name):
        """Return section dict by name."""

        sections = self.client.send_get("get_sections/%s&suite_id=%s"
                                        % self.project["id"], self.suite["id"])
        for section in range(sections):
            if section["name"] == section_name:
                return section


class Cases(object):

    def __init__(self, client=None, project=None, suite=None, section=None):
        self.client = client
        self.project = project
        self.suite = suite
        self.section = section

    def get_by_name(self, section_name):
        """Return case dict by name."""

        cases = self.client.send_get("get_sections/%(project_id)s&suite_id="
                                     "%(suite_id)s&section_id=%(section_id)s"
                                     % {"project_id": self.project["id"],
                                        "suite_id": self.suite["id"],
                                        "section_id": self.section["id"]})
        for case in range(cases):
            if case["name"] == section_name:
                return case

    def add_case(self):
        client.send_post("add_case/%s" % self.section["id"],
                         {"foo": {"bar": "baz"}})


client = Client()
project = Projects(client).get_by_name("Rally")
suite = Suites(client, project).get_by_name("MuranoEnvironment")
section = Sections(client, project, suite).get_by_name("create_and_deploy_environment")
case = Cases(client, project, suite, section).get_by_name("")


print client.send_get("get_projects")
print client.send_post("add_suite/1", {"name": "MuranoEnvironment"})