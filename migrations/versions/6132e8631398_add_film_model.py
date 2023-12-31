"""add film model

Revision ID: 6132e8631398
Revises: 1c6974c1c943
Create Date: 2023-12-22 03:11:51.457277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6132e8631398'
down_revision = '1c6974c1c943'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###
