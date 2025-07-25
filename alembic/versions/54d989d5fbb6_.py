"""empty message

Revision ID: 54d989d5fbb6
Revises: c8a4e510e620
Create Date: 2025-06-13 11:40:06.753749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54d989d5fbb6'
down_revision: Union[str, None] = 'c8a4e510e620'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=True),
    sa.Column('order_amount', sa.Float(), nullable=True),
    sa.Column('order_status', sa.String(), nullable=True),
    sa.Column('shipping_address', sa.Text(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_details',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_details')
    op.drop_table('order')
    # ### end Alembic commands ###
