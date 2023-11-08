"""crated is alive

Revision ID: 00923f63ac8a
Revises: b938f93e53e7
Create Date: 2023-10-16 23:58:52.984709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00923f63ac8a'
down_revision: Union[str, None] = 'b938f93e53e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('is_alive', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patients', 'is_alive')
    # ### end Alembic commands ###