"""create users table

Revision ID: d291498be933
Revises: 
Create Date: 2024-08-13 16:53:18.700022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd291498be933'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('number_card', sa.String),
        sa.Column('chat_id', sa.String),
        sa.Column('chat_id_number_card', sa.String,primary_key = True),
        sa.Column('money', sa.String),
    )

def downgrade():
    op.drop_table('users')
