"""

Revision ID: 0c563aa13135
Revises: 6a07a67cfa4b
Create Date: 2024-03-14 12:56:37.620888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c563aa13135'
down_revision = '6a07a67cfa4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'workers', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'workers', type_='unique')
    # ### end Alembic commands ###
