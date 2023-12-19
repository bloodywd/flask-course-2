"""add film model

Revision ID: 5ab51840442f
Revises: 37a30950b118
Create Date: 2023-12-19 18:32:11.177415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ab51840442f'
down_revision = '37a30950b118'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('films', schema=None) as batch_op:
        batch_op.drop_index('ix_films_release_date')

    op.drop_table('films')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('release_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('uuid', sa.VARCHAR(length=36), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('distributed_by', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('length', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('rating', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='films_pkey'),
    sa.UniqueConstraint('uuid', name='films_uuid_key')
    )
    with op.batch_alter_table('films', schema=None) as batch_op:
        batch_op.create_index('ix_films_release_date', ['release_date'], unique=False)

    # ### end Alembic commands ###
