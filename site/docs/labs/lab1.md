# Лабораторная работа №1

*Развертывание статического сайта на MkDocs с публикацией на GitHub Pages*
## Цель работы

- Освоить процесс создания статического сайта с использованием генератора документации **MkDocs**.
- Научиться организовывать структуру документации проекта (портфолио лабораторных работ).
- Изучить базовые принципы работы с системой контроля версий **Git** и платформой **GitHub**.
- Развернуть статический сайт с использованием механизма **GitHub Pages** на домене вида `username.github.io`.
- Освоить базовую настройку темы оформления и конфигурационного файла `mkdocs.yml`.

---
## Теоретическая часть
### Статические сайты
**Статический сайт** - это набор HTML, CSS и JS-файлов, которые генерируются заранее и размещаются на сервере без серверной логики.
**Преимущества:**
- простота размещения;
- высокая скорость загрузки;
- отсутствие серверной части;
- удобство версионирования.
### MkDocs
**MkDocs** - генератор статических сайтов, ориентированный на документацию проектов и портфолио.
**Основные возможности:**
- генерация сайта из Markdown-файлов;
- гибкая настройка структуры через `mkdocs.yml`;
- поддержка тем оформления;
- локальный сервер для предпросмотра (`mkdocs serve`).
**Документация:**
- [https://www.mkdocs.org/](https://www.mkdocs.org/)
- [https://www.mkdocs.org/user-guide/configuration/](https://www.mkdocs.org/user-guide/configuration/)
- [https://www.mkdocs.org/user-guide/writing-your-docs/](https://www.mkdocs.org/user-guide/writing-your-docs/)
### Git и GitHub
**Git** - распределённая система контроля версий.  
**GitHub** - облачная платформа для хранения Git-репозиториев и совместной работы.
**Документация:**
- [https://git-scm.com/docs](https://git-scm.com/docs)
- [https://docs.github.com/](https://docs.github.com/)
### GitHub Pages
**GitHub Pages** позволяет публиковать статические сайты напрямую из репозитория. В данной лабораторной работе используется публикация из каталога `/docs` ветки `main`.
**Документация:** 
- [https://docs.github.com/en/pages](https://docs.github.com/en/pages)

---
## Ход выполнения работы
### Этапы:
1. Создала файлы index, about, projects, lab1, lab2, lab3 в формате md
2. Зашла на GitHub и создала новый публичный репозиторий с названием `Anne4ka-rom.github.io`
3. Скопировала ссылку для локальной работы с репозиторием: `https://github.com/Anne4ka-rom/Anne4ka-rom.github.io`
```bash
git clone https://github.com/Anne4ka-rom/Anne4ka-rom.github.io.git
cd Anne4ka-rom.github.io
```
4. Создала виртуальную оболочку
```bash
python -m venv venv
source venv/Scripts/activate
```
5. Создала .gitignore
```bash
explorer .
touch .gitignore
```
6. Установила mkdocs
```bash
pip install mkdocs
```
7. Создала новый сайт
```bash
mkdocs new site
cd site
```
8. Сделала в mkdocs.yml nav и прописала тему
``` yml
site_name: Портфолио Романовой Анны
site_description: Портфолио Python-разработчика, содержащее мой опыт, проекты и контакты
site_author: Анна Романова
repo_url: https://github.com/Anne4ka-rom/Anne4ka-rom.github.io

theme:
  name: material
  language: ru
  features:
    - navigation.tabs
    - navigation.sections
    - toc.integrate
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/toggle-switch-off-outline
        name: Переключить на тёмную тему
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/toggle-switch
        name: Переключить на светлую тему

nav:
  - Главная: index.md
  - Об авторе: about.md
  - Лабораторные работы:
    - Лабораторная работа №1: labs/lab1.md
    - Лабораторная работа №2: labs/lab2.md

markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences
  - admonition
  - footnotes
  - toc:
      permalink: true
```
9. Установка темы
```bash
pip install mkdocs-material
```
10. Протестировала сервер локально
```bash
mkdocs serve
```
11. Собрала структуру сайта с помощью build
```bash
mkdocs build --site-dir ../docs
cd ..
```
12. Добавила файлы
```bash
git add .
```
13. Сделала коммиты
```bash
git commit -m "Название комита"
```
14. Отправила на сервер
```bash
git push
```

---
## Результат
### Список осознанных коммитов:
``` bush
- "Add name, topic, nav in mkdocs.yml" - добавление названия, темы, навигации и т.д. в mkdocs.yml
  
- "Add venv, site/, *pyc, __pycache__ in .gitignore" - добавление виртуальной оболочки, папки с сайтом, скомпилированного кода и байт кода в гитигнор
  
- "Add file lab1 about static site with mkdocs in dir docs" - создание файла с лабораторной работой №1 и добавление её в статический сайт
  
- "Delete site/ in .gitignore" - удаление папки сайта из гитигнора
  
- "Update structure: create dir labs with 3 labs" - создала отдельно папку с лабами для всех лаб и обновила структуру проекта
  
- "Update file projects: add current project" - добавила проект статического сайта в текущие
```
### Ссылки:
- **Ссылка на репозиторий:** [https://github.com/Anne4ka-rom/Anne4ka-rom.github.io](https://github.com/Anne4ka-rom/Anne4ka-rom.github.io)
- **Ссылка на опубликованный сайт:** [https://anne4ka-rom.github.io](https://anne4ka-rom.github.io)
Сайт доступен, все страницы открываются, навигация работает.

---
## Вывод

В ходе выполнения лабораторной работы я освоила процесс создания статического сайта с помощью генератора MkDocs: настроила виртуальное окружение, установила необходимые зависимости, создала структуру страниц (главная, об авторе, проекты и лабораторные работы) и подключила тему Material с поддержкой светлой и тёмной тем. С помощью Git я инициализировала репозиторий, выполнила коммиты и опубликовала проект на GitHub, после чего настроила GitHub Pages для автоматической публикации сайта из папки `/docs`. В результате сайт-портфолио стал доступен по адресу `https://anne4ka-rom.github.io`, а полученные навыки позволят мне в дальнейшем легко добавлять новые лабораторные работы на сайт в течение семестра.

---
[Вернуться на главную](/index)