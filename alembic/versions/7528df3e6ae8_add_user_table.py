"""add user table

Revision ID: 7528df3e6ae8
Revises: 49985a61e692
Create Date: 2023-05-24 11:31:59.374378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7528df3e6ae8'
down_revision = '49985a61e692'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
