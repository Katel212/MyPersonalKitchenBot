"""update user language

Revision ID: 0b4025914a12
Revises: 6139bb48f1c8
Create Date: 2021-04-07 21:32:15.565046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b4025914a12'
down_revision = '6139bb48f1c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'language',
               existing_type=sa.VARCHAR(),
               nullable=True,
               existing_server_default=sa.text("'en_US'::character varying"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'language',
               existing_type=sa.VARCHAR(),
               nullable=False,
               existing_server_default=sa.text("'en_US'::character varying"))
    # ### end Alembic commands ###
