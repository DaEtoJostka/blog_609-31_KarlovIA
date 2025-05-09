Okay, let's break down this Django lab work into a detailed step-by-step plan. This plan assumes you have a Django project set up with `accounts` and `articles` apps already created, along with basic templates and views.

**Цель:** Implement article creation functionality, including user authentication, form handling, database interaction, URL routing, template modifications, and handling potential issues like duplicate slugs. Finally, answer theoretical questions about Django and Python concepts used.

**Общая стратегия:** Follow the instructions sequentially, testing frequently. Take screenshots as requested for the report.

---

**Подробный План Выполнения Лабораторной Работы №9**

**Часть 1: Настройка URL и Базовых Шаблонов**

1.  **Шаг 1 (Инструкция 1.1): Настройка Пространств Имен URL (Namespacing)**
    *   **Действие:** Откройте файл `accounts/urls.py`. Добавьте строку `app_name = 'accounts'`. Сохраните.
    *   **Действие:** Откройте файл `articles/urls.py`. Добавьте строку `app_name = 'articles'`. Сохраните.
    *   **Цель:** Это позволяет использовать пространства имен (например, `'accounts:login'`) для уникальной идентификации URL-адресов, предотвращая конфликты имен между приложениями.

2.  **Шаг 2 (Инструкция 1.2): Использование Тега `{% url %}` в Шаблонах**
    *   **Действие:** Откройте файл `templates/accounts/login.html`. Найдите тег `<form>` и замените атрибут `action="/accounts/login/"` на `action="{% url 'accounts:login' %}"`. Сохраните.
    *   **Действие:** Откройте файл `templates/accounts/signup.html`. Найдите тег `<form>` и замените атрибут `action` (если он жестко прописан) на `action="{% url 'accounts:signup' %}"`. Сохраните.
    *   **Действие:** Откройте файл `templates/articles/article_list.html`. Найдите любые жестко прописанные URL-адреса, ведущие к статьям или страницам аккаунта, и замените их тегом `{% url %}` с соответствующим пространством имен (например, `{% url 'articles:list' %}`, `{% url 'articles:article_detail' article.slug %}`, `{% url 'accounts:login' %}`). Сохраните.
    *   **Действие:** Откройте файл `templates/base_layout.html` (или ваш базовый шаблон). В навигационной панели (если она там есть) замените все жестко прописанные URL-адреса на тег `{% url %}` (например, `{% url 'homepage' %}`, `{% url 'about' %}`, `{% url 'accounts:login' %}`, `{% url 'articles:list' %}`). Сохраните.
    *   **Цель:** Использование тега `{% url %}` делает URL-адреса динамическими. Если вы измените путь в `urls.py`, вам не придется менять его во всех шаблонах.

3.  **Шаг 3 (Инструкция 1.3): Перенос Навигации в Базовый Шаблон**
    *   **Действие:** Убедитесь, что вся навигационная панель (код `<nav>...</nav>`, показанный на скриншоте в инструкции 1.3) находится в файле `templates/base_layout.html`. Если она была в другом файле (например, `article_list.html`), переместите ее.
    *   **Действие:** Проверьте, что в `base_layout.html` используются теги `{% url %}` для всех ссылок в навигации, включая логику `{% if user.is_authenticated %}` для отображения "Logout" или "Login".
    *   **Цель:** Обеспечить единую навигацию на всех страницах сайта, наследующих базовый шаблон.
    *   **Тестирование:** Запустите сервер (`python manage.py runserver`) и проверьте несколько страниц (главную, список статей, вход), чтобы убедиться, что навигация отображается корректно.

**Часть 2: Создание Представления и Шаблона для Создания Статей**

4.  **Шаг 4 (Инструкция 1.4): Добавление URL для Создания Статьи**
    *   **Действие:** Откройте файл `articles/urls.py`. В списке `urlpatterns` добавьте новый путь: `path('create/', views.article_create, name='create'),`. Убедитесь, что запятая стоит после предыдущего элемента списка. Сохраните.
    *   **Цель:** Определить URL-адрес, по которому будет доступна страница создания новой статьи.

5.  **Шаг 5 (Инструкция 1.5): Создание Функции Представления `article_create`**
    *   **Действие:** Откройте файл `articles/views.py`.
    *   **Действие:** Импортируйте декоратор `login_required`: `from django.contrib.auth.decorators import login_required`.
    *   **Действие:** Импортируйте `render`: `from django.shortcuts import render` (если еще не импортирован).
    *   **Действие:** Создайте новую функцию `article_create`:
        ```python
        @login_required(login_url='/accounts/login/') # Или 'accounts:login' если настроены URL resolver
        def article_create(request):
            # Пока просто рендерим шаблон
            return render(request, 'articles/article_create.html')
        ```
    *   **Примечание:** В инструкции указано `login_url='accounts:login'`. Убедитесь, что ваши настройки Django позволяют разрешать такие URL на этом этапе, или используйте абсолютный путь `/accounts/login/` для надежности на данном шаге.
    *   **Цель:** Создать базовое представление, которое будет отображать форму создания статьи, требуя предварительной аутентификации пользователя.

6.  **Шаг 6 (Инструкция 1.6): Создание Шаблона `article_create.html`**
    *   **Действие:** В директории `templates/articles/` создайте новый файл `article_create.html`.
    *   **Действие:** Напишите базовый код шаблона, наследуя `base_layout.html`:
        ```html
        {% extends "base_layout.html" %}
        {% load static %} {# Если используете статику #}

        {% block title %}Create Article{% endblock title %}

        {% block content %}
          <h1>Create a New Article</h1>
          {# Сюда позже добавим форму #}
        {% endblock content %}
        ```
    *   **Цель:** Создать HTML-страницу для формы создания статьи.

7.  **Шаг 7 (Инструкция 1.7): Тестирование Доступа к `article/create/`**
    *   **Действие:** Убедитесь, что сервер разработки запущен.
    *   **Действие:** Выйдите из аккаунта (если были вошли).
    *   **Действие:** Перейдите в браузере по адресу ``. Вас должно перенаправить на страницу входа (`/accounts/login/`).
    *   **Действие:** **Сделайте скриншот** страницы входа, на которую вас перенаправило.
    *   **Действие:** Войдите в аккаунт.
    *   **Действие:** Снова перейдите по адресу `/articles/create/`. Теперь вы должны увидеть страницу с заголовком "Create a New Article" (или "Create article", как на скриншоте).
    *   **Действие:** **Сделайте скриншот** этой страницы (`article_create.html`).
    *   **Цель:** Проверить работу декоратора `@login_required` и доступность нового шаблона для авторизованных пользователей.

**Часть 3: Улучшение Редиректа и Добавление Формы**

8.  **Шаг 8 (Инструкция 1.8): Улучшение Редиректа после Логина**
    *   **Действие:** Откройте файл `accounts/views.py`.
    *   **Действие:** Импортируйте `redirect`: `from django.shortcuts import redirect` (если `HttpResponseRedirect` импортировался оттуда же, просто добавьте `redirect`). Замените импорт `HttpResponseRedirect` (если он был из `django.http`) на `redirect` из `django.shortcuts`.
    *   **Действие:** В функции `login_view` найдите блок `if form.is_valid():`. Внутри него измените логику редиректа, как показано на скриншоте:
        ```python
        if form.is_valid():
            user = form.get_user()
            login(request, user)
           /articles/create/ if 'next' in request.POST: # Проверяем POST, т.к. форма методом POST
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list') # Или 'homepage', если уже изменили
        ```
    *   **Цель:** Сделать так, чтобы после входа пользователь перенаправлялся на ту страницу, на которую он пытался зайти до логина (если такая информация передана в параметре `next`), а не всегда на список статей.

9.  **Шаг 9 (Инструкция 1.9): Добавление Скрытого Поля `next` в Шаблон Логина**
    *   **Действие:** Откройте файл `templates/accounts/login.html`.
    *   **Действие:** Внутри тега `<form>`, после `{{ form }}` и перед кнопкой `submit`, добавьте код для скрытого поля, как показано на скриншоте:
        ```html
        {% if request.GET.next %}
          <input type="hidden" name="next" value="{{ request.GET.next }}">
        {% endif %}
        ```
    *   **Цель:** Передать URL исходной страницы (на которую пытался зайти неавторизованный пользователь) в POST-запросе формы логина, чтобы представление `login_view` могло использовать его для редиректа.

10. **Шаг 10 (Инструкция 1.10): Тестирование Улучшенного Редиректа**
    *   **Действие:** Повторите действия из **Шага 7**: выйдите из системы, попробуйте зайти на `/articles/create/`. Вас перенаправит на `/accounts/login/?next=/articles/create/`.
    *   **Действие:** Войдите в аккаунт.
    *   **Действие:** Проверьте, что теперь вас перенаправило сразу на `/articles/create/`, а не на список статей.
    *   **Действие:** **Сделайте скриншот** страницы `/articles/create/` после этого редиректа.
    *   **Действие:** **Опишите изменения** в поведении по сравнению с Шагом 7 (т.е. раньше перенаправляло на список статей, теперь – на целевую страницу `/articles/create/`).
    *   **Цель:** Убедиться, что механизм `next` работает корректно.

11. **Шаг 11 (Инструкция 1.11): Добавление Ссылки "Create article"**
    *   **Действие:** Откройте файл `templates/articles/article_list.html`.
    *   **Действие:** Добавьте ссылку/кнопку "Create article" так, чтобы она отображалась *только* для аутентифицированных пользователей. Используйте тег `{% url 'articles:create' %}` для ссылки. Примерный код:
        ```html
        {% extends "base_layout.html" %}
        {# ... другие блоки ... #}
        {% block content %}
          <h1>Article List</h1>
          {% if user.is_authenticated %}
            <p><a href="{% url 'articles:create' %}" class="btn btn-primary">Create article</a></p> {# Используйте свои классы CSS #}
          {% endif %}
          {# ... цикл вывода статей ... #}
        {% endblock content %}
        ```
    *   **Цель:** Предоставить пользователям удобный способ перейти к созданию статьи со страницы списка статей.
    *   **Тестирование:** Зайдите на страницу списка статей (`/articles/` или главную, если она уже изменена) под логином и без. Убедитесь, что кнопка/ссылка видна только залогиненному пользователю.

12. **Шаг 12 (Инструкция 1.12): Создание Файла `forms.py`**
    *   **Действие:** В директории приложения `articles/` создайте новый файл `forms.py`.
    *   **Действие:** Напишите код для формы `CreateArticle`:
        ```python
        from django import forms
        from . import models # Импортируем модели из текущего приложения

        class CreateArticle(forms.ModelForm):
            class Meta:
                model = models.Article
                fields = ['title', 'slug', 'body', 'thumbnail']
        ```
    *   **Цель:** Создать Django-форму, которая автоматически генерируется на основе модели `Article`, для удобной обработки данных формы.

13. **Шаг 13 (Инструкция 1.13): Добавление Формы в Шаблон `article_create.html`**
    *   **Действие:** Откройте файл `templates/articles/article_create.html`.
    *   **Действие:** Измените содержимое блока `content`, чтобы включить форму:
        ```html
        {% block content %}
          <h1>Create a New Article</h1>
          <form class="form-article" action="{% url 'articles:create' %}" method="post" enctype="multipart/form-data"> {# Добавлен enctype для загрузки файлов #}
            {% csrf_token %}
            {{ form.as_p }} {# Или другой способ рендеринга формы #}
            <button type="submit">Create Article</button>
          </form>
        {% endblock content %}
        ```
    *   **Действие:** Откройте файл `articles/views.py`. Измените `article_create`, чтобы передавать экземпляр формы в контекст:
        ```python
        from . import forms # Импортировать формы

        @login_required(login_url='/accounts/login/')
        def article_create(request):
            form = forms.CreateArticle() # Создаем пустой экземпляр формы
            return render(request, 'articles/article_create.html', {'form': form}) # Передаем форму в шаблон
        ```
    *   **Цель:** Отобразить поля формы на странице создания статьи. `enctype="multipart/form-data"` необходим для загрузки файлов (thumbnail).
    *   **Тестирование:** Перейдите на `/articles/create/` (будучи залогиненным). Вы должны увидеть поля формы (Title, Slug, Body, Thumbnail).

**Часть 4: Модификация Модели и Обработка Данных Формы**

14. **Шаг 14 (Инструкция 1.14): Добавление Поля `author` в Модель `Article`**
    *   **Действие:** Откройте файл `articles/models.py`.
    *   **Действие:** Импортируйте модель `User`: `from django.contrib.auth.models import User`.
    *   **Действие:** В классе `Article` добавьте новое поле `author`:
        ```python
        author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
        ```
    *   **Цель:** Связать каждую статью с пользователем, который ее создал. `on_delete=models.CASCADE` означает, что при удалении пользователя удалятся и все его статьи.

15. **Шаг 15 (Инструкция 1.15): Удаление Старых Статей (если есть)**
    *   **Действие:** Войдите в админ-панель Django (`/admin/`).
    *   **Действие:** Перейдите в раздел Articles.
    *   **Действие:** Выделите все существующие статьи (если они были созданы до добавления поля `author` и не имеют автора, они могут вызвать проблемы).
    *   **Действие:** В выпадающем меню "Action" выберите "Delete selected articles" и нажмите "Go". Подтвердите удаление.
    *   **Цель:** Очистить базу данных от статей, которые не будут соответствовать новой структуре модели (отсутствие автора). *Примечание: это необходимо, т.к. мы добавили не-nullable ForeignKey без `null=True`.*

16. **Шаг 16 (Инструкция 1.16): Создание и Применение Миграций**
    *   **Действие:** В терминале выполните команду: `python manage.py makemigrations articles`
    *   **Действие:** Затем выполните команду: `python manage.py migrate`
    *   **Цель:** Обновить структуру таблицы `articles_article` в базе данных, добавив новое поле `author_id`.

17. **Шаг 17 (Инструкция 1.17): Реализация Логики Сохранения Статьи в `article_create`**
    *   **Действие:** Откройте файл `articles/views.py`.
    *   **Действие:** Импортируйте `redirect` (если еще не сделано): `from django.shortcuts import redirect`.
    *   **Действие:** Дополните функцию `article_create`, чтобы обрабатывать POST-запросы:
        ```python
        from . import forms

        @login_required(login_url='/accounts/login/')
        def article_create(request):
            if request.method == 'POST':
                form = forms.CreateArticle(request.POST, request.FILES) # Добавлен request.FILES
                if form.is_valid():
                    # Сохранить статью в БД, но пока не коммитить
                    instance = form.save(commit=False)
                    # Присвоить автора
                    instance.author = request.user
                    # Теперь сохранить в БД
                    instance.save()
                    return redirect('articles:list') # Редирект на список статей (или homepage)
            else: # Если GET-запрос
                form = forms.CreateArticle()
            return render(request, 'articles/article_create.html', {'form': form})
        ```
    *   **Цель:** Обработать данные, отправленные из формы, валидировать их, связать статью с текущим пользователем и сохранить в базе данных. `commit=False` позволяет изменить объект перед окончательным сохранением. `request.FILES` нужен для обработки загруженного изображения.

18. **Шаг 18 (Инструкция 1.18): Тестирование Создания Новых Статей**
    *   **Действие:** Перейдите на `/articles/create/`.
    *   **Действие:** Заполните форму (включая загрузку изображения, если поле `thumbnail` обязательно или вы хотите его проверить).
    *   **Действие:** Нажмите "Create Article".
    *   **Действие:** Вас должно перенаправить на список статей, и новая статья должна появиться в списке.
    *   **Действие:** Повторите процесс, создав 1-2 статьи.
    *   **Действие:** **Сделайте скриншот** страницы со списком статей, где видны созданные вами статьи.
    *   **Цель:** Убедиться, что весь процесс создания статьи работает корректно от начала до конца.

**Часть 5: Настройка Главной Страницы и Обработка Дубликатов Слагов**

19. **Шаг 19 (Инструкция 1.19): Назначение Списка Статей Главной Страницей**
    *   **Действие:** Откройте файл `mysite/urls.py` (основной файл URL проекта).
    *   **Действие:** Импортируйте представления `articles`: `from articles import views as article_views`.
    *   **Действие:** Найдите путь для главной страницы (`path('', ...)`). Измените его так, чтобы он использовал `article_views.article_list` и имел `name='homepage'`:
        ```python
        path('', article_views.article_list, name='homepage'),
        ```
    *   **Действие:** Убедитесь, что остальные пути (admin, about, articles/, accounts/) также присутствуют и настроены правильно, как на скриншоте.
    *   **Действие:** Убедитесь, что настроена раздача медиафайлов в режиме разработки (строка `urlpatterns += static(...)`), как показано на скриншоте. Импортируйте `static` и `settings`:
        ```python
        from django.conf import settings
        from django.conf.urls.static import static
        # ... urlpatterns = [...]
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    *   **Цель:** Сделать так, чтобы при заходе на корень сайта (`/`) отображался список статей.

20. **Шаг 20 (Инструкция 1.20): Замена `'articles:list'` на `'homepage'`**
    *   **Действие:** Пройдитесь по всем файлам проекта (представления `.py`, шаблоны `.html`), где вы использовали `{% url 'articles:list' %}` или `redirect('articles:list')`.
    *   **Действие:** Замените все эти вхождения на `{% url 'homepage' %}` или `redirect('homepage')`. Обратите особое внимание на `articles/views.py` (в `article_create` после сохранения) и `accounts/views.py` (в `login_view` как редирект по умолчанию). Проверьте также `base_layout.html` и `article_list.html`.
    *   **Цель:** Привести все ссылки и редиректы в соответствие с новым именем URL главной страницы.

21. **Шаг 21 (Инструкция 1.21): Тестирование Главной Страницы и Ссылок**
    *   **Действие:** Перейдите на главную страницу сайта (`/`). Убедитесь, что отображается список статей.
    *   **Действие:** Проверьте работу ссылок в навигации (Articles/Homepage, About, Login/Logout, Create Article). Убедитесь, что они ведут на правильные страницы и используют `homepage` там, где раньше был `articles:list`.
    *   **Действие:** **Сделайте скриншот** главной страницы (`/`) со списком статей и работающей навигацией.
    *   **Цель:** Убедиться, что реконфигурация главной страницы прошла успешно.

22. **Шаг 22 (Инструкция 1.22): Проблема Дублирующихся Слагов**
    *   **Действие:** Перейдите на страницу создания статьи (`/articles/create/`).
    *   **Действие:** Создайте статью с определенным `title` и `slug` (например, `title="Test Article"`, `slug="test-article"`).
    *   **Действие:** Снова перейдите на `/articles/create/`.
    *   **Действие:** Попытайтесь создать *еще одну* статью с *точно таким же* `slug` ("test-article").
    *   **Действие:** Вероятно, Django не позволит вам перейти к этой статье или покажет ошибку, так как слаг должен быть уникальным для детального просмотра (`path('<slug:slug>/', ...)` обычно использует `get()`, который ожидает один результат). Если у вас настроено `Article.objects.filter(slug=slug).first()`, вы увидите первую созданную статью, а не вторую.
    *   **Действие:** Перейдите по URL детального просмотра статьи, используя этот дублирующийся слаг (например, `/articles/test-article/`). Посмотрите, какая статья отображается (скорее всего, первая созданная).
    *   **Действие:** **Сделайте скриншот**, иллюстрирующий проблему (например, скриншот страницы детального просмотра, которая показывает не ту статью, которую вы ожидали, или скриншот ошибки, если она возникает). *Примечание: Если ошибки нет, а просто показывается первая статья, опишите это поведение.*
    *   **Цель:** Продемонстрировать проблему, возникающую из-за неуникальных слагов.

23. **Шаг 23 (Инструкция 1.23): Создание Файла Сигналов `signals.py`**
    *   **Действие:** В директории приложения `articles/` создайте новый файл `signals.py`.
    *   **Действие:** Напишите код для генерации уникального слага перед сохранением:
        ```python
        from django.db.models.signals import pre_save # Используем pre_save
        from django.dispatch import receiver
        from django.utils.text import slugify
        from django.utils.crypto import get_random_string
        from .models import Article
        import uuid # Альтернативный способ генерации уникальности

        @receiver(pre_save, sender=Article)
        def create_slug(sender, instance, **kwargs):
            if not instance.slug: # Создаем слаг, только если он еще не задан
                base_slug = slugify(instance.title)
                # Проверяем уникальность и добавляем случайную строку при необходимости
                # (Простая версия из скриншота, менее надежная, т.к. может быть коллизия)
                # slug_str = "%s %s" % (instance.title, get_random_string(length=4))
                # instance.slug = slugify(slug_str)

                # Более надежный способ гарантировать уникальность:
                slug = base_slug
                counter = 1
                while Article.objects.filter(slug=slug).exists():
                    # Проверяем, не создан ли уже такой слаг
                    slug = f"{base_slug}-{get_random_string(length=4)}" # Добавляем случайные символы
                    # Или можно использовать счетчик:
                    # slug = f"{base_slug}-{counter}"
                    # counter += 1
                    # Или UUID:
                    # slug = f"{base_slug}-{str(uuid.uuid4())[:8]}"
                instance.slug = slug
            # Если слаг уже есть (например, редактирование), можно добавить логику
            # для его обновления, если изменился title, но это не требуется по заданию.

        ```
        *Важно:* Используйте более надежный способ генерации уникального слага (второй вариант в комментарии), а не просто добавление случайной строки к title, как в скриншоте инструкции (это может привести к коллизиям и не очень читаемым слагам). Логика должна проверять, существует ли уже такой слаг в БД. *Обновлено:* Код в скриншоте `signals.py` (1.23) генерирует слаг ВСЕГДА перед сохранением, даже при редактировании, и просто добавляет 4 случайных символа к заголовку. Это перезапишет существующий слаг. Чтобы избежать этого, лучше генерировать слаг только если `instance.slug` пуст или если `title` изменился. Для простоты выполнения задания, можно оставить как в скриншоте, но понимать его недостатки. Адаптируем под скриншот для точности выполнения задания:
        ```python
        from django.db.models.signals import pre_save
        from django.dispatch import receiver
        from django.utils.text import slugify
        from django.utils.crypto import get_random_string
        from .models import Article

        @receiver(pre_save, sender=Article)
        def create_slug(sender, instance, **kwargs):
            # Генерируем слаг ВСЕГДА перед сохранением, как на скриншоте 1.23
            # Это может быть нежелательно при редактировании!
            random_str = get_random_string(length=4)
            slug_base = f"{instance.title} {random_str}"
            instance.slug = slugify(slug_base)
            # Примечание: Если слаг должен быть уникальным, нужна проверка на существование в БД.
            # Код в скриншоте не делает проверку уникальности, просто генерирует новый слаг.
        ```
    *   **Цель:** Автоматически генерировать потенциально уникальный слаг для статьи перед ее сохранением в базу данных, используя сигналы Django.

24. **Шаг 24 (Инструкция 1.24): Подключение Сигналов в `apps.py`**
    *   **Действие:** Откройте файл `articles/apps.py`.
    *   **Действие:** В классе `ArticlesConfig` добавьте метод `ready`:
        ```python
        from django.apps import AppConfig

        class ArticlesConfig(AppConfig):
            default_auto_field = 'django.db.models.BigAutoField'
            name = 'articles'

            def ready(self):
                import articles.signals # Импортируем сигналы при готовности приложения
        ```
    *   **Цель:** Зарегистрировать обработчики сигналов, определенные в `signals.py`, чтобы Django знал о них и вызывал их в нужные моменты.

**Часть 6: Финализация и Ответы на Вопросы**

25. **Шаг 25 (Инструкция 1.25): Удаление Поля `slug` из Формы**
    *   **Действие:** Откройте файл `articles/forms.py`.
    *   **Действие:** В классе `CreateArticle`, в `Meta`, удалите `'slug'` из списка `fields`:
        ```python
        fields = ['title', 'body', 'thumbnail'] # Убрали 'slug'
        ```
    *   **Цель:** Пользователь больше не должен вводить слаг вручную, так как он будет генерироваться автоматически.

26. **Шаг 26 (Инструкция 1.26): Скрытие Поля `slug` в Админ-панели**
    *   **Действие:** Откройте файл `articles/admin.py`.
    *   **Действие:** Зарегистрируйте модель `Article` с кастомным классом администрирования, чтобы скрыть поле `slug` (оно будет генерироваться сигналом):
        ```python
        from django.contrib import admin
        from .models import Article

        class ArticleAdmin(admin.ModelAdmin):
            list_display = ('title', 'author', 'date') # Какие поля показывать в списке
            exclude = ('slug',) # Скрываем слаг из формы редактирования/создания

        admin.site.register(Article, ArticleAdmin)
        ```
        *(Если `admin.py` не существует, создайте его)*
    *   **Действие:** Перезапустите сервер. Войдите в админку (`/admin/`), перейдите к статьям. Попробуйте добавить или отредактировать статью.
    *   **Действие:** Убедитесь, что поле `slug` больше не отображается в форме админ-панели.
    *   **Цель:** Сделать интерфейс админки более чистым, убрав поле, которое теперь управляется автоматически.

27. **Шаг 27 (Инструкция 1.27): Тестирование Автоматической Генерации Слага**
    *   **Действие:** Перейдите на страницу создания статьи (`/articles/create/`). Форма больше не должна содержать поле `slug`.
    *   **Действие:** Создайте новую статью, заполнив только `title`, `body`, `thumbnail`.
    *   **Действие:** После создания статьи вас перенаправит на главную страницу. Найдите созданную статью и перейдите на ее детальную страницу.
    *   **Действие:** Посмотрите на URL-адрес в адресной строке браузера. Он должен содержать автоматически сгенерированный слаг (например, `/articles/my-new-article-title-abcd/`).
    *   **Действие:** **Сделайте скриншот** страницы детального просмотра этой новой статьи, где виден URL с автоматически сгенерированным слагом.
    *   **Цель:** Убедиться, что сигнал работает и слаг генерируется автоматически при создании статьи через веб-интерфейс.

28. **Шаг 28 (Инструкция 1.28): Добавление Стилей (CSS)**
    *   **Действие:** Если вы еще не сделали этого, создайте файл CSS (например, `static/css/style.css`) и подключите его в `base_layout.html`.
    *   **Действие:** Напишите базовые стили для форм (`.form-article`, поля ввода), кнопок, навигации, списка статей (`.article-item`), чтобы приложение выглядело аккуратнее. Используйте классы, которые вы добавляли в HTML (или добавьте их).
    *   **Действие:** **Сделайте скриншоты** нескольких ключевых страниц (например, главная со списком статей, форма создания статьи) с примененными стилями.
    *   **Цель:** Улучшить внешний вид приложения.

29. **Шаг 29 (Инструкция 1.29): Работа с Git и GitHub**
    *   **Действие:** Инициализируйте Git-репозиторий в папке проекта (если еще не сделано): `git init`.
    *   **Действие:** Создайте файл `.gitignore`, чтобы исключить ненужные файлы (например, `__pycache__`, `db.sqlite3`, `media/`, виртуальное окружение). Найдите стандартные шаблоны `.gitignore` для Django.
    *   **Действие:** Добавьте все нужные файлы проекта в индекс: `git add .`
    *   **Действие:** Сделайте коммит: `git commit -m "Implement article creation functionality"`
    *   **Действие:** Создайте репозиторий на GitHub.
    *   **Действие:** Свяжите локальный репозиторий с удаленным: `git remote add origin <URL вашего репозитория на GitHub>`
    *   **Действие:** Отправьте изменения на GitHub: `git push -u origin main` (или `master`).
    *   **Действие:** Скопируйте **ссылку на ваш репозиторий GitHub**. Эта ссылка должна быть включена в отчет.
    *   **Цель:** Сохранить историю изменений проекта и поделиться кодом через GitHub.

**Часть 7: Ответы на Вопросы и Формирование Отчета**

30. **Шаг 30 (Вопросы 1-10): Подготовка Ответов**
    *   **Действие:** Внимательно прочитайте каждый вопрос (1-10) на страницах 10-11.
    *   **Действие:** Найдите ответы в документации Django (docs.djangoproject.com), статьях в интернете или исходя из полученного опыта при выполнении работы.
    *   **Вопрос 1 (app_name):** Объясните назначение `app_name` в `urls.py` (пространства имен) и как он используется в теге `{% url %}` (синтаксис `'имя_приложения:имя_url'`).
    *   **Вопрос 2 (Декоратор, login_required):** Дайте определение декоратора в Python. Объясните, что делает `@login_required` и зачем нужен параметр `login_url`.
    *   **Вопрос 3 (HttpResponseRedirect vs redirect):** Объясните разницу. `redirect()` - это шорткат, который может принимать имя URL, модель или URL-строку и сам создает `HttpResponseRedirect` или `HttpResponsePermanentRedirect`. `HttpResponseRedirect` требует явного указания URL.
    *   **Вопрос 4 (input hidden "next", request.GET.next):** Объясните, что скрытое поле передает URL в запросе. `request.GET` содержит параметры из URL (?next=...), `request.POST` содержит данные из тела POST-запроса (включая скрытые поля формы). `request.GET.next` в шаблоне `login.html` берет параметр `next` из URL, на который пользователя перенаправили *до* логина. `request.POST.get('next')` в `views.py` извлекает значение этого поля *после* отправки формы логина.
    *   **Вопрос 5 (forms.py):** Объясните назначение файла `forms.py` и класса `forms.Form` / `forms.ModelForm` (валидация данных, рендеринг HTML-форм, очистка данных).
    *   **Вопрос 6 (ForeignKey, on_delete):** Объясните, что `models.ForeignKey(User)` создает связь "многие-к-одному" с моделью `User`. `default=None` (в сочетании с `null=True` в БД, если миграция так сделает, или если поле не обязательное) позволяет не указывать автора. `on_delete=models.CASCADE` указывает, что при удалении связанного `User` нужно удалить и все его `Article`.
    *   **Вопрос 7 (request.FILES, commit=False):** `request.FILES` - словарь, содержащий загруженные файлы (как `thumbnail`). Его нужно передавать в форму при инициализации, если форма содержит `FileField` / `ImageField`. `form.save(commit=False)` создает объект модели из данных формы, но не сохраняет его в БД, позволяя внести изменения (например, присвоить `author`) перед вызовом `instance.save()`.
    *   **Вопрос 8 (Ошибка при создании дублей):** Ошибка возникает (или показывается не та статья), потому что слаг (`slug`) часто используется как уникальный идентификатор в URL (`path('<slug:slug>/', ...)`). Если слаги не уникальны, Django не может однозначно определить, какую статью показывать (`Model.objects.get(slug=...)` вернет ошибку MultipleObjectsReturned, если найдено больше одного, или покажет первый попавшийся, если используется `.first()`). Мы решили это автоматической генерацией уникального слага.
    *   **Вопрос 9 (Сигналы):** Объясните, что такое сигналы Django (механизм, позволяющий одним частям приложения оповещать другие о событиях). Как создать сигнал (определить функцию-получатель и декорировать ее `@receiver(signal, sender=...)`). Как его использовать (подключить в `apps.py` через метод `ready`).
    *   **Вопрос 10 (Скрытие полей в админке):** Объясните, как скрыть поля в админ-панели Django, используя класс `ModelAdmin` и его атрибут `exclude = ('field_name', ...)` при регистрации модели (`admin.site.register(Model, ModelAdmin)`).

31. **Шаг 31: Формирование Отчета**
    *   **Действие:** Создайте документ отчета.
    *   **Действие:** Включите в отчет:
        *   Цель работы.
        *   Краткое описание выполненных шагов (можно ссылаться на пункты этого плана).
        *   Все скриншоты, которые вы делали на Шагах 7, 10, 18, 21, 22, 27, 28. Подпишите каждый скриншот, поясняя, что он иллюстрирует.
        *   Описание изменений в поведении редиректа (из Шага 10).
        *   Ссылку на ваш GitHub репозиторий (из Шага 29).
        *   Подробные ответы на все 10 вопросов (из Шага 30).
    *   **Действие:** Проверьте отчет на полноту и корректность.

---

Следуя этому плану, вы систематически выполните все требования лабораторной работы и подготовите исчерпывающий отчет. Удачи!