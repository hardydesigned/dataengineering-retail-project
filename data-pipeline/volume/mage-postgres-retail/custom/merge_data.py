import pandas as pd


if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here

    merged_df = pd.merge(args[0], args[1], on=['Date', 'Product'], how='inner')
    merged_df.drop(columns=["index_x"], inplace=True)
    merged_df.drop(columns=["index_y"], inplace=True)
    merged_df.drop(columns=["ROI"], inplace=True)
    merged_df.drop(columns=["Acquisition_Cost"], inplace=True)

    merged_df.rename(columns={"Channel_Used": "channel_used"}, inplace=True)
    merged_df.rename(columns={"Conversion_Rate": "conversion_rate"}, inplace=True)
    merged_df.rename(columns={"Location": "location"}, inplace=True)
    merged_df.rename(columns={"Date": "date"}, inplace=True)
    merged_df.rename(columns={"Category": "category"}, inplace=True)
    merged_df.rename(columns={"Final Quantity": "final_quantity"}, inplace=True)
    merged_df.rename(columns={"Total Revenue": "total_revenue"}, inplace=True)
    merged_df.rename(columns={"Price Reductions": "price_reductions"}, inplace=True)
    merged_df.rename(columns={"Refunds": "refunds"}, inplace=True)
    merged_df.rename(columns={"Final Revenue": "final_revenue"}, inplace=True)
    merged_df.rename(columns={"Sales Tax": "sales_tax"}, inplace=True)
    merged_df.rename(columns={"Overall Revenue": "overall_revenue"}, inplace=True)
    merged_df.rename(columns={"Refunded Item Count": "refunded_item_count"}, inplace=True)
    merged_df.rename(columns={"Purchased Item Count": "purchased_item_count"}, inplace=True)
    merged_df.rename(columns={"Return Reason": "return_reason"}, inplace=True)
    merged_df.rename(columns={"Product": "product"}, inplace=True)

    merged_df['date'] = pd.to_datetime(merged_df['date'])

    merged_df.reset_index(inplace=True)


    return merged_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
