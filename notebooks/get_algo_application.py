# Same function, refactored for use in an application.
def get_algo(harness_id,
             data_portal,
             metadata_reader,
             backtest_results_reader):

    algo_metadata = metadata_reader.get_metadata(harness_id)
    backtest_result = backtest_results_reader.get(
        algo_metadata['remote_id']
    )
    return business_logic(algo_metadata, backtest_result)

