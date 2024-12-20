"""Add default values for prices

Revision ID: 558b7c2fcac3
Revises: 
Create Date: 2024-11-27 00:31:55.467749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '558b7c2fcac3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trailer',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False, comment='Название прицепа'),
    sa.Column('description', sa.Text(), nullable=False, comment='Описание'),
    sa.Column('height', sa.Integer(), nullable=False, comment='Высота'),
    sa.Column('width', sa.Integer(), nullable=False, comment='Ширина'),
    sa.Column('year_of_production', sa.Date(), nullable=False, comment='Год производства'),
    sa.Column('color', sa.String(length=120), nullable=False, comment='Цвет'),
    sa.Column('max_weight', sa.Integer(), nullable=False, comment='Максимальная масса'),
    sa.Column('curb_weight', sa.Integer(), nullable=False, comment='Масса в снаряженном состоянии'),
    sa.Column('deposit', sa.Integer(), nullable=False, comment='Залог'),
    sa.Column('slug', sa.String(length=200), nullable=False, comment='URL'),
    sa.Column('price_1', sa.Integer(), nullable=False, default=800, comment='Базовая цена'),
    sa.Column('price_2', sa.Integer(), nullable=False, default=700, comment='Цена от 3 суток'),
    sa.Column('price_3', sa.Integer(), nullable=False, default=600, comment='Цена от 7 суток'),
    sa.Column('status', sa.Enum('AVAILABLE', 'RESERVED', 'UNAVAILABLE', name='trailerstatus'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trailer')
    # ### end Alembic commands ###
