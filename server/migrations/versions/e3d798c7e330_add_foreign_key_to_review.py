"""add foreign key to Review

Revision ID: e3d798c7e330
Revises: 4098b5578e49
Create Date: 2024-01-08 09:25:24.291955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3d798c7e330'
down_revision = '4098b5578e49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###
