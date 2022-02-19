"""add last few columns to posts table

Revision ID: 912646da15c9
Revises: 9a782640ba75
Create Date: 2022-02-18 14:25:29.731025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "912646da15c9"
down_revision = "9a782640ba75"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE")
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "created_at")
    op.drop_column("posts", "published")
    pass
