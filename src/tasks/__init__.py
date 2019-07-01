# -*- coding: utf-8 -*-
from flask.cli import AppGroup
from tasks.task1 import task1_run

# グループを作成
task = AppGroup('task')

# task関連のコマンドを追加していく
task.add_command(task1_run)
