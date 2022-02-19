"""add content column to posts table

Revision ID: 4b0dca703bf5
Revises: a04e9e108ecf
Create Date: 2022-02-18 13:54:13.409440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4b0dca703bf5"
down_revision = "a04e9e108ecf"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
