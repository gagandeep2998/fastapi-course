"""add last few columns to posts table

Revision ID: 246f96b65048
Revises: 9ae75d3c29c3
Create Date: 2023-05-24 12:32:22.819336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '246f96b65048'
down_revision = '9ae75d3c29c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'
    ))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')
    ))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
