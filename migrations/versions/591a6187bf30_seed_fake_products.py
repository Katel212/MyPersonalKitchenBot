"""seed fake products

Revision ID: 591a6187bf30
Revises: b1ebe6dc222c
Create Date: 2020-11-25 17:36:49.040383

"""
from datetime import date

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import table

revision = '591a6187bf30'
down_revision = 'b1ebe6dc222c'
branch_labels = None
depends_on = None


def upgrade():
    products = table(
        'products',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('expiration_date', sa.Date(), nullable=True),
        sa.Column('bought_date', sa.Date(), nullable=True),
        sa.Column('info', sa.String(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
    )

    op.bulk_insert(
        products,
        [
            {
                'name': 'молоко',
                'expiration_date': date(2020, 12, 20),
                'bought_date': date(2020, 12, 10),
                'info': 'lorem ipsum',
                'user_id': 280536886
            },
            {
                'name': 'хлеб',
                'expiration_date': date(2020, 12, 19),
                'bought_date': date(2020, 12, 10),
                'info': None,
                'user_id': 280536886
            },
            {
                'name': 'кофе',
                'expiration_date': date(2020, 12, 20),
                'bought_date': date(2020, 12, 10),
                'info': 'lorem ipsum',
                'user_id': 280536886
            },
            {
                'name': 'свинина',
                'expiration_date': date(2020, 12, 13),
                'bought_date': date(2020, 12, 10),
                'info': 'lorem ipsum',
                'user_id': 280536886
            },
            {
                'name': 'соль',
                'expiration_date': date(2021, 12, 20),
                'bought_date': date(2020, 12, 10),
                'info': 'lorem ipsum',
                'user_id': 280536886
            },
            {
                'name': 'сода',
                'expiration_date': date(3020, 12, 20),
                'bought_date': date(2020, 12, 10),
                'info': None,
                'user_id': 280536886
            },
            {
                'name': 'мандарины',
                'expiration_date': date(2021, 1, 1),
                'bought_date': date(2020, 12, 10),
                'info': '2 кг',
                'user_id': 280536886
            },
            {
                'name': 'макароны',
                'expiration_date': date(2021, 6, 18),
                'bought_date': date(2020, 12, 10),
                'info': 'lorem ipsum',
                'user_id': 280536886
            },
            {
                'name': 'печенье',
                'expiration_date': date(2021, 1, 20),
                'bought_date': date(2020, 12, 10),
                'info': None,
                'user_id': 280536886
            },
            {
                'name': 'картофель',
                'expiration_date': date(2020, 12, 15),
                'bought_date': date(2020, 12, 10),
                'info': '5 кг',
                'user_id': 280536886
            },
            {
                'name': 'орехи грецкие',
                'expiration_date': date(2021, 12, 10),
                'bought_date': date(2020, 12, 10),
                'info': 'lorem ipsum',
                'user_id': 280536886
            },
            {
                'name': 'икра',
                'expiration_date': date(2020, 12, 31),
                'bought_date': date(2020, 12, 10),
                'info': 'lorem ipsum',
                'user_id': 280536886
            },
            {
                'name': 'бананы',
                'expiration_date': date(2020, 12, 14),
                'bought_date': date(2020, 12, 10),
                'info': None,
                'user_id': 280536886
            },
            {
                'name': 'рыба',
                'expiration_date': date(2021, 12, 25),
                'bought_date': date(2020, 12, 10),
                'info': None,
                'user_id': 280536886
            },
            {
                'name': 'сметана',
                'expiration_date': date(2020, 12, 13),
                'bought_date': date(2020, 12, 10),
                'info': 'lorem ipsum',
                'user_id': 280536886
            },
        ]
    )


def downgrade():
    pass
