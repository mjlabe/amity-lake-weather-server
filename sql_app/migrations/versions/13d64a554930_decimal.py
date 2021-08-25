"""decimal

Revision ID: 13d64a554930
Revises: 7f975ea06baa
Create Date: 2021-08-25 17:31:33.850819

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '13d64a554930'
down_revision = '7f975ea06baa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('lake', 'temp_lake',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(precision=5, scale=2),
               existing_nullable=False)
    op.alter_column('lake', 'temp_air',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(precision=5, scale=2),
               existing_nullable=False)
    op.alter_column('lake', 'humidity_air',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(precision=5, scale=2),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('lake', 'humidity_air',
               existing_type=sa.Numeric(precision=5, scale=2),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)
    op.alter_column('lake', 'temp_air',
               existing_type=sa.Numeric(precision=5, scale=2),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)
    op.alter_column('lake', 'temp_lake',
               existing_type=sa.Numeric(precision=5, scale=2),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)
    # ### end Alembic commands ###
