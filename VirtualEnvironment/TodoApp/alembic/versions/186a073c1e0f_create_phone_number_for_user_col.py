"""create phone number for user col

Revision ID: 186a073c1e0f
Revises: 
Create Date: 2023-08-08 15:31:38.641706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '186a073c1e0f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # pass
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    # pass
    op.drop_column('users', 'phone_number')
