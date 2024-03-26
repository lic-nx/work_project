"""

Revision ID: d9ea72b48dd1
Revises: a6d62f4cf68c
Create Date: 2024-03-22 07:48:52.979248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9ea72b48dd1'
down_revision = 'a6d62f4cf68c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'carts_info', ['id'])
    op.create_unique_constraint(None, 'clients', ['id'])
    op.create_unique_constraint(None, 'group_workers', ['id'])
    op.create_unique_constraint(None, 'workers', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'workers', type_='unique')
    op.drop_constraint(None, 'group_workers', type_='unique')
    op.drop_constraint(None, 'clients', type_='unique')
    op.drop_constraint(None, 'carts_info', type_='unique')
    # ### end Alembic commands ###
