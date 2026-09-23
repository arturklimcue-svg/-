# -*- coding: utf-8 -*-
"""Python Learn — приложение для изучения Python (ПК + Android APK)."""
import os
import sys
import json

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, BooleanProperty, NumericProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.togglebutton import ToggleButton

try:
    from content.modules import MODULES
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from content.modules import MODULES


def user_data_dir():
    if hasattr(os, "android") and os.environ.get("ANDROID_ARGUMENT"):
        from android.storage import primary_external_storage_path
        base = os.path.join(primary_external_storage_path(), "pythonlearn")
    else:
        base = os.path.join(os.path.expanduser("~"), ".python_learn")
    os.makedirs(base, exist_ok=True)
    return base


STORE = JsonStore(os.path.join(user_data_dir(), "progress.json"))

KV = """
#:import utils kivy.utils

<RoundedButton@Button>:
    background_normal: ''
    background_color: utils.get_color_from_hex('#2D7FF9') if self.state == 'normal' else utils.get_color_from_hex('#1B5FD0')
    color: 1, 1, 1, 1
    font_size: '16sp'
    bold: True

<FlatButton@Button>:
    background_normal: ''
    background_color: 0, 0, 0, 0
    color: utils.get_color_from_hex('#2D7FF9')

<MainMenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: '12dp'
        spacing: '8dp'

        Label:
            text: 'Python Learn'
            font_size: '28sp'
            bold: True
            color: utils.get_color_from_hex('#2D7FF9')
            size_hint_y: None
            height: '48dp'

        Label:
            id: progress_label
            text: root.progress_text
            font_size: '14sp'
            color: 0.7, 0.7, 0.7, 1
            size_hint_y: None
            height: '24dp'

        ProgressBar:
            id: total_progress
            max: 100
            value: root.progress_value
            size_hint_y: None
            height: '14dp'

        ScrollView:
            id: menu_scroll
            do_scroll_x: False
            BoxLayout:
                id: menu_list
                orientation: 'vertical'
                padding: '4dp'
                spacing: '6dp'
                size_hint_y: None
                height: self.minimum_height

<ModuleScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: '8dp'
        spacing: '6dp'

        BoxLayout:
            size_hint_y: None
            height: '44dp'
            spacing: '8dp'
            RoundedButton:
                text: '← Назад'
                size_hint_x: None
                width: '110dp'
                on_release: app.go_menu()
            Label:
                id: title_label
                text: root.title_text
                font_size: '18sp'
                bold: True
                color: utils.get_color_from_hex('#2D7FF9')
                text_size: self.width, None
                halign: 'center'
                valign: 'middle'

        BoxLayout:
            size_hint_y: None
            height: '40dp'
            spacing: '4dp'
            ToggleButton:
                id: tab_theory
                text: 'Теория'
                group: 'tabs'
                state: 'down'
                background_normal: ''
                background_color: utils.get_color_from_hex('#2D7FF9') if self.state == 'down' else utils.get_color_from_hex('#2A2A3A')
                color: 1, 1, 1, 1
                on_release: root.show_tab('theory')
            ToggleButton:
                id: tab_examples
                text: 'Примеры'
                group: 'tabs'
                background_normal: ''
                background_color: utils.get_color_from_hex('#2D7FF9') if self.state == 'down' else utils.get_color_from_hex('#2A2A3A')
                color: 1, 1, 1, 1
                on_release: root.show_tab('examples')
            ToggleButton:
                id: tab_quiz
                text: 'Тест'
                group: 'tabs'
                background_normal: ''
                background_color: utils.get_color_from_hex('#2D7FF9') if self.state == 'down' else utils.get_color_from_hex('#2A2A3A')
                color: 1, 1, 1, 1
                on_release: root.show_tab('quiz')
            ToggleButton:
                id: tab_docs
                text: 'Документация'
                group: 'tabs'
                background_normal: ''
                background_color: utils.get_color_from_hex('#2D7FF9') if self.state == 'down' else utils.get_color_from_hex('#2A2A3A')
                color: 1, 1, 1, 1
                on_release: root.show_tab('docs')

        ScrollView:
            id: scroll
            do_scroll_x: False
            BoxLayout:
                id: content_box
                orientation: 'vertical'
                padding: '6dp'
                spacing: '8dp'
                size_hint_y: None
                height: self.minimum_height

        RoundedButton:
            id: complete_btn
            text: 'Отметить модуль изученным'
            size_hint_y: None
            height: '48dp'
            on_release: root.mark_complete()
"""


# ---------------------------------------------------------------------------
# Хранилище прогресса
# ---------------------------------------------------------------------------
def is_done(mid):
    try:
        return bool(STORE.get(str(mid))["done"])
    except KeyError:
        return False


def set_done(mid, value=True):
    STORE.put(str(mid), done=bool(value))


def done_count():
    return sum(1 for m in MODULES if is_done(m["id"]))


# ---------------------------------------------------------------------------
# Экраны
# ---------------------------------------------------------------------------
class MainMenuScreen(Screen):
    progress_text = StringProperty("")
    progress_value = NumericProperty(0)

    def on_pre_enter(self):
        self.refresh()

    def refresh(self):
        done = done_count()
        total = len(MODULES)
        self.progress_text = f"Изучено {done} из {total} модулей"
        self.progress_value = 100.0 * done / total if total else 0
        mlist = self.ids.menu_list
        mlist.clear_widgets()
        for m in MODULES:
            d = is_done(m["id"])
            row = _card(utils_get('#12351F') if d else utils_get('#1E1E2E'))

            title = Label(
                text=f'{m["id"]}. {m["title"]}',
                font_size="15sp",
                color=(1, 1, 1, 1),
                halign="left",
                valign="middle",
                text_size=(self.width - dp(160), None),
            )
            title.bind(size=lambda inst, s: setattr(inst, "text_size", (s[0], None)))
            row.add_widget(title)

            status = Label(
                text="✓" if d else "●",
                font_size="20sp",
                color=utils_get("#4CAF50") if d else (0.5, 0.5, 0.5, 1),
                size_hint_x=None, width=dp(28),
            )
            row.add_widget(status)

            btn = Button(
                text="Открыть",
                size_hint_x=None,
                width=dp(84),
                background_normal="",
                background_color=utils_get("#2D7FF9"),
                color=(1, 1, 1, 1),
                font_size="14sp",
                bold=True,
            )
            mid = m["id"]
            btn.bind(on_release=lambda inst, m_id=mid: App.get_running_app().open_module(m_id))
            row.add_widget(btn)

            mlist.add_widget(row)


class ModuleScreen(Screen):
    title_text = StringProperty("")
    mid = StringProperty("")

    def load(self, mid):
        self.mid = str(mid)
        module = next(m for m in MODULES if str(m["id"]) == str(mid))
        self.title_text = f'{module["id"]}. {module["title"]}'
        self.ids.title_label.text = self.title_text
        self._module = module
        self._q_index = 0
        self._q_score = 0
        self._answered = False
        self.show_tab("theory")
        btn = self.ids.complete_btn
        btn.text = "Модуль изучен ✓" if is_done(mid) else "Отметить модуль изученным"

    def show_tab(self, tab):
        ids = self.ids
        ids.tab_theory.state = "down" if tab == "theory" else "normal"
        ids.tab_examples.state = "down" if tab == "examples" else "normal"
        ids.tab_quiz.state = "down" if tab == "quiz" else "normal"
        ids.tab_docs.state = "down" if tab == "docs" else "normal"
        box = ids.content_box
        box.clear_widgets()
        if tab == "theory":
            self._build_theory(box)
        elif tab == "examples":
            self._build_examples(box)
        elif tab == "docs":
            self._build_docs(box)
        else:
            self._build_quiz(box)

    # ---- Документация ----
    def _build_docs(self, box):
        url = self._module.get("doc_url", "https://docs.python.org/3/")
        label = self._module.get("doc_label", "Официальная документация")
        head = Label(
            text="Официальная документация",
            color=utils_get("#7CC4FF"),
            font_size="18sp",
            bold=True,
            halign="left",
            valign="top",
            size_hint_y=None,
            height=dp(30),
        )
        box.add_widget(head)

        txt = Label(
            text=f"Раздел: {label}\n\nСсылка:\n{url}\n\n"
                 "Для открытия в браузере нажмите кнопку ниже.",
            color=(1, 1, 1, 1),
            font_size="15sp",
            halign="left",
            valign="top",
            text_size=(self.width - dp(24), None),
            size_hint_y=None,
        )
        txt.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)),
                 height=lambda inst, h: setattr(inst, "height", h.texture_size[1] + dp(10)))
        box.add_widget(txt)

        btn = Button(
            text="🌐 Открыть документацию",
            size_hint_y=None,
            height=dp(52),
            background_normal="",
            background_color=utils_get("#2D7FF9"),
            color=(1, 1, 1, 1),
            font_size="16sp",
            bold=True,
        )
        btn.bind(on_release=lambda *_: _open_url(url))
        box.add_widget(btn)

        info = Label(
            text="* Для работы модуля интернет не обязателен — ссылка "
                 "открывается при наличии соединения.",
            color=(0.6, 0.6, 0.6, 1),
            font_size="13sp",
            halign="left",
            valign="top",
            text_size=(self.width - dp(24), None),
            size_hint_y=None,
        )
        info.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)),
                  height=lambda inst, h: setattr(inst, "height", h.texture_size[1] + dp(10)))
        box.add_widget(info)

    # ---- Теория ----
    def _build_theory(self, box):
        for line in self._module["theory"].splitlines():
            if not line.strip():
                box.add_widget(Label(text="", size_hint_y=None, height=dp(6)))
                continue
            color = (1, 1, 1, 1)
            bold = False
            font = "15sp"
            if line.startswith("# "):
                color = utils_get("#2D7FF9")
                bold = True
                font = "22sp"
            elif line.startswith("## "):
                color = utils_get("#7CC4FF")
                bold = True
                font = "18sp"
            elif line.startswith("|"):
                color = (0.85, 0.85, 0.85, 1)
            elif line.startswith("```"):
                continue
            lbl = Label(
                text=line.replace("**", ""),
                color=color,
                font_size=font,
                bold=bold,
                halign="left",
                valign="top",
                text_size=(self.width - dp(24), None),
                size_hint_y=None,
            )
            lbl.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)),
                     height=lambda inst, h: setattr(inst, "height", h.texture_size[1] + dp(4)))
            box.add_widget(lbl)

    # ---- Примеры ----
    def _build_examples(self, box):
        mono = _mono_font()
        for i, ex in enumerate(self._module["examples"], 1):
            header = Label(
                text=f"Пример {i}: {ex['explain']}",
                color=utils_get("#7CC4FF"),
                font_size="14sp",
                halign="left",
                valign="top",
                text_size=(self.width - dp(24), None),
                size_hint_y=None,
            )
            header.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)),
                        height=lambda inst, h: setattr(inst, "height", h.texture_size[1] + dp(4)))
            box.add_widget(header)

            code = Label(
                text=ex["code"],
                font_size="13sp",
                font_name=mono,
                color=utils_get("#D4D4D4"),
                halign="left",
                valign="top",
                size_hint_y=None,
            )
            code.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)),
                      height=lambda inst, h: setattr(inst, "height", h.texture_size[1] + dp(8)))
            box.add_widget(code)
            box.add_widget(Label(text="", size_hint_y=None, height=dp(8)))

    # ---- Тест ----
    def _build_quiz(self, box):
        quiz = self._module.get("quiz", [])
        if not quiz:
            box.add_widget(Label(text="Тест не найден", color=(1, 1, 1, 1)))
            return
        if self._q_index >= len(quiz):
            total = len(quiz)
            score = self._q_score
            res = Label(
                text=f"Результат: {score} / {total}\n" + ("Отлично! 🎉" if score == total else "Попробуйте ещё раз"),
                color=utils_get("#4CAF50") if score == total else utils_get("#FFC107"),
                font_size="20sp",
                halign="center",
                size_hint_y=None,
                height=dp(90),
            )
            box.add_widget(res)
            btn = RoundedButton(text="Пройти заново", size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda *_: self._restart_quiz())
            box.add_widget(btn)
            if score / total >= 0.75:
                btn2 = RoundedButton(text="Отметить изученным ✓", size_hint_y=None, height=dp(44))
                btn2.bind(on_release=lambda *_: self.mark_complete())
                box.add_widget(btn2)
            return

        q = quiz[self._q_index]
        head = Label(
            text=f"Вопрос {self._q_index + 1} / {len(quiz)}   (верно: {self._q_score})",
            color=(0.7, 0.7, 0.7, 1),
            font_size="14sp",
            size_hint_y=None,
            height=dp(28),
        )
        box.add_widget(head)

        qlbl = Label(
            text=q["q"],
            color=(1, 1, 1, 1),
            font_size="17sp",
            bold=True,
            halign="left",
            valign="top",
            text_size=(self.width - dp(24), None),
            size_hint_y=None,
        )
        qlbl.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)),
                  height=lambda inst, h: setattr(inst, "height", h.texture_size[1] + dp(10)))
        box.add_widget(qlbl)

        self._answered = False
        for idx, opt in enumerate(q["options"]):
            b = Button(
                text=opt,
                size_hint_y=None,
                height=dp(46),
                background_normal="",
                background_color=utils_get("#2A2A3A"),
                color=(1, 1, 1, 1),
                font_size="15sp",
            )
            b.bind(on_release=lambda inst, i=idx, correct=q["correct"]: self._answer(i, correct, box))
            box.add_widget(b)

    def _answer(self, chosen, correct, box):
        if self._answered:
            return
        self._answered = True
        if chosen == correct:
            self._q_score += 1
        self._q_index += 1
        self.show_tab("quiz")

    def _restart_quiz(self):
        self._q_index = 0
        self._q_score = 0
        self.show_tab("quiz")

    def mark_complete(self):
        set_done(self.mid, True)
        self.ids.complete_btn.text = "Модуль изучен ✓"


def dp(v):
    from kivy.metrics import dp as _dp
    return _dp(v)


def utils_get(hex_color):
    from kivy.utils import get_color_from_hex
    return get_color_from_hex(hex_color)


def _card(bg_color):
    from kivy.uix.boxlayout import BoxLayout
    from kivy.graphics import Color, RoundedRectangle
    row = BoxLayout(size_hint_y=None, height=dp(60), spacing=dp(8), padding=[dp(8), 0, dp(8), 0])
    with row.canvas.before:
        Color(*bg_color)
        rr = RoundedRectangle(radius=[dp(8)])
    row.bind(pos=lambda w, v: setattr(rr, 'pos', w.pos),
             size=lambda w, v: setattr(rr, 'size', w.size))
    return row


def _open_url(url):
    """Открыть ссылку в браузере (ПК и Android)."""
    try:
        if os.environ.get("ANDROID_ARGUMENT") or hasattr(os, "android"):
            from android import mActivity
            from jnius import autoclass
            Intent = autoclass("android.content.Intent")
            uri = autoclass("android.net.Uri").parse(url)
            intent = Intent(Intent.ACTION_VIEW, uri)
            mActivity.startActivity(intent)
        else:
            import webbrowser
            webbrowser.open(url)
    except Exception:
        pass


def _mono_font():
    candidates = [
        "/system/fonts/DroidSansMono.ttf",
        "/system/fonts/RobotoMono-Regular.ttf",
        "/system/fonts/NotoSansMono-Regular.ttf",
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cour.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return "Default"


# ---------------------------------------------------------------------------
# Приложение
# ---------------------------------------------------------------------------
class PythonLearnApp(App):
    title = "Python Learn"

    def build(self):
        Window.clearcolor = (0.08, 0.08, 0.12, 1)
        Builder.load_string(KV)
        self.sm = ScreenManager(transition=SlideTransition(duration=0.15))
        self.menu = MainMenuScreen(name="menu")
        self.module_screen = ModuleScreen(name="module")
        self.sm.add_widget(self.menu)
        self.sm.add_widget(self.module_screen)
        return self.sm

    def open_module(self, mid):
        self.module_screen.load(mid)
        self.sm.current = "module"

    def go_menu(self):
        self.sm.current = "menu"


if __name__ == "__main__":
    PythonLearnApp().run()
