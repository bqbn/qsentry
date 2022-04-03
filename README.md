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
  members   Member related commands
  orgs      Organization related commands
  projects  Project related commands
  teams     Team related commands
```

Member commands

```
$ qsentry members --help
Usage: qsentry members [OPTIONS] COMMAND [ARGS]...

  Member related commands

Options:
  --help  Show this message and exit.

Commands:
  list       List members
  search-by  Search a member by a term.
```
