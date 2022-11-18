def get_config(flag: str):
    from conf.config import Config
    return Config().conf_insert_svr(flag)


def ui(dialog):
    from func.GetSYSGB import GetSYSGB
    from ui.CommonUI import Layout, Label, Lineedit, ToolButton, Combobox
    from PyQt5.QtWidgets import QVBoxLayout, QDialogButtonBox, QRadioButton
    from PyQt5.QtGui import QIcon

    dialog.setWindowTitle(get_config("window_title"))
    dialog.setWindowIcon(QIcon(get_config("icon")))
    dialog.setGeometry(700, 350, 300, 200)
    dialog.setStyleSheet("QDialog {background: white;}")

    dialog.main_layout = QVBoxLayout()
    dialog.code_layout = Layout()
    dialog.ip_layout = Layout()
    dialog.host_layout = Layout()
    dialog.disk_layout = Layout()
    dialog.svc_layout = Layout()
    dialog.task_layout = Layout()
    dialog.win_layout = Layout()

    dialog.sys_lbl = Label("시스템", 100)
    dialog.sys_combo = Combobox()
    dialog.sys_combo.setFixedWidth(120)
    dialog.sys_list = GetSYSGB.get_syslist()
    for i in dialog.sys_list:
        dialog.sys_combo.addItem(i[1])

    dialog.gb_lbl = Label("구분", 100)
    dialog.gb_combo = Combobox()
    dialog.gb_combo.setFixedWidth(120)
    dialog.gb_list = GetSYSGB.get_gblist()
    for i in dialog.gb_list:
        dialog.gb_combo.addItem(i[1])

    dialog.ip_lbl = Label("IP", 100)
    dialog.ip_le = Lineedit(0)

    dialog.host_lbl = Label("호스트명", 100)
    dialog.host_le = Lineedit(0)

    # self.buttonBox = QDialogButtonBox(QtCore.Qt.Vertical)
    dialog.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    dialog.buttonBox.accepted.connect(dialog.accepted)
    dialog.buttonBox.rejected.connect(dialog.rejected)

    dialog.disk_nm_lbl = Label("디스크", 100)
    dialog.disk_le = Lineedit(170)
    #dialog.disk_le.setFixedWidth(170)
    dialog.disk_ex_lbl = Label("예: C", 100)
    dialog.disk_toolbtn = ToolButton("추가", "blue")
    dialog.disk_toolbtn.clicked.connect(dialog.click_disk_toolbtn)

    dialog.svc_nm_lbl = Label("서비스", 100)
    dialog.sys_le = Lineedit(170)
    #dialog.sys_le.setFixedWidth(170)
    dialog.sys_ex_lbl = Label("예: WebtoB", 100)
    dialog.sys_toolbtn = ToolButton("추가", "blue")
    dialog.sys_toolbtn.clicked.connect(dialog.click_svc_toolbtn)

    dialog.task_nm_lbl = Label("작업스케줄러", 100)
    dialog.task_le = Lineedit(170)
    #dialog.task_le.setFixedWidth(170)
    dialog.task_ex_lbl = Label("예: HRCollector", 100)
    dialog.task_toolbtn = ToolButton("추가", "blue")
    dialog.task_toolbtn.clicked.connect(dialog.click_task_toolbtn)

    dialog.wdef_nm_lbl = Label("윈도우 디펜더", 100)
    dialog.wdef_yes_radio = QRadioButton("사용", dialog)
    #dialog.wdef_yes_radio.setStyleSheet("QRadioButton {color: red}")
    dialog.wdef_no_radio = QRadioButton("미사용", dialog)
    dialog.wdef_yes_radio.clicked.connect(dialog.click_wdef_radio)
    dialog.wdef_no_radio.clicked.connect(dialog.click_wdef_radio)

    dialog.code_layout.addWidget(dialog.sys_lbl, 0, 0)
    dialog.code_layout.addWidget(dialog.sys_combo, 0, 1)
    dialog.code_layout.addWidget(dialog.buttonBox, 0, 2)
    dialog.code_layout.addWidget(dialog.gb_lbl, 1, 0)
    dialog.code_layout.addWidget(dialog.gb_combo, 1, 1)
    dialog.sys_lbl.setContentsMargins(0, 0, 42, 0)
    dialog.gb_lbl.setContentsMargins(0, 0, 42, 0)

    dialog.ip_layout.addWidget(dialog.ip_lbl, 0, 0)
    dialog.ip_layout.addWidget(dialog.ip_le, 0, 1)
    dialog.host_layout.addWidget(dialog.host_lbl, 0, 0)
    dialog.host_layout.addWidget(dialog.host_le, 0, 1)
    dialog.ip_lbl.setContentsMargins(0, 0, 30, 0)
    dialog.host_lbl.setContentsMargins(0, 0, 30, 0)

    dialog.disk_layout.addWidget(dialog.disk_nm_lbl, 0, 0)
    dialog.disk_layout.addWidget(dialog.disk_le, 0, 1)
    dialog.disk_layout.addWidget(dialog.disk_ex_lbl, 0, 2)
    dialog.disk_layout.addWidget(dialog.disk_toolbtn, 0, 3)
    dialog.disk_nm_lbl.setContentsMargins(0, 0, 42, 0)
    dialog.disk_ex_lbl.setContentsMargins(30, 0, 28, 0)

    dialog.svc_layout.addWidget(dialog.svc_nm_lbl, 0, 0)
    dialog.svc_layout.addWidget(dialog.sys_le, 0, 1)
    dialog.svc_layout.addWidget(dialog.sys_ex_lbl, 0, 2)
    dialog.svc_layout.addWidget(dialog.sys_toolbtn, 0, 3)
    dialog.svc_nm_lbl.setContentsMargins(0, 0, 42, 0)
    dialog.sys_ex_lbl.setContentsMargins(15, 0, 10, 0)

    dialog.task_layout.addWidget(dialog.task_nm_lbl, 0, 0)
    dialog.task_layout.addWidget(dialog.task_le, 0, 1)
    dialog.task_layout.addWidget(dialog.task_ex_lbl, 0, 2)
    dialog.task_layout.addWidget(dialog.task_toolbtn, 0, 3)
    dialog.task_nm_lbl.setContentsMargins(0, 0, 6, 0)

    dialog.win_layout.addWidget(dialog.wdef_nm_lbl, 0, 0)
    dialog.win_layout.addWidget(dialog.wdef_yes_radio, 0, 1)
    dialog.win_layout.addWidget(dialog.wdef_no_radio, 0, 2)

    dialog.main_layout.addLayout(dialog.code_layout)
    dialog.main_layout.addLayout(dialog.ip_layout)
    dialog.main_layout.addLayout(dialog.host_layout)
    dialog.main_layout.addLayout(dialog.disk_layout)
    dialog.main_layout.addLayout(dialog.svc_layout)
    dialog.main_layout.addLayout(dialog.task_layout)
    dialog.main_layout.addLayout(dialog.win_layout)
    dialog.setLayout(dialog.main_layout)
