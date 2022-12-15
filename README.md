# OhtuTube

University of Helsinki Software Engineering mini-project Autumn 2022

![workflow badge](https://github.com/smannist/ohtuvarasto/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/JanneKarki/OhtuTube/branch/main/graph/badge.svg?token=926J1FN1OR)](https://codecov.io/gh/JanneKarki/OhtuTube)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Project [Backlog](https://docs.google.com/spreadsheets/d/10WoYOFuoc0nGcKmTAKLrLbm1TYcGsJvkDpc3olPwmWM/edit?usp=sharing)

## Releases

[Release 1.0 - Sprint 1](https://github.com/JanneKarki/OhtuTube/releases/tag/Sprint1)

[Release 1.1 - Sprint 2](https://github.com/JanneKarki/OhtuTube/releases/tag/Sprint2)

[Release 1.2 - Sprint 3](https://github.com/JanneKarki/OhtuTube/releases/tag/Sprint3)

## Definition of Done

- Functionality is integrated to the rest of the software
- User story's acceptance criterias are tested by Robot framework
- Code is tested with automated tests
- Test Coverage is over 80% (UI excluded)
- CI-enviroment tests are passed
- Coding style follows best-pracites confirmed by pylint, score over 9

## Installation

The application uses Poetry for dependency management, so it must be installed before running the application.

1. Install required dependencies with the command:

```bash
poetry install

```

2. Initialize the application with the command:

```bash
poetry run invoke build
```

3. And finally run the application with the command:

```bash
poetry run invoke start
```

## Testing

Unit tests can be performed with the command:

```bash
poetry run invoke test
```

End-to-end tests can be performed with the command:

```bash
poetry run invoke robot
```

## Test coverage

Test coverage report can be generated with the command:

```bash
poetry run invoke coverage-report
```

## Importing and exporting references in bibtex form

Default path for importing and exporting bibtex file:

```bash
src/bibtex_data/references.bib

```
Configuration for filename and path can be found in:

```bash
src/bibtex_config.py

```
