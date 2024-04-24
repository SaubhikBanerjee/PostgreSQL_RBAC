import psycopg2 as pg
from libs import ReadConfig
from libs import LoggerClass
from libs import create_schema_sql, create_role_sql, grant_sql
from psycopg2 import sql


def main():
    config = ReadConfig("./config/config.ini")
    logger_class = LoggerClass()
    logger = logger_class.set_logger()
    try:
        conn = pg.connect(
            host=getattr(config, "db_server_address"),
            database=getattr(config, "db_database_name"),
            user=getattr(config, "db_user_name"),
            password=getattr(config, "db_password"),
            port=getattr(config, "db_port")
        )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        logger.debug("Connected to: " + str(cursor.fetchone()))
        for i in range(1, int(config.total_teams) + 1):
            try:
                role_str = "team" + str(i) + "_role_name"
                pass_str = "team" + str(i) + "_passwd"
                role_name = getattr(config, role_str)
                role_password = getattr(config, pass_str)
                schema_str = "team" + str(i) + "_schema_name"
                schema_name = getattr(config, schema_str)
                create_role = sql.SQL(create_role_sql).format(sql.Identifier(role_name),
                                                              sql.Literal(role_password)
                                                              )

                create_schema = sql.SQL(create_schema_sql).format(sql.Identifier(schema_name),
                                                                  sql.Identifier(role_name)
                                                                  )

                grant_permission = sql.SQL(grant_sql).format(sql.Identifier(schema_name),
                                                             sql.Identifier(role_name)
                                                             )
                cursor.execute(create_role)
                logger.debug("Role created for team: "+str(i))
                cursor.execute(create_schema)
                logger.debug("Schema created for team: "+str(i))
                cursor.execute(grant_permission)
                logger.debug("Permission granted for team: " + str(i))

            except Exception as e:
                logger.error("Error in creating Role & Schema!")
                logger.critical(e)
        cursor.close()
        conn.close()

    except Exception as e:
        logger.error("Problem in connecting database!")
        logger.critical(e)


if __name__ == '__main__':
    main()
