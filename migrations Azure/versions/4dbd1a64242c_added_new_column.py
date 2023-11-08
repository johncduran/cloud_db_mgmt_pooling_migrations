"""added new column

Revision ID: 4dbd1a64242c
Revises: 406f916ce18d
Create Date: 2023-11-07 20:53:21.676829

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4dbd1a64242c'
down_revision: Union[str, None] = '406f916ce18d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('is_breathing', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patients', 'is_breathing')
    # ### end Alembic commands ###
