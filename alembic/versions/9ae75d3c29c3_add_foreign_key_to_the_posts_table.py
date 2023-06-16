"""add foreign-key to the posts table

Revision ID: 9ae75d3c29c3
Revises: 7528df3e6ae8
Create Date: 2023-05-24 11:52:27.637420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ae75d3c29c3'
down_revision = '7528df3e6ae8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('owner_id', sa.Integer(),
                            nullable=False))
    op.create_foreign_key('post_user_fk',
                          source_table="posts",
                          referent_table="users",
                          local_cols=['owner_id'],
                          remote_cols=['id'],
                          ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
