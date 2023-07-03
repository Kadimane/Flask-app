"""create table

Revision ID: 87657438d617
Revises: ebd6e28218fb
Create Date: 2023-06-25 11:28:34.643526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87657438d617'
down_revision = 'ebd6e28218fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
