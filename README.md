# Sprint_5

UI-тесты сервиса "Доска" на Selenium и pytest.

- `test_successful_registration_shows_user_in_header` - после регистрации на главной видны аватар и имя User.
- `test_invalid_email_highlights_registration_fields` - email не по маске: поля красные, под Email текст "Ошибка"
- `test_existing_user_highlights_registration_fields` - повторная регистрация тем же email: поля красные, под Email текст "Ошибка"
- `test_successful_login_shows_user_in_header` - после входа на главной видны аватар и имя User.
- `test_logout_shows_login_button_instead_of_user` - после выхода вместо аватара кнопка "Вход и регистрация"
- `test_guest_place_ad_shows_auth_modal` - гость при размещении объявления видит окно с просьбой авторизоваться
- `test_authorized_user_ad_appears_in_profile` - созданное объявление видно в блоке "Мои объявления"

```
pytest tests
```
