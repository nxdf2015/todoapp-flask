"""empty message

Revision ID: 6557aea0db82
Revises: ac75b964d37f
Create Date: 2021-03-15 10:39:55.314791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6557aea0db82'
down_revision = 'ac75b964d37f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lists')
    # ### end Alembic commands ###