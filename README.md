# Qsentry

Qsentry is a command line wrapper for Sentry's API.

## Some Command Examples

Top level commands

```
$ qsentry --help
Usage: qsentry [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  get     Display resources such as members, teams, organizations and etc.
  update  Update a resource such as a client key
```

Get command

```
$ qsentry members --help
Usage: qsentry get [OPTIONS] COMMAND [ARGS]...

  Display resources such as members, teams, organizations and etc.

Options:
  --help  Show this message and exit.

Commands:
  client-keys  Get all client keys of the given project.
  members      Get the members
  projects     Get the projects
  teams        Get the teams
  users        Get all users of the given organization.
```
