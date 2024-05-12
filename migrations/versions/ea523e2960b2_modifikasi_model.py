"""modifikasi model

Revision ID: ea523e2960b2
Revises: a99f169be071
Create Date: 2024-05-12 03:04:42.504097

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ea523e2960b2'
down_revision = 'a99f169be071'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jawaban_responden',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('responden_id', sa.Integer(), nullable=False),
    sa.Column('kuis_id', sa.Integer(), nullable=False),
    sa.Column('jawaban', sa.String(length=50), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['kuis_id'], ['kuis.id'], ),
    sa.ForeignKeyConstraint(['responden_id'], ['responden.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('kuis', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_modified', sa.DateTime(), nullable=True))

    with op.batch_alter_table('responden', schema=None) as batch_op:
        batch_op.drop_column('jawaban')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('responden', schema=None) as batch_op:
        batch_op.add_column(sa.Column('jawaban', mysql.VARCHAR(length=50), nullable=True))

    with op.batch_alter_table('kuis', schema=None) as batch_op:
        batch_op.drop_column('date_modified')

    op.drop_table('jawaban_responden')
    # ### end Alembic commands ###