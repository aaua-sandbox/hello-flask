import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from datetime import datetime
from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    @classmethod
    def get_all(cls):
        """
        全ユーザを取得
        :return: Userリスト
        """
        return db.session.query(cls).all()
