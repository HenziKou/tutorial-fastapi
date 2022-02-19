"""create posts table

Revision ID: a04e9e108ecf
Revises: 
Create Date: 2022-02-18 13:13:45.991811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a04e9e108ecf"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
