"""tambahkan auth

Revision ID: 5e001ff2b289
Revises: ea523e2960b2
Create Date: 2024-05-12 11:28:21.733413

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5e001ff2b289'
down_revision = 'ea523e2960b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.drop_table('kuis_responden')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kuis_responden',
    sa.Column('kuis_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('responden_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['kuis_id'], ['kuis.id'], name='kuis_responden_ibfk_1'),
    sa.ForeignKeyConstraint(['responden_id'], ['responden.id'], name='kuis_responden_ibfk_2'),
    sa.PrimaryKeyConstraint('kuis_id', 'responden_id'),
    mysql_collate='latin1_swedish_ci',
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('profile')
    op.drop_table('user')
    # ### end Alembic commands ###
