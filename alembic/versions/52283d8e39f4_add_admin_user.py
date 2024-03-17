"""add admin user

Revision ID: 52283d8e39f4
Revises: 3693b9e0d0c1
Create Date: 2024-03-17 15:34:58.083501

"""

from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy import text

from alembic import op
from app.core.config import settings
from app.core.security import get_password_hash

# revision identifiers, used by Alembic.
revision: str = "52283d8e39f4"
down_revision: Union[str, None] = "3693b9e0d0c1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    conn = op.get_bind()
    hashed_password = get_password_hash(settings.ADMIN_PASSWORD)
    conn.execute(
        text(
            f"INSERT INTO users (username, password, created_at, updated_at, deleted_at, disabled)"
            f"VALUES ('{settings.ADMIN_USERNAME}', '{hashed_password}', :created_at, :updated_at, null, false)"
        ).bindparams(created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    )


def downgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
            DELETE FROM users WHERE username = 'admin'
            """
        )
    )
