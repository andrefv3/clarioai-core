import os
from dotenv import load_dotenv
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Carga variables de entorno desde archivo .env en la raíz
load_dotenv()

config = context.config

# Configura logging desde alembic.ini (si existe)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importa el metadata de tus modelos para autogenerar migraciones
from app.database import Base

target_metadata = Base.metadata

# Toma la URL de la base de datos (sin async) desde .env
database_url = os.getenv("DATABASE_URL_SYNC")
if not database_url:
    raise RuntimeError("DATABASE_URL_SYNC not set in .env")

# Sobrescribe la URL en configuración para que Alembic la use
config.set_main_option("sqlalchemy.url", database_url)


def include_object(object, name, type_, reflected, compare_to):
    """
    Controla qué objetos Alembic debe considerar para autogeneración.
    Aquí evitas eliminar tablas específicas, pero permites compararlas.
    """
    if type_ == "table" and object.name in ("routines", "analysis", "task_routine"):
        # Incluye para comparación pero evita eliminarla
        return True
    return True


def run_migrations_offline():
    """Ejecuta migraciones en modo offline (generar SQL sin conectar)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Ejecuta migraciones en modo online (conectando a la DB)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
