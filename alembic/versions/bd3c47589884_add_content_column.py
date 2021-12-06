"""add content column

Revision ID: bd3c47589884
Revises: 23e2854451e5
Create Date: 2021-12-06 16:28:46.747097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd3c47589884'
down_revision = '23e2854451e5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
