
from sqlalchemy.sql import Select
from app.misc import db
from app.models.user import UserRelatedModel


class UserSettings(UserRelatedModel):
    __tablename__ = 'user_settings'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    notifications_general_enabled = db.Column(db.Boolean)
    notifications_advance_enabled = db.Column(db.Boolean)
    notifications_periodical_frequency_enabled = db.Column(db.Boolean)
    notifications_advance_days_until_expiration = db.Column(db.Integer)
    notifications_periodical_frequency = db.Column(db.Integer)
    notifications_weekly_enabled = db.Column(db.Boolean)
    notifications_weekly_day = db.Column(db.Integer)
    last_notify_day_frequency = db.Column(db.Date)
    query: Select

