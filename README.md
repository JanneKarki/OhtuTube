# OhtuTube
HY Ohjelmistotuotantokurssin miniprojekti Syksy -22



### Project [Backlog](https://docs.google.com/spreadsheets/d/10WoYOFuoc0nGcKmTAKLrLbm1TYcGsJvkDpc3olPwmWM/edit?usp=sharing)




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
