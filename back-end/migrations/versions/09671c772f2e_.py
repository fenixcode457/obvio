"""empty message

Revision ID: 09671c772f2e
Revises: 
Create Date: 2021-07-05 22:01:04.626148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09671c772f2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipo_usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombreTipo', sa.String(length=45), nullable=True),
    sa.Column('descripcion', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tipo_usuario')
    # ### end Alembic commands ###
