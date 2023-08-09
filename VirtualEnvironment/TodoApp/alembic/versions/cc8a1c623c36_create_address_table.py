"""create address table

Revision ID: cc8a1c623c36
Revises: 186a073c1e0f
Create Date: 2023-08-08 15:55:28.804909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc8a1c623c36'
down_revision: Union[str, None] = '186a073c1e0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # pass
    op.create_table('address', 
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(), nullable=False), 
                    sa.Column('address2', sa.String(), nullable=False), 
                    sa.Column('city', sa.String(), nullable=False), 
                    sa.Column('state', sa.String(), nullable=False), 
                    sa.Column('country', sa.String(), nullable=False), 
                    sa.Column('postalcode', sa.String(), nullable=False)
                    )


def downgrade() -> None:
    # pass
    op.drop_table('address')
