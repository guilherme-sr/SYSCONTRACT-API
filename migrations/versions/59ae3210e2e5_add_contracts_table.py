"""add contracts table

Revision ID: 59ae3210e2e5
Revises: bc66109ccaed
Create Date: 2024-11-10 17:26:14.217926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59ae3210e2e5'
down_revision: Union[str, None] = 'bc66109ccaed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contracts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('value_hour', sa.String(), nullable=False),
    sa.Column('hours_total', sa.String(), nullable=False),
    sa.Column('hours_month', sa.String(), nullable=False),
    sa.Column('total_value', sa.String(), nullable=False),
    sa.Column('parcels', sa.String(), nullable=False),
    sa.Column('value_month', sa.String(), nullable=False),
    sa.Column('payment_date', sa.String(), nullable=False),
    sa.Column('start_date', sa.String(), nullable=False),
    sa.Column('end_date', sa.String(), nullable=False),
    sa.Column('auto_renewal', sa.String(), nullable=False),
    sa.Column('payment_type', sa.String(), nullable=False),
    sa.Column('service', sa.String(), nullable=False),
    sa.Column('times_week', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contracts')
    # ### end Alembic commands ###
