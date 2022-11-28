# OhtuTube
HY Ohjelmistotuotantokurssin miniprojekti Syksy -22

![workflow badge](https://github.com/smannist/ohtuvarasto/workflows/CI/badge.svg)

### Project [Backlog](https://docs.google.com/spreadsheets/d/10WoYOFuoc0nGcKmTAKLrLbm1TYcGsJvkDpc3olPwmWM/edit?usp=sharing)

### [Test Coverage ](https://github.com/JanneKarki/OhtuTube/blob/main/documents/coverage_28_11.png)of version 1.0

## Releases
[Release 1.0 - Sprint 1](https://github.com/JanneKarki/OhtuTube/releases/tag/Sprint1)

## Definition of Done
- Functionality is integrated to the rest of the software
- User story's acceptance criterias are manually tested
- Code is tested with automated tests
- Test Coverage is over 80% (UI excluded)
- CI-enviroment tests are passed
- Coding style follows best-pracites confirmed by pylint, score over 9

## Asennus

Sovellus käyttää riippuvuuksien hallintaan poetrya, joten se tulee olla asennettuna koneelle.

1. Asenna sovelluksen tarvitsemat riippuvuudet komennolla:
```bash
poetry install
```
2. Suorita alustustoimet ennen sovelluksen käynnistämistä komennolla:
```bash
poetry run invoke build
```
3. Käynnistä sovellus komennoilla:

```bash
poetry run invoke start
```

## Testaus
Testaus voidaan suorittaa komennolla:

```bash
poetry run invoke test
```

## Testikattavuus
Testikattavuusraportin generointi tapahtuu komennolla:

```bash
poetry run invoke coverage-report
```


