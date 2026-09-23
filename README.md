# Python Learn

Приложение для изучения Python — 24 модуля курса (теория, примеры кода, тесты).
Работает на ПК (Windows/Linux/macOS) и собирается в APK для Android.

## Возможности

- 24 учебных модуля: от основ до Django и нейросетей
- Теория в удобном виде + примеры кода
- Тесты для самопроверки с результатом
- Отслеживание прогресса (сохраняется на устройстве)

## Запуск на ПК

```bash
pip install -r requirements.txt
python main.py
```

## Сборка APK для Android

```bash
pip install buildozer cython
buildozer android debug
```

Артефакт: `bin/pythonlearn-0.1-arm64-v8a-debug.apk`

Для сборки нужны Java/JDK, `python3`, `zip`, `unzip` (в Linux или WSL; Android SDK/NDK ставится автоматически).

## Структура

```
main.py            # приложение Kivy (ПК + Android)
content/modules.py # весь учебный контент
requirements.txt   # зависимости
buildozer.spec     # конфиг APK
```