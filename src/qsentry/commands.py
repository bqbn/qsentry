import json
import jmespath
import logging
import random

from .api import SentryApi

logger = logging.getLogger(__name__)


def multiselect_hash_string(attributes):
    """Construct and return a jmespath multiselect hash."""
    return "{" + ", ".join([f"{attr}: {attr}" for attr in attributes]) + "}"


class Command:
    def __init__(self, **kwargs):
        self.host_url = kwargs.get("host_url")
        self.org_slug = kwargs.get("org")
        self.auth_token = kwargs.get("auth_token")
        self.print_count = kwargs.get("count")
        self.count = 0

    def call_api_and_print_attrs(self, api, jmes_filter, *args, **kwargs):
        sentry = SentryApi(self.host_url, self.org_slug, self.auth_token)
        for page in getattr(sentry, api)(*args, **kwargs):
            for item in jmespath.search(jmes_filter, page):
                print(", ".join([str(val) for val in item.values()]))
                self.count += 1
        if self.print_count:
            print(f"Count: {self.count}")

    def call_api_and_print_one(self, api, *args, **kwargs):
        sentry = SentryApi(self.host_url, self.org_slug, self.auth_token)
        for page in getattr(sentry, api)(*args, **kwargs):
            print(json.dumps(random.choice(page), indent=4))
            return None

    def search_by(self, search_by_term, *args, **kwargs):
        sentry = SentryApi(self.host_url, self.org_slug, self.auth_token)
        search_key, search_val = search_by_term.split("=")

        items = []
        for page in getattr(sentry, self.search_by_api)(*args, **kwargs):
            for item in page:
                value = item.get(search_key)
                if type(value) == bool:
                    if bool(search_val) == value:
                        items.append(item)
                else:
                    if search_val == value:
                        items.append(item)

        print(json.dumps(items, indent=4))


class MembersCommand(Command):
    def __init__(self, **kwargs):
        self.search_by_api = "org_members_api"
        super().__init__(**kwargs)

    def list_command(self, **kwargs):
        if kwargs["team"]:
            self.handle_the_team_option(kwargs["team"], kwargs["role"])
        else:
            if kwargs.get("attrs"):
                self.handle_the_list_all_option(attrs=kwargs["attrs"])
            else:
                self.handle_the_list_all_option(attrs=["id", "email"])

    def handle_the_list_all_option(self, attrs):
        self.call_api_and_print_attrs(
            "org_members_api", f"[].{ multiselect_hash_string(attrs) }"
        )

    def handle_the_list_one_option(self, **kwargs):
        self.call_api_and_print_one("org_members_api")

    def handle_the_team_option(self, team_slug, role):
        self.call_api_and_print_attrs(
            "team_members_api",
            f"[?role == '{role}' && flags.\"sso:linked\"].{ multiselect_hash_string(['id', 'name', 'email']) }",
            team_slug,
        )


class TeamsCommand(Command):
    def __init__(self, **kwargs):
        self.search_by_api = "org_teams_api"
        super().__init__(**kwargs)

    def list_command(self, attrs):
        self.call_api_and_print_attrs(
            "org_teams_api", f"[].{ multiselect_hash_string(attrs) }"
        )

    def list_projects(self, team_slug, attrs):
        self.call_api_and_print_attrs(
            "team_projects_api", f"[].{ multiselect_hash_string(attrs) }", team_slug
        )

    def handle_the_list_one_option(self, **kwargs):
        self.call_api_and_print_one("org_teams_api")

    def handle_list_one_project(self, team_slug):
        self.call_api_and_print_one("team_projects_api", team_slug)


class ProjectsCommand(Command):
    def __init__(self, **kwargs):
        self.search_by_api = "org_projects_api"
        super().__init__(**kwargs)

    def list_projects(self, attrs):
        self.call_api_and_print_attrs(
            "org_projects_api", f"[].{ multiselect_hash_string(attrs) }"
        )

    def list_one_project(self):
        self.call_api_and_print_one("org_projects_api")

    def list_keys(self, project_slug, attrs):
        self.call_api_and_print_attrs(
            "project_keys_api", f"[].{ multiselect_hash_string(attrs) }", project_slug
        )

    def handle_list_one_key(self, project_slug):
        self.call_api_and_print_one("project_keys_api", project_slug)

    def update_key(self, project_slug, key_id, data):
        if SentryApi(
            self.host_url, self.org_slug, self.auth_token
        ).update_project_client_key(project_slug, key_id, data):
            print(f"Key {key_id} successfully updated.")


class UsersCommand(Command):
    def __init__(self, **kwargs):
        self.search_by_api = "org_users_api"
        super().__init__(**kwargs)

    def list_users(self, attrs):
        self.call_api_and_print_attrs(
            "org_users_api", f"[].{ multiselect_hash_string(attrs) }"
        )
        logger.warn(
            "Warning: This command may not list all users because the org_users "
            "api does not paginate. Use the get members command instead for full "
            "list of members."
        )

    def list_one_user(self):
        self.call_api_and_print_one("org_users_api")
