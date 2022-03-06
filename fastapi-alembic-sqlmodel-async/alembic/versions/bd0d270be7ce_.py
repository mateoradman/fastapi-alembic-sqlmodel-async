"""empty message

Revision ID: bd0d270be7ce
Revises: 
Create Date: 2022-03-06 05:56:26.237476

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added


# revision identifiers, used by Alembic.
revision = 'bd0d270be7ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('song',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('artist', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('headquarters', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_team_name'), 'team', ['name'], unique=False)
    op.create_table('hero',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('secret_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hero_age'), 'hero', ['age'], unique=False)
    op.create_index(op.f('ix_hero_name'), 'hero', ['name'], unique=False)
    op.create_table('user',
    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('birthdate', sa.DateTime(), nullable=True),
    sa.Column('phone', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('state', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('country', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_hashed_password'), 'user', ['hashed_password'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_hashed_password'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_hero_name'), table_name='hero')
    op.drop_index(op.f('ix_hero_age'), table_name='hero')
    op.drop_table('hero')
    op.drop_index(op.f('ix_team_name'), table_name='team')
    op.drop_table('team')
    op.drop_table('song')
    op.drop_table('role')
    # ### end Alembic commands ###
