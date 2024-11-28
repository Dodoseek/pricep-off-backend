"""Add is_main column to TrailerImage

Revision ID: a2b8bab0ef31
Revises: 673f7379033b
Create Date: 2024-11-28 15:37:59.653728

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'a2b8bab0ef31'
down_revision: Union[str, None] = '673f7379033b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trailer_image', sa.Column('is_main', sa.Boolean(), nullable=False, comment='Является ли изображение главным'))
    op.drop_column('trailer_image', 'description')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trailer_image', sa.Column('description', mysql.VARCHAR(length=200), nullable=True, comment='Описание изображения'))
    op.drop_column('trailer_image', 'is_main')
    # ### end Alembic commands ###