"""initial migration

Revision ID: 9d317e6c95a7
Revises: 
Create Date: 2022-11-19 20:07:46.130155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d317e6c95a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dispenser',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('flow_volume', sa.Float(), nullable=False),
    sa.Column('status', sa.Enum('OPEN', 'CLOSED', name='dispenserstatus'), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dispenser_usage',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('flow_volume', sa.Float(), nullable=False),
    sa.Column('total_spent', sa.Float(), nullable=False),
    sa.Column('opened_at', sa.DateTime(), nullable=False),
    sa.Column('closed_at', sa.DateTime(), nullable=False),
    sa.Column('dispenser_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['dispenser_id'], ['dispenser.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dispenser_usage')
    op.drop_table('dispenser')
    # ### end Alembic commands ###