
from langchain.document_loaders import SnowflakeLoader

QUERY = "select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.customer limit 10"
snowflake_loader = SnowflakeLoader(
    query=QUERY,
    user="PRAKASH3105",
    password="PrisonBreak@1",
    account="ejdbkav-ix82585",
    warehouse="COMPUTE_WH",
    role="ACCOUNTADMIN",
    database="SNOWFLAKE_SAMPLE_DATA",
    schema="TPCH_SF1",
)
snowflake_documents = snowflake_loader.load()
i=1
for document in snowflake_documents:
    print("row number = {} =======================".format(i))
    print(document.page_content)
    i=i+1
