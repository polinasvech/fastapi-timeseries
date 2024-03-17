"""add disabled column

Revision ID: 3693b9e0d0c1
Revises: 2c7d62e29370
Create Date: 2024-03-17 15:08:38.507003

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3693b9e0d0c1"
down_revision: Union[str, None] = "2c7d62e29370"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("users", sa.Column("disabled", sa.Boolean, default=False))


def downgrade():
    op.drop_column("users", "disabled")
