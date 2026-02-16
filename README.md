Indian Traffic E-Challan Daily Dataset (2015–2026)<br>

About Dataset<br>
Context<br>
This dataset provides a daily granularity of traffic challan (fine) issuance and collection across India. The data is sourced from the Parivahan E-Challan system, which is the centralized digital traffic enforcement solution used by the Government of India. It captures the volume of traffic violations, the financial value of these fines, and their settlement status (paid vs. pending vs. court).<br>

----------------------------------------------------------


If you have installed poetry simply run the program using followng command
-> "poetry run python sample.py"

Dataset Info:
<class 'pandas.DataFrame'><br>
RangeIndex: 4061 entries, 0 to 4060<br>
Data columns (total 10 columns):<br>
 #   Column           Non-Null Count  Dtype<br>
---  ------           --------------  -----
 0   date             4061 non-null   datetime64[us]<br>
 1   totalChallan     4061 non-null   int64<br>
 2   disposedChallan  4061 non-null   int64<br>
 3   pendingChallan   4061 non-null   int64<br>
 4   pendingAmount    4061 non-null   int64<br>
 5   disposedAmount   4061 non-null   int64<br>
 6   totalAmount      4061 non-null   int64<br>
 7   pendingCourt     4061 non-null   int64<br>
 8   disposedCourt    4061 non-null   int64<br>
 9   totalCourt       4061 non-null   int64<br>
dtypes: datetime64[us](1), int64(9)<br>
memory usage: 317.4 KB<br>
None<br>

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-3.png)

![alt text](image-4.png)

