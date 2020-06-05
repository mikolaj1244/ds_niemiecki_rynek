# Data Science na rynku niemieckim
* Dlaczego nie polski rynek? - Takie było moje pierwsze założenie, jednak stwierdziłem, że rynek polski ma mało ofert pracy. Dlatego postawiłem na rynek niemiecki (szczególny nacisk na firmy które wymagają języka angielskiego).
* Zescrapowałem 500 ogłoszeń pracy z portalu glassdoorprzy pomocy pythona i selenium.
* Sprawdziłem jakich umiejetności oczekują pracodawcy.
* Sprawdziłem czy niemcy są otwarci na osoby posługujące się językiem angielskim.


## Użyte materiały
* **Python Wersja**: 3.7
* **Paczki**: pandas, numpy, seaborn, selenium
* **Scraper Github**: https://github.com/arapfaik/scraping-glassdoor-selenium
* **Scraper Artykuł**: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
* **Czyszczenie i obróbka danych**: https://github.com/PlayingNumbers/ds_salary_proj
* **Upiększenie README**: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet


## Web Scraping
Ustawiłem web screpera na 500 ogłoszeń z portalu [glassdoor.com](https://www.glassdoor.com). Z każdego ogłoszenia otrzymalismy:
* Job title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors
Jest to portal polularny w ameryce dlatego niektóre z powyższych wartości były puste.


## Czyszczenie danych
Wiekszość danych nadawała się do użytku. Dodałem kilka kolumn aby zaprezętować dane w lepszy sposób.

## Obróbka danych
Całość można zaleść w pliku obrobka_danych.ipynb. Tutaj zaprezentuje kilka przykładowych wykresów.

![alt text](https://github.com/mikolaj1244/ds_niemiecki_rynek/blob/master/angielski.png "Czy firma przyjmuje osoby mówiące po angielsku")
![alt text](https://github.com/mikolaj1244/ds_niemiecki_rynek/blob/master/python.png "Zapotrzebowanie na osoby posługujące się pythonem")

![alt text](https://github.com/mikolaj1244/ds_niemiecki_rynek/blob/master/localisation.png "Miasta, w których jest najwięcej ofert")
![alt text](https://github.com/mikolaj1244/ds_niemiecki_rynek/blob/master/wielkosc_firm.png "Wielkość firm")

## Wartość biznesowa
Projektu tego nie można wykożystac w biznesie, jednak pokazuje on obszary w których data scientist powinien się rozwijać. Jedną z jego zalet jest ukazanie, że pracy w obszarze data science można szukać nie tylko w Polsce ale też za granicą.
