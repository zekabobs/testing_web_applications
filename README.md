[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Prompt&duration=3000&pause=150&color=DC189DFF&width=435&lines=Selenium+%2B+PyTest;Example+of+testing+a+web+application)](https://git.io/typing-svg)
____________
<a href="https://www.python.org/"><img src="https://img.shields.io/static/v1?label=python&message=3.10.0&color=blue&link=https://selenium.com" /></a>
<a href="https://github.com/SergeyPirogov/webdriver_manager"><img src="https://img.shields.io/static/v1?label=webdriver--manager&message=3.8.4&color=blue&link=https://selenium.com" /></a>
<a href="https://github.com/SeleniumHQ/selenium"><img src="https://img.shields.io/static/v1?label=selenium&message=4.5.0&color=blue&link=https://selenium.com" /></a>
<a href="https://github.com/pytest-dev/pytest"><img src="https://img.shields.io/static/v1?label=pytest&message=7.2.0&color=blue&link=https://selenium.com" /></a>
### Пример команд:
  pytest -s -m "need_review" # default language=en; browser=firefox
  <br>
  pytest -s --language=ru -m "need_review"
  <br>
  pytest -s --browser=chrome -m "need_review"
  <br>
  pytest -s --language=ru --browser=chrome -m "need_review"
### Поддерживаемые браузеры:
  1. Edge (--browser=edge);
  2. Firefox (--browser=firefox);
  3. Chrome (--browser=chrome).
### Разновидность языков (около 20):
1. Русский (--language=ru);
2. English (--language=en);
3. Український (--language=uk);
4. Français (--language=fr);
5. Italiano (--language=it);
6. Deutsch (--language=de);
###### Полный перечень в файле 'conftest.py'
### Маркеры:
  1. need_review - Маркер кода для тестирования работы на странице с продуктом;
  2. main_page - Маркер кода для тестирования работы на главной странице;
  3. user_test - Пример работы маркера для класса.
