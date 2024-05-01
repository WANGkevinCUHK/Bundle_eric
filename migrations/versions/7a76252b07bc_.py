"""empty message

Revision ID: 7a76252b07bc
Revises: e14d07e017bf
Create Date: 2024-04-27 15:30:14.686525

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7a76252b07bc'
down_revision = 'e14d07e017bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('friendship', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dst', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('src_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('friendship_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['src_id'], ['id'])
        batch_op.drop_column('src')
        batch_op.drop_column('dst_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('friendship', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dst_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('src', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('friendship_ibfk_1', 'users', ['dst_id'], ['id'])
        batch_op.drop_column('src_id')
        batch_op.drop_column('dst')

    # ### end Alembic commands ###
