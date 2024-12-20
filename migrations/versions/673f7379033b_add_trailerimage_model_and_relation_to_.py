"""Add TrailerImage model and relation to Trailer

Revision ID: 673f7379033b
Revises: e5fba50db8f2
Create Date: 2024-11-27 23:16:17.115357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '673f7379033b'
down_revision: Union[str, None] = 'e5fba50db8f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trailer_image',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('trailer_id', sa.BigInteger(), nullable=False),
    sa.Column('file_path', sa.String(length=300), nullable=False, comment='Путь к изображению'),
    sa.Column('description', sa.String(length=200), nullable=True, comment='Описание изображения'),
    sa.ForeignKeyConstraint(['trailer_id'], ['trailer.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trailer_image')
    # ### end Alembic commands ###
