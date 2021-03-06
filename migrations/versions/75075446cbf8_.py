"""empty message

Revision ID: 75075446cbf8
Revises: 05fb54d2dfa8
Create Date: 2020-07-22 14:41:08.383828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75075446cbf8'
down_revision = '05fb54d2dfa8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
