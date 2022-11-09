def get_config(flag: str):
    from conf.config import Config
    return Config().conf_insert_svr(flag)


def ui(dialog):
    from func.GetSYSGB import GetSYSGB
    from ui.CommonUI import Layout, Label, Lineedit, ToolButton, Combobox
    from PyQt5.QtWidgets import QVBoxLayout, QComboBox, QDialogButtonBox, QRadioButton
    from PyQt5.QtGui import QIcon

    dialog.setWindowTitle(get_config("window_title"))
    dialog.setWindowIcon(QIcon(get_config("icon")))
    dialog.setStyleSheet("QDialog {background: white;}")

    dialog.main_layout = QVBoxLayout()
    dialog.code_layout = Layout()
    dialog.ih_layout = Layout()
    dialog.disk_layout = Layout()
    dialog.svc_layout = Layout()
    dialog.task_layout = Layout()
    dialog.win_layout = Layout()

    dialog.code_sys_lbl = Label("시스템")
    dialog.code_sys_combo = Combobox()
    dialog.sys_list = GetSYSGB.get_syslist()
    for i in dialog.sys_list:
        dialog.code_sys_combo.addItem(i[1])
    dialog.code_sys_combo.setFixedWidth(120)

    dialog.code_gb_lbl = Label("구분")
    dialog.code_gb_combo = Combobox()
    dialog.gb_list = GetSYSGB.get_gblist()
    for i in dialog.gb_list:
        dialog.code_gb_combo.addItem(i[1])
    dialog.code_gb_combo.setFixedWidth(120)

    dialog.ih_ip_lbl = Label("IP")
    dialog.ih_ip_le = Lineedit()
    dialog.ih_host_lbl = Label("호스트명")
    dialog.ih_host_le = Lineedit()

    # self.buttonBox = QDialogButtonBox(QtCore.Qt.Vertical)
    dialog.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    dialog.buttonBox.accepted.connect(dialog.accepted)
    dialog.buttonBox.rejected.connect(dialog.rejected)

    dialog.disk_nm_lbl = Label("디스크")
    dialog.disk_le = Lineedit()
    dialog.disk_ex_lbl = Label("예: C")
    dialog.disk_pushbtn = ToolButton("추가", "blue")
    dialog.disk_pushbtn.clicked.connect(dialog.click_disk_pushbtn)

    dialog.svc_nm_lbl = Label("서비스")
    dialog.sys_le = Lineedit()
    dialog.sys_ex_lbl = Label("예: WebtoB")
    dialog.sys_pushbtn = ToolButton("추가", "red")
    dialog.sys_pushbtn.clicked.connect(dialog.click_svc_pushbtn)

    dialog.task_nm_lbl = Label("작업스케줄러")
    dialog.task_le = Lineedit()
    dialog.task_ex_lbl = Label("예: HRCollector")
    dialog.task_pushbtn = ToolButton("추가", "blue")
    dialog.task_pushbtn.clicked.connect(dialog.click_task_pushbtn)

    dialog.wdef_nm_lbl = Label("윈도우 디펜더")
    dialog.wdef_yes_radio = QRadioButton("사용", dialog)
    #dialog.wdef_yes_radio.setStyleSheet("QRadioButton {color: red}")
    dialog.wdef_no_radio = QRadioButton("미사용", dialog)
    dialog.wdef_yes_radio.clicked.connect(dialog.click_wdef_radio)
    dialog.wdef_no_radio.clicked.connect(dialog.click_wdef_radio)

    dialog.code_layout.addWidget(dialog.code_sys_lbl, 0, 0)
    dialog.code_layout.addWidget(dialog.code_sys_combo, 0, 1)
    dialog.code_layout.addWidget(dialog.buttonBox, 0, 2)
    dialog.code_layout.addWidget(dialog.code_gb_lbl, 1, 0)
    dialog.code_layout.addWidget(dialog.code_gb_combo, 1, 1)
    dialog.code_sys_lbl.setContentsMargins(0, 0, 42, 0)
    dialog.code_gb_lbl.setContentsMargins(0, 0, 42, 0)

    dialog.ih_layout.addWidget(dialog.ih_ip_lbl, 0, 0)
    dialog.ih_layout.addWidget(dialog.ih_ip_le, 0, 1)
    dialog.ih_layout.addWidget(dialog.ih_host_lbl, 1, 0)
    dialog.ih_layout.addWidget(dialog.ih_host_le, 1, 1)
    dialog.ih_ip_lbl.setContentsMargins(0, 0, 30, 0)
    dialog.ih_host_lbl.setContentsMargins(0, 0, 30, 0)

    dialog.disk_layout.addWidget(dialog.disk_nm_lbl, 0, 0)
    dialog.disk_layout.addWidget(dialog.disk_le, 0, 1)
    dialog.disk_layout.addWidget(dialog.disk_ex_lbl, 0, 2)
    dialog.disk_layout.addWidget(dialog.disk_pushbtn, 0, 3)
    dialog.disk_nm_lbl.setContentsMargins(0, 0, 42, 0)
    dialog.disk_ex_lbl.setContentsMargins(30, 0, 28, 0)

    dialog.svc_layout.addWidget(dialog.svc_nm_lbl, 0, 0)
    dialog.svc_layout.addWidget(dialog.sys_le, 0, 1)
    dialog.svc_layout.addWidget(dialog.sys_ex_lbl, 0, 2)
    dialog.svc_layout.addWidget(dialog.sys_pushbtn, 0, 3)
    dialog.svc_nm_lbl.setContentsMargins(0, 0, 42, 0)
    dialog.sys_ex_lbl.setContentsMargins(15, 0, 10, 0)

    dialog.task_layout.addWidget(dialog.task_nm_lbl, 0, 0)
    dialog.task_layout.addWidget(dialog.task_le, 0, 1)
    dialog.task_layout.addWidget(dialog.task_ex_lbl, 0, 2)
    dialog.task_layout.addWidget(dialog.task_pushbtn, 0, 3)
    dialog.task_nm_lbl.setContentsMargins(0, 0, 6, 0)

    dialog.win_layout.addWidget(dialog.wdef_nm_lbl, 0, 0)
    dialog.win_layout.addWidget(dialog.wdef_yes_radio, 0, 1)
    dialog.win_layout.addWidget(dialog.wdef_no_radio, 0, 2)

    dialog.main_layout.addLayout(dialog.code_layout)
    dialog.main_layout.addLayout(dialog.ih_layout)
    dialog.main_layout.addLayout(dialog.disk_layout)
    dialog.main_layout.addLayout(dialog.svc_layout)
    dialog.main_layout.addLayout(dialog.task_layout)
    dialog.main_layout.addLayout(dialog.win_layout)
    dialog.setLayout(dialog.main_layout)
