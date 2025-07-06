<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


[![Typing SVG](https://readme-typing-svg.demolab.com/?duration=4500&color=FFFFFF&center=True&width=1100&height=74&size=46&font=Tektur&lines=LaptopParseAndNotify_bot)](https://git.io/typing-svg)
============================================================================================================================


<div align="center">
  <h3 align="center">Телеграм бот для отслеживания изменения цен</b></h3>
</div>


<!-- ABOUT THE PROJECT -->
# О чём проект

<div>   
  <img src="logo2 (2).jpg" alt="Logo" width="210" height="420">  
  <img src="logo (2).jpg" alt="Logo" width="210" height="420">  
</div>

Этот Telegram-бот предназначен для автоматического отслеживания цен на различные ноутбуки на сайте MVideo<br>
Он поможет вам первыми получать уведомления о изменении цен, экономя ваше время и силы<br>

# Принцип работы

Пользователи могут добавлять/удалять в коризну нужные бренды ноутбуков для мониторинга, а также просматривать выбранные модели. <br>После этого активировать/деактивировать отправку уведомлений при изменении цен<br>
Парсер каждые 24 часа собирает информацию о ноутбуках и сохраняет её в EXCEL и JSON файлы, после сравнивает старые цены ноутбуков из файла parser.csv и позже перезаписывает в файл новые данные, при изменении цен бот отправляет уведомление пользователю.


<!-- GETTING STARTED -->
## Описание функционала основных кнопок
* <b>✅ Activate</b>: Пользователь активирует функцию отправки сообщений, его id добавляется в файл activate_users 
* <b>❌ Deactivate</b>: Пользователь деактивирует функцию отправки сообщений, его id удаляется из файла activate_users 
* <b>Добавить модель</b>: Выдаётся отдельная панель с брендами ноутбуков. После ему будут приходить уведомления об изменении цен только на выбранные модели
* <b>Удалить модель</b>:  Выдаётся отдельная панель с брендами ноутбуков. Удаляет выбранную модель из своего списка
* <b>Мои модели</b>: Выдаются выбранные модели, при изменении цен которых будут приходить уведомления</b>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
