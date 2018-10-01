# Original version of a function written for notebook use.
def get_algo(harness_id,
             metadata_db=None,
             results_db=None,
             session=None,
             dp=None):

    if metadata_db is None:
        import config
        metadata_db = create_engine(config.META_CONF)

    if results_db is None:
        import config
        results_db = create_engine(config.RESULT_CONF)

    if session is None:
        import config
        session = cassandra_session(config.CASSANDRA_CONFIG)

    if dp is None:
        dp = make_dataportal()

    return business_logic(harness_id, metadata_db, results_db,
                          session, dp)
