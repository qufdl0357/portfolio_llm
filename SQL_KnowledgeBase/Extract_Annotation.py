from sqlalchemy import create_engine, MetaData, Table,text
 
# 엔진을 생성합니다.
engine = create_engine(connection_string)
 
 
# 데이터베이스에서 주석을 추출합니다.
connection = engine.connect()
 
# 특정 테이블과 컬럼에 대한 주석을 추출합니다.
table_name = "TEMP_TB_QMS_DYN_VEND_RESULT"  # 여기에 원하는 테이블의 이름을 입력하세요.
 
# 테이블 주석 추출
table_comment_query = text(f"SELECT [value] FROM sys.extended_properties WHERE major_id = OBJECT_ID('{table_name}') AND minor_id = 0;")
table_comment_result = connection.execute(table_comment_query)
table_comment = table_comment_result.scalar()
 
# 테이블 주석 디코딩
decoded_table_comment = table_comment.decode('utf-8')
print(f"Decoded Table Comment for {table_name}: {decoded_table_comment}")
 
# 연결을 닫습니다.
connection.close()