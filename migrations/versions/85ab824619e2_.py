"""empty message

Revision ID: 85ab824619e2
Revises: 0e84a85c43c8
Create Date: 2020-07-20 15:54:06.791060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85ab824619e2'
down_revision = '0e84a85c43c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###
    op.execute('update todos set completed=False where completed is null;')
    op.alter_column('todos','completed',nullable=False)
def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
