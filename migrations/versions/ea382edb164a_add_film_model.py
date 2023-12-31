"""add film model

Revision ID: ea382edb164a
Revises: 6132e8631398
Create Date: 2023-12-22 03:39:36.182711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea382edb164a'
down_revision = '6132e8631398'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('distributed_by', sa.String(length=120), nullable=False),
    sa.Column('length', sa.Float(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    with op.batch_alter_table('films', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_films_release_date'), ['release_date'], unique=False)

    op.create_table('movies_actors',
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.PrimaryKeyConstraint('actor_id', 'film_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies_actors')
    with op.batch_alter_table('films', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_films_release_date'))

    op.drop_table('films')
    op.drop_table('actors')
    # ### end Alembic commands ###
