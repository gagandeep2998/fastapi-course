"""add content column to the table

Revision ID: 49985a61e692
Revises: 30cf74b842ba
Create Date: 2023-05-24 10:53:20.755887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49985a61e692'
down_revision = '30cf74b842ba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
