def get_config(flag: str):
    from conf.config import Config
    return Config().conf_delete_svr(flag)


def ui(dialog):
    from ui.CommonUI import Layout, Label, Lineedit, PushButton
    from PyQt5.QtGui import QIcon

    dialog.setWindowTitle(get_config("window_title"))
    dialog.setWindowIcon(QIcon(get_config("icon")))

    dialog.layout = Layout()
    dialog.label = Label("호스트명")
    dialog.linedit = Lineedit()
    dialog.button = PushButton("삭제")
    dialog.button.clicked.connect(dialog.click_delete_btn)

    dialog.layout.addWidget(dialog.label, 0, 0)
    dialog.layout.addWidget(dialog.linedit, 0, 1)
    dialog.layout.addWidget(dialog.button, 0, 2)

    dialog.setLayout(dialog.layout)
