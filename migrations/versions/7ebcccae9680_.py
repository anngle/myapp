"""empty message

Revision ID: 7ebcccae9680
Revises: 45585827986b
Create Date: 2018-07-27 23:20:56.849076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ebcccae9680'
down_revision = '45585827986b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sysconfig',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('web_name', sa.String(length=80), nullable=False),
    sa.Column('web_describe', sa.String(length=500), nullable=True),
    sa.Column('user_register', sa.Boolean(), nullable=True),
    sa.Column('active_site', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sysconfig')
    # ### end Alembic commands ###
