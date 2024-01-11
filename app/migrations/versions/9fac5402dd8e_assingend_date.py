"""Assingend date

Revision ID: 9fac5402dd8e
Revises: b762a5dd1380
Create Date: 2023-09-07 15:05:06.115267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9fac5402dd8e'
down_revision: Union[str, None] = 'b762a5dd1380'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inspections', sa.Column('assigned_date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inspections', 'assigned_date')
    # ### end Alembic commands ###