"""add user table

Revision ID: c44c9949f4bb
Revises: 4b0dca703bf5
Create Date: 2022-02-18 14:00:18.156043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c44c9949f4bb"
down_revision = "4b0dca703bf5"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
