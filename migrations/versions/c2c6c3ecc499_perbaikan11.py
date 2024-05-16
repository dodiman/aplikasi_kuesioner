"""perbaikan11

Revision ID: c2c6c3ecc499
Revises: 
Create Date: 2024-05-16 11:10:37.398133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2c6c3ecc499'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kategori',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kategori', sa.String(length=100), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('responden',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=50), nullable=False),
    sa.Column('nip', sa.String(length=50), nullable=False),
    sa.Column('jabatan', sa.String(length=50), nullable=False),
    sa.Column('asal_instansi', sa.String(length=50), nullable=False),
    sa.Column('no_hp', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('kuis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teks', sa.String(length=200), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('kategori_id', sa.Integer(), nullable=False),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['kategori_id'], ['kategori.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('jawaban_responden',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('responden_id', sa.Integer(), nullable=False),
    sa.Column('kuis_id', sa.Integer(), nullable=False),
    sa.Column('jawaban', sa.String(length=50), nullable=True),
    sa.Column('bukti_pelaksanaan', sa.String(length=50), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['kuis_id'], ['kuis.id'], ),
    sa.ForeignKeyConstraint(['responden_id'], ['responden.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jawaban_responden')
    op.drop_table('profile')
    op.drop_table('kuis')
    op.drop_table('user')
    op.drop_table('responden')
    op.drop_table('kategori')
    # ### end Alembic commands ###