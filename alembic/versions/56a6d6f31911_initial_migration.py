"""initial migration

Revision ID: 2c7d62e29370
Revises:
Create Date: 2024-02-16 12:38:13.990440

"""

from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2c7d62e29370"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(100), unique=True, nullable=False),
        sa.Column("password", sa.String(100), nullable=False),
        sa.Column("created_at", sa.DateTime, default=datetime.utcnow),
        sa.Column("updated_at", sa.DateTime, nullable=True),
        sa.Column("deleted_at", sa.DateTime, nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "calculation_history",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("dataset_file_name", sa.String(100), nullable=False),
        sa.Column("calculation_date", sa.DateTime, nullable=False, default=datetime.utcnow),
        sa.Column("success", sa.Boolean, nullable=False, default=False),
        sa.Column("result", sa.JSON, nullable=True),
        sa.Column("errors", sa.JSON, nullable=True),
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("calculation_history")
    op.drop_table("users")
