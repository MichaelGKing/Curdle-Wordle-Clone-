"""empty message

Revision ID: 5e32c33dd353
Revises: ce2ee85381b6
Create Date: 2022-05-21 02:38:46.120613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e32c33dd353'
down_revision = 'ce2ee85381b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puzzle_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_puzzle_id', sa.Integer(), nullable=False),
    sa.Column('server_puzzle_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puzzle_history')
    # ### end Alembic commands ###
